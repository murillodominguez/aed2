class ListaLinear:
    def __init__(self, max: int):
        self.max = max
        self.vetor = [None] * self.max
        self.ini = -1
        self.fim = -1

    def tamanho(self):
        if self.is_vazio():
            return 0
        
        return self.fim - self.ini + 1

    def is_vazio(self):
        for node in self.vetor:
            if node != None:
                return False

        return True

    def exibir(self):
        print(self.vetor)
        print("INICIO E FIM:",self.ini,self.fim)

    def inserir(self, pos: int, node: int):
        if (pos <= 0 or pos > self.tamanho() + 1) or (self.ini == 0 and self.fim == self.max - 1):
            return False

        if self.is_vazio():
            self.ini = 0
            self.fim = 0

        # if self.ini != 0 and self.fim != self.max - 1:
        #     go_left = False
        #     go_right = False

        #     elem_to_the_left = self.ini
        
        elif self.fim != self.max - 1:
            for i in range(self.fim, self.ini + pos - 2, -1):
                self.vetor[i+1] = self.vetor[i]
                print(i)
            self.fim += 1
        else:
            for i in range(self.ini, self.ini + pos - 1):
                self.vetor[i-1] = self.vetor[i]
                print(i)
            self.ini -= 1
            print(node)
            print(self.vetor)
        print(self.ini + pos - 1)
        self.vetor[self.ini + pos - 1] = node
        return True