# 1.5 Você quer ler o número de cada pessoa da agenda telefônica.

agenda = [
    {"nome": "Ana", "telefone": "1111-1111"},
    {"nome": "Carlos", "telefone": "2222-2222"},
    {"nome": "Daniel", "telefone": "3333-3333"},
    {"nome": "Eduarda", "telefone": "4444-4444"},
    {"nome": "Fernanda", "telefone": "5555-5555"}
]   

def ler_agenda_inteira(lista):
    for contato in lista:
        print(f"Nome: {contato['nome']} | Tel: {contato['telefone']}")

ler_agenda_inteira(agenda)