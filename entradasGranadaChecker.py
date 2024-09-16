import requests
import time

url = "https://entradas.granadacf.es/api/visit/events/available-public"

interval = 5 * 60

def check_endpoint():
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()

        if not data:
            print("Todavia no estan las entradas")
        else:
            print("Las entradas han salido ya a la venta")
    
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")

while True:
    check_endpoint()
    time.sleep(interval)
