from aws_cdk import (
    core,
    aws_dynamodb
)
from config import config


class AmazonCdkStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # create dynamo table
        employees_table = aws_dynamodb.Table(
            self, config.TABLE_NAME,
            partition_key=aws_dynamodb.Attribute(
                name='country-city-warehouse',
                type=aws_dynamodb.AttributeType.STRING
            ),
            sort_key=aws_dynamodb.Attribute(
                name='employee',
                type=aws_dynamodb.AttributeType.STRING
            )
        )

        employees_table.add_global_secondary_index(
            partition_key=aws_dynamodb.Attribute(
                name='city',
                type=aws_dynamodb.AttributeType.STRING
            ),
            sort_key=aws_dynamodb.Attribute(
                name='employee',
                type=aws_dynamodb.AttributeType.STRING
            ),
            # non_key_attributes=['country', 'warehouse', 'name', 'address', 'date_of_birth', 'position'],
            index_name='city-index'
        )

        employees_table.add_global_secondary_index(
            partition_key=aws_dynamodb.Attribute(
                name='warehouse',
                type=aws_dynamodb.AttributeType.STRING
            ),
            sort_key=aws_dynamodb.Attribute(
                name='employee',
                type=aws_dynamodb.AttributeType.STRING
            ),
            # non_key_attributes=['country', 'city', 'name', 'address', 'date_of_birth', 'position'],
            index_name='warehouse-index'
        )

        employees_table.add_global_secondary_index(
            partition_key=aws_dynamodb.Attribute(
                name='position-city',
                type=aws_dynamodb.AttributeType.STRING
            ),
            sort_key=aws_dynamodb.Attribute(
                name='employee',
                type=aws_dynamodb.AttributeType.STRING
            ),
            # non_key_attributes=['country', 'warehouse', 'name', 'address', 'date_of_birth'],
            index_name='position-city-index'
        )