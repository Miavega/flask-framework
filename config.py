import os
from app import app

_DEVELOPMENT = "DEVELOPMENT"
_PRODUCTION = "PRODUCTION"

def start_app(mode):
    if mode == "DEVELOPMENT":
        os.environ["FLASK_ENV"] = _DEVELOPMENT
        app.run(host="127.0.0.1", port="3000", debug=True)
    elif mode == "PRODUCTION":
        os.environ["FLASK_ENV"] = _PRODUCTION
        app.run(host="0.0.0.0", port="3001", debug=False)
