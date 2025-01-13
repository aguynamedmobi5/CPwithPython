import sys
import boto3

ec2 = boto3.client('ec2')

action = sys.argv[1]
print(action)
instance_ids = sys.argv[2:]
print(instance_ids)


def start_instances(instance_ids):
    try:
        response = ec2.start_instances(InstanceIds=instance_ids)
        print(response)
    except:
        print("Something else went wrong") 



def stop_instances(instance_ids):
    try:
        response = ec2.stop_instances(InstanceIds=instance_ids)
        print(response)
    except:
        print("Something else went wrong") 



if action == "start":
    start_instances(instance_ids)

else:
    stop_instances(instance_ids)