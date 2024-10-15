from controllers.atm_controllers import CaixaEletronico
from views.atm_views import iniciar_caixa_eletronico

def main():
    caixa_eletronico = CaixaEletronico() 
    caixa_eletronico.iniciar_sessao() 
    iniciar_caixa_eletronico(caixa_eletronico) 

if __name__ == "__main__":
    main()
