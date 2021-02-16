"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb mikole')
os.system('createdb mikole')

model.connect_to_db(server.app)
model.db.create_all()

### Create Party Packages
pkgA = Party_Package(title='Package A',overview='',cost='400',qty_of_guest='20')
pkgB = Party_Package(title='Package B',overview='',cost='1000',qty_of_guest='50')
pkgC = Party_Package(title='Package C',overview='',cost='1800',qty_of_guest='100')
pkgD = Party_Package(title='Package D',overview='',cost='',qty_of_guest='15o')

db.session.add(pkgA)
db.session.add(pkgB)
db.session.add(pkgC)
db.session.add(pkgD)

db.session.commit()


# Adding locations

locationOne = Location(city='San Francisco', address='2342 Hamilton Way')
locationTwo = Location(city='New York', address='5425 Lincoln Drive')
locationThree = Location(city='Las Vegas', address='324 Washington Ave')

db.session.add(locationOne)
db.session.add(locationTwo)
db.session.add(locationThree)

db.session.commit()


##Add inventory items
food = Inventory(item_dept='',vendor_id_num=,name='',image='',description='',people_per_item=)
decorations = Inventory(item_dept='',vendor_id_num=,name='',image='',description='',people_per_item=)
products = Inventory(item_dept='',vendor_id_num=,name='',image='',description='',people_per_item=)
equipment = Inventory(item_dept='',vendor_id_num=,name='',image='',description='',people_per_item=)

db.session.add(food)
db.session.add(decorations)
db.session.add(products)
db.session.add(equipment)

db.session.commit()

Host =  Staffer(
    fname = '',
    lname = '',
    dept = '',
    phone_num = '',
    email = '',
    pay_grade = '',
    work_status = '',
    emp_attributes = '',
    emp_exceptions = '',
    availability = ''
    )

Setup_Teardown =  Staffer(
    fname = '',
    lname = '',
    dept = '',
    phone_num = '',
    email = '',
    pay_grade = '',
    work_status = '',
    emp_attributes = '',
    emp_exceptions = '',
    availability = ''
    )

Kitchen =  Staffer(
    fname = '',
    lname = '',
    dept = '',
    phone_num = '',
    email = '',
    pay_grade = '',
    work_status = '',
    emp_attributes = '',
    emp_exceptions = '',
    availability = ''
    )
Entertainment =  Staffer(
    fname = '',
    lname = '',
    dept = '',
    phone_num = '',
    email = '',
    pay_grade = '',
    work_status = '',
    emp_attributes = '',
    emp_exceptions = '',
    availability = ''
    )

db.session.add(Host)
db.session.add(Kitchen)
db.session.add(Setup_Teardown)
db.session.add(Entertainment)

db.session.commit() 