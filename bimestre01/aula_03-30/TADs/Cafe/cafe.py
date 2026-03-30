class Cafeteira:
    def __init__(self, cap_max):
        self.cap_max = cap_max
        self.nivel_agua = 0
        self.nivel_cafe = 0
        self.acesa = False
    
    def abastecer_agua(self, qtd):
        soma_agua = self.nivel_agua + self.nivel_cafe + qtd

        if soma_agua > self.cap_max:
            print("Operação negada. A quantidade de água acrescentada excede a capacidade máxima.")
            return

        self.nivel_agua += qtd

    def abastecer_cafe(self, qtd):
        self.nivel_cafe += qtd

    def acende(self):
        self.acesa = not self.acesa

    def ver_status(self):
        print(f"Nível de água atual: {self.nivel_agua}ml\nNível de café atual: {self.nivel_cafe}\nA cafeteira está {"acesa" if self.acesa else "desligada"}")
    
    def fazer_cafe(self):
        print("Bem vindo à Cafeteira Digital! Começando a fazer seu café...")
        if not self.acesa:
            print("Ligando a cafeteira...")
            self.acende()

        if self.nivel_agua >= 100 and self.nivel_cafe >= 10:
            self.nivel_agua -= 100
            self.nivel_cafe -= 10

            print("Fazendo café...")
            print("Seu café está pronto!!!")
            return
        
        print("Insumos insuficientes (Água ou Café)")