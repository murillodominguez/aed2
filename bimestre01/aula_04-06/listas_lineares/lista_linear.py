class ListaLinear:
    def __init__(self, max):
        self.max = max
        self.vetor = [None] * self.max
        self.ini = -1
        self.fim = -1

    def tamanho(self):
        if self.is_vazio:
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

    def inserir(self, node, pos):
        if(pos < 0):
            return False

        if self.is_vazio():
            self.ini = 0
            self.fim = 0
        
        elif self.fim < self.max-1:
            for i in range(self.fim, self.ini + pos - 2, -1):
                self.vetor[i+1] = self.vetor[i]

            self.fim = self.fim + 1

        self.vetor[self.ini + pos - 1] = node
        self.ini = pos
            
