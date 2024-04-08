class Manga:

    ''' Lista de objetos contendo os diferentes mangás '''

    estoque = []

    def __init__(self, titulo, autor, volume, preco):
        self._titulo = titulo.title()
        self._autor = autor.title()
        self._volume = volume
        self._preco = preco

    def __str__(self):

        ''' Traduz de maneira legível as classes '''

        return (f"| Título: {self._titulo.ljust(10)} | Autor: {self._autor.ljust(10)} | Volume:"
                f" {self._volume.ljust(10)} | Preço: {self._preco}")

    @classmethod
    def adiciona_manga_na_lista(cls, titulo, autor, volume, preco):

        ''' Adiciona um novo mangá na lista estoque '''

        manga = cls(titulo, autor, volume, preco)
        cls.estoque.append(manga)
        Manga.adiciona_lista_ao_banco()
        Manga.estoque = []

    @classmethod
    def adiciona_lista_ao_banco(cls):

        ''' Preenche o arquivo de texto com os elementos contidos na lista estoque
            servindo como um exemplo de banco de dados. '''

        with open('estoque.txt', 'a') as arquivo:
            for manga in cls.estoque:
                arquivo.write(str(manga) + '\n')

    @classmethod
    def imprimir_estoque(cls):

        ''' Imprime todas as linhas do arquivo estoque.txt '''

        with open('estoque.txt', 'r') as arquivo:
            for linha in arquivo:
                print(linha.strip())

    @classmethod
    def procura_manga(cls, titulo, autor, volume):

        ''' Localiza linhas Específicas no arquivo estoque.txt usando como pesquisa título, autor e volume 
        ( funciona mais ou menos pois é um arquivo.txt, não é uma file ideal para esse tipo de pesquisa, então os resultados não são tão precisos ) '''
        
        encontrado = False
        with open('estoque.txt', 'r') as arquivo:
            for linha in arquivo:
                if (titulo.lower() in linha.lower()) or (autor.lower() in linha.lower()) or (
                        volume.lower() in linha.lower()):
                    print(linha.strip())
                    encontrado = True

            if not encontrado:
                print('Nenhum manga encontrado com os critérios fornecidos.')

    @classmethod
    def retira_manga(cls, titulo, volume):

        ''' Retira uma determinada linha do arquivo estoque.txt que tenha o título e o volume escolhidos '''
        
        encontrado = False
        linhas_modificadas = []

        with open('estoque.txt', 'r') as arquivo:
            for linha in arquivo:
                if (titulo.lower() in linha.lower()) and (volume.lower() in linha.lower()):
                    encontrado = True
                else:
                    linhas_modificadas.append(linha)

        if encontrado:
            with open('estoque.txt', 'w') as arquivo:
                for linha in linhas_modificadas:
                    arquivo.write(linha)

            print('Mangá removido com sucesso.')
        else:
            print('Nenhum mangá encontrado com os critérios fornecidos.')
