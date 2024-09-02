class Bichinho:
    def _init_(self, nome, fome=0, tedio=0):
        self.nome = nome
        self.fome = fome
        self.tedio = tedio

    def alimentar(self, comida):
        reducao_fome = comida * 2
        self.fome = max(0, self.fome - reducao_fome)
    
    def brincar(self, tempo):
        reducao_tedio = tempo * 3
        self.tedio = max(0, self.tedio - reducao_tedio)
    
    def _str_(self):
        return f"Nome: {self.nome}, Fome: {self.fome}, Tédio: {self.tedio}"

class Fazenda:
    def _init_(self, bichinhos):
        self.bichinhos = bichinhos

    def alimentar_brincar(self, comida, tempo):
        for bichinho in self.bichinhos:
            bichinho.alimentar(comida)
            bichinho.brincar(tempo)

    def _str_(self):
        return "\n".join(str(b) for b in self.bichinhos)

def main():
    bichinhos = [Bichinho("Tama", fome=5, tedio=10), Bichinho("Gushi", fome=7, tedio=8)]
    fazenda = Fazenda(bichinhos)
    
    while True:
        print("\nMenu:")
        print("1. Alimentar e brincar com os bichinhos")
        print("2. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            comida = int(input("Informe a quantidade de comida: "))
            tempo = int(input("Informe o tempo de brincadeira: "))
            fazenda.alimentar_brincar(comida, tempo)
            print("\nEstado atual dos bichinhos:")
            print(fazenda)
        
        elif escolha == "2":
            print("Saindo do programa.")
            break
        
        elif escolha == "admin": 
            print("SEGREDO ACHADO")
            for bichinho in fazenda.bichinhos:
                print(bichinho) 
            
        else:
            print("Opção inválida. Tente novamente.")
if __name__ == "__main__":
    main()
