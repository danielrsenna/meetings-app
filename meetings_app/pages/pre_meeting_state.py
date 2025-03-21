import reflex as rx
from .supabase_client import supabase_client
from dotenv import load_dotenv
import uuid
import datetime

load_dotenv()

class PreReuniaoState(rx.State):
    nome: str = ""
    proposito: str = ""
    periodicidade: str = ""

    novo_participante: str = ""
    participantes: list[dict] = []
    itens: list[dict] = []
    novo_item: str = ""
    responsavel: str = ""
    tipo_dado: str = "Texto"

    reuniao_id: str = ""

    def set_novo_participante(self, value: str):
        self.novo_participante = value


    #def criar_reuniao(self):

    def add_participante(self):
        if self.novo_participante.strip():
            participante_id = str(uuid.uuid4())
            participante_nome = self.novo_participante.strip()

            self.participantes.append({
                "id": participante_id,
                "nome": participante_nome
            })

            self.novo_participante = ""

    #def add_items(self):

    #def add_outputs(self):





    def adicionar_item(self):
        if self.novo_item:
            self.itens.append({
                "descricao": self.novo_item,
                "responsavel": self.responsavel,
                "tipo_dado": self.tipo_dado
            })
            self.novo_item = ""
            self.responsavel = ""
            self.tipo_dado = "Texto"

    def salvar_reuniao(self):
        supabase = supabase_client()
        dados = {
            "nome": self.nome,
            "proposito": self.proposito,
            "periodicidade": self.periodicidade,
            "participantes": self.participantes,
            "itens": self.itens
        }
        supabase.table("reunioes").insert(dados).execute()
        self.clear_form()

    def clear_form(self):
        self.nome = ""
        self.proposito = ""
        self.periodicidade = ""
        self.participantes = []
        self.itens = []
