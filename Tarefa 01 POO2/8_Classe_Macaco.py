class macaco:
    def __init__(self, nome, bucho, macaco1, macaco2, banana, laranja, caju):
        self.nome
        self.bucho = []
        self.macaco1
        self.macaco2
        self.banana
        self.laranja
        self.caju
        
    def comer(self, comida):
        self.bucho.append(comida)
        print(f"{self.nome} comeu {comida}")
        
    def verBucho(self):
        if not self.bucho:
            print(f"bucho de {self.nome} está vazio")
        else:
            print(f"No bucho de {self.nome} tem {','.join(self.bucho)}")
        
    def digerir(self):
        if not self.bucho:
            print(f"O bucho de {self.name} não tem comida pra digerir")
        else: 
            digerir = self.bucho.pop(0)
            print(f"{self.nome} digeriu {digerir}")