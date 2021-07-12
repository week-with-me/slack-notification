from datetime  import datetime

from config    import MEMBER


class GitHub:
    def __init__(self, body):
        self.body = body

    def get_repository_name(self):
        repository   = self.body['repository']['name']

        return repository

    def parsing_pull_request(self):
        pull_request = self.body['pull_request']
        merged       = pull_request['merged']
        repository   = self.get_repository_name()        
        title        = pull_request['title']
        url          = pull_request['html_url']
        user_id      = pull_request['user']['login']
        user_name    = MEMBER[repository][user_id]
        now          = datetime.now()
        today        = now.strftime('%Y-%m-%d')
        
        data = {
            'user': user_name,
            'title': title,
            'date': today,
            'URL': url
        }

        return merged, data

    