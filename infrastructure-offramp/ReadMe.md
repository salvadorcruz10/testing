# ADP Offramp Service

The Offramp service is available for users who require AWS services not available in the core ADP stack and/or who require more control to configure AWS services to support their use case. For example, a data scientist may wish to utilize the Sagemaker service to create a new machine learning model, or they may require an EC2 instance configured with specific R and Python packages. Provisioning an offramp for these users will provide the capability to meet these types of requirements.

## AWS Services available in a standard offramp

```bash
IAM
APIGateway
Cloudformation
Cloudwatch
EC2
Glue
Lambda
S3
Sagemaker
SSM
ECR
```

## Stack creation process
[Stack creation process](https://wiki.autodesk.com/display/ADP/Stack+Creation+Process)

## Offramp usage tips
Once the offramp is provisioned, it will be available in your list of accounts when logging onto the AWS console at awsconsole.autodesk.com:

Note: Use your Admin account when logging on to the AWS Console. Also, if the offramp has been created but you do not see it available in your list of accounts, confirm that your Admin account is associated to the Active Directory security group which corresponds to the AWS role.

General guidelines when creating resources from the Offramp account:

-   When providing Names for the resources, include the “Offramp Tag Name” as the prefix. For instance, the Offramp tag name for the test offramp is daa-adp-tool-svc-offramp. So, EC2 instances created under the offramp should begin with daa-adp-tool-svc-offramp and likewise for Sagemaker resources, lambda functions, glue jobs, etc.
-   When it is possible to add tags while creating a resource, please add a Name tag which again will start with the Offramp tag name.
-   Other tags (adsk:moniker, adsk:team, and owner) will be added automatically to the offramp resources. For many resources, there are conditions in place to verify that the adsk:moniker and adsk:team tags are present in order to allow the resource to be updated or deleted. This is to prevent a user logged into an offramp account from accidentally modifying a resource created under a different account.
-   Please see the below table for the restrictions and conditions that are enforced via the CF template.

|Resource Category|Resource                       |Action                               |Restrictions / Conditions                                                                                             |
|-----------------|-------------------------------|-------------------------------------|----------------------------------------------------------------------------------------------------------------------|
|CloudFormation   |Stack                          |Delete*                              |Resource Name (not the Name tag) begins with OfframpTagName                                                           |
|                 |Stackset                       |Update*                              |                                                                                                                      |
|EC2              |All                            |Describe*                            |region=us-east-1                                                                                                      |
|                 |                               |GetConsole*                          |                                                                                                                      |
|EC2              |Instance                       |RunInstances                         |Name tag begins with OfframpTagName                                                                                   |
|                 |Volume                         |CreateVolume                         |                                                                                                                      |
|EC2              |Instance                       |CreateTags                           |Allow adding tags only when creating the instance or volume                                                           |
|                 |Volume                         |                                     |                                                                                                                      |
|EC2              |Instance                       |TerminateInstances                   |adsk:moniker and adsk:team tags exist with correct values                                                             |
|                 |                               |StartInstances                       |                                                                                                                      |
|                 |                               |StopInstances                        |                                                                                                                      |
|EC2              |All                            |autoscaling:Attach*                  |Name tag begins with OfframpTagName (note: this condition does not apply to autoscaling:Create*)                      |
|                 |                               |autoscaling:Exit*                    |                                                                                                                      |
|                 |                               |autoscaling:Put*                     |                                                                                                                      |
|                 |                               |autoscaling:Detach*                  |                                                                                                                      |
|                 |                               |autoscaling:CompleteLifecycleAction  |                                                                                                                      |
|                 |                               |autoscaling:Enable*                  |                                                                                                                      |
|                 |                               |autoscaling:Suspend*                 |                                                                                                                      |
|                 |                               |autoscaling:Delete*                  |                                                                                                                      |
|                 |                               |autoscaling:Disable*                 |                                                                                                                      |
|                 |                               |autoscaling:Resume*                  |                                                                                                                      |
|                 |                               |autoscaling:Update*                  |                                                                                                                      |
|                 |                               |autoscaling:Set*                     |                                                                                                                      |
|                 |                               |autoscaling:Terminate*               |                                                                                                                      |
|                 |                               |autoscaling:Enter*                   |                                                                                                                      |
|                 |                               |autoscaling:Record*                  |                                                                                                                      |
|EC2              |Instance                       |RunInstances                         |Key-pair in format  <OfframpTagName>-<Environment>;                                                                   |
|                 |                               |                                     |Security Group is default security group for Offramp (sg-7764f03d in PRD)                                             |
|EC2              |All                            |ec2:ResetImageAttribute              |region=us-east-1                                                                                                      |
|                 |                               |ec2:DeregisterImage                  |                                                                                                                      |
|                 |                               |ec2:ModifyNetworkInterfaceAttribute  |                                                                                                                      |
|                 |                               |ec2:RegisterImage                    |                                                                                                                      |
|                 |                               |ec2:DeleteNetworkInterface           |                                                                                                                      |
|                 |                               |ec2:CreateImage                      |                                                                                                                      |
|                 |                               |ec2:AssociateIamInstanceProfile      |                                                                                                                      |
|                 |                               |ec2:ModifyImageAttribute             |                                                                                                                      |
|                 |                               |ec2:CreateNetworkInterface           |                                                                                                                      |
|                 |                               |ec2:CreateLaunchTemplate             |                                                                                                                      |
|                 |                               |sts:DecodeAuthorizationMessage       |                                                                                                                      |
|                 |                               |ec2:DescribeImage*                   |                                                                                                                      |
|                 |                               |ec2:AttachNetworkInterface           |                                                                                                                      |
|                 |                               |ec2:*LaunchTemplate*                 |                                                                                                                      |
|                 |                               |ec2:ImportImage                      |                                                                                                                      |
|Glue             |All                            |DeleteCrawler                        |adsk:moniker and adsk:team tags exist with correct values                                                             |
|                 |                               |DeleteJob                            |                                                                                                                      |
|                 |                               |DeleteTrigger                        |                                                                                                                      |
|                 |                               |StartCrawler                         |                                                                                                                      |
|                 |                               |StartTrigger                         |                                                                                                                      |
|                 |                               |StopCrawler                          |                                                                                                                      |
|                 |                               |StopTrigger                          |                                                                                                                      |
|                 |                               |UpdateCrawler                        |                                                                                                                      |
|                 |                               |UpdateJob                            |                                                                                                                      |
|                 |                               |UpdateTrigger                        |                                                                                                                      |
|IAM              |Role                           |PassRole                             |All roles which begin with adp-<OfframpTagName>                                                                       |
|Lambda           |Function                       |CreateFunction                       |Resource Name (not the Name tag) begins with OfframpTagName                                                           |
|Lambda           |Function                       |DeleteFunction                       |Resource Name (not the Name tag) begins with OfframpTagName                                                           |
|                 |                               |InvokeFunction                       |                                                                                                                      |
|                 |                               |UpdateFunctionCode                   |                                                                                                                      |
|                 |                               |UpdateFunctionConfiguration          |                                                                                                                      |
|Sagemaker        |All                            |CreateEndpoint                       |Name tag begins with OfframpTagName                                                                                   |
|                 |                               |CreateEndpointConfig                 |                                                                                                                      |
|                 |                               |CreateHyperParameterTuningJob        |                                                                                                                      |
|                 |                               |CreateModel                          |                                                                                                                      |
|                 |                               |CreateNotebookInstance               |                                                                                                                      |
|                 |                               |CreateNotebookInstanceLifecycleConfig|                                                                                                                      |
|                 |                               |CreateTrainingJob                    |                                                                                                                      |
|                 |                               |CreateTransformJob                   |                                                                                                                      |
|Sagemaker        |NotebookInstance               |StartNotebookInstance                |Resource Name (not the Name tag) begins with OfframpTagName; adsk:moniker and adsk:team tags exist with correct values|
|                 |                               |CreatePresignedNotebookInstanceUrl   |                                                                                                                      |
|Sagemaker        |Endpoint                       |Delete*                              |Resource Name (not the Name tag) begins with OfframpTagName; adsk:moniker and adsk:team tags exist with correct values|
|                 |EndpointConfig                 |Invoke*                              |                                                                                                                      |
|                 |HyperParameterTuningJob        |Stop*                                |                                                                                                                      |
|                 |Model                          |Update*                              |                                                                                                                      |
|                 |NotebookInstance               |                                     |                                                                                                                      |
|                 |NotebookInstanceLifecycleConfig|                                     |                                                                                                                      |
|                 |TrainingJob                    |                                     |                                                                                                                      |
|Sagemaker        |TransformJob                   |Delete*                              |Resource Name (not the Name tag) begins with OfframpTagName                                                           |
|                 |                               |Invoke*                              |                                                                                                                      |
|                 |                               |Stop*                                |                                                                                                                      |
|                 |                               |Update*                              |                                                                                                                      |
|Sagemaker        |All                            |AddTags                              |adsk:moniker and adsk:team tags exist with correct values                                                             |
|SSM              |Parameter                      |PutParameter                         |Resource Name (not the Name tag) begins with OfframpTagName                                                           |
|SSM              |Parameter                      |GetParameterHistory                  |Resource Name (not the Name tag) begins with OfframpTagName; adsk:moniker and adsk:team tags exist with correct values|
|                 |                               |GetParametersByPath                  |                                                                                                                      |
|                 |                               |GetParameters                        |                                                                                                                      |
|                 |                               |GetParameter                         |                                                                                                                      |
|                 |                               |DeleteParameter                      |                                                                                                                      |
|                 |                               |DeleteParameters                     |                                                                                                                      |
|S3               |S3 bucket                      |Get*                                 |Green bucket                                                                                                          |
|                 |                               |List*                                |                                                                                                                      |
|                 |                               |Head*                                |                                                                                                                      |
|S3               |S3 bucket                      |s3:*                                 |Full access to the S3 bucket which includes the “bucket suffix” (based on team name) at the end of the bucket name    |

Further details in [Wiki](https://wiki.autodesk.com/display/ADP/Offramp+Usage+Tips)

If other services are required, please reach out to the ADP Tools & Services team: adp-tools-and-services@autodesk.com
