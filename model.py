"""Models for Mikole app."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# db_uri = "postgresql:///mikole"

db = SQLAlchemy()


class Client(db.Model):
    """A user. Class will include Clients Info and Event Needs."""

    __tablename__ = 'clients'

    client_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50))
    phone_num = db.Column(db.Integer)
    email = db.Column(db.String, unique=True)
    
    def __repr__(self):
        return f'<Clients client_id={self.client_id} name={self.name}>'

class Event(db.Model):
    """Unique Event selection set by Client."""

    __tablename__ = 'events'

    event_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    goh_name = db.Column(db.String(50))
    date_of_event = db.Column(db.DateTime)
    added_details = db.Column(db.String)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.location_id'))
    purchase_id = db.Column(db.Integer, db.ForeignKey('partypackages.purchase_id'))
    client_id = db.Column(db.Integer, db.ForeignKey('clients.user_id'))
    partystaff_id = db.Column(db.Integer, db.ForeignKey('partystaffers.partystaff_id'))
    
    location = db.relationship('Location', backref='events')
    client = db.relationship('Client', backref='events')
    partypackage = db.relationship('Party_Package', backref='events')
    partystaff = db.relationshp('Partystaffer', backref='events')

    def __repr__(self):
        return f'<Event event_id={self.event_id} goh_name={self.goh_name} date_of_event{self.date_of_event} party_package{self.party_package}>'

class Party_Package(db.Model):
    """Party packages."""

    __tablename__ = 'partypackages'

    purchase_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String)
    overview = db.Column(db.Text)
    cost = db.Column(db.Float)
    qty_of_guest = db.Column(db.Integer)

    def __repr__(self):
        return f'<Party_Package purchase_id={self.purchase_id} title={self.title}>'

class Location(db.Model):
    """Location of Party"""

    __tablename__= 'locations'

    location_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    city = db.Column(db.String)
    address = db.Column(db.String)

    def __repr__(self):
        return f'<Location location_id={self.location_id} city={self.city}>'


class Party_Purchase_Items(db.Model):
    """Items needed for party packages."""

    __tablename__ = 'ppilists'

    ppi_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    dept = db.Column(db.Integer)
    name = db.Column(db.String(50))
    purchase_id = db.Column(db.Integer, db.ForeignKey('partypackages.purchase_id'))
    inventory_id = db.Column(db.Integer, db.ForeignKey('inventories.inventory_id'))

    party_package = db.relationship('Party_Package', backref='ppilists')
    inventory = db.relationship('Inventory', backref='ppilists')

    def __repr__(self):
        return f'<Party_Package_List pp_list_id={self.pp_list_id} name={self.name} dept={self.dept} qty={self.qty} party_cost{self.party_cost}>'

class Inventory(db.Model):
    """In house Inventory."""

    __tablename__ = 'inventories'

    inventory_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    item_dept = db.Column(db.String)
    vendor_id_num = db.Column(db.Integer)
    name = db.Column(db.String(50))
    image = db.Column(db.String)
    description = db.Column(db.String)
    people_per_item = db.Column(db.Integer)
    
    def __repr__(self):
        return f'<Inventory inventory_id={self.inventory_id} name={self.name} item_dept={self.item_dept} people_per_item={self.people_per_item}>'

class Staffer(db.Model):
    """Staff Members."""

    __tablename__ = 'staffers'

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
    availability = db.Column(db.String)

    def __repr__(self):
        return f'<Staffer staff_id={self.staff_id} dept={self.dept} fname={self.fname} lname={self.lname}>'

class PartyStaffer(db.Model):
    """Party Staff Members."""

    __tablename__ = 'partystaffers'

    partystaff_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.purchase_id'))
    staffer_id = db.Column(db.Integer, db.ForeignKey('staffers.staff_id'))
    
    def __repr__(self):
        return f'<PartyStaffer partystaff_id={self.partystaff_id}>'


def connect_to_db(flask_app, db_uri='postgresql:///mikole', echo=True):
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

# Future description class on Inventory Data(db.Model)
#     inventory_data = db.Column(db.String)
#     qty = db.Column(db.Integer)
#     available = db.Column(db.String)
#     qty_needed = db.Column(db.Integer)
#     item_cost = db.Column(db.Float)
#     purchase_id = db.Column(db.Integer, db.ForeignKey('partypackages.purchase_id'))
#     inventory_id = db.Column(db.Integer, db.ForeignKey('inventorys.inventory_id'))
#     purchase = db.relationship('Party_Package', backref='ppilists')
#     inventory = db.relationship('Inventory', backref='ppilists')
    