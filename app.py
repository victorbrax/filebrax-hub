from flask import Flask, render_template
from apps import register_blueprints
from dotenv import load_dotenv
import os


load_dotenv()
APP_KEY = os.getenv("APP_KEY")

app = Flask(__name__)
app.secret_key = APP_KEY

# Rota padrão para página 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('includes/not_found.html')

register_blueprints(app)

if __name__ == "__main__":
    app.run(debug=True, port=8000)

# Obrigado pelo Prestígio! :)