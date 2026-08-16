import string,secrets
from .models import URLMapping

def create_unique_token(model_class):
    token = generate_token()
    while model_class.objects.filter(short_token=token).exists():
        token=generate_token()
    return token
        


def generate_token():
    token = ""
    generator_str = string.ascii_letters + string.digits
    for i in range(0,6):
        token = token + secrets.choice(generator_str)
    return token

