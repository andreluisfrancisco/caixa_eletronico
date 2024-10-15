from models.atm_models import Cliente, Conta
from services.atm_services import AtmServices

class CaixaEletronico:

    def __init__(self):
        self.conta = None

    def iniciar_sessao(self):
        nome = input('Nome: ')
        cpf = input('CPF: ')
        
        cliente = self._criar_cliente(nome, cpf)
        if cliente:
            self.conta = Conta(cliente)
            self._exibir_mensagem_boas_vindas()
    
    def _criar_cliente(self, nome, cpf):
        try:
            return Cliente(nome, cpf)
        except ValueError as e:
            print(f"Erro ao criar cliente: {e}")
            return None

    def _exibir_mensagem_boas_vindas(self):
        print(f"Olá {self.conta.titular.nome}, sua conta foi criada. Número da conta: {self.conta.numero}")

    def menu(self):
        if not self._verificar_sessao_ativa():
            return
        
        while True:
            self._exibir_menu_opcoes()
            opcao = input('Digite uma opção: ')
            if not self._processar_opcao_menu(opcao):
                break

    def _verificar_sessao_ativa(self):
        if not self.conta:
            print("Você precisa iniciar uma sessão antes de acessar o menu.")
            return False
        return True

    def _exibir_menu_opcoes(self):
        print("\nMenu do Caixa Eletrônico:")
        print('1- Consultar Saldo\n2- Depositar\n3- Sacar\n4- Ver Extrato\n5- Sair')

    def _processar_opcao_menu(self, opcao):
        opcoes_menu = {
            '1': self._consultar_saldo,
            '2': self._realizar_deposito,
            '3': self._realizar_saque,
            '4': self._gerar_extrato,
            '5': self._encerrar_operacao
        }

        acao = opcoes_menu.get(opcao)
        if acao:
            return acao()
        else:
            print("Opção inválida. Tente novamente.")
            return True

    def _consultar_saldo(self):
        saldo = self.conta.consultar_saldo()
        print(f"Seu saldo atual é: R${saldo:.2f}")
        return True

    def _realizar_deposito(self):
        valor = self._obter_valor("Digite o valor para depósito: ")
        if valor is not None:
            AtmServices.depositar(self.conta, valor)
        return True

    def _realizar_saque(self):
        valor = self._obter_valor("Digite o valor para saque: ")
        if valor is not None:
            AtmServices.sacar(self.conta, valor)
        return True

    def _gerar_extrato(self):
        AtmServices.gerar_extrato(self.conta)
        return True

    def _encerrar_operacao(self):
        print("Encerrando operação. Até logo!")
        return False

    def _obter_valor(self, mensagem):
        try:
            valor = float(input(mensagem))
            if valor <= 0:
                print("O valor deve ser positivo.")
                return None
            return valor
        except ValueError:
            print("Valor inválido. Tente novamente.")
            return None
