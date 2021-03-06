# import the json utility package since we will be working with a JSON object
import json
# import the AWS SDK (for Python the package name is boto3)
import boto3
# import two packages to help us with dates and date formatting
from time import gmtime, strftime

# create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb',region_name='ap-south-1')
# use the DynamoDB object to select our table
table = dynamodb.Table('komlalebuTable')
# store the current time in a human readable format in a variable
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

# define the handler function that the Lambda service will use as an entry point
def lambda_handler(event, context):
# extract values from the event object we got from the Lambda service and store in a variable
       try:
            event = json.loads(event['body'])
            visitor = event['visitorCount'] +' '+ event['visitorResponse']
# write 'visitor' and time to the DynamoDB table using the object we instantiated and save response in a variable
            response = table.put_item(
                            Item={
                                'id': visitor,
                                'LatestGreetingTime':now
                                 })
       except:
             visitor = 'request error'

# return a properly formatted JSON object
       return {
        'statusCode': 200,
        

    }





