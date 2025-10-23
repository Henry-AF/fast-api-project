from fastapi import FastAPI, HTTPException
from app.models import alunos_db

app = FastAPI()


@app.get("/alunos")
def listar_alunos():
    return alunos_db


@app.get("/alunos/{aluno_id}")
def buscar_aluno(aluno_id: int):
    aluno = next((a for a in alunos_db if a["id"] == aluno_id), None)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno


@app.post("/alunos")
def criar_aluno(aluno: dict):
    # Validação simples para garantir que nome e email existem
    if "nome" not in aluno or "email" not in aluno:
        raise HTTPException(
            status_code=422, detail="Campos 'nome' e 'email' são obrigatórios"
        )

    novo_id = max([a["id"] for a in alunos_db]) + 1 if alunos_db else 1
    novo_aluno = {"id": novo_id, "nome": aluno["nome"], "email": aluno["email"]}
    alunos_db.append(novo_aluno)
    return novo_aluno
