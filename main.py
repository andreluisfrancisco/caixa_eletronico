from controllers.atmControllers import CaixaEletronico
from views.atmViews import iniciar_caixa_eletronico

def main():
    caixa_eletronico = CaixaEletronico() 
    caixa_eletronico.iniciar_sessao() 
    iniciar_caixa_eletronico(caixa_eletronico) 

if __name__ == "__main__":
    main()
