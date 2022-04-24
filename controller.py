import bcrypt # criptografia 
from sqlalchemy import create_engine # engine do DB
from sqlalchemy.orm import sessionmaker # sessao do DB
from model import Login # modularização do model
from sqlalchemy import or_ # talvez utlizar o 'or' na pesquisa do DB

def return_session():
    USUARIO = "root"
    SENHA = ""
    HOST = "localhost"
    DB = "projeto_login"
    PORT = "3306"

    CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{DB}"

    engine = create_engine(CONN, echo= True)
    Session = sessionmaker(bind = engine)
    return Session()

# class que verifica e cadastra o usuario no banco de dados
class ControllerCadastro():
    @classmethod
    def verifica_dados(cls, user: str, email: str, hash_senha: str):
        if len(user) < 3 or len(user) > 30:
            return 2 # tamanho do nome invalido
        if len(email) > 50 or len(email) < 5:
            return 3 # tamanho do email invalido
        if len(hash_senha) > 200 or len(hash_senha) < 5:
            return 4 # tamanho da senha invalido
    
        return 1

    @classmethod
    def cadastrar_pessoa(cls, user: str, email: str, senha: str):
    
        if ControllerCadastro.verifica_dados(user, email, senha) != 1:
            return ControllerCadastro.verifica_dados(user, email, senha)

        session = return_session()

        a = session.query(Login).filter(Login.email == email).all()

        if len(a) != 0:
            return 5 # email ja cadastrado

        senha_crypto = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()) # gerando senha hash com bcrypt

        x = Login(user = user,
                  email = email,
                  senha_hash = senha_crypto)
        session.add(x)
        session.commit()              
        #       print(ControllerCadastro.cadastrar_pessoa('eduardo', 'eduardo@hotmail.com', 'edu12345'))

class ControllerLogin():
    @classmethod
    def verificar_login(cls, email: str, senha: str):
        session = return_session()
        x = session.query(Login).filter(Login.email == email).all()
        
        if len(x) != 1:
            return 2
            
        # if x[0].email != email:
        #     return 2 # email nao cadastrado no banco de dados(conta nao existe)
        
        if bcrypt.checkpw(senha.encode(), x[0].senha_hash.encode()) == False:
            return 3 #senha incorreta 

        return 1 # logado com sucesso
        

# print(ControllerLogin.verificar_login('eduardo@hotmail.com', 'edu12345'))