import os

class Config(object):
    SECRET_KEY = os.environ.get('S3CR3TK3Y') or "you'll never guess"