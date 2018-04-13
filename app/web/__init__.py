from flask import Blueprint

web = Blueprint('web', __name__)

from . import book, main, auth, drift, gift, wish
