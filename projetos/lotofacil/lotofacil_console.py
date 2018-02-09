import os, sys

menu_actions = {}

def main_menu():
    """ Exibe o menu principal """

    os.system('cls')
    print('Boas vindas!')
    print("Por favor, escolha uma das opções para começar.\n")

    print("1 - Configuração inicial do programa")
    #print("2. Configuração inicial do programa")
    print("0 - Para sair")

    choice = input('>> ')
    execute_action(choice)


def execute_action(choice):
    """Executa uma opção escolhida"""

    os.system('cls')

    choice = choice.lower()
    if choice == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[choice]()
        except KeyError:
            print('Opção selecionada inválida.')
            menu_actions['main_menu']()


def exit_menu():
    """Sai do programa."""
    sys.exit()

# define os itens do menu
menu_actions = {
    'main_menu': main_menu,
    '0': exit_menu
}

if __name__ == "__main__":
    main_menu()


