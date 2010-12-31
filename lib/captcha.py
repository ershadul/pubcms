import random
import sha

from django.conf import settings

def generate_captcha():
    operand1 = random.choice( [10,11,12,13,14,15,17,18,19,20])
    operand2 = random.choice( [1,2,3,4,5,6,7,8] )
    operator = random.choice([1,2])
    
    if operator == 1:
        result = operand1 + operand2
        text = '%s + %s = ' % (operand1, operand2)
    else:
        result = operand1 - operand2
        text = '%s - %s = ' % (operand1, operand2)
    
    SALT = settings.SECRET_KEY[:20]
    # create hash
    texthash = sha.new(SALT + str(result)).hexdigest()
    return (text, texthash)

def check_captcha(imgtext, imghash):
    try:
        SALT = settings.SECRET_KEY[:20]
        if imghash == sha.new(SALT + imgtext).hexdigest():
            return True
    except:
        pass
    return False
