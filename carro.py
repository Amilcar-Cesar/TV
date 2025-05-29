class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

carro = Carro(marca="Fiat",modelo="Palio",ano= 2015)

print(carro.get_marca())

carro.set_marca("Toyota")
print("Nova marca do carro:", carro.get_marca())