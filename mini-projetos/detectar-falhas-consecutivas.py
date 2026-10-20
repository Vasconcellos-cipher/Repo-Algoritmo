eventos = ["LOGIN", "FAILED", "FAILED", "LOGIN", "LOGOUT"]

encontrou = False

for i in range(len(eventos) - 1):
    if eventos[i] == "FAILED" and eventos[i + 1] == "FAILED":
        encontrou = True
        break

if encontrou:
    print("Foram encontradas falhas consecutivas!")
else:
    print("Não foram encontradas falhas consecutivas.")