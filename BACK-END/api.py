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
    return {"mensagem": "🎥Gerenciador de filmes🎬"}

@app.post("/filmes")
def criar_filmes(titulo: str, genero: str, ano: int, avaliacao: float):
    inserir_filme(titulo, genero, ano, avaliacao)
    return {"mensagem": "Filme adicionado com sucesso!!! ✔"}

@app.get("/listar_filmes")
def exibir():
    filmes = listar_filme()
    lista = []
    for linha in filmes:
        lista.append({ "id": linha[0], 
            "titulo":linha[1],
            "genero": linha[2],
            "ano": linha[3],
            "avaliacao": linha[4]
        })
    return {"filmes": lista}

