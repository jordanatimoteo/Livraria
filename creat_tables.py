from sqlalchemy import *

from model.models import Livro,Editora, Usuario,Autor,Lista

engine = create_engine("mysql+pymysql://root:@localhost/python?charset=utf8mb4", echo=True)

editora= Editora.__table__ 
editora.create(engine, checkfirst=True)

autor = Autor.__table__ 
autor.create(engine, checkfirst=True)

livro = Livro.__table__ 
livro.create(engine, checkfirst=True)

lista = Lista.__table__ 
lista.create(engine, checkfirst=True)

usuario = Usuario.__table__
usuario.create(engine, checkfirst=True)