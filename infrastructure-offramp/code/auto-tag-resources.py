#Python function to tag AWS resources such as EC2, Lambda, Glue, Sagemaker and SSM based on a CloudWatch trigger.

import boto3
import os

def tagEc2Instances (event, moniker_tag, team_tag, owner_tag):
    ec2 = boto3.client('ec2')
    for instance in event['detail']['responseElements']['instancesSet']['items']:
        response = ec2.create_tags (
            Resources=[instance['instanceId']],
            Tags=[
                {
                    'Key':'adsk:moniker',
                    'Value': moniker_tag
                },
                {
                    'Key':'adsk:team',
                    'Value': team_tag
                },
                {
                    'Key':'owner',
                    'Value': owner_tag
                }
            ]
        )
    print(response)

def tagGlueJob(event, moniker_tag, team_tag, owner_tag):
    glueClient = boto3.client('glue')
    glue_job = event['detail']['responseElements']['name']
    glue_job_arn = 'arn:aws:glue:' + os.environ['REGION'] + ':' + os.environ['ACCOUNTID'] + ':job/' + glue_job
    response = glueClient.tag_resource(
        ResourceArn=glue_job_arn,
        TagsToAdd={
            'adsk:moniker': moniker_tag,
            'adsk:team': team_tag,
            'owner': owner_tag
        }
    )
    print(response)

def tagGlueCrawler(event, moniker_tag, team_tag, owner_tag):
    glueClient = boto3.client('glue')
    crawler = event['detail']['requestParameters']['name']
    crawler_arn = 'arn:aws:glue:' + os.environ['REGION'] + ':' + os.environ['ACCOUNTID'] + ':crawler/' + crawler
    response = glueClient.tag_resource(
        ResourceArn=crawler_arn,
        TagsToAdd={
            'adsk:moniker': moniker_tag,
            'adsk:team': team_tag,
            'owner': owner_tag
        }
    )
    print(response)

def tagGlueTrigger(event, moniker_tag, team_tag, owner_tag):
    glueClient = boto3.client('glue')
    trigger = event['detail']['requestParameters']['name']
    trigger_arn = 'arn:aws:glue:' + os.environ['REGION'] + ':' + os.environ['ACCOUNTID'] + ':trigger/' + trigger
    response = glueClient.tag_resource(
        ResourceArn=trigger_arn,
        TagsToAdd={
            'adsk:moniker': moniker_tag,
            'adsk:team': team_tag,
            'owner': owner_tag
        }
    )
    print(response)

def tagLambda(event, moniker_tag, team_tag, owner_tag):
    lambdaClient = boto3.client('lambda')
    function = event['detail']['requestParameters']['functionName']
    function_arn = 'arn:aws:lambda:' + os.environ['REGION'] + ':' + os.environ['ACCOUNTID'] + ':function:' + function
    response = lambdaClient.tag_resource(
        Resource=function_arn,
        Tags={
            'adsk:moniker': moniker_tag,
            'adsk:team': team_tag,
            'owner': owner_tag
        }
    )
    print(response)

def tagSmNotebook(event, moniker_tag, team_tag, owner_tag):
    sagemakerClient = boto3.client('sagemaker')
    notebook = event['detail']['requestParameters']['notebookInstanceName']
    notebook_arn = 'arn:aws:sagemaker:' + os.environ['REGION'] + ':' + os.environ['ACCOUNTID'] + ':notebook-instance/' + notebook
    response = sagemakerClient.add_tags(
        ResourceArn=notebook_arn,
        Tags=[
            {
                'Key':'adsk:moniker',
                'Value': moniker_tag
            },
            {
                'Key':'adsk:team',
                'Value': team_tag
            },
            {
                'Key':'owner',
                'Value': owner_tag
            }
        ]
    )
    print(response)

