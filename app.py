from flask import Flask, Blueprint
from os.path import abspath

app = Flask(__name__,
            static_folder=abspath("src/templates/static"),
            template_folder=abspath("src/templates"),
            )

css_blueprint = Blueprint('css', __name__, static_url_path='/css', static_folder=abspath("src/templates/utils/css"))
app.register_blueprint(css_blueprint)

js_blueprint = Blueprint('js', __name__, static_url_path='/js', static_folder=abspath("src/templates/utils/js"))
app.register_blueprint(js_blueprint)