Feature: SMS testing with Mailosaur

@smstest
Scenario: Test basic SMS usage
    Given the Mailosaur API key and server ID are set for SMS test
    When I search for an SMS sent to "0192456789"
    Then that SMS should be sent from "0192456789"
