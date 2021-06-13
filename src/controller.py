import boto3
from config import config
from .model import Employee, EmployeeSchema
from boto3.dynamodb.conditions import Key
from marshmallow import ValidationError
from botocore.exceptions import ClientError


class Controller:
    def __init__(self):
        self.client = boto3.resource('dynamodb')
        self.table = self.client.Table(config.TABLE_NAME)
        self.schema = EmployeeSchema()
    
    def put_employee(self, employee):
        try:
            new_employee = self.schema.load(employee)
        except ValidationError as e:
            print(f'{e.messages}')
        try:
            response = self.table.put_item(Item=self.schema.dump(new_employee))
            print('New Employee added')
        except ClientError as e:
            print(f'{e}')



    def query_by_city(self, city):
        try: 
            response = self.table.query(
                IndexName='city-index',
                KeyConditionExpression=Key('city').eq(city)
            )
            items = response['Items']
            while 'LastEvaluetionKey' in response:
                response = self.table.query(
                    IndexName='city-index',
                    KeyConditionExpression=Key('city').eq(city),
                    ExlusiveStartKey=response['LastEvaluetedKey']
                )
                items.extend(response['Items'])
        except ClientError as e:
            print(f'{e}')

        try:
            validated_items = self.schema.load(items, many=True)
            result = [Employee(**item) for item in validated_items]
        except ValidationError as e:
            print(f'{e.messages}')

        return result


    def query_by_warehouse(self, warehouse):
        try:
            response = self.table.query(
                IndexName='warehouse-index',
                KeyConditionExpression=Key('warehouse').eq(warehouse)
            )
            items = response['Items']
            while 'LastEvaluetionKey' in response:
                response = self.table.query(
                    IndexName='warehouse-index',
                    KeyConditionExpression=Key('warehouse').eq(warehouse),
                    ExlusiveStartKey=response['LastEvaluetedKey']
                )
                items.extend(response['Items'])
        except ClientError as e:
            print(f'{e}')

        try:
            validated_items = self.schema.load(items, many=True)
            result = [Employee(**item) for item in validated_items]
        except ValidationError as e:
            print(f'{e.messages}')
            
        return result


    def query_by_position_in_a_city(self, position, city):
        try:
            response = self.table.query(
                IndexName='position-city-index',
                KeyConditionExpression=Key('position_city').eq(f'{position};{city}')
            )
            items = response['Items']
            while 'LastEvaluetionKey' in response:
                response = self.table.query(
                    IndexName='position-city-index',
                    KeyConditionExpression=Key('position_city').eq(f'{position};{city}'),
                    ExlusiveStartKey=response['LastEvaluetedKey']
                )
                items.extend(response['Items'])
        except ClientError as e:
            print(f'{e}')

        try:
            validated_items = self.schema.load(items, many=True)
            result = [Employee(**item) for item in validated_items]
        except ValidationError as e:
            print(f'{e.messages}')
            
        return result
