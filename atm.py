from models import Cliente, Conta

class CaixaEletronico:

    def __init__(self):
        self.conta = None

    def iniciar_sessao(self):
        nome = input('Nome: ')
        cpf = input('CPF: ')
        try:
            cliente = Cliente(nome, cpf)
            self.conta = Conta(cliente)
            print(f'Olá {self.conta.titular.nome}, sua conta foi criada. Número da conta: {self.conta.numero}')
        except ValueError as e:
            print(e)
            return

    def menu(self):
        if not self.conta:
            print("Você precisa iniciar uma sessão antes de acessar o menu.")
            return

        while True:
            print("\nMenu do Caixa Eletrônico:")
            print('1- Consultar Saldo\n2- Depositar\n3- Sacar\n4- Ver Extrato\n5- Sair')
            opcao = input('Digite uma opção: ')

            if opcao == '1':
                print(f'Seu saldo atual é: R${self.conta.consultar_saldo():.2f}')
            
            elif opcao == '2':
                valor = self._obter_valor("Digite o valor para depósito: ")
                if valor is not None:
                    self.conta.depositar(valor)

            elif opcao == '3':
                valor = self._obter_valor("Digite o valor para saque: ")
                if valor is not None:
                    if not self.conta.sacar(valor):
                        print("Operação de saque falhou.")

            elif opcao == '4':
                self.conta.extrato()

            elif opcao == '5':
                print("Encerrando operação. Até logo!")
                break

            else:
                print("Opção inválida. Tente novamente.")

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
