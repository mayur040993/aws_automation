import boto3
import os
retention_period=os.environ['retention_period']
no_of_days=os.environ['no_of_days']
creation_time=os.environ['creation_time']
deletion_time=os.environ['deletion_time']

def get_regions():
    session=boto3.Session()
    regions=session.get_available_regions(services)
    return regions

def generate_ami_regions(retention_period,regions):
    for region in regions:
        session=boto3.session.Session(region_name=region)
        client=session.client('ec2')
        dict_ami=get_reservations(client)
        create_ami(dict_ami,client)

def get_reservations(client):
        dict_ami={}
        reservations=client.describe_instances()
        for reservation in reservations['Reservations']:
                instances=reservation['Instances']
                for instance in instances:
                        tags=instance['Tags']
                        for tag in tags:
                                if tag['Key']=='Name':
                                        instance_name=tag['Value']
                        if not instance_name:
                                instance_name=instance['InstanceId']
                        dict_ami[instance['InstanceId']]=instance_name
        return dict_ami

def create_ami(dict_ami,client):
    for inst_id in dict_ami.keys():
        date=datetime.datetime.now()
        str_date=str(date)
        inst_name=dict_ami[inst_id]+str_date
        print inst_name
        inst_name=re.sub('[:-_/.)( ]', '', inst_name)
        print inst_name
        response = client.create_image(
                DryRun=False,
                InstanceId=inst_id,
                Name=inst_name,
                Description=inst_name,
                NoReboot=True
               )
        print response

def lambda_handler(event,context):
    regions=get_regions('ec2')
    generate_ami_regions(regions)
