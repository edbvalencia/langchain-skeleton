import os

from dotenv import find_dotenv, load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI, OpenAI

load_dotenv(find_dotenv(), override=True)

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]


template = """
Escribe un mensaje corto muy sintetizado de felicitaciones a {nombre} por su {ocasion}  
"""

prompt = PromptTemplate(input_variables=["nombre", "ocasion"], template=template)


llm = OpenAI(temperature=0.7, max_tokens=1024)

respuesta = llm(prompt.format(nombre="Eduardo", ocasion="Graduación"))
print(respuesta)
