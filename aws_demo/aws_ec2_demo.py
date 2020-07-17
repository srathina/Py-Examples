import boto3

Instances = ['i-0003792f1759aef5b', 'i-099040673568c3b96']

ec2 = boto3.client('ec2')

def start_instance():
    response = ec2.start_instances(
        InstanceIds=[
            Instances[0],
            Instances[1],
        ],
    )
    print(response)
    return(response)


def stop_instance():
    response = ec2.stop_instances(
        InstanceIds=[
            Instances[0],
            Instances[1],
        ],
    )
    print(response)
    return(response)


if __name__ == '__main__':
    start_instance()
    stop_instance()
    print(__name__)
else:
    print(__name__)





