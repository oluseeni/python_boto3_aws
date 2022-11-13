import boto3
import json

ddb_table = boto3.client('dynamodb')  #DynamoDB method used to call python boto3's DynamoDB resource

scan_response = ddb_table.scan(         #scan method used to scan the table.
    TableName = 'wk14_movies_table'
    )

for i in scan_response["Items"]:        #Iteration to show results of scan.
    print(json.dumps(i))
    
