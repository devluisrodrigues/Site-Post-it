from pathlib import Path
import json
from database import Database,Note

CUR_DIR = Path(__file__).parent
db = Database('data/banco')

def extract_route(route):
    "Separa a primeira linha da requisicao"
    return route.split()[1][1:] if len(route.split()) > 1 else ""

def read_file(path):
    "Le o arquivo e retorna seu conteudo"
    try:
        file = open(path, 'rb')
        content = file.read()
        file.close()
        return content
    except:
        return None
    
def load_template(Template):
    "Carrega os dados do arquivo html"
    try:
        path = CUR_DIR / "templates"
        file = open(path / Template, 'r', encoding= 'utf-8')
        data = file.read()
        file.close()
        return data
    except:
        return None
    
def build_response(body='', code=200, reason='OK', headers=''):
    "Retorna a resposta do servidor"
    if headers == '':
        headers = "Content-Type: text/html; charset=utf-8"
    return (f"HTTP/1.1 {code} {reason}\n{headers}\n\n{body}").encode()

def load_data():
    notes = db.get_all()
    return notes

def load_data_id(id):
    note = db.get(id)
    return note.title, note.content

def add_data(data):
    db.add(Note(title=data[0], content=data[1]))

def delete_data(id):
    db.delete(id)

def update_data(data):
    db.update(Note(id=data[0], title=data[1], content=data[2]))