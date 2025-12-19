import traceback
from utils import Utils
import ttkbootstrap as ttb
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
from tkinter.ttk import (Frame)
from tkinter import (ttk, X, filedialog, messagebox, BOTH)

class UI(Frame):
    def __init__(self, utils:Utils):
        try:
            self.utils = utils
            self.config = self.utils.carrega_json('config.ui')
            self.__entradas = {}
            self.__resp_entrada = {}
            self.__frames = {}

            # Diagramação
            
            ## Entry Box
            self.entry_fill = self.config["LAYOUT"]["TEntry"]["fill"]
            self.entry_padx = self.config["LAYOUT"]["TEntry"]["padx"]
            self.entry_pady = self.config["LAYOUT"]["TEntry"]["pady"]
            self.entry_expand = self.config["LAYOUT"]["TEntry"]["expand"]
            self.entry_state = self.config["LAYOUT"]["TEntry"]["state"]

            ## Date Box
            self.date_fill = self.config["LAYOUT"]["TDate"]["fill"]
            self.date_padx = self.config["LAYOUT"]["TDate"]["padx"]
            self.date_pady = self.config["LAYOUT"]["TDate"]["pady"]
            self.date_expand = self.config["LAYOUT"]["TDate"]["expand"]

            ## Frame
            self.fr_fill = self.config["LAYOUT"]["TFrame"]["fill"]
            self.fr_pady = self.config["LAYOUT"]["TFrame"]["pady"]
            self.fr_expand = self.config["LAYOUT"]["TFrame"]["expand"]

            ## Label
            self.lbl_fill = self.config["LAYOUT"]["TLabel"]["fill"]
            self.lbl_padx = self.config["LAYOUT"]["TLabel"]["padx"]
            self.lbl_pady = self.config["LAYOUT"]["TLabel"]["pady"]
            self.lbl_side = self.config["LAYOUT"]["TLabel"]["side"]
            self.lbl_width = self.config["LAYOUT"]["TLabel"]["width"]
            self.lbl_expand = self.config["LAYOUT"]["TLabel"]["expand"]

            ## Button
            self.btn_fill = self.config["LAYOUT"]["TButton"]["fill"]
            self.btn_padding = self.config["LAYOUT"]["TButton"]["padding"]
            self.btn_side = self.config["LAYOUT"]["TButton"]["side"]
            self.btn_expand = self.config["LAYOUT"]["TButton"]["expand"]
            self.btn_state = self.config["LAYOUT"]["TButton"]["state"]

            ## Notebook
            self.ntb_fill = self.config["LAYOUT"]["TNotebook"]["fill"]
            self.ntb_padx = self.config["LAYOUT"]["TNotebook"]["padx"]
            self.ntb_pady = self.config["LAYOUT"]["TNotebook"]["pady"]
            self.ntb_padding = self.config["LAYOUT"]["TNotebook"]["padding"]
            self.ntb_expand = self.config["LAYOUT"]["TNotebook"]["expand"]

            ## Tabela
            self.tbl_fill = self.config["LAYOUT"]["TTabela"]["fill"]
            self.tbl_padx = self.config["LAYOUT"]["TTabela"]["padx"]
            self.tbl_pady = self.config["LAYOUT"]["TTabela"]["pady"]
            self.tbl_expand = self.config["LAYOUT"]["TTabela"]["expand"]
            self.tbl_paginated = self.config["LAYOUT"]["TTabela"]["paginated"]
            self.tbl_searchable = self.config["LAYOUT"]["TTabela"]["searchable"]

            # Root
            self.root = ttb.Window(themename=self.config["LAYOUT"]["ROOT"]["theme"],
                                size=(self.config["LAYOUT"]["ROOT"]["width"],
                                        self.config["LAYOUT"]["ROOT"]["height"]),
                                    position=(self.config["LAYOUT"]["ROOT"]["position_horizontal"],
                                                self.config["LAYOUT"]["ROOT"]["position_vertical"]),
                                    resizable=(self.config["LAYOUT"]["ROOT"]["resizable_width"],
                                            self.config["LAYOUT"]["ROOT"]["resizable_heigth"]))
            
            super().__init__()

            # Estilização
            style = ttk.Style()

            TButton = self.config["LAYOUT"]["TButton"]
            self.button_bootstyle = TButton["theme"]
            style.configure("TButton",
                            font = (TButton["font"], int(TButton["font_size"]), TButton["font_style"]))
            
            TLabel = self.config["LAYOUT"]["TLabel"]
            self.label_bootstyle = TLabel["theme"]
            style.configure("TLabel",
                            font = (TLabel["font"], int(TLabel["font_size"]), TLabel["font_style"]))
            
            TEntry = self.config["LAYOUT"]["TEntry"]
            self.entry_bootstyle = TEntry["theme"]
            style.configure("TEntry",
                            font = (TEntry["font"], int(TEntry["font_size"]), TEntry["font_style"]))
            
            TDate = self.config["LAYOUT"]["TDate"]
            self.date_bootstyle = TDate["theme"]
            
            TNotebook = self.config["LAYOUT"]["TNotebook"]
            self.notebook_bootstyle = TNotebook["theme"]
            style.configure("TNotebook",
                            tabposition = TNotebook["tabposition"])
            
            TFrame = self.config["LAYOUT"]["TFrame"]
            self.frame_bootstyle = TFrame["theme"]
            style.configure("TFrame",
                            borderwidth = TFrame["borderwidth"],
                            relief = TFrame["relief"])
            
            TTabela = self.config["LAYOUT"]["TTabela"]
            self.tabela_bootstyle = TTabela["theme"]


        except Exception as e:
            msg = "Erro no construtor da classe UI."
            print(msg, traceback.format_exc())
            raise e(msg)
        
    def iniciar_handler(self):
        try:
            self.root.mainloop()

        except Exception as e:
            pass
    
    def finalizar_handler(self):
        try:
            self.root.destroy()
        
        except Exception as e:
            pass
    
    def criar_frame(self, elemento_pai = None):
        try:
            if not elemento_pai:
                frame = ttb.Frame(self.root)
            else:
                frame = ttb.Frame(elemento_pai)
            
            frame.pack(fill=self.fr_fill, expand=self.fr_expand, pady=self.fr_pady)
            return frame
        
        except Exception as e:
            pass

    def enviar_entradas(self):
        try:
            for chave, valor in self.__entradas.items():
                self.__resp_entrada.update({chave:valor.get()})
            self.quit()
        
        except Exception as e:
            pass
    
    def botao_enviar_entradas(self, frame: Frame, rotulo: str):
        try:
            newframe = ttb.Frame(frame)
            newframe.pack()
            botao = ttb.Button(newframe, text=rotulo, command=self.enviar_entradas, bootstyle=self.button_bootstyle)
            botao.pack(fill=self.btn_fill, side=self.btn_side)
        
        except Exception as e:
            print('erro', traceback.format_exc())
            exit()
    
    def entry_box(self, frame: Frame, rotulo: str, mask=False):
        try:
            newframe = ttb.Frame(frame)
            newframe.pack(fill=self.fr_fill, expand=self.fr_expand, pady=self.fr_pady)
            lbl = ttb.Label(newframe, text=rotulo, width=self.lbl_width, bootstyle=self.label_bootstyle)
            lbl.pack(fill=self.lbl_fill, side = self.lbl_side, padx=self.lbl_padx, pady=self.lbl_pady)
            if not mask:
                entrada = ttb.Entry(newframe, bootstyle=self.entry_bootstyle)
            else:
                entrada = ttb.Entry(newframe, show='*', bootstyle=self.entry_bootstyle)
            entrada.pack(fill=self.entry_fill, padx=self.entry_padx, pady=self.entry_pady)
            self.__entradas.update({rotulo: entrada})
        
        except Exception as e:
            pass
    
    def receber_entradas(self):
        return self.__resp_entrada

    def limpar_entradas(self):
        self.__entradas = {}
        self.__resp_entrada = {}
    
    def date_box(self, frame: Frame, rotulo: str):
        try:
            newframe = ttb.Frame(frame)
            newframe.pack(fill=self.fr_fill, expand=self.fr_expand, pady=self.fr_pady)
            lbl = ttb.Label(newframe, text=rotulo, width=self.lbl_width, bootstyle=self.label_bootstyle)
            lbl.pack(fill=self.lbl_fill, side = self.lbl_side, padx=self.lbl_padx, pady=self.lbl_pady)
            date_box = ttb.DateEntry(newframe, bootstyle=self.date_bootstyle)
            date_box.pack(fill=self.date_fill, padx=self.date_padx, pady=self.date_pady)
            self.__entradas.update({rotulo: date_box})
        
        except Exception as e:
            pass
    
    def gera_tabela(self, titulo, colunas, dados):
        try:
            app = ttb.Toplevel(self.root)
            app.title(titulo)

            coldata = [{"text": c, "stretch": True} for c in colunas]
            table = Tableview(
                master=app,
                coldata=coldata,
                rowdata=dados,
                paginated=self.tbl_paginated,
                searchable=self.tbl_searchable,
                bootstyle=self.tabela_bootstyle
            )
            table.pack(fill=self.tbl_fill, expand=self.tbl_expand, padx=self.tbl_padx, pady=self.tbl_pady)

        except Exception as e:
            msg = f"Erro ao gerar tabela.\n{traceback.format_exc()}."
            print(msg)
            exit()

    def inserir_cliente(self):
        try:
            self.app_cadastro = ttb.Toplevel(self.root)
            self.app_cadastro.title('Cadastramento de clientes')

            frame = self.criar_frame(self.app_cadastro)
            self.entry_box(frame, 'CPF')
            self.entry_box(frame, 'nome')
            self.entry_box(frame, 'email')
            self.entry_box(frame, 'endereco')
            self.entry_box(frame, 'datanascimento')
            self.botao_enviar_entradas(frame, 'Cadastrar')
        
        except Exception:
            print(traceback.format_exc())

    def novo_notebook(self):
        try:
            self.notebook = ttb.Notebook(self.root, bootstyle=self.notebook_bootstyle)
            self.notebook.pack(fill=self.ntb_fill, padx=self.ntb_padx, pady=self.ntb_pady, expand=self.ntb_expand)
        
        except Exception as e:
            pass
    
    def gera_frames_notebook(self, frames:list, rotulo:str):
        try:
            for frame in frames:
                nova_aba = list(zip(frame, rotulo))
                self.__frames.append(nova_aba)
            
        
        except Exception as e:
            pass
    
    def adiciona_elemento(self):
        try:
            for valor in self.__frames:
                self.nova_aba(valor[0], valor[1])
        
        except Exception as e:
            pass
    
    def nova_aba(self, frame: Frame, rotulo: str):
        try:
            self.notebook.add(frame, text=rotulo, padding=self.ntb_padding)
        
        except Exception as e:
            pass
    
    def abrir_arquivo(self, mode: str):
        try:
            file = filedialog.askopenfile(mode)
            return file

        except Exception as e:
            pass
    
    def abrir_pasta(self):
        try:
            pasta = filedialog.askdirectory()
            return pasta
    
        except Exception as e:
            pass
    
    def mensagem_info(self, titulo:str, msg:str):
        messagebox.showinfo(title=titulo, message=msg)
    
    def mensagem_erro(self, titulo:str, msg:str):
        messagebox.showerror(title=titulo, message=msg)
