# -*- coding: utf-8 -*-
import requests


class AbstractPlatform:

    def __init__(self, identifier: str, base_url: str):
        self.identifier = identifier
        self.base_url = base_url
        self.session = requests.session()

    def login(self, user: str, password: str) -> bool:
        pass

    def logout(self):
        self.session.close()

    def list_active_users(self) -> dict:
        pass
