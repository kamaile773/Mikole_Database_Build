"""Models for Mikole app."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Client(db.Model):
    """A user. Class will inculde Clients Info and Event Needs."""

    __tablename__ = 'clients'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50))
    goh_name = db.Column(db.String(50))
    phone_num = db.Column(db.Integer(10))
    event_type = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    location = db.Column(db.String)
    added_details = db.Column(db.String)

    def __repr__(self):
        return f'<User user_id={self.user_id} phone_num={self.phone_num} email={self.email} event_type{self.event_type} location{}>'


class Staffer(db.Model):
    """Staff Members."""

    __tablename__ = 'staff'

    staff_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    dept = db.Column(db.String)
    phone_num = db.Column(db.Integer)
    email = db.Column(db.String, unique=True)
    pay = db.Column(db.Float)
    work_status = db.Column(db.String)

    def __repr__(self):
        return f'<Staffer staff_id={self.staff_id} dept={self.dept} fname={self.fname} lname={self.lname}>'


class Party_Package(db.Model):
    """Party packages."""

    __tablename__ = 'partypackages'

    purchase_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String)
    overview = db.Column(db.Text)
    cost = db.Column(db.Float)
    party_date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('clients.user_id')
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.user_id')
    
    user = db.relationship('Client', backref='partypackages')
    staff = db.relationship('Staffer', backref='partypackages')


    def __repr__(self):
        return f'<Party_Package purchase_id={self.purchase_id} title={self.title}>'


class Inventory(db.Model):
    """In house Inventory."""

    __tablename__ = 'inventorys'

    inventory_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    vendor_id_num = db.Column(db.Integer)
    name = db.Column(db.String(50))
    image = db.Column(db.String)
    description = db.Column(db.String)
    qty = db.Column(db.Integer)
    qty_sold = db.Column(db.Integer)
    item_dept = db.Column(db.String)
    location_warehouse = db.Column(db.String)
    
    


    def __repr__(self):
        return f'<Rating rating_id={self.rating_id} score={self.score}>'


def connect_to_db(flask_app, db_uri='postgresql:///ratings', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
