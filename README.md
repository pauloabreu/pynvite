## Basic
Import the xenforo module and initialize the object with the forum base url:

```python
from platforms.xf.xenforo import Xenforo

xenforo = Xenforo('http://myawesomeforum.com')
```
Now you can use `xenforo` variable to:

### Login
```python
if xenforo.login('user', 'pass'):
  print('Authenticated! :D')
```
### Private Message (conversations)
> Start a new conversation with a group of users:

```python
if xenforo.login('user', 'pass'):
  xenforo.start_conversation('title', 'conversation contents', ['user1', 'user2', 'user3])
```
### Posting
>  Post a new thread:

```python
if xenforo.login('user', 'pass'):
  xenforo.post_thread(312, 'the thread title', 'the thread contents! :D'):
```
> Post on specific thread:

```python
if xenforo.login('user', 'pass'):
  xenforo.post_comment(432, 'My awesome comment!')
```

### Likes
> Like a forum thread or post:

```python
if xenforo.login('user', 'pass'):
  xenforo.like_post(432)
```

> Like a profile post:

```python
if xenforo.login('user', 'pass'):
  xenforo.like_profile_post(12)
```

> Like a comment on a specific profile post:

```python
if xenforo.login('user', 'pass'):
  xenforo.like_profile_post_comment(111)
```

