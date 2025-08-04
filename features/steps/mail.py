import os
from dotenv import load_dotenv
from behave import *
from mailosaur import MailosaurClient
from mailosaur.models import SearchCriteria

load_dotenv()  # take environment variables

@given('the Mailosaur API key and server ID are set for email test')
def step_impl(context):
    global apiKey
    global serverId
    global mailosaurClient
    apiKey = os.getenv('MAILOSAUR_API_KEY')
    serverId = os.getenv('MAILOSAUR_SERVER_ID')
    assert apiKey, 'MAILOSAUR_API_KEY environment variable must be set'
    assert serverId, 'MAILOSAUR_SERVER_ID environment variable must be set'
    mailosaurClient = MailosaurClient(apiKey)

@when('I search for the "{subject}" email I sent earlier')
def step_impl(context, subject):
    global message
    criteria = SearchCriteria()
    criteria.subject = subject
    message = mailosaurClient.messages.get(serverId, criteria)
    assert message, 'Message not found'

@then('that email should be sent from "{name}" at "{email}"')
def step_impl(context, name, email):
    assert message.sender[0].name == name, 'Email sender name does not match'
    assert message.sender[0].email == email, 'Email sender email address does not match'
