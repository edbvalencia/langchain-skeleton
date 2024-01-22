"""
EJEMPLO DE PROMT TEMPLATE LANGCHAIN
# Este script utiliza la API de OpenAI para generar mensajes de felicitación personalizados.
# Se configura una plantilla con marcadores de posición para el nombre y la ocasión,
# se inicializa el modelo de lenguaje de OpenAI y se genera un mensaje específico.
"""

import os

from dotenv import find_dotenv, load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

load_dotenv(find_dotenv(), override=True)

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]


template = """
Escribe un mensaje corto muy sintetizado de felicitaciones a {nombre} por su {ocasion}  
"""

prompt = PromptTemplate(input_variables=["nombre", "ocasion"], template=template)


llm = OpenAI(temperature=0.7)

respuesta = llm(prompt.format(nombre="Eduardo", ocasion="Graduación"))
print(respuesta)
