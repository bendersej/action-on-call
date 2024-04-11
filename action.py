"""
A simple AI Action that returns the current engineer on call
"""

from robocorp.actions import action, Secret
import requests


@action
def who_is_on_call_today(alertops_group_id: Secret, alertops_api_key: Secret) -> str:
    """
    Prints the current engineer on call
    """
    api_url = f"https://app.alertops.com/api/v2/schedules/oncallnow?group_id={alertops_group_id.value}"

    headers = {"api-key": alertops_api_key.value}

    response = requests.get(api_url, headers=headers)
    engineer_on_call = response.json()[0]["members"][0]
    engineer_name = engineer_on_call["name"]
    engineer_email = engineer_on_call["official_email"]

    return f"{engineer_name} ({engineer_email})"
