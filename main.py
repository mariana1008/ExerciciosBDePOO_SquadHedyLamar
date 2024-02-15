from clear import clear
from time import sleep

def iniciar_biblioteca():
    print("Biblioteca iniciada")

def finalizar_biblioteca():
    print("Biblioteca finalizada")
    exit()

while True:
    print("1. Adicionar usuário")
    print("2. Adicionar livro")
    print("3. Empretar livro")
    print("4. Devolver livro")
    print("5. bucar livro")
    print("6. bucar usuário")
    option = int(input("Opção: "))

    if option == 1:
        iniciar_biblioteca()
    elif option == 2:
        finalizar_biblioteca()
        break
    else:
        print("Opção inválida")
    sleep(0.5)
    clear()