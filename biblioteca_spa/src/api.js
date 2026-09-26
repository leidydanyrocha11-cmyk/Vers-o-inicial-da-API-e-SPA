const API_URL = "http://127.0.0.1:8000";

export async function listarLivros() {
    const resposta = await fetch(`${API_URL}/livros`);
    return resposta.json();
}

export async function criarLivro(livro) {
    const resposta = await fetch(`${API_URL}/livros`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(livro)
    });

    return resposta.json();
}

export async function excluirLivro(id) {
    await fetch(`${API_URL}/livros/${id}`, {
        method: "DELETE"
    });
}