# Standard library dependencies
import datetime
import json
import uuid

# Third-party dependencies
import hug

# Internal dependencies
from api import db

# Initialize the database.
db.create_tables()

# Read the various configuration files.
with open('../config/auth.json') as fh:
    auth_config = json.load(fh)

authentication = hug.authentication.basic(hug.authentication.verify(auth_config['API_KEY'], ''))

## -- Contacts Resource

# GET /contacts
#
# Globally list all contacts.
@hug.get('/api/v1/contacts', requires=authentication, output=hug.output_format.json)
def contact_listing_handler():
    contacts = {}
    for contact in db.Contact.select():
        contacts[str(contact.uuid)] = str(contact.email_address)
    return json.dumps(contacts)


# POST /contacts
#
# Create a new contact.
@hug.default_input_format("application/json")
@hug.post('/api/v1/contacts', requires=authentication)
def contact_creation_handler(body):
    data = hug.input_format.json(body)
    contact, created = db.Contact.get_or_create(uuid=uuid.uuid4(),
                                                created_at=datetime.datetime.now(),
                                                updated_at=datetime.datetime.now(),
                                                email_address=data['email_address'])
    if created:
        return created
    else:
        return 'A contact with that email already exists!'


## -- Sensors Resource

# GET /sensors
#
# List all currently registered sensors and their status.
@hug.get('/api/v1/sensors', requires=authentication, output=hug.output_format.json)
def sensor_listing_handler():
    sensors = {}
    for sensor in db.Sensor.select():
        sensors[str(sensor.uuid)] = str(sensor.ipv4_address)
    return json.dumps(sensors)


# POST /sensors
#
# Register a new sensor.
@hug.default_input_format("application/json")
@hug.post('/api/v1/sensors', requires=authentication)
def sensor_registration_handler(body):
    data = hug.input_format.json(body)
    sensor, created = db.Sensor.get_or_create(uuid=uuid.uuid4(),
                                              created_at=datetime.datetime.now(),
                                              updated_at=datetime.datetime.now(),
                                              hostname=data['hostname'],
                                              mac_address=data['mac_address'],
                                              ipv4_address=data['ipv4_address'])
    if created:
        return created
    else:
        return 'A sensor with that hostname already exists!'