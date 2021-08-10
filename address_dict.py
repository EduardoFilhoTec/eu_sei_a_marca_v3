# Lista de endereços dos concentradores
class Address_dict():
    def __init__(self, nome):
        self.nome = nome
        """
        EDITE AQUI SUA LISTA DE CONCENTRADORES, SEGUINDO O PADRÃO DA TUPLA ABAIXO
        """
        self.address_list = [
            ('aldeota1', '172.17.0.92'), ('aldeotai', '172.17.0.92'),
            
            ('aldeota2', '172.17.0.137'), ('aldeotaii', '172.17.0.137'),
            
            ('aquiraz', '172.17.0.125'), ('aquir', '172.17.0.125'),
            
            ('coacu', '172.17.0.97'), ('coaçu', '172.17.0.97'),

            ('damas', '172.17.0.65'),
            
            ('diasmacedo', '172.17.0.49'), ('dias', '172.17.0.49'), ('macedo', '172.17.0.49'),

            ('esperanca', '172.17.0.87'), ('esperança', '172.17.0.87'),

            ('guararapes', '172.17.0.11'), ('guarara', '172.17.0.11'), ('guararape', '172.17.0.11'),

            ('messejana1', '172.17.0.12'), ('messejanai', '172.17.0.12'), ('josedealencar1', '172.17.0.12'),

            ('messejana2', '172.17.0.96'), ('messejanaii', '172.17.0.96'),

            ('messejanashell', '172.17.0.134'), ('messejananovo', '172.17.0.134'), ('postoms', '172.17.0.134'),
            
            ('passare', '172.17.0.8'), ('passaré', '172.17.0.8'),
            
            ('pedrabranca', '172.17.0.10'), ('pedra', '172.17.0.10'),

            ('portodunas', '172.17.0.25'),
            ('portodasdunas', '172.17.0.25'), ('portaldunas', '172.17.0.25'), 
            ('portaldasdunas', '172.17.0.25'),

            ('saogerardo', '172.17.0.105'),

            ('viasul', '172.20.3.2')

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