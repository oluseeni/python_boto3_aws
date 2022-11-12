import boto3

ec2_resource = boto3.resource("ec2")

# Launch EC2 instance Using boto3
#instances = ec2_resource.create_instances(
#    ImageId = 'ami-09d3b3274b6c5d4aa', #free tier eligible
#    InstanceType = 't2.micro', #free tier eligible
#    MaxCount = 1,
#    MinCount = 1,
#)

#Get Instance ID using boto3
#x = ec2_resource.describe_instances()
#data = x["Reservations"][0]
#data_instances = data["Instances"]
#for i in range(len(data_instances)):
#    print(f"instance id is {data_instances[i]['InstanceId']}")

#create multiple EC2s
#response = ec2_resource.create_instances(
#    ImageId = 'ami-09d3b3274b6c5d4aa',
#    InstanceType = 't2.micro',
#    MaxCount = 3,
#    MinCount = 3)

#Terminate instances using boto3
#ec2_resource.instances.filter(InstanceIds=['string']).terminate()
