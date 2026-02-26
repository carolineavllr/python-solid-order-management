from pagamento.pagamento import Pagamento


class PagamentoPix(Pagamento):
    def processar_pagamento(self, valor):
        print(f"Processando pagamento de R${valor:.2f} com PIX.")
