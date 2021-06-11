from botocore.exceptions import ClientError
from marshmallow import ValidationError
from marshmallow import fields, validate, Schema


def full(f):
    def wrap(*args):
        wrapped_output = f(*args) + ': '
        for arg in args:
            wrapped_output += f'{arg.__dict__}'
        return wrapped_output
    return wrap


class Employee:
    def __init__(self, country, city, warehouse, employee, name, address, date_of_birht, position):
        self.country = country
        self.city = city
        self.warehouse = warehouse
        self.employee = employee
        self.name = name
        self.address = address
        self.date_of_birth = date_of_birht
        self.position = position
        self.position_city = f'{position};{city}'
        self.country_city_warehouse = f'{country};{city};{warehouse}'
    
    @full
    def __repr__(self):
        return f'{type(self).__name__}[{self.employee}]'


class EmployeeSchema(Schema):
    country = fields.String(required=True, validate=validate.Length(min=1))
    city = fields.String(required=True, validate=validate.Length(min=1))
    warehouse = fields.String(required=True, validate=validate.Length(min=1))
    employee = fields.UUID(required=True)
    name = fields.String(validate=validate.Length(min=1))
    address = fields.String(validate=validate.Length(min=1))
    date_of_birth = fields.Date()
    position = fields.String(required=True, validate=validate.Length(min=1))
    position_city = fields.String(required=True, validate=validate.Length(min=1))
    country_city_warehouse = fields.String(required=True, validate=validate.Length(min=1))


def validate_date(date):
    return date.strftime('%Y-%m-%d')
