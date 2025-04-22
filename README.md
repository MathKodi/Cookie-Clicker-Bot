# 🧁 Cookie Clicker Bot com Selenium

Este é um bot automatizado usando **Selenium** para jogar [Cookie Clicker](https://orteil.dashnet.org/experiments/cookie/). Ele clica no cookie automaticamente e, a cada 5 segundos, tenta comprar o item mais caro possível da loja com base no dinheiro atual. O bot roda por 5 minutos e, ao final, exibe os cookies por segundo (CPS).

---

## 🚀 Como funciona

- Clica continuamente no cookie principal.
- A cada 5 segundos:
  - Verifica quanto dinheiro você tem.
  - Identifica todos os itens da loja.
  - Compra o item **mais caro que for possível pagar**.
- Após 5 minutos:
  - O bot para automaticamente.
  - Exibe o valor atual de **cookies por segundo (CPS)** no console.

---

## 🧰 Requisitos

- Python 3.x
- Google Chrome
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) compatível com sua versão do Chrome

---

## 📦 Instalação

1. Clone o repositório ou copie o script Python.
2. Instale as dependências:

```bash
pip install selenium
