import redis
import os
import json


class Cache:
    REDIS_HOST = os.environ.get("REDIS_HOST")
    REDIS_PORT = os.environ.get("REDIS_PORT")
    REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")

    redis_client = redis.Redis(
        host=REDIS_HOST, port=REDIS_PORT, db=0, password=REDIS_PASSWORD
    )

    def query(self, key, reset_expiration=False, expiration_extension=0):
        data = self.redis_client.get(key)
        if data is not None:
            print(f"Successfully retrieved {key} from cache")
            if reset_expiration:
                print(f"Extended '{key}' expiration")
                self.redis_client.expire(key, expiration_extension)
            return 200, json.loads(data)
        else:
            print(f"Did not find {key} in cache")
            return 404, None

    def add(self, key, data, expiration=30):
        cached = self.redis_client.set(key, json.dumps(data), ex=expiration)
        if cached:
            print(f"Successfully added {key} to cache")
        else:
            print(f"Unable to store {key} in cache")
        return cached