def tagSmTrainingJob(event, moniker_tag, team_tag, owner_tag):
    sagemakerClient = boto3.client('sagemaker')
    trainingJob = event['detail']['requestParameters']['trainingJobName']
    trainingJob_arn = 'arn:aws:sagemaker:' + os.environ['REGION'] + ':' + os.environ['ACCOUNTID'] + ':training-job/' + trainingJob
    response = sagemakerClient.add_tags(
        ResourceArn=trainingJob_arn,
        Tags=[
            {
                'Key':'adsk:moniker',
                'Value': moniker_tag
            },
            {
                'Key':'adsk:team',
                'Value': team_tag
            },
            {
                'Key':'owner',
                'Value': owner_tag
            }
        ]
    )
    print(response)

def tagSmModel(event, moniker_tag, team_tag, owner_tag):
    sagemakerClient = boto3.client('sagemaker')
    model = event['detail']['requestParameters']['modelName']
    model_arn = 'arn:aws:sagemaker:' + os.environ['REGION'] + ':' + os.environ['ACCOUNTID'] + ':model/' + model
    response = sagemakerClient.add_tags(
        ResourceArn=model_arn,
        Tags=[
            {
                'Key':'adsk:moniker',
                'Value': moniker_tag
            },
            {
                'Key':'adsk:team',
                'Value': team_tag
            },
            {
                'Key':'owner',
                'Value': owner_tag
            }
        ]
    )
    print(response)

def tagSmEndPoint(event, moniker_tag, team_tag, owner_tag):
    sagemakerClient = boto3.client('sagemaker')
    endpoint = event['detail']['requestParameters']['endpointName']
    endpoint_arn = 'arn:aws:sagemaker:' + os.environ['REGION'] + ':' + os.environ['ACCOUNTID'] + ':endpoint/' + endpoint
    response = sagemakerClient.add_tags(
        ResourceArn=endpoint_arn,
        Tags=[
            {
                'Key':'adsk:moniker',
                'Value': moniker_tag
            },
            {
                'Key':'adsk:team',
                'Value': team_tag
            },
            {
                'Key':'owner',
                'Value': owner_tag
            }
        ]
    )
    print(response)

def tagSmEndPointConfig(event, moniker_tag, team_tag, owner_tag):
    sagemakerClient = boto3.client('sagemaker')
    endpointConfig = event['detail']['requestParameters']['endpointConfigName']
    endpointConfig_arn = 'arn:aws:sagemaker:' + os.environ['REGION'] + ':' + os.environ['ACCOUNTID'] + ':endpoint-config/' + endpointConfig
    response = sagemakerClient.add_tags(
        ResourceArn=endpointConfig_arn,
        Tags=[
            {
                'Key':'adsk:moniker',
                'Value': moniker_tag
            },
            {
                'Key':'adsk:team',
                'Value': team_tag
            },
            {
                'Key':'owner',
                'Value': owner_tag
            }
        ]
    )
    print(response)

def tagSmHyperParameterTuningJob(event, moniker_tag, team_tag, owner_tag):
    sagemakerClient = boto3.client('sagemaker')
    hptJob= event['detail']['requestParameters']['hyperParameterTuningJobName']
    hptJob_arn = 'arn:aws:sagemaker:' + os.environ['REGION'] + ':' + os.environ['ACCOUNTID'] + ':hyper-parameter-tuning-job/' + hptJob
    response = sagemakerClient.add_tags(
        ResourceArn=hptJob_arn,
        Tags=[
            {
                'Key':'adsk:moniker',
                'Value': moniker_tag
            },
            {
                'Key':'adsk:team',
                'Value': team_tag
            },
            {
                'Key':'owner',
                'Value': owner_tag
            }
        ]
    )
    print(response)

