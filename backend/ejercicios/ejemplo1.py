"""
PRIMEROS PASOS CONFIGURACION Y PRUEBA
# Configuro variables de entorno
# Pruebo la herramienta 
"""


import os

from dotenv import find_dotenv, load_dotenv
from langchain_openai import OpenAI

load_dotenv(find_dotenv(), override=True)

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

llm = OpenAI()
print("Ejemplo 2")
print(llm.invoke("Ojo por ojo diente... ", max_tokens=6))
