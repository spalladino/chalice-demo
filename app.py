import json
import boto3

from botocore.exceptions import ClientError
from chalice import Chalice, NotFoundError

app = Chalice(app_name='helloworld')

S3 = boto3.client('s3', region_name='us-east-1')
BUCKET = 'my-bucket'
FOLDER = 'tests/chalice-demo'

@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/contact/{who}', methods=['POST'])
def contact(who):
    request = app.current_request
    key = "%s/%s" % (FOLDER, who)
    S3.put_object(Bucket=BUCKET, Key=key, Body=json.dumps(request.json_body))
    return { 'ok': True }
    
