# Ex_77_Objects_First_Class.py

''' Your First Class - Social Media Comments

It's time to define your own class! Suppose we're creating a social network
application where users can comment on posts and photos.

Create a class called "Comment". Each comment should have the followign 
attributes:
- username - the username of the person who created the comment
(like "bluethecat")
- text - the actual itself (like "omg so cute!" or "hahaha)
- likes - the number of likes the comment has. Likes sould default the 0.

Define the Comment class below:

c = Comment("davey123", "lol you're so silly", 3)
c.username
c.text
c.likes

another_comment = Comment("rosa77", "soooo cute!!!")
another_comment.username
another_comment.text
another_comment_likes
'''

#Social Media Comment Class Solution:
#Here's my class definition for the Comment class.  Notice the default value for 
# likes in the __init__() definition.

class Comment():
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes

another_comment = Comment("rosa77", "soooo cute!!!")
print(another_comment.username) # rosa77
print(another_comment.text) # soooo cute!!!
print(another_comment.likes) # 0