# /usr/bin/python2.7
# written by Tomas (www.lisenet.com) on 05/11/2012
# copyleft free software
'''
$ /usr/bin/python aws.py start
Starting the instance...

$ /usr/bin/python aws.py stop
Stopping the instance...
'''

import boto.ec2
import sys

# specify AWS keys
auth = {"aws_access_key_id": "xxx", "aws_secret_access_key": "xxxx"}

def main():
    # read arguments from the command line and 
    # check whether at least two elements were entered
    if len(sys.argv) < 2:
        print("Usage: python aws.py")
        sys.exit(0)
    else:
	    action = sys.argv[1] 
    if action == "start":
	    startInstance()
    elif action == "stop":
    	stopInstance()
    else:
    	print("Usage: python aws.py")

def startInstance():
    print("Starting the instance...")
    # change "eu-west-1" region if different
    try:
        ec2 = boto.ec2.connect_to_region("eu-central-1", **auth)
    except Exception as e1:
        error1 = "Error1: %s" % str(e1)
        print(error1)
        sys.exit(0)
    # change instance ID appropriately  
    try:
         ec2.start_instances(instance_ids="xxx")
    except Exception as e2:
        error2 = "Error2: %s" % str(e2)
        print(error2)
        sys.exit(0)
    print(".......................")
    print("Started the instance...")
        

def stopInstance():
    print("Stopping the instance...")
    try:
        ec2 = boto.ec2.connect_to_region("eu-central-1", **auth)

    except Exception as e1:
        error1 = "Error1: %s" % str(e1)
        print(error1)
        sys.exit(0)

    try:
         ec2.stop_instances(instance_ids="xxx")

    except Exception as e2:
        error2 = "Error2: %s" % str(e2)
        print(error2)
        sys.exit(0)
    print(".......................")
    print("Stopped the instance...")
    

if __name__ == '__main__':
    stopInstance()
