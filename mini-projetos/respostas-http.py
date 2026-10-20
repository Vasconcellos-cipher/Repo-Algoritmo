tentativas = [200, 401, 403, 200, 500, 401]
contador = 0

for i in tentativas:
    print(i)

    if i == 401:
        contador += 1

print("Total de respostas 401:", contador)