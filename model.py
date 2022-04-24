# imports DB
from sqlalchemy import create_engine, Column, Integer, String # interligacao com banco de dados e itens da tabela
from sqlalchemy.ext.declarative import declarative_base # base da tabela
from sqlalchemy.orm import sessionmaker # criacao de sessions

# Config. DB
USUARIO = "root"
SENHA = ""
HOST = "localhost"
DB = "projeto_login"
PORT = "3306"

# string to connection DB
CONNECTION = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{DB}"

engine = create_engine(CONNECTION, echo = True)
Session = sessionmaker(bind = engine)
session = Session()
Base = declarative_base()

#criacao de tabela
class Login(Base):
    __tablename__ = "login" # nome da tabela
    id = Column(Integer, primary_key = True) 
    user = Column(String(30))
    email = Column(String(50))
    senha_hash = Column(String(200))

Base.metadata.create_all(engine) # criar a tabela

