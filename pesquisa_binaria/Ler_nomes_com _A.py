''' Você quer ler os números apenas dos nomes que começam com A. (Isso
é complicado! Esse algoritmo envolve conceitos que são abordados mais
profundamente no Capítulo 4. Leia a resposta – você cará surpreso!)'''

agenda = [
    {"nome": "Ana", "telefone": "1111-1111"},
    {"nome": "Carlos", "telefone": "2222-2222"},
    {"nome": "Daniel", "telefone": "3333-3333"},
    {"nome": "Eduarda", "telefone": "4444-4444"},
    {"nome": "Fernanda", "telefone": "5555-5555"}
]   
def ler_apenas_letra_a(lista):
    for contato in lista:
        if contato["nome"].startswith("A"):
            print(f"Encontrado com A: {contato['nome']}")

ler_apenas_letra_a(agenda)