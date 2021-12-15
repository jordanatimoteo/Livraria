import datetime
from sqlalchemy import Column, Integer, String, Date, Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.elements import collate
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.sqltypes import DECIMAL, INT, NVARCHAR, VARCHAR, DateTime, Time

Base = declarative_base()



class Editora(Base):
    __tablename__ = 'editora'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    codigo = Column(Integer, nullable=False)
    nome = Column(NVARCHAR(45), nullable=False)
    nome_gerente = Column(NVARCHAR(45), nullable=False)
    tipo_livro = Column(NVARCHAR(45),unique=True ,nullable=False)
    numero = Column(Integer,nullable=False)

class Autor(Base):
    __tablename__ = 'autor'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    nome = Column(NVARCHAR(45), nullable=False)
    idade = Column(Integer,nullable=False) 

class Livro(Base):
    __tablename__ = 'livro'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    id_autor = Column(Integer, ForeignKey('autor.id'))
    id_editora = Column(Integer,ForeignKey('editora.id'))
    quantide_estoque = Column(Integer,nullable=False)
    titulo = Column(NVARCHAR(45), nullable=False)
    valor = Column(Integer,nullable=False)
    assunto = Column(NVARCHAR(45), nullable=False)
    autor = relationship("Autor", backref="Livro")
    editora = relationship("Editora", backref="Livro")
     

class Lista(Base):
    __tablename__ = 'lista'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    id_livro = Column(Integer, ForeignKey('livro.id'))
    livro = relationship("Livro",backref="Lista")

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    id_lista = Column(Integer,ForeignKey('lista.id'))
    codigo = Column(Integer, unique=True, nullable=False) 
    compra = Column(Date, nullable=False)
    endereco = Column(String(255), nullable=False)
    telefone = Column(String(45), nullable=False)
    cpf = Column(Integer, nullable=False)
    lista = relationship("Lista", backref="Usuario")


