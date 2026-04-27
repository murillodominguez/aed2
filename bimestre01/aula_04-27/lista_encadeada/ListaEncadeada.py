class Node:
    def __init__(self, dado):
        self.info = dado # valor armazenado no nó
        self.prox = None # ponteiro para o próximo nó

    def link_node(self, new_node):
        self.prox = new_node

class ListaEncadeada:
    def __init__(self):
        self.ini = None
        self.tam = 0

    def add_node(self, node: Node):
        if self.tam == 0:
            self.ini = Node
        self.ini.link_node(node)
        self.tam += 1