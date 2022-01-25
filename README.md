# Este projeto tem o objetivo de auxiliar na ligação do banco de dados com uma aplicação Python


## Tecnologias utilizadas:
(SQLAlchemy)[https://www.sqlalchemy.org/]


### O que é o SQLAlchemy?
Kit de ferramentas de banco de dados para Python!
Ele fornece para os desenvolvedores de todo o poder e flexibilidade do SQL, tem um conjunto de padrões de persistência (no banco), projetados para acesso eficiente e de alto desempenho, adaptado em uma linguagem de domínio simples e Pythônica.


### Como o SQLALchemy cria automaticamente nossas tabelas no banco?
A função do SQLAlchemy chamada declarative_base retorna uma Classe base do SQLAlchemy, e nossas classes de declaração de tabelas devem herdar desta classe base..
Exemplo:
~~~
class AlunoModel(Base):
    __tablename__ = 'aluno'

    id = Column(String, primary_key=True, default=str(uuid4()))
    name = Column(String)
    estado = Column(String)
    
~~~
Acima podemos analisar a criação de uma classe chamada AlunoModel, ela extende a classe Base do SQLAlchemy.
Ao executar o comando, informando para nossa engine do banco criar todas as classes bases na base:
~~~ 
Base.metadata.create_all(engine) 
~~~ 
Serão criados no banco de dados todas as tabelas que herdam da classe base do SQLALchemy.



### Para que serve o requirements.txt?
Ele é o arquivo onde se encontram as bibliotecas externas que o nosso projeto utiliza, que devem ser instaladas com o pip.
Um exemplo de biblioteca externa é o SQLAlchemy, que é nossa biblioteca auxiliar para manipular o banco de dados.
Se você for analisar este arquivo, vai encontrar várias bibliotecas, com sua versão ao lado. Ex: "postgres==3.0.0"

(Documentação do requirements-file)[https://pip.pypa.io/en/latest/user_guide/#requirements-files]
Para instalar as dependencias, deve ser aberto o terminal no diretório que contém o arquivo e utilizzar o comando: "pip install -r requirements.txt"


### Como funciona a engine de conexão com o banco de dados?
xxx


###  Passo-a-passo para rodar o projeto com sucesso:

- Instalar as dependencias: No terminal executar o comando pip install -r requirements.txt
- Criar em seu banco de dados uma nova base, chamada mvcad-cursos
- Executar o arquivo chamado main.py: Comando python main.py
- Olhar na base de dados criada, se a tabela aluno foi criada com sucesso.



### Problemas que podem ocorrer: 

Problema: ImportError: DLL load failed while importing _psycopg: The specified module could not be found.
O que pode ser: Provavelmente a biblioteca psycopg2-binary não foi instalada com sucesso. Vá no arquivo model e analise se há uma mensagem do pycharm informando: "Package requirement psycopg2-binary=2.8.5 is not satisfied" 
Solução: Clique na opção apresentada na mensagem "install requirement" e execute novamente o arquivo main.py
