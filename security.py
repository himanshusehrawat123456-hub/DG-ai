# DG AI Security System

import hashlib


def encrypt_password(password):

    encrypted = hashlib.sha256(
        password.encode()
    ).hexdigest()

    return encrypted



def check_password(password, saved_password):

    encrypted = encrypt_password(password)


    if encrypted == saved_password:

        return True

    else:

        return False



def security_status():

    print("DG AI Security System Active")
