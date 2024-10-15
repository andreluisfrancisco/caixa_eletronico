from random import randint

class Cliente: 
    def __init__(self, nome, cpf):
        if not self.validar_cpf(cpf):
            raise ValueError("CPF inválido.")
        self.nome = nome
        self.cpf = cpf

    def validar_cpf(self, cpf):
        # Implementar uma validação real
        return len(cpf) == 11 and cpf.isdigit()

class Conta:
    def __init__(self, cliente):
        self.titular = cliente
        self.numero = self.gerar_numero_conta()
        self.saldo = 0

    def gerar_numero_conta(self):
        return f'{randint(1000, 9999)}-{randint(1, 9)}'

    def consultar_saldo(self):
        return self.saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor:.2f} realizado com sucesso.')
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} realizado com sucesso.')
            return True
        elif valor <= 0:
            print("Valor de saque inválido.")
            return False
        else:
            print("Saldo insuficiente.")
            return False

    def extrato(self):
        print(f'Número da Conta: {self.numero}\nSaldo: R${self.saldo:.2f}')
