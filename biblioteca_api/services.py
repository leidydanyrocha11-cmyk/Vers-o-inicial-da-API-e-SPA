from sqlalchemy.orm import Session

from biblioteca_api.models import Livro
from schemas import LivroCreate


def criar_livro(db: Session, dados: LivroCreate):
    livro = Livro(**dados.model_dump())

    db.add(livro)
    db.commit()
    db.refresh(livro)

    return livro


def listar_livros(db: Session):
    return db.query(Livro).all()


def buscar_livro(db: Session, livro_id: int):
    return db.query(Livro).filter(Livro.id == livro_id).first()


def atualizar_livro(db: Session, livro_id: int, dados: LivroCreate):
    livro = buscar_livro(db, livro_id)

    if not livro:
        return None

    for campo, valor in dados.model_dump().items():
        setattr(livro, campo, valor)

    db.commit()
    db.refresh(livro)

    return livro


def excluir_livro(db: Session, livro_id: int):
    livro = buscar_livro(db, livro_id)

    if not livro:
        return False

    db.delete(livro)
    db.commit()

    return True