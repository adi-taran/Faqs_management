import redis
import json
from django.conf import settings

class RedisHandler:
    def __init__(self):
        # Initialize the Redis client with settings from Django configuration
        self.redis_client = redis.StrictRedis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB,
            decode_responses=True
        )

    def set_cache_with_transaction(self, key, value):
        # Set a cache value in Redis using a transaction
        try:
            with self.redis_client.pipeline() as pipe:
                pipe.multi()  # Start the transaction
                pipe.set(key, json.dumps(value))  # Set the key-value pair
                pipe.execute()  # Execute the transaction
        except redis.RedisError as e:
            print(f"Redis transaction failed: {e}")

    def get_cache(self, key):
        # Retrieve a cache value from Redis
        try:
            cached_data = self.redis_client.get(key)
            if cached_data:
                return json.loads(cached_data)  # Return the value if found
            return None  # Return None if the key does not exist
        except redis.RedisError as e:
            print(f"Failed to get cache: {e}")
            return None

    def delete_cache(self, key):
        # Delete a cache value from Redis
        try:
            self.redis_client.delete(key)
        except redis.RedisError as e:
            print(f"Failed to delete cache: {e}")