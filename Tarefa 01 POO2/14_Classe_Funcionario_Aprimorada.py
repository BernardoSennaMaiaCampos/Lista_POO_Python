class funcionario:
    def __init__(self, nome, salario=0):
        self.nome = nome
        self.salario = salario
    
        def returnNome(self):
            return self.nome
        
        def returnSalario(self):
            return self.salario
        
        def aumentarSalario(self, porcentualDeAumento):
            aumento = self.salario * (porcentualDeAumento / 100)
            self.salario += aumento
            return self.salario