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
    paid = db.Column(db.boolean)

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
    pay_grade = db.Column(db.Float)
    work_status = db.Column(db.String)
    emp_attributes = db.Column(db.String)
    emp_exceptions = db.Column(db.String)

    def __repr__(self):
        return f'<Staffer staff_id={self.staff_id} dept={self.dept} fname={self.fname} lname={self.lname}>'


class Party_Package(db.Model):
    """Party packages."""

    __tablename__ = 'partypackages'

    purchase_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String)
    overview = db.Column(db.Text)
    cost = db.Column(db.Float)
    total_cost = db.Column(db.Float)
    party_date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('clients.user_id')
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.staff_id')
    
    user = db.relationship('Client', backref='partypackages')
    staff = db.relationship('Staffer', backref='partypackages')

    def __repr__(self):
        return f'<Party_Package purchase_id={self.purchase_id} title={self.title} total_cost{self.total_cost}>'


class Party_Purchase_List(db.Model):
    """Items needed for party packages."""

    __tablename__ = 'pplists'

    pp_list_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    dept = db.Column(db.Integer)
    name = db.Column(db.String(50))
    description = db.Column(db.String)
    qty = db.Column(db.Integer)
    available = db.Column(db.String)
    qty_needed = db.Column(db.Integer)
    party_cost = db.Column(db.Float)
    purchase_id = db.Column(db.Integer, db.ForeignKey('partypackages.purchase_id')
    inventory_id = db.Column(db.Integer, db.ForeignKey('inventorys.inventory_id')

    purchase = db.relationship('Party_Package', backref='pplists')
    inventory = db.relationship('Inventory', backref='pplists')
    
    def __repr__(self):
        return f'<Party_Package_List pp_list_id={self.pp_list_id} name={self.name} dept={self.dept} qty={self.qty} party_cost{self.party_cost}>'


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
        return f'<Inventory inventory_id={self.inventory_id} name={self.inventory} item_dept={self.item_dept} qty={self.qty}>'


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
