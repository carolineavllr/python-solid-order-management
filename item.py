class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"Item: {self.nome}, Preco: {self.preco}"
