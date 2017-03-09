# -*- coding: utf-8 -*-
from itertools import chain
from bs4 import BeautifulSoup as bsoup
from platforms.abstract_platform import AbstractPlatform


class Xenforo(AbstractPlatform):

    def __init__(self, base_url):
        super(Xenforo, self).__init__('Xenforo', base_url)

    def login(self, user: str, password: str) -> bool:
        login_url = '{}/login/login'.format(self.base_url)

        params = {'login': user, 'password': password, 'remember': 1, 'register': 0}
        response = self.session.post(login_url, params=params)

        if response.status_code == 200:
            bs = bsoup(response.content, 'html.parser')
            self.xtoken = bs.find('input', attrs={'name': '_xfToken', 'type': 'hidden'}).get('value')

            if not self.xtoken:
                raise Exception('Fail to get/find the "xtoken" value.')

        return True

    def get_token(self) -> str:
        """
        Get the value from Xenforo "xtoken".
        @returns the xtoken value.
        """
        return self.xtoken

    def start_conversation(self, title: str, message: str, users: list) -> bool:
        """
        Initialize a new private message.

        @param title: the conversation title.
        @param message: the conversation contents.
        @param users: a list of users to submit the message.

        @returns true if the conversation is sucessfully started.
        """
        url = '{}/conversations/insert'.format(self.base_url)
        users = ','.join(users)

        params = self.include_params({'recipients': users, 'title': title, 'message_html': message})
        response = self.session.post(url, params=params).json()

        return 'error' not in response and response['_redirectStatus'] == 'ok'

    def post_thread(self, forum_id: int, title: str, contents: str) -> bool:
        """
        Post a new message to the correspondent forum.

        @param forum_id: the forum id.
        @param title: the topic title.
        @param contents: the topic contents, the html message.

        @returns true if the message is sucessfully submitted.
        """
        url = '{}/forums/{}/add-thread'.format(self.base_url, forum_id)

        params = self.include_params({'title': title, 'message_html': contents})
        return 'error' not in self.session.post(url, params=params).json()

    def post_comment(self, post_id: int, message: str) -> bool:
        """
        Post comment in a specific thread.

        @param post_id: the post/thread id.
        @param message: the comment contents, the html message.
        
        @returns true if the comment is sucessfully submitted.
        """
        url = '{}/threads/{}/add-reply'.format(self.base_url, post_id)
        
        params = self.include_params({'message_html': message})
        return 'error' not in self.session.post(url, params=params).json()

    def like_post(self, post_id: int):
        url = '{}/posts/{}/like'.format(self.base_url, post_id)

        params = self.include_params({})
        return 'error' not in self.session.post(url, params=params).json()

    def like_profile_post(self, post_id: int):
        url = '{}/profile-posts/comments/{}/like'.format(self.base_url, post_id)

        params = self.include_params({})
        return 'error' not in self.session.post(url, params=params).json()
    
    def post_profile(self, profile_id: int, message: str ) -> bool:
        url = '{}/members/{}/post'.format(self.base_url, profile_id)
        
        params = self.include_params({'message':message})
        return 'error' not in self.session.post(url, params=params).json()
    
    def report_post(self, post_id: int, message: str ) -> bool:
        url = '{}/posts/{}/report'.format(self.base_url, post_id)
        
        params = self.include_params({'message':message})
        return 'error' not in self.session.post(url, params=params).json()

    # def get_recente_activity_from_member(self, member_id):
    #
    #     url = '{}/members/{}/recent-content'.format(self.base_url, member_id)
    #
    #     params = self.include_params({})
    #     response = self.session.post(url, params=params).json()
    #
    #     print(response)
    #
    #     return 'error' not in response

    def include_params(self, params:dict) -> dict:
        required = {'_xfToken': self.xtoken, '_xfResponseType': 'json'}
        return dict(chain(required.items(), params.items()))
