import string
import secrets
import pasteboard

alphabet = string.ascii_letters + string.digits + string.punctuation
pass_length = 15
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(pass_length))
    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password) 
            and any(string.punctuation) for c in password):
        break
pasteboard.set_string(password)
