from os import name
import routeros_api
import address_dict as dct

class Metodos():
    def __init__(self):
        """
        CLASSE CONTÉM VÁRIOS MÉTODOS PARA INTEREÇÃO COM A GUI, E CÁLCULOS, ALÉM DE CONSUMOS DE API.
        valida_entrada = confere se usuário digitou um endereço IP ou nome do concentrador e retornará valor acessa_mikrotik()
        acessa_mikrotik() =  consulta mikrotik via api e pega dados digitados por valida_entrada()
        acesso_remoto() / porta_54321 = abre nova guia no navegador com IP do cliente
        """

    
    
    def valida_entrada(self, ent_concentrador, ent_login, lb_output, frame_layout):
        """
        Confere se usuário digitou um endereço IP ou nome do concentrador, em seguida chama o método
        acessa_mikrotik()
        """
        # Transforma argumento em string e tira espaços e deixa em minúsculo
        self.ent_concentrador = str(ent_concentrador.get()).strip().lower()
        # Transforma argumento em string e tira espaços e deixa em minúsculo
        self.ent_login = str(ent_login.get()).strip().lower()
        # Label de resposta que será editada 
        self.lb_out = lb_output
        self.frame = frame_layout
        self.frame.pack_forget()
        # Recebe ent_concentrador, tirando todos os espaços
        ent_concen_espaco = ''.join(self.ent_concentrador.split())
        # Se ent_concentrador, sem pontos, é apenas númerico
        if ''.join(ent_concen_espaco.split('.')).isnumeric():
            self.concentrador = ent_concen_espaco
            self.acessa_mikrotik()
        else:
            """
            Objeto para chamar a função esta_aqui(), checa se ent_concen_espaco existe
            no dicionário dos concentradores, e se sim, retorna o IP
            """
            if dct.Address_dict(ent_concen_espaco).esta_aqui() != '':
                self.concentrador = dct.Address_dict(ent_concen_espaco).esta_aqui()
                self.acessa_mikrotik()
            else:
                self.lb_out['text'] = 'Não encontrei esse concentrador, tente novamente'
                self.lb_out.update()

    
    # FAZ CONEXÃO VIA api NO MIKROTIK DIGITADO
    def acessa_mikrotik(self):
        """
        TENTA FAZER CONEXÃO VIA api NO MIKROTIK DIGITADO, verifica se valor de ent_login existe dentro do MIKROTIK
        E se sim, chama método api_mac()
        """
        try:
            self.connection = routeros_api.RouterOsApiPool(host=self.concentrador, username='nome_de_usuário', password='senha', plaintext_login=True)
            api = self.connection.get_api()
        except:
            print('Conexão falhou')
            texto = 'A Conexão com Concentrador falhou,\nverifique se porta API está habilitada\nou se nome/ip está correto'
            self.lb_out['text'] = texto
            self.lb_out.update()
        else:
            # COMANDO PARA PEGAR DADOS DOS CLIENTES PPPoE
            comando_pppoe = api.get_resource('/ppp/active')  
            # Recebe todas as informações do pppoe e transforma numa string só
            self.info_pppoe = str(comando_pppoe.get(name=self.ent_login))
            if self.info_pppoe == '[]':
                print('Não achei PPPoE')
                self.lb_out['text'] = "Não encontrei esse PPPoE no concentrador\nlogin pode estar incorreto ou cliente Offilne"
                self.lb_out.update()
                self.connection.disconnect()
            else: 
                self.api_mac(self.encontra_valores_no_mikrotik('caller-id', self.info_pppoe))
                ip_cliente = (self.encontra_valores_no_mikrotik('address', self.info_pppoe))
                self.ip = ip_cliente
            
            self.connection.disconnect()

    
    # Faz consulta via API a um BD para saber a qual fabricante, pertence endereço MAC
    def api_mac(self, mac):
        '''
        Recebe argumento 'mac' e faz consulta no MACVendors, retornando marca do roteador como string
        '''
        self.mac = mac
        from requests import get
        # Faz requisão no site MACVENDORS
        mac_request = get('https://api.macvendors.com/{}'.format(self.mac))  

        if mac_request.status_code == 404:
            outText = ('Mac não encontrado, por favor tente novamente!{:=^40}'.format(''))
            self.lb_out['text'] = outText
            self.lb_out.update()
        else:
            outText = str('{:=^40}'.format(' ' + mac_request.text + ' ')).upper()
            print(outText)
            self.lb_out['text'] = outText
            self.lb_out.update()
            self.frame.pack()
            return print('Deu certo!')

    # Abrir navegador no IP do cliente
    def acesso_remoto(self):
        """
        Recebe de valor 'ip' do método encontra_valores_no_mikrotik e retorna uma função webbrowser.open_new_tab()
        """
        ip_para_acesso = self.ip
        print (ip_para_acesso)
        import webbrowser
        url = str('http://'+ip_para_acesso)
        print(url)
        return webbrowser.open_new_tab(url)

    def acesso_remoto_porta_54321(self):
        """
        Recebe de valor 'ip' do método encontra_valores_no_mikrotik e retorna uma função webbrowser.open_new_tab() com porta 54321
        """
        ip_para_acesso = self.ip
        print (ip_para_acesso)
        import webbrowser
        url = str('http://'+ip_para_acesso+':54321')
        print(url)
        return webbrowser.open_new_tab(url)
        
    
    def encontra_valores_no_mikrotik(self, palavra_chave, string_completa):
        """
        Faz o calculo: A partir da palavra_chave digitada até a próxima chave de string_completa, pegue o conteúdo que tem no meio como uma string
        ex: 'id': '*F4036D', 'name': '<pppoe-4ba9c28etx>' -->  de ('id': + 3 espaços) até (,) - 1 espaço = *F4036D
        """
        self.string_analise = str(string_completa)
        # Procura a palavra-chave dentro da string_completa, ex: remote-address
        palavra_chave = str(palavra_chave).lower().strip()
        # encontra dentro da string_completa em qual posição(index) está a busca_chave
        palavra_chave = str(self.string_analise[self.string_analise.find(palavra_chave):len(self.string_analise)])
        # recebe uma str do conteudo entre a palavra chave e a próxima palavra chave
        conteudo = str(palavra_chave[int(palavra_chave.find(':') + 3): int(palavra_chave.find(',') - 1)]).strip()
        if conteudo != '':
            return conteudo
        else:
            print('!!! Chave Inválida !!!\nAs chaves permitidas são:\n')
            print(string_completa)
