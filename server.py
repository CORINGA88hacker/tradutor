from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import threading
import time

app = Flask(__name__)

# Função que executa o bot para cada conta
def enviar_seguidores(alvo):
    with open("contas.txt", "r") as f:
        contas = [linha.strip().split(":") for linha in f.readlines()]

    for usuario, senha in contas:
        print(f"Logando com {usuario}...")
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Comente essa linha para ver o navegador
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)

        try:
            driver.get("https://www.instagram.com/accounts/login/")
            time.sleep(5)

            driver.find_element(By.NAME, "username").send_keys(usuario)
            driver.find_element(By.NAME, "password").send_keys(senha)
            driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
            time.sleep(7)

            driver.get(f"https://www.instagram.com/{alvo}/")
            time.sleep(5)

            btn_seguir = driver.find_element(By.XPATH, "//button[contains(text(),'Seguir')]")
            btn_seguir.click()
            print(f"{usuario} seguiu {alvo}")
            time.sleep(3)

        except Exception as e:
            print(f"Erro com {usuario}: {e}")

        finally:
            driver.quit()

@app.route("/enviar", methods=["POST"])
def enviar():
    data = request.get_json()
    alvo = data.get("alvo")

    if not alvo:
        return jsonify({"mensagem": "Usuário alvo não informado!"}), 400

    # Rodar o bot em thread para não travar o servidor
    thread = threading.Thread(target=enviar_seguidores, args=(alvo,))
    thread.start()

    return jsonify({"mensagem": f"Envio iniciado para @{alvo}. Aguarde."})

if __name__ == "__main__":
    app.run(debug=True)
