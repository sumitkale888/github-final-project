"""Accounts service application package."""
from flask import Flask
from flask_cors import CORS
from flask_talisman import Talisman

app = Flask(__name__)
# Disable HTTPS redirection in this educational development service so local
# HTTP tests and curl examples work while the security headers are enabled.
Talisman(app, force_https=False)
CORS(app)

from service import routes  # noqa: E402,F401
