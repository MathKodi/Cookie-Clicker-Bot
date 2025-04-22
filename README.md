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
- ChromeDriver compatível com sua versão do Chrome

---

## 📦 Instalação

1. Clone o repositório ou copie o script Python.
2. Instale a biblioteca Selenium com o comando:

pip install selenium

3. Certifique-se de que o ChromeDriver está instalado e disponível no PATH do sistema, ou especifique o caminho diretamente no script.

---

## ▶️ Como usar

Execute o script com o Python:

python cookie_bot.py

O navegador será aberto automaticamente, e o bot começará a jogar.

---

## 📝 Resultado esperado

Após 5 minutos, o terminal exibirá algo como:

Tempo encerrado! Cookies por segundo: 123.4

---

## ⚠️ Observações

- O script simula cliques e interações reais com a página. Não o use em competições ou ambientes onde automação não é permitida.
- O site usado é uma versão experimental do Cookie Clicker, apenas para fins de aprendizado.

---

## 📄 Licença

Este projeto é livre para uso pessoal e educacional.