def tagSmNotebookLifecycleConfig(event, moniker_tag, team_tag, owner_tag):
    sagemakerClient = boto3.client('sagemaker')
    nbilConfig = event['detail']['requestParameters']['notebookInstanceLifecycleConfigName']
    nbilConfig_arn = 'arn:aws:sagemaker:' + os.environ['REGION'] + ':' + os.environ['ACCOUNTID'] + ':notebook-instance-lifecycle-config/' + nbilConfig
    response = sagemakerClient.add_tags(
        ResourceArn=nbilConfig_arn,
        Tags=[
            {
                'Key':'adsk:moniker',
                'Value': moniker_tag
            },
            {
                'Key':'adsk:team',
                'Value': team_tag
            },
            {
                'Key':'owner',
                'Value': owner_tag
            }
        ]
    )
    print(response)

def tagSsmParameter(event, moniker_tag, team_tag, owner_tag):
    ssmClient = boto3.client('ssm')
    ssmParameter = event['detail']['requestParameters']['name']
    response = ssmClient.add_tags_to_resource(
        ResourceType='Parameter',
        ResourceId=ssmParameter,
        Tags=[
            {
                'Key':'adsk:moniker',
                'Value': moniker_tag
            },
            {
                'Key':'adsk:team',
                'Value': team_tag
            },
            {
                'Key':'owner',
                'Value': owner_tag
            }
        ]
    )
    print(response)

#Identifies the eventname from the CloudTrail and event and tags the resulting resource with the moniker, owner and team tags
def lambda_handler(event, context):
    print(event)

    #Passed from Cloudformation of the offramp template
    moniker_tag = os.environ['MONIKER']

    #Passed from Cloudformation of the offramp template
    team_tag = os.environ['TEAM']

    #Retrieved from Cloudwatch event. Will be in the form of the ADS admin account (Eg. anandradmin)
    owner_tag = event['detail']['userIdentity']['arn'].split('/')[-1]

    #For EC2 instances
    if event['detail']['eventName'] == 'RunInstances':
        tagEc2Instances (event, moniker_tag, team_tag, owner_tag)

    #For Glue jobs
    elif event['detail']['eventName'] == 'CreateJob':
        tagGlueJob(event, moniker_tag, team_tag, owner_tag)

    #For Glue crawlers
    elif event['detail']['eventName'] == 'CreateCrawler':
        tagGlueCrawler(event, moniker_tag, team_tag, owner_tag)

    #For Glue Triggers
    elif event['detail']['eventName'] == 'CreateTrigger':
        tagGlueTrigger(event, moniker_tag, team_tag, owner_tag)

    #For Lambda functions
    elif event['detail']['eventName'] == 'CreateFunction20150331':
        tagLambda(event, moniker_tag, team_tag, owner_tag)

    #For Sagemaker Notebooks
    elif event['detail']['eventName'] == 'CreateNotebookInstance':
        tagSmNotebook(event, moniker_tag, team_tag, owner_tag)

    #For Sagemaker Training jobs
    elif event['detail']['eventName'] == 'CreateTrainingJob':
        tagSmTrainingJob(event, moniker_tag, team_tag, owner_tag)
    #For Sagemaker models
    elif event['detail']['eventName'] == 'CreateModel':
        tagSmModel(event, moniker_tag, team_tag, owner_tag)

    #For Sagemaker Endpoints
    elif event['detail']['eventName'] == 'CreateEndpoint':
        tagSmEndPoint(event, moniker_tag, team_tag, owner_tag)

    #For Sagemaker endpoint configurations
    elif event['detail']['eventName'] == 'CreateEndpointConfig':
        tagSmEndPointConfig(event, moniker_tag, team_tag, owner_tag)

    #For Sagemaker Hyperparameter Tuning Jobs
    elif event['detail']['eventName'] == 'CreateHyperParameterTuningJob':
        tagSmHyperParameterTuningJob(event, moniker_tag, team_tag, owner_tag)

    #For Sagemaker Notebook Lifecycle configurations
    elif event['detail']['eventName'] == 'CreateNotebookInstanceLifecycleConfig':
        tagSmNotebookLifecycleConfig(event, moniker_tag, team_tag, owner_tag)

    #For SSM Parameters
    elif event['detail']['eventName'] == 'PutParameter':
        tagSsmParameter(event, moniker_tag, team_tag, owner_tag)


