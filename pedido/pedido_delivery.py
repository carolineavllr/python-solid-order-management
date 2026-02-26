from pedido.pedido import Pedido


# classe para pedidos de delivery, seguindo o princípio de aberto/fechado (OCP)
class PedidoDelivery(Pedido):
    def __init__(self, cliente, itens, taxa_entrega):
        super().__init__(cliente, itens)
        self.taxa_entrega = taxa_entrega

    def calcular_total(self):
        total = sum(item.preco for item in self.itens) + self.taxa_entrega
        return total
