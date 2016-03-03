# Standard library dependencies
import socket
import struct

# Third-party dependencies
from peewee import *

# Internal dependencies
from api import util

db = MySQLDatabase('tenko', user='tenko', password='test')

# -- Custom Fields

class IPV4AddressField(Field):
    db_field = 'int unsigned'

    def db_value(self, value):
        return struct.unpack("!L", socket.inet_aton(value))[0]

    def python_value(self, value):
        return socket.inet_ntoa(struct.pack('!L', value))


class MacAddressField(Field):
    db_field = 'bigint unsigned'

    def db_value(self, value):
        return util.from_base(value, 16, 10)

    def python_value(self, value):
        return util.to_base(value, 16)

# -- Models

class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    uuid = UUIDField(null=False, unique=True)
    username = CharField(null=False, unique=True)

    class Meta:
        order_by = ('username',)
        db_table = 'users'


class Host(BaseModel):
    uuid = UUIDField(null=False, unique=True)

    class Meta:
        db_table = 'hosts'


class Sensor(BaseModel):
    """
    A remote sensor that monitors network activity and
    serves a variety of honeypots on a specified subnet.
    """
    uuid = UUIDField(null=False, unique=True)
    created_at = DateTimeField()
    updated_at = DateTimeField()
    hostname = CharField(null=False, unique=True)
    mac_address = MacAddressField(null=False, unique=True)
    ipv4_address = IPV4AddressField(null=False, unique=True)
    description = TextField()

    class Meta:
        order_by = ('hostname',)
        db_table = 'sensors'


class Contact(BaseModel):
    uuid = UUIDField(null=False, unique=True)
    created_at = DateTimeField()
    updated_at = DateTimeField()
    email_address = CharField(null=False, unique=True)

    class Meta:
        order_by = ('email_address',)
        db_table = 'contacts'


# Simple utility to create tables
def create_tables():
    db.connect()
    db.create_tables([User, Host, Sensor, Contact], safe=True)