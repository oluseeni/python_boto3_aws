import boto3

ddb_table = boto3.resource('dynamodb')  #DynamoDB method used to call python boto3's DynamoDB resource

table = ddb_table.create_table(     #Create table using python boto3
    TableName='wk14_movies_table',  #Name giving to my Table.
    KeySchema=[
        {
            'AttributeName': 'Movie_Title', #Name of partition key
            'KeyType': 'HASH'  #Partition key type
        },
        {
            'AttributeName': 'Genre',       #Name of sort key
            'KeyType': 'RANGE'  #Sort key type
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Movie_Title',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'Genre',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,     #the read capacity of the table.
        'WriteCapacityUnits': 1     #the write capacity to the table.
    }
)

print("Table status:", table.table_status)  #Display message that the table is being created.