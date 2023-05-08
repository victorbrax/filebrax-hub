from flask import Blueprint, render_template, url_for, send_file, redirect
from utils.format_functions import *
from dotenv import load_dotenv
import os
import zipfile


downloads = Blueprint('downloads', __name__, static_folder="static", template_folder="templates")

load_dotenv()
DOWNLOADS_DIR = os.getenv("DOWNLOADS_DIR")
UPLOADS_DIR = os.getenv("UPLOADS_DIR")
JUNK_DIR = os.getenv("JUNK_DIR")

# # Página de Download de algum Projeto
@downloads.route('/<project>')
def downloads_page(project: str):

    # Verificação caso a pasta de Downloads esteja vazia
    download_info = []
    downloads_folder = os.path.join(DOWNLOADS_DIR, project)
    if not os.path.exists(downloads_folder) or not os.listdir(downloads_folder):
        return render_template('includes/not_found.html'), 404

    # Loop que fornece as informações pra tabela da pasta de Downloads
    for download_file in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, download_file)
        url = url_for('static', filename=f'reports/downloads/{project}/{download_file}', _external=True)

        download_info.append({
            "name": download_file,
            "size": os.path.getsize(file_path),
            "modified": os.path.getmtime(file_path),
            "url": url
        })

    # Verificação caso a pasta de Uploads esteja vazia.
    upload_info = []
    uploads_folder = os.path.join(UPLOADS_DIR, project)
    if not os.path.exists(uploads_folder) or not os.listdir(uploads_folder):
        return render_template('includes/not_found.html'), 404

    # Loop que fornece as informações pra tabela da pasta de Uploads
    for upload_file in os.listdir(uploads_folder):
        file_path = os.path.join(uploads_folder, upload_file)
        url = url_for('static', filename=f'reports/uploads/{project}/{upload_file}', _external=True)

        upload_info.append({
            "name": upload_file,
            "size": os.path.getsize(file_path),
            "modified": os.path.getmtime(file_path),
            "url": url
        })

    return render_template('downloads/downloads.html', project=project,
                           uploads=upload_info,
                           downloads=download_info,
                           format_size=format_size,
                           format_date=format_date)

# Rota de Downloads de Projeto
@downloads.route('/<project>/<int:id>')
def zip(project: str, id: int):
    # Os botões possuem o ID de qual escolha o usuário fez
    if id == 1:
        ZIP_PROJECT = os.path.join(UPLOADS_DIR, project)
        zip_name = f'uploads-{project}.zip'

    elif id == 2:
        ZIP_PROJECT = os.path.join(DOWNLOADS_DIR, project)
        zip_name = f'downloads-{project}.zip'

    # Path para onde o .zip irá ser armazenado
    zip_file_path = os.path.join(JUNK_DIR, zip_name)

    # Gerar o .zip
    with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zip_obj:
        for current_dir, sub_folders, files in os.walk(ZIP_PROJECT):
            for file in files:
                caminho_completo = os.path.join(current_dir, file)
                zip_obj.write(caminho_completo, os.path.relpath(
                    caminho_completo, ZIP_PROJECT))

    return send_file(zip_file_path, as_attachment=True)
