from .models import User
import hashlib
import jwt

from .models import User

def verifyNurseryLogin(data):
    
    error = {}

    try:
        User.objects.get(username=data['username'])
    except User.DoesNotExist:
        error['usernameError'] = 'user not found'
        return error

    if len(error.keys()) == 0:
        user = User.objects.get(username=data['username'])
        requestPassword = hashlib.sha256(data['password'].encode())
        result = requestPassword.hexdigest()
    
    if user.password != result:
        error['passwordError'] = 'wrong password'
        return error

    if user.is_nursery_user is False:
        error['authenticationError'] = 'not valid login'
        return error
    
    return error

def verifyNormalLogin(data):
    
    error = {}

    try:
        User.objects.get(username=data['username'])
    except User.DoesNotExist:
        error['usernameError'] = 'user not found'
        return error

    if len(error.keys()) == 0:
        user = User.objects.get(username=data['username'])
        requestPassword = hashlib.sha256(data['password'].encode())
        result = requestPassword.hexdigest()
    
    if user.password != result:
        error['passwordError'] = 'wrong password'
        return error

    if user.is_normal_user is False:
        error['authenticationError'] = 'not valid login'
        return error
    
    return error

def jwtAuth(authHeader):
    encoded_jwt = authHeader['authorization']
    token = encoded_jwt.split('Bearer ')[1]
    decoded_jwt = jwt.decode(token, 'secret', algorithms=['HS256'])
    user = User.objects.get(username=decoded_jwt['username'])
    return user