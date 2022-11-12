import boto3

client = boto3.client("ec2")

#Create VPC using boto3
#response = client.create_vpc(
#    CidrBlock='10.0.0.0/16'
#)
#print(response)

#Describe VPC using boto3
#response_desc = client.describe_vpcs()["Vpcs"]
#for vpc in response_desc:
#   print(vpc["VpcId"])
#    Filters=[
#        {
#            'Name': 'string',
#            'Values': [
#                'string',
#            ]
#        },
#    ],
#    VpcIds=[
#        'vpc-006bec8185fd7d535',
#    ],
#)
#print(response_desc)

#Remove VPC using boto3
#response_del = client.delete_vpc(
#    VpcId='string',
#)
#print(response_del)
