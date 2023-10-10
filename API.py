# ALTO RENDIMIENTO
# GENERA DOCUMENTACIÓN AUTOMÁTICA
# VALIDACIÓN DE DATOS (PARÁMETROS OPCIONALES)

import random
from genSaldo import generar_json_saldo
from genTarjetas import generar_json_tarjetas
from genCuentas import generar_json_cuentas
from genUltMovimientos import generarFechas

from fastapi import FastAPI, HTTPException, Request

import asyncio

app = FastAPI()

# Variable para realizar un seguimiento del número de solicitudes
request_count = 0

@app.post('/billetera/redlink/login')
async def login(request: Request):
      
    global request_count  # Accede a la variable global, es la que esta afuera.
    request_count += 1  # Incrementar el conteo de solicitudes
    base_delay = 0.2  # Tiempo de demora inicial en segundos
    exponential_factor = 0.001  # Factor exponencial para ajustar la velocidad de aumento
    # Calcular el tiempo de demora utilizando una fórmula exponencial
    delay_seconds = base_delay * (2 ** (exponential_factor * request_count))
    # Aplica la demora utilizando asyncio.sleep
    await asyncio.sleep(delay_seconds)
    json_generado = generar_json_tarjetas()
    return json_generado

@app.post('/billetera/redlink/logout')
async def ultmovimientos():
    global request_count  # Accede a la variable global
    request_count += 1  # Incrementar el conteo de solicitudes
    base_delay = 0.01  # Tiempo de demora inicial en segundos
    exponential_factor = 0.001  # Factor exponencial para ajustar la velocidad de aumento
    # Calcular el tiempo de demora utilizando una fórmula exponencial
    delay_seconds = base_delay * (2 ** (exponential_factor * request_count))
    # Aplica la demora utilizando asyncio.sleep
    await asyncio.sleep(delay_seconds)
    #raise HTTPException(status_code=500, detail="Error interno del servidor")
    return {"message": "Has cerrado sesion exitosamente"}

@app.post("/billetera/redlink/cuentas")
async def cuentas():
    global request_count  # Accede a la variable global
    request_count += 1  # Incrementar el conteo de solicitudes
    base_delay = 0.04  # Tiempo de demora inicial en segundos
    exponential_factor = 0.001  # Factor exponencial para ajustar la velocidad de aumento
    # Calcular el tiempo de demora utilizando una fórmula exponencial
    delay_seconds = base_delay * (2 ** (exponential_factor * request_count))
    # Aplica la demora utilizando asyncio.sleep
    await asyncio.sleep(delay_seconds)
    # Verifica si 'nrotarjeta' está presente en los datos
    
    return generar_json_cuentas()

    

@app.post('/billetera/redlink/saldo')
async def saldo(request: Request):
    global request_count  # Accede a la variable global
    request_count += 1  # Incrementar el conteo de solicitudes
    base_delay = 0.02  # Tiempo de demora inicial en segundos
    exponential_factor = 0.001  # Factor exponencial para ajustar la velocidad de aumento
    # Calcular el tiempo de demora utilizando una fórmula exponencial
    delay_seconds = base_delay * (2 ** (exponential_factor * request_count))
    # Aplica la demora utilizando asyncio.sleep
    await asyncio.sleep(delay_seconds)
    # print(request.headers)
    json_generado = generar_json_saldo()
    #body = {"tarjetas":[{"numero":"125055111609","descripcion":"BANCO BICA"},{"numero":"736200459801","descripcion":"BANCO DE SALTA"},{"numero":"872000234502","descripcion":"BANCO LIBRE"}]}
    return json_generado

@app.post('/billetera/redlink/ultmovimientos')
async def ultmovimientos(fecha_desde: str,fecha_hasta: str):
    global request_count  # Accede a la variable global
    request_count += 1  # Incrementar el conteo de solicitudes
    base_delay = 0.01  # Tiempo de demora inicial en segundos
    exponential_factor = 0.001  # Factor exponencial para ajustar la velocidad de aumento
    # Calcular el tiempo de demora utilizando una fórmula exponencial
    delay_seconds = base_delay * (2 ** (exponential_factor * request_count))
    # Aplica la demora utilizando asyncio.sleep
    await asyncio.sleep(delay_seconds)
    
    # random_number = random.randint(0, 9)

    # if random_number == 0:
    #     raise HTTPException(status_code=500, detail="Error interno del servidor")
    # else:
    # bodyjson = await request.json()
    # fecha_desde = bodyjson["fecha desde"]
    # fecha_hasta = bodyjson["fecha hasta"]
    return generarFechas(fecha_desde,fecha_hasta)
    

    