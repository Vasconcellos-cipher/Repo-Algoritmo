eventos = ["LOGIN", "FAILED", "LOGIN", "FAILED", "LOGOUT"]

while True:
    print("1 - Ver eventos, 2 - Ver alertas, 3 - Sair.")
    


    try:
        resposta = int(input("Digite uma opção: "))
    except ValueError:
        print("Digite um número válido")
        continue
  
    if resposta == 1:
        for i in eventos:
            print(i)

    elif resposta == 2:
        contador = 0
        for i in eventos:
            if i == "FAILED":
                contador += 1
        print(f"São {contador} alertas!")

    elif resposta == 3:
        print("Encerrando programa")
        break
    else:
        print("Opção inválida")
