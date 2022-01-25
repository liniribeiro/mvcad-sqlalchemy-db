

from uuid import uuid4

from sqlalchemy import Column, String

from db_connection import Base


# Classe que criamos, para mapear a tabela aluno
class AlunoModel(Base):
    __tablename__ = 'aluno'

    id = Column(String, primary_key=True, default=str(uuid4()))
    name = Column(String)
    estado = Column(String)
