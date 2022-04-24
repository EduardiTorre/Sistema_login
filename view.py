from controller import ControllerCadastro, ControllerLogin

while True:
    print("========== Menu ==========")

    print("1. Logar no sistema\n"
          "2. Cadastrar no sistema\n"
          "3. Sair do menu\n")
    escolha = 0
    while True:
        escolha = int(input('Opção desejada: '))
    
        if escolha >= 1 and escolha <= 3:
            break

        print("escolha umas das opções acima.")

    if escolha == 1:
        print("\x1b[2J")
        print('===== Logando no sistema =====')
        email = str(input('Digite seu email: '))
        senha = str(input('Digite sua senha: '))
        resultado = ControllerLogin.verificar_login(email, senha)

        if resultado == 1:
            print("Logado no sistema.")
        if resultado == 2:
            print("Email inválido.")
        if resultado == 3:
            print("Senha inválida.")

    if escolha == 2:
        print("\x1b[2J")
        print('===== Cadastro de usuario =====')
        user  = str(input('Digite seu nome de usuario: '))
        email = str(input('Digite seu email: '))
        senha = str(input('Digite sua senha: '))
        resultado = ControllerCadastro.cadastrar_pessoa(user, email, senha)
        
        if resultado == 1:
            print('Cadastro realizado com sucesso.')
        if resultado == 2:
            print('Tamanho do nome inválido.')
        if resultado == 3:
            print('Tamanho do email inválido.')
        if resultado == 4:
            print('Tamanho da senha inválido.')
        if resultado == 5:
            print('Email já cadastrado.')
        
    if escolha == 3:
        break        
    