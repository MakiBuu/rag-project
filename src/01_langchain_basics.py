from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline
# Utilizando modelo Local

prompt = PromptTemplate.from_template(
    "Responde a la siguiente pregunta de manera muy breve. Pregunta:{pregunta} Respuesta:"
)

# Ahora utilizamos un LLM local (modelo pequeño):
pipe = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct",
    max_new_tokens=50
)

llm_local = HuggingFacePipeline(pipeline=pipe)

parser = StrOutputParser()

cadena_local = prompt | llm_local | parser
resultado = cadena_local.invoke({"pregunta" : "¿Cuál es el planeta más grande del sistema solar?"})
print(resultado)
