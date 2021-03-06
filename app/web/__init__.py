from flask import Blueprint
from flask import render_template

web = Blueprint('web', __name__)


@web.app_errorhandler(404)
def handle404(e):
    return render_template('404.html')


@web.app_errorhandler(500)
def handle500(e):
    return render_template('500.html')


from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish
