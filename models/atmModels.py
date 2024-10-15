from random import randint

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = self._validar_ou_lancar_excecao(cpf)

    def _validar_ou_lancar_excecao(self, cpf):
        if not self._cpf_valido(cpf):
            raise ValueError("CPF inválido.")
        return cpf

    def _cpf_valido(self, cpf):
        return len(cpf) == 11 and cpf.isdigit()


class Conta:
    def __init__(self, cliente):
        self.titular = cliente
        self.numero = self._gerar_numero_conta()
        self.saldo = 0

    def _gerar_numero_conta(self):
        return f'{randint(1000, 9999)}-{randint(1, 9)}'

    def consultar_saldo(self):
        return self.saldo
