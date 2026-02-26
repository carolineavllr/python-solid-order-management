from cliente import Cliente
from item import Item
from pedido.pedido_delivery import PedidoDelivery
from pagamento.pagamento_factory import PagamentoFactory
from notificacao.notificacao_facade import NotificacaoFacade
from observador.observador_status import ObservadorStatus


# criando cliente, itens e pedidos
cliente = Cliente("Caroline Avellar", "Rua das Flores, 123")
item_1 = Item("Notebook", 2500.00)
item_2 = Item("Mouse", 150.00)
itens = [item_1, item_2]

taxa_entrega = 10.0
pedido = PedidoDelivery(cliente, itens, taxa_entrega)


# processando pagamento para pedido delivery
valor_pedido = pedido.calcular_total()
tipo_pagamento = "pix"
pagamento = PagamentoFactory.criar_pagamento(tipo_pagamento).processar_pagamento(
    valor_pedido
)


# enviando notificações para o cliente
MENSAGEM_PAGO = "O pagamento foi confirmado!"
MENSAGEM_PREPARANDO = "O pedido está sendo preparado!"
MENSAGEM_ENVIADO = "O pedido saiu para a entrega!"

notificacoes = NotificacaoFacade()
observador = ObservadorStatus(notificacoes)
pedido.adicionar_observadores(observador)

pedido.status = MENSAGEM_PAGO
pedido.status = MENSAGEM_PREPARANDO
pedido.status = MENSAGEM_ENVIADO
