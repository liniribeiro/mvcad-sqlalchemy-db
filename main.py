from db_connection import conn_session
from model import AlunoModel


def save_user():
    with conn_session() as session:
        aluno = AlunoModel(name='John Snow', estado='SC')
        session.add(aluno)


def get_user():
    with conn_session() as session:
        db_user = session.query(AlunoModel).filter_by(name='John Snow').first()
        print(db_user)


save_user()
get_user()

