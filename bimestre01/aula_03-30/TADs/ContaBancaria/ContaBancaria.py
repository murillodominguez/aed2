class ContaBancaria:
    def __init__(self, numero_conta, titular, _saldo):
        self.numero_conta = numero_conta
        self.titular = titular
        self._saldo = _saldo

    def depositar(self, valor):
        if valor < 0:
            print("Não é possível depositar valores negativos.")
            return
        self._saldo += valor

    def sacar(self, valor):
        if valor > self._saldo:
            print("Saldo insuficiente para operação de saque.")
            return
        self._saldo -= valor
        print(f"Você sacou R${valor:.2f}")