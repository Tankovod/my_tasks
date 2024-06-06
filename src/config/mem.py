from redis import Redis


redis = Redis(
    host="redis",
    port=6379,
    db=5,
    charset="utf-8",
    decode_responses=True
)
