from flask import Blueprint, render_template


includes = Blueprint('includes', __name__, static_folder="static", template_folder="templates")

