from flask import Flask
from .extensions import db, migrate
import os


def create_app():

    #  取得目前文件資料夾路徑
    pjdir = os.path.abspath(os.path.dirname(__file__))

    app = Flask(__name__)
    #  新版本的部份預設為none，會有異常，再設置True即可。
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #  設置sqlite檔案路徑
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(pjdir, 'data.sqlite')

    db.init_app(app)
    from . import model             # 這個有待研究 如果沒有他 flask db migrate 不到model的table
    migrate.init_app(app, db)

    return app
