import os
import socket
import json
from datetime import datetime

class Utils:
    """
    Classe de utilidades que, dentre suas funções, realiza logs de execução de programas que a implementam.
    """
    def __init__(self, nome_programa: str):
        self.nome = nome_programa
        self.user = os.environ.get('USER')
        self.maquina = socket.gethostname()
        print(self.user)
        pasta_logs = os.path.join(os.getcwd(), 'logs')
        if not os.path.exists(pasta_logs):
            os.makedirs(pasta_logs)
        self.caminho_log = os.path.join(pasta_logs, f'log_{self.nome}.txt' )
    
    def set_pasta_log(self, caminho:str):
        """
        Altera o caminho destino para os logs.
        """
        pasta_log = caminho
        if not os.path.exists(pasta_log):
            os.makedirs(pasta_log)
        self.caminho_log = os.path.join(pasta_log, f'log_{self.nome}.txt')
    
    def carrega_json(self, nome:str) -> dict:
        try:
            config = json.load(open(nome+'.json', 'r'))
            return config
        except Exception as e:
            msg = f'Arquivo json não encontrado.'
            print(msg)
            exit()

    def log_acerto(self, msg: str):
        msg = f'{datetime.now()};{self.user};{self.maquina};{self.nome};OK;{msg}\n'
        with open(self.caminho_log, 'a') as f:
            f.write(msg)

    def log_erro(self, msg:str):
        msg = f'{datetime.now()};{self.user};{self.maquina};{self.nome};NOK;{msg}\n'
        with open(self.caminho_log, 'a') as f:
            f.write(msg)
    
    def log_inicio(self):
        msg = f'{datetime.now()};{self.user};{self.maquina};{self.nome};OK;Início\n'
        with open(self.caminho_log, 'a') as f:
            f.write(msg)

    def log_fim(self):
        msg = f'{datetime.now()};{self.user};{self.maquina};{self.nome};OK;Fim\n'
        with open(self.caminho_log, 'a') as f:
            f.write(msg)