class AtmServices:

    @staticmethod
    def depositar(conta, valor):
        if valor > 0:
            conta.saldo += valor
            print(f'Depósito de R${valor:.2f} realizado com sucesso.')
        else:
            print("Valor de depósito inválido.")

    @staticmethod
    def sacar(conta, valor):
        if valor > 0 and conta.saldo >= valor:
            conta.saldo -= valor
            print(f'Saque de R${valor:.2f} realizado com sucesso.')
            return True
        elif valor <= 0:
            print("Valor de saque inválido.")
            return False
        else:
            print("Saldo insuficiente.")
            return False

    @staticmethod
    def gerar_extrato(conta):
        print(f'Número da Conta: {conta.numero}\nSaldo: R${conta.saldo:.2f}')
