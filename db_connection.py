from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# DATABASE_URL = 'postgresql://<USUARIO>:<SENHA>@localhost/<NOME DO BANCO>'
DATABASE_URL = 'postgresql://postgres:postgres@localhost/mvcad-cursos'
engine = create_engine(DATABASE_URL)


# declarative_base é uma função que retorna uma Classe base do SQLAlchemy para criar tabelas no banco.
Base = declarative_base()

# Comando para que o SQLALchemy crie todas as tabelas que herdam da classe base do SQLALchemy
Base.metadata.create_all(engine)


@contextmanager
def conn_session():
    main_session = scoped_session(sessionmaker(bind=engine))
    session = main_session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
