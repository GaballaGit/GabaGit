import os
import hashlib

GIT_DIR = '.gabagit'

def init():
    os.makedirs(GIT_DIR)
    os.makedirs(f'{GIT_DIR}/objects')


def hash_object(data):
    old = hashlib.sha1(data).hexdigest()
    with open(f'{GIT_DIR}/objects{oid}', 'wb') as out:
        out.write(data)

    return oid
