from slack import MySlack


class AttitudeBot(object):
    def __init__(self, config):
        token = config.get('slack_integration', 'token')
        self.slack = MySlack(token)
        self.user_list = self.slack.user_list()

    def remind_users(self):
        for user_id in self.user_list:
            self.slack.send_reminder(user_id)
