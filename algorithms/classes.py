class Usuario:
    def __init__(self, nome, usuario_id, email, senha):
        self.usuario_id = usuario_id
        self.nome = nome  
        self.email = email
        self.senha = senha

class Equipamento:
    def __init__(self, id, nome, nome_fabricante, potencia, rigidez):
        self.id = id  
        self.nome = nome 
        self.nome_fabricante = nome_fabricante
        self.potencia = potencia
        self.rigidez = rigidez 

class HorariosDeUso:
    def __init__(self, id, inicio, fim, equipamento_id):
        self.id = id
        self.inicio = inicio
        self.fim = fim
        self.equipamento_id = equipamento_id