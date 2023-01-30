'''example for normale SQLAlchemy
"""Example SQLAlchemy ORM models."""
from sqlalchemy import CheckConstraint, Column, ForeignKey, UniqueConstraint, orm, types

Base = orm.declarative_base()


class User(Base):
    """A ``user``."""

    __tablename__ = "dbusers"
    __table_args__ = (UniqueConstraint("first_name", "last_name"),)
    pk = Column(types.Integer, primary_key=True)
    first_name = Column(types.String, doc="The name of the user.")
    last_name = Column(types.String(255), doc="The surname of the user.")
    dob = Column(types.Date, nullable=False, doc="The date of birth.")


class Address(Base):
    """An address."""

    __tablename__ = "addresses"
    __table_args__ = (CheckConstraint("number>0", name="check1"),)
    pk = Column(types.Integer, primary_key=True)
    number = Column(types.Integer, nullable=False, doc="The number of the address.")
    postcode = Column(
        types.String, nullable=False, index=True, doc="The postcode of the address."
    )
    user_id = Column(types.Integer, ForeignKey("dbusers.pk"))
    user = orm.relationship("User")
'''



#added myself
import pymysql
pymysql.install_as_MySQLdb()
#------

from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:FabianAchim67!@localhost/documentation_test_database'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))

def __init__(self, name, city, addr,pin):
    self.name = name
    self.city = city
    self.addr = addr
    self.pin = pin

@app.route('/')
def show_all():
    return render_template('show_all.html', students = students.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            flash('Please enter all the fields', 'error')
        else:
            student = students(request.form['name'], request.form['city'],
                               request.form['addr'], request.form['pin'])

            db.session.add(student)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
    return render_template('new.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug = True)
'''


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://test_user:1234@localhost/documentation_test_database"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

@app.route("/")
def index():
    user = User(name="John Doe", email="johndoe@example.com")
    db.session.add(user)
    db.session.commit()
    return "User added to the database."

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
'''
