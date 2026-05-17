# 1.4 Você tem um número de telefone e deseja encontrar o dono dele em uma agenda telefônica. (Dica: Deve procurar pela agenda inteira!)

agenda = [
    {"nome": "Ana", "telefone": "1111-1111"},
    {"nome": "Carlos", "telefone": "2222-2222"},
    {"nome": "Daniel", "telefone": "3333-3333"},
    {"nome": "Eduarda", "telefone": "4444-4444"},
    {"nome": "Fernanda", "telefone": "5555-5555"}
]

def buscar_dono_do_telefone(lista, telefone_procurado):
    for contato in lista:
        if contato["telefone"] == telefone_procurado:
            return contato["nome"] 
    return None

print(buscar_dono_do_telefone(agenda, "4444-4444"))  