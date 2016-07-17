import logging
from constants import REMINDER
from slackclient import SlackClient

log = logging.getLogger(__name__)

class MySlack(object):
    def __init__(self, token):
        self.slack_client = SlackClient(token)

    def user_list(self):
        my_user_list = []
        user_list = self.slack_client.api_call('users.list')
        if not user_list['ok']:
            log.error('Could not find list of users: {}'.format(user_list.get('error')))
            return []
        log.debug('User list: {}'.format(user_list))
        for user in user_list['members']:
            user_id = user['id']
            if user.get('is_bot') or user_id == 'USLACKBOT':
                continue
            my_user_list.append(user_id)
        return my_user_list

    def send_reminder(self, user_id):
        dm = self.slack_client.api_call('im.open', user=user_id)['channel']['id']
        self.slack_client.api_call('chat.postMessage', as_user='true:', channel=dm, text=REMINDER)
