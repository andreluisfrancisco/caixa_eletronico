from common.cpf_utils import validar_cpf 
from random import randint

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = self._validar_ou_lancar_excecao(cpf)

    def _validar_ou_lancar_excecao(self, cpf):
        if not validar_cpf(cpf):  
            raise ValueError("CPF inválido.")
        return cpf

class Conta:
    def __init__(self, cliente):
        self.titular = cliente
        self.numero = self._gerar_numero_conta()
        self.saldo = 0

    def _gerar_numero_conta(self):
        return f'{randint(1000, 9999)}-{randint(1, 9)}'

    def consultar_saldo(self):
        return self.saldo
