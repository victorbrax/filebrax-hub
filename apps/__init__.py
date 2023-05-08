# Local de Import das rotas dos aplicativos
from apps.admin import menu
from apps.home import home
from apps.uploads import uploads
from apps.downloads import downloads
from apps.includes import includes

# Registro das rotas dos aplicativos
def register_blueprints(app):
    app.register_blueprint(home, url_prefix="/")
    app.register_blueprint(menu, url_prefix="/menu")
    app.register_blueprint(downloads, url_prefix="/downloads")
    app.register_blueprint(uploads, url_prefix="/uploads")
    app.register_blueprint(includes, url_prefix="/")

    return app