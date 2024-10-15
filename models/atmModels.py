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
