import boto3 #It is used to import boto3
import json 
import datetime

#Variables
sg_name = 'rds-sg-dev-demo'
sg_description = 'RDS Security Group for AWS Dev Study Guide'
my_ip_cidr = '0.0.0.0/0'

#Create the EC2 Client to create the Security Group for your Database
ec2_client = boto3.client('ec2')

response = ec2_client.create_security_group(Description=sg_description, GroupName=sg_name)
print(json.dumps(response, indent=2, sort_keys=True))

response = ec2_client.authorize_security_group_ingress(CidrIp=my_ip_cidr, FromPort=3306, GroupName=sg_name, ToPort=3306, IpProtocol='tcp')
print("Security Group should be created! Verify this in the AWS Console.")