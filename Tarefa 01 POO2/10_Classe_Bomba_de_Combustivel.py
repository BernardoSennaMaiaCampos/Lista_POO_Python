class bombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self):
        valor = float(input("Qual o valor a abastecer? "))
        litros = valor / self.valorLitro
        if litros <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros
            print(f"Foram abastecidos {litros:.2f} litros.")
        else:
            print("Quantidade de combustível na bomba é insuficiente!")

    def abastecerPorLitro(self):
        litros = float(input("Quantos litros serão adicionados? "))
        valor = litros * self.valorLitro
        self.quantidadeCombustivel -= litros
        print(f"O valor a pagar é {valor:.2f}.")

    def alterarValor(self):
        novo_valor = float(input("Qual o novo valor?"))
        self.valorLitro = novo_valor
        print(f"Novo valor é {self.valorLitro:.2f}.")

    def alterarCombustivel(self):
        novo_combustivel = input("Qual o novo tipo de combustível? ")
        self.tipoCombustivel = novo_combustivel
        print(f"Novo tipo é {self.tipoCombustivel}.")

    def alterarQuantidadeCombustivel(self):
        nova_quantidade = float(input("Qual a nova quantidade de combustível na bomba? "))
        self.quantidadeCombustivel = nova_quantidade
        print(f"Nova quantidade de combustível na bomba é {self.quantidadeCombustivel:.2f} litros.")
