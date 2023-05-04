from app import apps


@apps.route('/')
@apps.route('/index')
def index():
    return "Hello, World!"
