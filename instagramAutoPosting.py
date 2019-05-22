import os
import time
import random

from random import randint
from os import listdir
from os.path import isfile, join
from InstagramAPI import InstagramAPI

PhotoPath='/Users/incheolha/Desktop/images'
InstaGramUser='tonyha1650'
InstaGramPass='Tony4023933$'

hashTags = '#tonyha #test #sample #sporter'


retrieve = os.getcwd()
print(retrieve)

os.chdir(PhotoPath)

changeDir = os.getcwd()
print(changeDir)

ListFiles=sorted([ f for f in listdir(PhotoPath) if isfile(join(PhotoPath, f))])

print(ListFiles)
print('Total photo in this folder'+str(len(ListFiles)))

instaAPI = InstagramAPI(InstaGramUser, InstaGramPass)
instaAPI.login()

for i, ele in enumerate(ListFiles) : 
    photo=ListFiles[i]
    print('Processing..')
    print('Now uploading......')
    instaAPI.uploadPhoto(photo, caption=hashTags, upload_id=None)
    os.remove(photo)
    n=randint(60,120)
    print('upload for ' + str(n))
    time.sleep(n)

