def validar_cpf(cpf):
    if not cpf.isdigit() or len(cpf) != 11:
        return False
    
    if cpf == cpf[0] * 11:
        return False

    return True
