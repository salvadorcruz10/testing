
#!/usr/bin/env bash
export Environment=${Environment:-dev}
export Team="${Team:-autodesk}"

#Receives core ADP template parameters
Team = $1
= $2
 = $3




#Launch the ADP Core template
aws cloud formation create-stack $stackname --parameters ParameterKey=Team,ParameterValue=$team ParameterKey=Team,ParameterValue=$team ParameterKey=OfframpBucket,ParameterValue=$OfframpBucket ParameterKey=Team,ParameterValue=$team

#Verify if the directory exist

if [ -d offramp-extensions/extension1/ ];
then
    echo "the stack exists"
    #Lanza el template del offramp extension
    #aws cloudformation create-stack --stack-name $extensionTagName --template-body file:/Users/mayela.gomez/Projects/autodesk/daa-adp-tools-services/infrastructure-offramp/cloudformation/offramp-template.yaml --parameters ParameterKey=Parm1,ParameterValue=test1 ParameterKey=Parm2,ParameterValue=test2

else
    echo "does not exist"

fi


Deploy-stuff --extensions extension1,extension2
IFS=","



