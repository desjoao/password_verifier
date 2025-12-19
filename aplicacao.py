import traceback
from ui import UI
from password_verifier import PasswordVerifier

def main():
    nome = 'verificador_senha'
    verificador = PasswordVerifier(nome)
    utils = verificador.utils
    utils.log_inicio()
    ui = UI(utils)
    if not inserir_dados(verificador, ui):
        exit()
    if not verificar_dados(verificador, ui):
        exit()
    verificador.utils.log_fim()

def inserir_dados(verificador: PasswordVerifier, ui: UI):
    try:
        instrucao = ('Insira uma senha com:'
                     '\n - tamanho de ao menos 8 caracteres'
                     '\n - ao menos 1 letra minúscula'
                     '\n - ao menos 1 letra maiúscula'
                     '\n - ao menos 1 número'
                     '\n - ao menos 1 caracter especial')
        ui.mensagem_info('Verificador de Senha', instrucao)
        frame = ui.criar_frame()
        ui.entry_box(frame, 'password', mask=True)
        ui.botao_enviar_entradas(frame, 'OK')
        ui.iniciar_handler()
        return True

    except Exception as e:
        msg = ('Erro ao gerar tela para inserção de dados.',
               traceback.format_exc())
        print(msg)
        verificador.utils.log_erro(msg)
        verificador.utils.log_fim()
        return False

def verificar_dados(verificador: PasswordVerifier, ui: UI):
    try:
        senha = ui.receber_entradas()
        if not verificador.verificar_senha(senha['password']):
            ui.mensagem_erro('', 'Senha fraca')
        else:
            ui.mensagem_info('', 'OK')
        return True
    
    except Exception as e:
        msg = ('Erro ao verificar senha', traceback.format_exc())
        print(msg)
        verificador.utils.log_erro(msg)
        verificador.utils.log_fim()
        return False


if __name__ == "__main__":
    main()