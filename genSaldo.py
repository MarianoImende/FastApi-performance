import random
from babel.numbers import format_currency

locale.setlocale(locale.LC_ALL, 'C.UTF-8')

# Función para generar un JSON con un saldo aleatorio en formato de dinero
def generar_json_saldo():
    saldo = random.uniform(100, 1000000)  # Generar un número aleatorio entre 100 y 1,000,000
    saldo_formateado = format_currency(saldo, 'USD', locale='es_AR')  # Formatear el número como dinero en dólares (puedes ajustar la moneda si es diferente)

    data = {
        "saldo": saldo_formateado
    }

    return data  # Devuelve el JSON como cadena con formato

