from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import glob

# Cria a instância principal da aplicação FastAPI
app = FastAPI()

# 1. Configure o middleware CORS para aceitar requisições de qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Defina caminhos absolutos para a pasta de imagens
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# 3. Crie uma lista chamada `figurinhas` com as 30 figurinhas,
#    cada uma com: id, nome, categoria, imagem_url
#    O imagem_url deve apontar para "/figurinhas/{id}/imagem"
#    Comente as figurinhas que ainda não estão disponíveis
#    Deixe ativas apenas as figurinhas cujas imagens existem na pasta figurinhas/
figurinhas = [
    {
        "id": 1,
        "nome": "Alan Turing",
        "categoria": "IA",
        "imagem_url": "/figurinhas/1/imagem"
    },
    {
        "id": 2,
        "nome": "John McCarthy",
        "categoria": "IA",
        "imagem_url": "/figurinhas/2/imagem"
    },
    {
        "id": 3,
        "nome": "Sam",
        "categoria": "IA",
        "imagem_url": "/figurinhas/3/imagem"
    },
    {
        "id": 4,
        "nome": "Geoffrey",
        "categoria": "IA",
        "imagem_url": "/figurinhas/4/imagem"
    },
    {
        "id": 5,
        "nome": "Yann",
        "categoria": "IA",
        "imagem_url": "/figurinhas/5/imagem"
    },
    {
        "id": 6,
        "nome": "Guido",
        "categoria": "Programação",
        "imagem_url": "/figurinhas/6/imagem"
    },
    {
        "id": 7,
        "nome": "Tim",
        "categoria": "Tecnologia",
        "imagem_url": "/figurinhas/7/imagem"
    },
    {
        "id": 8,
        "nome": "Ray",
        "categoria": "IA",
        "imagem_url": "/figurinhas/8/imagem"
    },
    {
        "id": 9,
        "nome": "Travis",
        "categoria": "Tecnologia",
        "imagem_url": "/figurinhas/9/imagem"
    },
    {
        "id": 10,
        "nome": "Wes",
        "categoria": "Dados",
        "imagem_url": "/figurinhas/10/imagem"
    },
    {
        "id": 11,
        "nome": "Edgar",
        "categoria": "Programação",
        "imagem_url": "/figurinhas/11/imagem"
    },
    {
        "id": 12,
        "nome": "Larry",
        "categoria": "Tecnologia",
        "imagem_url": "/figurinhas/12/imagem"
    },
    {
        "id": 13,
        "nome": "Michael",
        "categoria": "Dados",
        "imagem_url": "/figurinhas/13/imagem"
    },
    {
        "id": 14,
        "nome": "Salvatore",
        "categoria": "Dados",
        "imagem_url": "/figurinhas/14/imagem"
    },
    {
        "id": 15,
        "nome": "Eliot",
        "categoria": "Dados",
        "imagem_url": "/figurinhas/15/imagem"
    },
    {
        "id": 16,
        "nome": "Linus",
        "categoria": "Sistemas Operacionais",
        "imagem_url": "/figurinhas/16/imagem"
    },
    {
        "id": 17,
        "nome": "Dennis",
        "categoria": "Sistemas Operacionais",
        "imagem_url": "/figurinhas/17/imagem"
    },
    {
        "id": 18,
        "nome": "Richard",
        "categoria": "Sistemas Operacionais",
        "imagem_url": "/figurinhas/18/imagem"
    },
    {
        "id": 19,
        "nome": "Bill",
        "categoria": "Tecnologia",
        "imagem_url": "/figurinhas/19/imagem"
    },
    {
        "id": 20,
        "nome": "Steve",
        "categoria": "Tecnologia",
        "imagem_url": "/figurinhas/20/imagem"
    },
    {
        "id": 21,
        "nome": "Paulo",
        "categoria": "Educação",
        "imagem_url": "/figurinhas/21/imagem"
    },
    {
        "id": 22,
        "nome": "Guilherme",
        "categoria": "Educação",
        "imagem_url": "/figurinhas/22/imagem"
    },
    {
        "id": 23,
        "nome": "Gus",
        "categoria": "Educação",
        "imagem_url": "/figurinhas/23/imagem"
    },
    {
        "id": 24,
        "nome": "Mauricio",
        "categoria": "Educação",
        "imagem_url": "/figurinhas/24/imagem"
    },
    {
        "id": 25,
        "nome": "Andre",
        "categoria": "Dados",
        "imagem_url": "/figurinhas/25/imagem"
    },
    {
        "id": 26,
        "nome": "Guilherme",
        "categoria": "Educação",
        "imagem_url": "/figurinhas/26/imagem"
    },
    {
        "id": 27,
        "nome": "Gi",
        "categoria": "Educação",
        "imagem_url": "/figurinhas/27/imagem"
    },
    {
        "id": 28,
        "nome": "Vinicius",
        "categoria": "Educação",
        "imagem_url": "/figurinhas/28/imagem"
    },
    {
        "id": 29,
        "nome": "Rafa",
        "categoria": "Educação",
        "imagem_url": "/figurinhas/29/imagem"
    },
    {
        "id": 30,
        "nome": "Gui",
        "categoria": "Educação",
        "imagem_url": "/figurinhas/30/imagem"
    },
    # {
    #     "id": 30,
    #     "nome": "Ada Lovelace",
    #     "categoria": "Programação",
    #     "imagem_url": "/figurinhas/30/imagem"
    # }
]

# 4. Crie o endpoint GET "/figurinhas" que retorna a lista
@app.get("/figurinhas")
def listar_figurinhas():
    return figurinhas

# 5. Crie o endpoint GET "/figurinhas/{id}/imagem"
@app.get("/figurinhas/{id}/imagem")
def obter_imagem_figurinha(id: int):
    # Usa glob para encontrar o arquivo com prefixo "{id:02d}[!0-9]*" na pasta figurinhas/
    pattern = os.path.join(PASTA_IMAGENS, f"{id:02d}[!0-9]*")
    matching_files = glob.glob(pattern)
    
    # Retorna 404 se não encontrar
    if not matching_files:
        raise HTTPException(status_code=404, detail="Imagem não encontrada")
        
    # Retorna FileResponse com o arquivo encontrado
    return FileResponse(matching_files[0])
