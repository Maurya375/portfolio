from datetime import datetime

from sqlalchemy.orm import *
from flask_sqlalchemy import *
from flask import *
app = Flask(__name__)
class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)
reg = registry()

class Fullstack(db.Model):
    id: Mapped[int] = MappedColumn(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    link: Mapped[str]
    image: Mapped[str]
class Frontend(db.Model):
    id: Mapped[int] = MappedColumn(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    link: Mapped[str]
    image: Mapped[str]
class Mobileapp(db.Model):
    id: Mapped[int] = MappedColumn(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    link: Mapped[str]

class Certifcate(db.Model):
    id: Mapped[int] = MappedColumn(primary_key=True)
    title: Mapped[str]
    description: Mapped[str]
    date: Mapped[datetime]
    link: Mapped[str]





# with app.app_context():
#     db.create_all()
# with app.app_context():
#
#     # db.session.add(Certifcate(title='Developong cloud apps with Node and React  ',description="",date=datetime(year=2022,month=10,day=30),link="https://github.com/Maurya375/portfolio/blob/main/certification/Node.js%20and%20React.pdf"))
#     db.session.add(Certifcate(title='Google Data Analytics',description="",date=datetime(year=2022,month=10,day=24),link="https://github.com/Maurya375/portfolio/blob/main/certification/google%20Data%20Analytics.pdf"))
#     db.session.add(Certifcate(title='Full Stack Web Developement',description="",date=datetime(year=2022,month=10,day=24),link="https://github.com/Maurya375/portfolio/blob/main/certification/fullstack%20web%20dev.pdf"))
#     db.session.commit()

# with app.app_context():
#     fullstack =[]
#     fullstack.append(Fullstack(name='scheduling Site',description="ksdjBFKsbdfkjbdkFJBKSDJF,SBKDBFKSDJFBK",link='https://mail.google.com',image='scheduling-site'))
#     fullstack.append(Fullstack(name='scheduling Site', description="ksdjBFKsbdfkjbdkFJBKSDJF,SBKDBFKSDJFBK",link='https://mail.google.com',image='scheduling-site'))
#     fullstack.append(Fullstack(name='scheduling Site', description="ksdjBFKsbdfkjbdkFJBKSDJF,SBKDBFKSDJFBK",link='https://mail.google.com',image='scheduling-site'))
#     fullstack.append(Fullstack(name='scheduling Site', description="ksdjBFKsbdfkjbdkFJBKSDJF,SBKDBFKSDJFBK",link='https://mail.google.com',image='scheduling-site'))
#     db.session.add_all(fullstack)
#     db.session.commit()
# with app.app_context():
#     frontend =[]
#     frontend.append(Frontend(name="Math operations site",description="ksdjBFKsbdfkjbdkFJBKSDJF,SBKDBFKSDJFBK",link='https://mail.google.com',image='mathoperation'))
#     frontend.append(Frontend(name="fruit Slicing app",description="ksdjBFKsbdfkjbdkFJBKSDJF,SBKDBFKSDJFBK",link='https://mail.google.com', image='fruit-slice-app'))
#
#     db.session.add_all(frontend)
#     db.session.commit()
