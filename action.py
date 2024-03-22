"""
A simple AI Action that returns the current engineer on call
"""

from robocorp.actions import action, Request
import requests
import json


@action
def who_is_on_call_today(request: Request) -> str:
    """
    Prints the current engineer on call
    """
    action_context = json.loads(request.headers.get("X-Action-Context"))

    alert_opsOpsGroupId = action_context["ALERTOPS_GROUP_ID"]
    api_key = action_context["ALERTOPS_API_KEY"]

    api_url = f"https://app.alertops.com/api/v2/schedules/oncallnow?group_id={alert_opsOpsGroupId}"

    headers = {"api-key": api_key}

    response = requests.get(api_url, headers=headers)
    engineer_on_call = response.json()[0]["members"][0]
    engineer_name = engineer_on_call["name"]
    engineer_email = engineer_on_call["official_email"]

    return f"{engineer_name} ({engineer_email})"
