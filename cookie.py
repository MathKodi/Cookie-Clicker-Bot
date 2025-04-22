from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, 'cookie')

start_time = time.perf_counter()
check_interval = 5  # segundos
duration_limit = 300  # 5 minutos

while True:
    cookie.click()

    current_time = time.perf_counter()

    if current_time - start_time >= duration_limit:
        cps = driver.find_element(By.ID, 'cps').text
        print(f"Tempo encerrado! Cookies por segundo: {cps}")
        break

    if int(current_time - start_time) % check_interval == 0:
        try:
            money_elem = driver.find_element(By.ID, 'money')
            money_str = money_elem.text.replace(",", "")
            money = int(money_str) if money_str.isdigit() else 0

            items = driver.find_elements(By.CSS_SELECTOR, '#store b')
            affordable_upgrades = {}

            for item in items:
                text = item.text
                if "-" in text:
                    name, price_text = text.split("-")
                    price_text = price_text.strip().replace(",", "")
                    if price_text.isdigit():
                        price = int(price_text)
                        if price <= money:
                            parent = item.find_element(By.XPATH, "..")
                            affordable_upgrades[price] = parent

            if affordable_upgrades:
                most_expensive = max(affordable_upgrades.keys())
                affordable_upgrades[most_expensive].click()
        except Exception as e:
            print(f"Erro ao tentar comprar: {e}")