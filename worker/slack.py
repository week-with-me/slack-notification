import json

from slack_sdk        import WebClient
from slack_sdk.errors import SlackApiError

from worker.github    import GitHub


class Slack:
    def __init__(self, token, body):
        self.client = WebClient(token = token)
        self.github = GitHub(body)

    def get_channel_id(self):
        try:
            repository_name = self.github.get_repository_name()

            result = self.client.conversations_list(
                types = 'public_channel,private_channel'
            )
            channels = result['channels']

            for channel in channels:
                if channel['name'] == repository_name.lower():
                    return channel['id']
            
            print('Channle Not Found')

        except SlackApiError as slack_error:
            print(slack_error)

        except Exception as error:
            print(error)

    def send_message(self):
        try:
            channel_id = self.get_channel_id()
            data       = self.github.parsing_pull_request()
            user_name  = data['user']
            title      = data['title']
            date       = data['date']
            url        = data['URL']

            self.client.chat_postMessage(
                channel = channel_id,
                text    = '누군가 글을 썼어요! \n' + f'이름: {user_name} \n' + \
                    f'제목: {title} \n' + f'일자: {date} \n' + f'URL: {url}'
            )
        
        except SlackApiError as slack_error:
            print(slack_error)
        
        except Exception as error:
            print(error)