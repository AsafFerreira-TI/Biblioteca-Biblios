from biblioteca.model.database import engine, Base

from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey

class Livro(Base):
    __tablename__ = 'LIVRO'
    id = Column(Integer, primary_key = True)
    titulo = Column(String)
    autor = Column(String)
    editora = Column(String)
    ano = Column(String)
    categoria = Column(String)

    def __init__(self, titulo, autor, ano, editora, categoria):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.editora = editora
        self.categoria = categoria

class Leitor(Base):
    __tablename__ = 'LEITOR'
    id = Column(Integer, primary_key = True)
    nome = Column(String)
    sobrenome = Column(String)
    telefone = Column(String)
    email = Column(String)

    def __init__(self, nome, sobrenome, telefone, email):
        self.nome = nome
        self.sobrenome = sobrenome
        self.telefone = telefone
        self.email = email

class Reserva(Base):
    __tablename__ = 'RESERVA'
    id = Column(Integer, primary_key = True)
    cod_leitor = Column(Integer, ForeignKey('LEITOR.id'))
    cod_livro = Column(Integer, ForeignKey('LIVRO.id'))
    DataReserva = Column(Date)
    DataPrazo = Column(Date)
    Status = Column(Boolean)

    def __init__(self, cod_leitor, cod_livro, DataReserva, DataPrazo, Status):
        self.cod_leitor = cod_leitor
        self.cod_livro = cod_livro
        self.DataReserva = DataReserva
        self.DataPrazo = DataPrazo
        self.Status = Status


Base.metadata.create_all(engine)
