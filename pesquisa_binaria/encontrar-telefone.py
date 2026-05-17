#1.3 Você tem um nome e deseja encontrar o número de telefone para esse nome em uma agenda telefônica

agenda = [
    {"nome": "Ana", "telefone": "1111-1111"},
    {"nome": "Carlos", "telefone": "2222-2222"},
    {"nome": "Daniel", "telefone": "3333-3333"},
    {"nome": "Eduarda", "telefone": "4444-4444"},
    {"nome": "Fernanda", "telefone": "5555-5555"}
]

def buscar_por_nome(lista, nome_procurado):
    baixo = 0
    alto = len(lista) - 1
    
    while baixo <= alto:
    
        meio = (baixo + alto) // 2
        chute = lista[meio]
        
        if chute["nome"] == nome_procurado:
            return chute["telefone"]
        if chute["nome"] > nome_procurado:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

print(buscar_por_nome(agenda, "Carlos"))