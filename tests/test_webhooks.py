from tests import client

def test_jira_webhook_issue_created():
    response = client.post(
        "/webhooks/",
        json={
            "webhookEvent": "jira:issue_created",
            "issue": {
                "id": "10001",
                "self": "https://your-jira-instance.atlassian.net/rest/api/3/issue/10001",
                "key": "JIRA-123",
                "fields": {
                    "summary": "Bug in login feature",
                    "description": "Users are unable to log in after the recent deployment.",
                    "issuetype": {
                        "id": "1",
                        "name": "Bug"
                    },
                    "project": {
                        "id": "20000",
                        "key": "PRJ",
                        "name": "Project Name"
                    },
                    "status": {
                        "id": "3",
                        "name": "To Do"
                    },
                    "priority": {
                        "id": "2",
                        "name": "High"
                    },
                    "reporter": {
                        "id": "5",
                        "displayName": "John Doe",
                        "emailAddress": "john.doe@example.com"
                    },
                    "assignee": {
                        "id": "6",
                        "displayName": "Jane Smith",
                        "emailAddress": "jane.smith@example.com"
                    },
                    "created": "2024-02-20T10:15:30.000+0000",
                    "updated": "2024-02-20T10:15:30.000+0000"
                }
            },
            "user": {
                "self": "https://your-jira-instance.atlassian.net/rest/api/3/user?accountId=abc123",
                "accountId": "abc123",
                "displayName": "John Doe",
                "emailAddress": "john.doe@example.com"
            }
        }
    )
    assert response.status_code in [200, 201, 202]
    assert response.json()["message"] == "Event received"

def test_jira_webhook_issue_updated():
    response = client.post(
        "/webhooks/",
        json={
            "webhookEvent": "jira:issue_updated",
            "issue": {
                "id": "10001",
                "self": "https://your-jira-instance.atlassian.net/rest/api/3/issue/10001",
                "key": "JIRA-123",
                "fields": {
                    "summary": "Bug in login feature",
                    "description": "Users are unable to log in after the recent deployment.",
                    "issuetype": {
                        "id": "1",
                        "name": "Bug"
                    },
                    "project": {
                        "id": "20000",
                        "key": "PRJ",
                        "name": "Project Name"
                    },
                    "status": {
                        "id": "4",
                        "name": "In Progress"
                    },
                    "priority": {
                        "id": "2",
                        "name": "High"
                    },
                    "reporter": {
                        "id": "5",
                        "displayName": "John Doe",
                        "emailAddress": "john.doe@example.com"
                    },
                    "assignee": {
                        "id": "6",
                        "displayName": "Jane Smith",
                        "emailAddress": "jane.smith@example.com"
                    },
                    "created": "2024-02-20T10:15:30.000+0000",
                    "updated": "2024-02-20T12:30:45.000+0000"
                }
            },
            "user": {
                "self": "https://your-jira-instance.atlassian.net/rest/api/3/user?accountId=abc123",
                "accountId": "abc123",
                "displayName": "John Doe",
                "emailAddress": "john.doe@example.com"
            }
        }
    )
    assert response.status_code in [200, 201, 202]
    assert response.json()["message"] == "Event received"

def test_jira_webhook_invalid_event():
    response = client.post(
        "/webhooks/",
        json={
            "webhookEvent": "jira:unknown_event",
            "issue": {
                "id": "10001",
                "self": "https://your-jira-instance.atlassian.net/rest/api/3/issue/10001",
                "key": "JIRA-123",
                "fields": {
                    "summary": "Bug in login feature",
                    "description": "Users are unable to log in after the recent deployment.",
                    "issuetype": {
                        "id": "1",
                        "name": "Bug"
                    },
                    "project": {
                        "id": "20000",
                        "key": "PRJ",
                        "name": "Project Name"
                    },
                    "status": {
                        "id": "3",
                        "name": "To Do"
                    },
                    "priority": {
                        "id": "2",
                        "name": "High"
                    },
                    "reporter": {
                        "id": "5",
                        "displayName": "John Doe",
                        "emailAddress": "john.doe@example.com"
                    },
                    "assignee": {
                        "id": "6",
                        "displayName": "Jane Smith",
                        "emailAddress": "jane.smith@example.com"
                    },
                    "created": "2024-02-20T10:15:30.000+0000",
                    "updated": "2024-02-20T10:15:30.000+0000"
                }
            },
            "user": {
                "self": "https://your-jira-instance.atlassian.net/rest/api/3/user?accountId=abc123",
                "accountId": "abc123",
                "displayName": "John Doe",
                "emailAddress": "john.doe@example.com"
            }
        }
    )
    assert response.status_code == 400  # Assuming you return 400 for invalid events
    assert response.json()["detail"] == "Event jira:unknown_event is not handled"
