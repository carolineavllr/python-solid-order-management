# python-solid-order-management

- Design Patterns: _Factory Method, Template, Strategy, Facade, Observer_.
- Princípios **SOLID**.

---

## **Estrutura do Projeto**

```
.
├── cliente.py
├── item.py
├── main.py
├── notificacao/
│   ├── notificacao.py
│   ├── notificacao_email.py
│   ├── notificacao_sms.py
│   └── notificacao_facade.py
├── observador/
│   └── observador_status.py
├── pagamento/
│   ├── pagamento.py
│   ├── pagamento_cartao.py
│   └── pagamento_pix.py
├── pedido/
│   ├── pedido.py
│   ├── pedido_delivery.py
│   └── pedido_retirada.py
└── README.md
```

---

## **Como Executar**

1. Acesse o arquivo `main.py`.
2. Execute o programa:
   ```bash
   python main.py
   ```

---

## **Exemplo de Uso**

- **Cadastrar Cliente e Itens**:
  Crie um cliente e adicione itens ao pedido.
- **Criar Pedido**:
  Escolha entre _delivery_ ou _retirada_.
- **Efetuar Pagamento**:
  Simule pagamentos via Pix ou Cartão.
- **Receber Notificações**:
  Clientes recebem notificações do status do pedido.

---

## **Autoria**

Projeto desenvolvido como estudo dos princípios **SOLID** e padrões de design para organização de software escalável e modular.
