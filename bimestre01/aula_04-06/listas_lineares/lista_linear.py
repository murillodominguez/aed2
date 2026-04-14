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
        tamanho = self.tamanho()
        if (pos <= 0 or pos > tamanho + 1) or (self.ini == 0 and self.fim == self.max - 1):
            return False

        if self.is_vazio():
            self.ini = 0
            self.fim = 0
        
        elif self.fim != self.max - 1 and self.ini != 0:
            go_left = False
            go_right = False
            print("Inserindo!")
            center = tamanho // 2 + 1
            if pos <= center:
                print("Vai esquerda!")
                go_left = True
            else:
                go_right = True
            
            if go_right:
                for i in range(self.fim, self.ini + pos - 2, -1):
                    self.vetor[i+1] = self.vetor[i]
                self.fim += 1

            if go_left:
                for i in range(self.ini, self.ini + pos - 1):
                    self.vetor[i-1] = self.vetor[i]
                self.ini -= 1

        elif self.fim != self.max - 1:
            for i in range(self.fim, self.ini + pos - 2, -1):
                self.vetor[i+1] = self.vetor[i]
            self.fim += 1
        else:
            for i in range(self.ini, self.ini + pos - 1):
                self.vetor[i-1] = self.vetor[i]
            self.ini -= 1

        self.vetor[self.ini + pos - 1] = node
        return True
    
    def remover(self, pos):
        if self.is_vazio() or (pos > self.tamanho() or pos <= 0):
            return False
        
        if pos != 1 and pos != self.tamanho():
            center = self.tamanho() // 2
            if pos <= center:
                for i in range(self.ini + pos - 2, self.ini - 1, -1):
                    self.vetor[i+1] = self.vetor[i]
                    if i == self.ini:
                        self.vetor[i] = None
                self.ini += 1
            else:
                for i in range(self.ini + pos, self.fim + 1):
                    self.vetor[i-1] = self.vetor[i]
                    if i == self.fim:
                        self.vetor[i] = None
                self.fim -= 1
        elif pos == 1:
            self.vetor[self.ini + pos - 1] = None
            self.ini += 1
            if self.tamanho() == 0:
                self.ini = -1
                self.fim = -1
        else:
            self.vetor[self.ini + pos - 1] = None
            self.fim -= 1
        
        return True

                    
            
        
    