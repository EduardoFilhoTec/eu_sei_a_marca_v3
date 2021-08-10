# Lista de endereços dos concentradores
class Address_dict():
    def __init__(self, nome):
        self.nome = nome
        """
        EDITE AQUI SUA LISTA DE CONCENTRADORES, SEGUINDO O PADRÃO DA TUPLA ABAIXO
        Nome tudo minúsculo e junto.
        IPV4 normal.
        ('nomeroteador', 'ip.do.seu.roteador')
        """
        self.address_list = [
            ('roteador1', '172.17.0.92'), ('ccr3600', '172.17.0.92'),
            ('meuroteador', '192.168.0.10'), ('ccr1072', '192.168.0.10'),
           
            ] # FIM DA TUPLA
    
    # Verifica se entrada 'nome' está na lista de endereços
    def esta_aqui(self):
         # dict_address recebe um dicionário criado da lista de endereços acima (address_list)
        dict_address = dict(self.address_list)
        
        # Se nome está no dicionário, retorne o valor da chave [nome]
        if self.nome in dict_address:
            print(dict_address[self.nome])
            return dict_address[self.nome]
        else:
            print('Não encontrei esse nome')
            return ''
