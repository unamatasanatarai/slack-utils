# Slack utilities

import slack

slack.token = "xoxo..."

print(slack.user.set_status("In a meeting", ":spiral_calendar_pad:", 3600)["ok"])
print(dnd.snooze(60)['ok'])
