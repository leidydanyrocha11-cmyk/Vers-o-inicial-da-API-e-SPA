from unittest.mock import MagicMock

from schemas import LivroCreate
import services


def test_criar_livro_com_mock():
    db = MagicMock()

    dados = LivroCreate(
        titulo="Dom Casmurro",
        autor="Machado de Assis",
        ano_publicacao=1899,
        disponivel=True
    )

    resultado = services.criar_livro(db, dados)

    db.add.assert_called_once()
    db.commit.assert_called_once()
    db.refresh.assert_called_once()

    assert resultado is not None


def test_buscar_livro_com_mock():
    db = MagicMock()

    livro_falso = MagicMock(id=10, titulo="Livro de Teste")

    db.query.return_value.filter.return_value.first.return_value = livro_falso

    resultado = services.buscar_livro(db, 10)

    assert resultado.id == 10
    assert resultado.titulo == "Livro de Teste"