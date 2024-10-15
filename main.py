from controllers.atmControllers import CaixaEletronico

def main():
    caixa_eletronico = CaixaEletronico()
    caixa_eletronico.iniciar_sessao() 
    
    resposta = ''
    
    while resposta != 's':
        print("\nBem-vindo ao Caixa Eletrônico!")
        resposta = input('Digite "e" para entrar no menu ou "s" para sair: ').lower()
        
        if resposta == 'e':
            caixa_eletronico.menu()
        elif resposta == 's':
            print('Obrigado por usar o caixa eletrônico. Até logo!')
        else:
            print('Resposta inválida. Tente novamente.')
            
if __name__ == "__main__":
    main()
