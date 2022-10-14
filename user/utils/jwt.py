import jwt


def encode(payload):
    return jwt.encode(payload, 'screct', algorithm='HS256')


def decode(payload):
    return jwt.decode(payload, 'screct', algorithm='HS256')

