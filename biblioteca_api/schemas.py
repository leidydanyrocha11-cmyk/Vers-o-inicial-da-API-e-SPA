from pydantic import BaseModel, Field


class LivroBase(BaseModel):
    titulo: str = Field(min_length=2, max_length=150)
    autor: str = Field(min_length=2, max_length=120)
    ano_publicacao: int = Field(ge=0, le=2100)
    disponivel: bool = True


class LivroCreate(LivroBase):
    pass


class LivroResponse(LivroBase):
    id: int

    class Config:
        from_attributes = True