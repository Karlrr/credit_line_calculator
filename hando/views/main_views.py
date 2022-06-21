from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_hando():
    return '한도페이지 입니다!'

@bp.route('/')
def index():
    return '한도페이지 index'