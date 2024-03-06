from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b"\xa5\xdbF:X\xaa\xcd\xd7'\x83L\xbb\xd1j\xba\xe6"

