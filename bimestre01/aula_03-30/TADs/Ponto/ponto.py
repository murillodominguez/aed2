from math import sqrt

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(f"Ponto criado: ({x},{y})")

    def distancia(p1, p2):
        dx = p2.x - p1.x
        dy = p2.y - p1.y
        return sqrt(dx**2 + dy**2)
    