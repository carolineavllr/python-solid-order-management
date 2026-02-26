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

## **Output esperado**
<img width="917" height="148" alt="Screenshot from 2026-02-25 23-11-18" src="https://github.com/user-attachments/assets/0b4319d3-e69f-4355-a310-fc145357589a" />


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
