from flask import Blueprint, render_template
from dotenv import load_dotenv
from utils.format_functions import *


menu = Blueprint('menu', __name__, static_folder="static", template_folder="templates")

load_dotenv()
DOWNLOADS_DIR = os.getenv("DOWNLOADS_DIR")

# # Página Menu de Projetos
@menu.route('/')
def menu_page():
    menu_info = []

    # Loop que fornece as informações pra tabela do Diretório Projetos
    for report in os.listdir(DOWNLOADS_DIR):
        download_path = os.path.join(DOWNLOADS_DIR, report)
        size = get_size(download_path)
        menu_info.append({
            "name": report,
            "size": size,
            "modified": os.path.getmtime(download_path)
        })

    return render_template('admin/menu.html', projects=menu_info,
                           format_size=format_size,
                           format_date=format_date)
