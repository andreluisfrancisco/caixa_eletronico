MENU_ENTRADA = 'e'
MENU_SAIR = 's'

def exibir_mensagem_boas_vindas():
    print("\nBem-vindo ao Caixa Eletrônico!")

def exibir_mensagem_despedida():
    print("Obrigado por usar o caixa eletrônico.")

def obter_opcao_usuario():
    return input('Digite "e" para entrar no menu ou "s" para sair: ').lower()

def processar_opcao(caixa_eletronico, opcao_usuario):
    if opcao_usuario == MENU_ENTRADA:
        caixa_eletronico.menu()
    elif opcao_usuario == MENU_SAIR:
        exibir_mensagem_despedida()
        return False
    else:
        print('Opção inválida. Tente novamente.')
    return True

def iniciar_caixa_eletronico(caixa_eletronico):
    opcao_usuario = None
    
    while opcao_usuario != MENU_SAIR:
        exibir_mensagem_boas_vindas()
        opcao_usuario = obter_opcao_usuario()
        if not processar_opcao(caixa_eletronico, opcao_usuario):
            break
