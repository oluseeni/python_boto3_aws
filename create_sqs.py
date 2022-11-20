import boto3

sqs = boto3.resource('sqs')     # Get the service resource

queue = sqs.create_queue(       # Create the queue. This returns an SQS.Queue instance
    QueueName = 'week15_messages', 
    Attributes = {
        'DelaySeconds': '30',
        'MessageRetentionPeriod': '86400'
    }
)

print(queue.url)                # You can now access identifiers and attributes
# print(queue.attributes.get('DelaySeconds'))

