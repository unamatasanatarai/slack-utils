import time
from slack import http_client

def set_status(message, icon="", duration=3600):
    """
    Update your status.

    Parameters:
        message (str): Message to be displayed
        icon (str): Icon next to the status, for example: ":spiral_calendar_pad"
        duration (int): Seconds, 0=infinite, how long from now should the status be active
    """
    data={
        "profile": {
            "status_text": message,
            "status_emoji": icon,
            "status_expiration": int(time.time()) + duration
        }
    }
    return http_client.post('users.profile.set', data)

def clear_status():
    return set_status("", "", 0)
