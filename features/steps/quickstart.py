import os
from dotenv import load_dotenv
from behave import *
from mailosaur import MailosaurClient

load_dotenv()  # take environment variables

@given('the Mailosaur API key is configured')
def step_impl(context):
    global apiKey
    apiKey = os.getenv('MAILOSAUR_API_KEY')
    assert apiKey, 'MAILOSAUR_API_KEY environment variable must be set'

@when('I connect to the Mailosaur API')
def step_impl(context):
    global mailosaurClient
    global emailServers
    mailosaurClient = MailosaurClient(apiKey)
    result = mailosaurClient.servers.list()
    emailServers = result.items

@then('I should see at least one inbox')
def step_impl(context):
    assert emailServers, 'Expected emailServers to be defined'
    assert len(emailServers) > 0, 'Expected at least one inbox/server'
