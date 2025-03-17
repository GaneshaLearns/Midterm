import json
from nlp import classificationPipeline  # Import your pipeline

def lambda_handler(event, context):
    try:
        # Parse the input from the API Gateway event
        body = json.loads(event['body'])
        text_data = body['text']
        
        # Make prediction using your pipeline
        prediction = classificationPipeline.predict([text_data])
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'prediction': int(prediction[0])
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
