from sqlalchemy import Column, Integer, Numeric, String, Boolean, ForeignKey, Table
from sqlalchemy.orm import mapper, relationship
from database import metadata, db_session

#objects
class Customer(object):
    def __init__(self, name=None, email=None, phone=None, company=None, registered=False):
		self.name = name
		self.email = email
		self.phone = phone
		self.company = company
		self.registered = registered

class Order(object):
	def __init__(self, customer_id=None, total_amount=None, discount=None, order_created=None, order_fulfilled=None):
		self.customer_id = customer_id
		self.total_amount = total_amount
		self.discount = discount
		self.order_created = order_created
		self.order_fulfilled = order_fulfilled

class Payment(object):
	def __init__(self, order_id=None, payment_on=None, payment_status=None, payment_method=None):
		self.order_id = order_id
		self.payment_on = payment_on
		self.payment_status = payment_status
		self.payment_method = payment_method

#tables
customers = Table('customers', metadata,
	Column('id', Integer, primary_key=True),
	Column('name', String(40)),
	Column('email', String(40)),
	Column('phone', String(15)),
	Column('company', String(40)),
	Column('registered', Boolean)
)

orders = Table('orders', metadata,
	Column('id', Integer, primary_key=True),
	Column('customer_id', Integer, ForeignKey('customers.id')),
	Column('total_amount', Numeric(2)),
	Column('discount', Numeric(2)),
	Column('order_created', String(40)),
	Column('order_fulfilled', String(40))
)

payments = Table('payments', metadata,
	Column('id', Integer, primary_key=True),
	Column('order_id', Integer, ForeignKey('orders.id')),
	Column('payment_on', String(40)),
	Column('payment_status', String(40)),
	Column('payment_method', String(40))
)

#mappers
mapper(Customer, customers)
mapper(Order, orders)
mapper(Payment, payments)



