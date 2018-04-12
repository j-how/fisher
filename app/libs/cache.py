from flask import request


def cache_key():
    #args = request.args
    key = request.path + '?' + request.url.rsplit('/', 1)[-1]
    return key