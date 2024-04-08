from modulos.manga import Manga


def finaliza_app():
    print('\n'*80)
    print('FIM DO PROGRAMA')


def retira():
    print()
    Manga.imprimir_estoque()
    print()
    print('Digite o título e o volume do mangá que deseja retirar do estoque.')
    titulo = input('Digite o título do mangá: ')
    volume = input('Digite o volume do mangá: ')
    Manga.retira_manga(titulo, volume)
    print()
    input('Pressione qualquer botão do teclado para voltar ao menu.')
    main()


def procura():
    titulo = input('Digite o título do mangá: ')
    autor = input('Digite o autor do mangá: ')
    volume = input('Digite o volume do mangá: ')
    Manga.procura_manga(titulo, autor, volume)


def lista_estoque():
    print()
    Manga.imprimir_estoque()
    print()
    input('Pressione qualquer botão do teclado para voltar ao menu.')
    main()


def adiciona():

    ''' Adiciona um novo mangá num banco de dados '''

    print()
    titulo = input('Digite o título do mangá: ')
    autor = input('Digite o autor do mangá: ')
    volume = input('Digite o volume do mangá: ')
    preco = input('Digite o preço do mangá: ')
    Manga.adiciona_manga_na_lista(titulo, autor, volume, preco)
    main()


def escolhe_opcao():

    ''' Recebe a escolha do usuário e filtra erros '''

    try:
        escolha = int(input('Escolha uma opção: '))
        if 1 <= escolha <= 5:
            if escolha == 1:
                adiciona()
            elif escolha == 2:
                retira()
            elif escolha == 3:
                procura()
            elif escolha == 4:
                lista_estoque()
            elif escolha == 5:
                finaliza_app()
        else:
            print('Escolha uma opção válida [1 a 5]')
            input('Pressione qualquer botão do teclado para voltar ao menu.')
            main()
    except ValueError:
        print('Escolha uma opção válida [1 a 5]')
        input('Pressione qualquer botão do teclado para voltar ao menu.')
        main()


def menu():

    ''' Exibe menu com as opções para o usuário escolher '''

    print('-------------------')
    print('𝙇𝙞𝙫𝙧𝙖𝙧𝙞𝙖 𝙎𝙚𝙡𝙛 𝙏𝙖𝙪𝙜𝙝𝙩')
    print('-------------------')
    print('1. Adicionar Mangá no Estoque.')
    print('2. Retirar Mangá do Estoque.')
    print('3. Procurar Mangá no Estoque.')
    print('4. Listar Estoque.')
    print('5. Sair do Programa.')
    print('-------------------')


def main():

    ''' Define a ordem principal do funcionamento do programa e suas funções '''
    print(f'\n' * 80)
    menu()
    escolhe_opcao()


if __name__ == '__main__':
    main()
