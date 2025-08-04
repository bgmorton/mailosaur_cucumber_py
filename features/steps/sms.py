import os
from dotenv import load_dotenv
from behave import *
from mailosaur import MailosaurClient
from mailosaur.models import SearchCriteria

load_dotenv()  # take environment variables

@given('the Mailosaur API key and server ID are set for SMS test')
def step_impl(context):
    global apiKey
    global serverId
    global mailosaurClient
    apiKey = os.getenv('MAILOSAUR_API_KEY')
    serverId = os.getenv('MAILOSAUR_SERVER_ID')
    assert apiKey, 'MAILOSAUR_API_KEY environment variable must be set'
    assert serverId, 'MAILOSAUR_SERVER_ID environment variable must be set'
    mailosaurClient = MailosaurClient(apiKey)

@when('I search for an SMS sent to "{toNumber}"')
def step_impl(context, toNumber):
    global message
    criteria = SearchCriteria()
    criteria.sent_to = toNumber
    message = mailosaurClient.messages.get(serverId, criteria)
    assert message, 'Message not found'
 
@then('that SMS should be sent from "{fromNumber}"')
def step_impl(context, fromNumber):
    assert message.sender[0].phone == fromNumber, 'Sender phone number does not match'