class contaInvestimento:
    def __init__(self, saldoInicial, taxaJuros, numeroConta, nomeCorrentista) :
        self.saldo = saldoInicial
        self.taxaJuros = taxaJuros
        self.numeroConta = numeroConta
        self.nomeCorrentista = nomeCorrentista

    def adicioneJuros(self):
        self.saldo += self.saldo * (self.taxaJuros / 100)

    def alterarNome(self, novoNome):
            self.nomeCorrentista = novoNome

conta = contaInvestimento(1000.00, 10)  

for _ in range(5):
    conta.adicioneJuros()

print(f"Saldo final é {conta.saldo:.2f}")
