# -*- coding: utf-8 -*-

import re


def parse_member_posting(post_links: list) -> list:

    posting_list = []

    for post_link in post_links:
        link = str(post_link['href'])

        result = re.search(r'\/(\d+)', link)
        if result:
            post_id = result.group(1)
        else:
            result = re.search(r'.(\d+)/', link)
            if result:
                post_id = result.group(1)

        if link.startswith('profile-post'):
            if 'comment' in link:
                posting_list.append({
                    'type': 'profile-comment',
                    'id': post_id
                })
            else:
                posting_list.append({
                    'type': 'profile-post',
                    'id': post_id
                })

        if link.startswith('thread'):
            posting_list.append({
                'type': 'thread',
                'id': post_id
            })

        if link.startswith('post'):
            posting_list.append({
                'type': 'post',
                'id': post_id
            })
       # print('item: {} id: {}'.format(link, post_id))
       # print('list content: {}'.format(posting_list))

    return posting_list
