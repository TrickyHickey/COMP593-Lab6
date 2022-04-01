from http import client
import re
import requests
from sys import argv

def main():

    user_info = argv[1]
    user_info = get_user_info(10)
    if user_info: 
        pastebin_strings = get_pastebin_strings(user_info)
        pastebin_url = post_to_pastebin(pastebin_strings[0], pastebin_strings[1])

        print(pastebin_url)
        
def post_to_pastebin(title, body_text):

    print("Posting to Paste...", end='')

    pastebin_params = {
        'api_dev_key': "f4R0OTFza_qTQ1NZJYLjoCeLqoHQux4X",
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_paste_name': title
    }

    response = requests.post('https://pastebin.com/api/api_post.php', data=pastebin_params)

    if response.status_code == 200:
        print('success')
        return response.text
    else:
        print('Uh Oh, got',response.status_code)
        return response.status_code


def get_pastebin_strings(user_dict):

    title = user_dict['name'] + "'s Geographical Location"
    body_text = "Latitude:" + user_dict['address']['geo']['lat'] + "\n"
    body_text += "Longitude: " + user_dict['address']['geo']['lng']
    return (title, body_text)

def get_user_info(user_num):
    print("Getting user information...", end='')
    response = requests.get('https://jsonplaceholder.typicode.com/users/' + str(user_num))

    if response.status_code == 200:
        print('success')
        return response.json()
    else:
        print('Uh Oh, got',response.status_code)
        return

main()