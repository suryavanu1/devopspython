from flask import Flask
import redis
import os

app = Flask(__name__)

# Get Redis config from environment variables
redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", 6379))

cache = redis.Redis(host=redis_host, port=redis_port)

def get_hit_count():
    count = cache.get('hits')
    if count is None:
        count = 0
    else:
        count = int(count)
    count += 1
    cache.set('hits', count)
    return count

@app.route('/')
def hello():
    count = get_hit_count()
    #return f'Hello from Docker with env variables! I have been seen {count} times.\n'
    return f'🚀 Hello from Docker CI/CD pipeline! You have visited {count} times.latest suryavanu 🚀\n'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
