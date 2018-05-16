# import boto3
#
# sns = boto3.client('sns', region_name='ap-northeast-1')
# snsTopic = 'arn:aws:sns:ap-northeast-1:334109173481:JenkinTest-dev-JenkinTest'
# message = 'TestMessage'
# response = sns.publish(TopicArn=snsTopic,
#                        Message=message,
#                        MessageStructure="string"
#                        )
#
# print(response)
#
def lambdaHandler(event, context):
    return {
        "statusCode": 200,
        'headers': {'Content-Type': 'application/json'},
        #'body': "event data type: {}, event content: {}".format(type(event), str(event))
        'body': 'test2'
        'body': 'test3'
    }



