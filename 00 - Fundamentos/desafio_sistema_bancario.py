import time

# Dados de usuários e senhas
usuarios = {
    "usuario1": {"senha": "senha1", "saldo": 0, "extrato": "", "numero_saques": 0},
    "usuario2": {"senha": "senha2", "saldo": 0, "extrato": "", "numero_saques": 0},
    "usuario3": {"senha": "senha3", "saldo": 0, "extrato": "", "numero_saques": 0},
}

LIMITE_SAQUES = 3
limite = 500



def validar_acesso():
    for _ in range(3):
        
        print("\n ================ BOAS-VINDAS ================")
        print("Seja Bem-vindo(a) ao Banco ACS")
        print("Para iniciarmos vosso atendimento insira o nome de usuário e senha cadastrados")
        usuario = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")

        if usuario in usuarios and usuarios[usuario]["senha"] == senha:
            return usuario
        else:
            print("Usuário ou senha incorretos. Tente novamente.")
    print("Conta bloqueada por 24 horas.")
    time.sleep(86400)  # Bloqueio simulado por 24 horas
    return None

while True:
    usuario_logado = validar_acesso()
    if not usuario_logado:
        break

    menu = """
================ MENU ================
     Escolha a operação desejada

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=======================================
=> """

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            if valor > 0:
                usuarios[usuario_logado]["saldo"] += valor
                usuarios[usuario_logado]["extrato"] += f"Depósito: R$ {valor:.2f}\n"
            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > usuarios[usuario_logado]["saldo"]
            excedeu_limite = valor > limite
            excedeu_saques = usuarios[usuario_logado]["numero_saques"] >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")
            elif valor > 0:
                usuarios[usuario_logado]["saldo"] -= valor
                usuarios[usuario_logado]["extrato"] += f"Saque: R$ {valor:.2f}\n"
                usuarios[usuario_logado]["numero_saques"] += 1
            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "e":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not usuarios[usuario_logado]["extrato"] else usuarios[usuario_logado]["extrato"])
            print(f"\nSaldo: R$ {usuarios[usuario_logado]['saldo']:.2f}")
            print("==========================================")

        elif opcao == "q":
            print("Obrigado por usar os serviços do Banco ACS!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

    #Retorna para o ínicio