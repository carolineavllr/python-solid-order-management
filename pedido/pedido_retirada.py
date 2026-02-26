from pedido.pedido import Pedido


# classe para pedidos de retirada, seguindo o princípio de aberto/fechado (OCP)
class PedidoRetirada(Pedido):
    # o cálculo do total para retirada é apenas a soma dos preços dos itens, seguindo o princípio de substituição de Liskov (LSP)
    def calcular_total(self):
        return sum(item.preco for item in self.itens)
