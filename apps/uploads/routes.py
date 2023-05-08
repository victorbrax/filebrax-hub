from flask import Blueprint, render_template, flash, request, redirect, url_for
from dotenv import load_dotenv
import os
import re
import shutil


uploads = Blueprint('uploads', __name__, static_folder="static", template_folder="templates")

load_dotenv()
UPLOADS_DIR = os.getenv("UPLOADS_DIR")
DOWNLOADS_DIR = os.getenv("DOWNLOADS_DIR")

# # Página de Upload de algum Projeto
@uploads.route('/')
def uploads_page():
    return render_template('uploads/uploads.html')

# Rota de requisição para Uploads
@uploads.route('/upload_project', methods=['POST'])
def upload_project():

    # O usuário irá definir o nome da pasta do projeto
    folder_name = request.form['folder_name']

    # Validação com Regex para o Flash
    letras = re.compile('^[a-zA-Z0-9_]+$')
    if not letras.match(folder_name):
        flash('O campo de entrada contém caracteres inválidos.', 'error')
        return redirect(url_for('uploads.uploads_page'))

    # Definição dos possíveis caminhos
    possible_upload = os.path.join(UPLOADS_DIR, folder_name)
    possible_download = os.path.join(DOWNLOADS_DIR, folder_name)

    if os.path.exists(possible_upload) or os.path.exists(possible_download):
        flash("Atenção, esses arquivos já existem no servidor e serão deletados.", "info")
        try:
            shutil.rmtree(possible_upload)
        except Exception as e:
            pass
        try:
            shutil.rmtree(possible_download)
        except Exception as e:
            pass
    os.makedirs(possible_upload)

    # Salvar os arquivos na nova pasta
    files = request.files.getlist('files[]')
    try:
        for file in files:
            filename = file.filename
            file.save(os.path.join(possible_upload, filename))
        flash('Sucesso no Upload.', 'success')

    except IOError:
        flash('Erro de E/S ao salvar o arquivo.', 'error')
    except Exception as e:
        flash('Ocorreu um erro durante o upload: ' + str(e), 'error')

    return redirect(url_for('uploads.uploads_page'))
