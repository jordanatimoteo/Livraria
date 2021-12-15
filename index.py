from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import desc


from model.models import Livro,Editora, Usuario,Autor,Lista

engine = create_engine("mysql+pymysql://root:@localhost/python", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

def create_autor(valor_nome,valor_idade):
    autor = Autor(nome=valor_nome,idade=valor_idade)
    session.add(autor)
    session.commit()
def create_editora(valor_codigo,valor_nome,valor_gerente,valor_livro,valor_numero):
    editora = Editora(codigo=valor_codigo,nome=valor_nome,nome_gerente=valor_gerente,tipo_livro=valor_livro,numero=valor_numero)
    session.add(editora)
    session.commit()
def create_livro(valor_id_autor,valor_id_editora,valor_quantidade,valor_titulo,valor,assunto):
    livro = Livro(id_autor=valor_id_autor,id_editora=valor_id_editora,quantide_estoque=valor_quantidade,titulo=valor_titulo,valor=valor,assunto=assunto)
    session.add(livro)
    session.commit()
def creat_lista(valor_id_livro):
    lista = Lista(id_livro=valor_id_livro)
    session.add(lista)
    session.commit()
def creat_usuario(valor_id_lista,valor_codigo,valor_compra,valor_endereco,valor_telefone,cpf):
    usuario = Usuario(id_lista = valor_id_lista, codigo = valor_codigo,compra = valor_compra, endereco = valor_endereco,telefone=valor_telefone,cpf=cpf)
    session.add(usuario)
    session.commit()

create_autor("Ricardo",21)
create_autor("Sergio",29)
create_autor("Kurt",27)
create_editora(123456,"Pingo","Champs","Terror",8922-9831)
create_editora(131313,"CBJR","Marcao","Romance",2341-2345)
create_editora(888888,"Raimundos","Choris","Comedia",3123-1222)
create_livro(1,4,30,"Pingo",30,"Aventura")
create_livro(2,5,30,"Ratos",30,"Ratos")
create_livro(3,6,30,"Anoes",60,"Senhor dos aneis")
creat_lista(8)
creat_lista(9)
creat_lista(7)
creat_usuario(13,123456,"2021-11-15","Varginha","99999999","21931293123213")
creat_usuario(10,123456789,"2021-11-14","TC","8888888","31293123213")
creat_usuario(11,12345678910,"2021-11-13","TP","7777777","21931293123")
