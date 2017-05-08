#####this file basically contains the settings related to your aws and some variables which is being used while creating lambda functions####
####lambda role should have a read and write acces to ec2 console######
AWS={
        'accountid':'',
        'lambdaRole':'',
        'aws_secret_key':'',
        'aws_access_key':''
}

BACKUP={
        'daily':{
            'retention_period':'',
            'no_of_days':'',
            'creation_time':'',
            'deletion_time':''
        },
        'monthly':{
            'creation_time':'',
            'deletion_time':'',
            'retention_period':'',
        },
        'weekly':{
            'creation_time':'',
            'deletion_time':'',
            'retention_period':'',
        }
}

EMAIL={
    'id':[],
    'sns':'',
}
