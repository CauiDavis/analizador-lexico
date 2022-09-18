

class lexico:
    
    def __init__(self, arquivo_fonte):
        self.__cabeca = 0
        self.__fita = []
        self.__tabela_de_simbolos = []
        self.__lexema = ''
        self.__fim_linha = '\n'
        self.__especiais = ['+','-','*','/','(',')','<','>','=',':',';']
        self.__arquivo_fonte = arquivo_fonte
        if not os.path.exists(self.__arquivo_fonte):
            util.erro("erro geral: arquivo {0} nao foi encontrado".format(self.__arquivo_fonte))
        else:
            self.__arquivo = open(self.__arquivo_fonte, 'r')
    
    def __avancar_cabeca(self):
        self.__cabeca += 1
    
    def __posicao_cabeca(self):
        return self.__cabeca
    
    def __atualizar_numero_linha(self):
        self.__numero_linha += 1
    
    def __obter_caracter(self):
        if self.__cabeca < len(self.__fita):
            self.__letra = self.__fita[self.__cabeca]
            self.__avancar_cabeca()
            if self.__letra != self.__fim_linha or not self.__letra.isspace():
                self.__lexema += self.__letra
            return self.__letra
        else:
            return '\n'
    
    def obter_tabela_tokens(self):
        for self.__linha in self.__arquivo:
            self.__fita = list(self.__linha)
            self.__q0()
            self.__atualizar_numero_linha()
            self.__cabeca = 0
        self.__arquivo.close()
        return self.__tabela_de_simbolos
    
    def __q0(self):
        self.__caracter = self.__obter_caracter()
        if 'r' == self.__caracter:
            self.__q1()