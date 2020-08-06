#!/usr/bin/env python3

from argparse import ArgumentParser
import sys
import yaml
import ruamel.yaml
import os  

yaml = ruamel.yaml.YAML()
path1 = '/Users/mayela.gomez/Projects/autodesk/daa-adp-tools-services/infrastructure-offramp'

# ArgumentParser with application description
parser = ArgumentParser(description='%(prog)s is an ArgumentParser demo')

# Receive team parameter and save in Team variable
parser.add_argument('team', help='team which made the request')
args = parser.parse_args()
team = args.team
print ('Team:', team)

#Verify if the directory with the team name exists
path = path1+'/cloudformation/'+team
isdir = os.path.isdir(path)  
print(isdir)  

if isdir:
    print ('The directory exists')
    extPath = path

    #Load the yaml files
    with open(path1 + '/cloudformation/test-base-template.yaml') as fp:
        data = yaml.load(fp)
    with open(extPath + '/extension.yaml') as fp:
        data1 = yaml.load(fp)

    #Add the resources from extension.yaml to base-template.yaml resources
    for i in data1['Resources']:
        print (i,data1['Resources'][i])
        data['Resources'].update({i:data1['Resources'][i]})

    #Create a new file with the merged yaml
    f = open(path1 + '/cloudformation/tmp.yaml','w')
    yaml.dump(data, f)

    #Add the Mappings from extension.yaml to base-template.yaml resources
    for i in data1['Mappings']:
        print (i,data1['Mappings'][i])
        data['Mappings'].append({i:data1['Mappings'][i]})
         
        
    #Create a new file with the merged yaml
    f = open(path1 + '/cloudformation/tmp.yaml','w')
    yaml.dump(data, f)

    #Deploy the tmp.yaml template which include base + extension


    #Once the stack is launched, clean the tmp.yaml template
    #open('/Users/mayela.gomez/Projects/autodesk/daa-adp-tools-services/infrastructure-offramp/code/tmp.yaml', 'w').close()

else:
    print('The directory does not exists')






