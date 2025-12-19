import re
import traceback
from utils import Utils

class PasswordVerifier:
    def __init__(self, nome_programa:str):
        self.utils = Utils(nome_programa)

    def verificar_senha(self, senha:str) -> bool:
        try:
            if len(senha) <=8:
                return False
            if not re.findall(r'\d', senha):
                return False
            if not re.findall(r'[A-Z]', senha):
                return False
            if not re.findall(r'[a-z]', senha):
                return False
            if not re.findall(r'[^\w\s]', senha):
                return False
            return True
        except Exception as e:
            msg = 'Erro ao verificar senha informada.' + traceback.format_exc()
            print(msg)
            self.utils.log_erro(msg)
            exit()