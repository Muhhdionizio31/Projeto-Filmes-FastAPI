from fastapi import FastAPI
from funcao import inserir_filme, listar_filme, atualizar_filme, deletar_filme

# Rodar o FastApi
"""python -m uvicorn api:app --reload"""

# Testar api FastAPI
""" /dosc > Documentação Swagger """
""" /redoc > Documentação  redoc """

# Iniciar FstApi
app = FastAPI(title="Gerenciador de filmes")

# GET = Pegar / Listar
# POST = Criar / Enviar 
# PUT = Atualiar
# DELETE = Deletar

@app.get("/")
def home():
    return {"mensagem": "Quero chocolate"}

@app.post("/filmes")
def criar_filmes(titulo: str, genero: str, ano: int, avaliacao: float):
    inserir_filme(titulo, genero, ano, avaliacao)
    return {"mensagem": "Filme adicionado com sucesso!!! ✔"}