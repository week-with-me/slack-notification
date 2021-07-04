import json

from worker.slack import Slack
from config       import TOKEN


def lambda_handler(event, context):
    body  = json.loads(event['body'])
    slack = Slack(TOKEN, body)
    slack.send_message()