import hashlib
import os
import time
import requests


def _get_cache_filename(url):
    return hashlib.md5(url.encode()).hexdigest()


class Cache:
    def __init__(self, cache_dir, expire_time):
        self.cache_dir = cache_dir
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)
        self.expire_time = expire_time

    def get(self, url):
        cache_file = os.path.join(self.cache_dir, _get_cache_filename(url))
        if os.path.exists(cache_file):
            with open(cache_file, 'r') as f:
                cache_data = f.read()
            cache_time = os.path.getmtime(cache_file)
            if time.time() - cache_time < self.expire_time:
                return cache_data
        return None

    def set(self, url, data):
        cache_file = os.path.join(self.cache_dir, _get_cache_filename(url))
        with open(cache_file, 'w') as f:
            f.write(data)


cache_dir = "./cache"
expire_time = 36000  # 1 hour
cache = Cache(cache_dir, expire_time)


def make_request(url):
    cached_data = cache.get(url)
    if cached_data is not None:
        return cached_data
    response = requests.get(url)
    cache.set(url, response.text)
    return response.text
