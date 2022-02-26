from urllib import response
import requests
import hashlib # built-in module for SHA1 hashing. 

def request_api_data(query_char):  # sends a request to the API with the hashed password and retruns back matches
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'Error Fetching : {response.status_code}, check API data')
    return response

def pwned_api_check(password):     #checks our actual password with the API response. 
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    password_api_check = request_api_data(first5_char)
    print(first5_char, tail)
    return read_response(password_api_check)

def read_response(password_api_check):
    print(password_api_check.text)

pwned_api_check('Armystrong12!')
