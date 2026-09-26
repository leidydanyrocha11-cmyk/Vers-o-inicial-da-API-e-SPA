from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from biblioteca_api.database import Base, engine, get_db
from .schemas import LivroCreate, LivroResponse
from biblioteca_api import services


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Biblioteca API", version="1.0.0")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/livros", response_model=list[LivroResponse])
def listar_livros(db: Session = Depends(get_db)):
    return services.listar_livros(db)


@app.get("/livros/{livro_id}", response_model=LivroResponse)
def buscar_livro(livro_id: int, db: Session = Depends(get_db)):
    livro = services.buscar_livro(db, livro_id)

    if not livro:
        raise HTTPException(
            status_code=404,
            detail="Livro não encontrado"
        )

    return livro


@app.post("/livros", response_model=LivroResponse, status_code=201)
def criar_livro(dados: LivroCreate, db: Session = Depends(get_db)):
    return services.criar_livro(db, dados)


@app.put("/livros/{livro_id}", response_model=LivroResponse)
def atualizar_livro(
    livro_id: int,
    dados: LivroCreate,
    db: Session = Depends(get_db)
):
    livro = services.atualizar_livro(db, livro_id, dados)

    if not livro:
        raise HTTPException(
            status_code=404,
            detail="Livro não encontrado"
        )

    return livro


@app.delete("/livros/{livro_id}", status_code=204)
def excluir_livro(livro_id: int, db: Session = Depends(get_db)):
    if not services.excluir_livro(db, livro_id):
        raise HTTPException(
            status_code=404,
            detail="Livro não encontrado"
        )