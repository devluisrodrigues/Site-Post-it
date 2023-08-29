from utils import load_data, load_template, add_data, build_response, delete_data,load_data_id, update_data

def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):

        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]

        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        itens = [0,0]
        for chave_valor in corpo.split('&'):
            chave, valor = chave_valor.split('=')
            if chave == 'titulo':
                itens[0] = valor.replace('+', ' ')
            elif chave == 'detalhes':
                itens[1] = valor.replace('+', ' ')
        add_data(itens)
        return build_response(code=303, reason='See Other', headers='Location: /')
        
            
        
    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(id = Note.id,title=Note.title, details=Note.content)
        for Note in load_data()
    ]
    notes = '\n'.join(notes_li)

    return build_response(body=load_template('index.html').format(notes=notes))

def delete(request):
    linhas = request.splitlines()
    id = linhas[-1].split('=')[1]
    delete_data(id)
    return build_response(code=303, reason='See Other', headers='Location: /')

def edit(request):
    linhas = request.splitlines()
    id = linhas[-1].split('=')[1]
    title, content = load_data_id(id)
    return build_response(body=load_template('edit.html').format(id=id,title=title, details=content))

def salvar(request):
    request = request.replace('\r', '')  # Remove caracteres indesejados
    # Cabeçalho e corpo estão sempre separados por duas quebras de linha
    partes = request.split('\n\n')
    corpo = partes[1]

    itens = [0,0,0]
    for chave_valor in corpo.split('&'):
        chave, valor = chave_valor.split('=')
        if chave == 'id':
            itens[0] = valor.replace('+', ' ')
        elif chave == 'titulo':
            itens[1] = valor.replace('+', ' ')
        elif chave == 'detalhes':
            itens[2] = valor.replace('+', ' ')
    update_data(itens)
    return build_response(code=303, reason='See Other', headers='Location: /')