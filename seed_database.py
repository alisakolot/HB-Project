"""Script to seed database."""

import os

from random import choice, randint
from datetime import datetime

import crud
import model
import server

import sample_users

# os.system('dropdb alisadb')
# os.system('createdb alisadb')

model.connect_to_db(server.app)
model.db.create_all()


# Create videos/images, store them in list so we can use them
# to create fake reactions
videos_in_db = []
# for video in sample_data:
for video in sample_users.v:
    video_path, description, date_posted = (video.video_path,
                                    video.description, video.date_posted)

    db_video = crud.create_video(video_path, description, date_posted)

    videos_in_db.append(db_video)

users_list = []


images_in_db = []
# for image in sample_data:
for image in sample_users.i:
    image_path, description, date_posted = (image.image_path,
                                    image.description, image.date_posted)

    db_image = crud.create_image(image_path, description, date_posted)

    images_in_db.append(db_image)

users_list = []






# Create 5 users; each user will make 5 reacts
for n in range(5):

    email = f'user{n}@test.com'  #unique email
    password = 'test'

    user = crud.create_user('first_name', 'last_name', 'username', email, password)
    users_list.append(user)


'''Assigning a reaction number to a video.'''
for _ in range(5):
    random_video = choice(videos_in_db)
    reaction = randint(1, 5) #similar to rating format, each reaction number will represent img/like

    random_user = choice(users_list)

    crud.create_reaction(random_user, reaction, video=random_video)


'''Assigning a reaction number to an image.'''
for _ in range(5):
    random_image = choice(images_in_db)
    reaction = randint(1, 5) #similar to rating format, each reaction number will represent img/like

    random_user = choice(users_list)

    crud.create_reaction(random_user, reaction, image=random_image)

"""Creating 'following' relationship"""
# Create following relationship: 
    #1. Choose user and create relationships between users 
    #2. User with email/user_id will be randomly assigned to another user
        #use randint, see assigning a reaction number to a video
    #3. Commit to db in crud.py

for user in users_list: 
    subscriber = choice(users_list)
    creator = choice(users_list)

    if subscriber != creator:

        crud.create_following(subscriber, creator)

    else:
        continue
        
    
    
    