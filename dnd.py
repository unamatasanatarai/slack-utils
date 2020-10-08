import time
from slack import http_client

def snooze(duration=30):
    """
    Pause notifications

    Parameters:
        duration (int): Minutes, how long to snooze for
    """
    data={
        "num_minutes": duration
    }
    return http_client.get('dnd.setSnooze', data)

def end():
    return http_client.post('dnd.endDnd', {})
