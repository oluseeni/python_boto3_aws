import boto3
import os
import glob

cwd = os.getcwd()
cwd = cwd + "/luit_python_code_repo/"
files = glob.glob(cwd + "*.py")

resource = boto3.resource("s3")
resource.buckets.all()

#search s3 bucket
for bucket in resource.buckets.all():
    print(bucket.name)
    
s3_resource = boto3.client("s3")
creation_date = s3_resource.list_buckets()["Buckets"]

#Get creation date of s3 bucket
for bucket in s3_resource.list_buckets()["Buckets"]:
    print(bucket["Name"])
    print(bucket["CreationDate"])

#Upload to s3 bucket   
#for file in files:
#    s3_resource.upload_file(
#    Filename = file,
#    Bucket = "bucket******",
#    Key = file.split("/"))

bucket_list = s3_resource.list_objects(Bucket = "bucket******")["Contents"]

#list objects in s3 bucket
for bucket in bucket_list:
    print(bucket["Key"])

#delete single object
s3_resource.delete_object(Bucket = 'bucket******',
    Key = '*.jpg')

bucket_list = s3_resource.list_objects(Bucket = "bucket******")["Contents"]

#delete multiple objects
for bucket in bucket_list:
    response = s3_resource.delete_object(Bucket = 'bucket******',
    Key = bucket["Key"])
    print(response)



