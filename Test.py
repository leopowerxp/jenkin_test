def lambdaHandler(event, context):
    return {
        "statusCode": 200,
        'headers': {'Content-Type': 'application/json'},
        'body': "event data type: {}, \n event content: {}".format(type(event), str(event))
    }