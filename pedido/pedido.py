from abc import ABC, abstractmethod


class Pedido(ABC):
    def __init__(self, cliente, itens):
        self.cliente = cliente
        self.itens = itens
        self._status = "Criado!"
        self.observadores = []

    @property
    def status(self):
        return self._status

    # método para atualizar o status do pedido e notificar os observadores
    @status.setter
    def status(self, novo_status):
        self._status = novo_status
        self.notificar_observadores()

    # método para adicionar observadores ao pedido
    def adicionar_observadores(self, observador):
        self.observadores.append(observador)

    # método para notificar os observadores sobre a mudança de status
    def notificar_observadores(self):
        for observador in self.observadores:
            observador.atualizar(self)

    # método abstrato para calcular o total do pedido, a ser implementado pelas subclasses
    @abstractmethod
    def calcular_total(self):
        pass
