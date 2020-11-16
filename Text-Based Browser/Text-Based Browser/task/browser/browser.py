import os
import sys
import requests
from bs4 import BeautifulSoup
import re
from colorama import Fore
nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''


def browser():
    command = input()
    while command != 'exit':
        if command == "back":
            show_last()
        elif command == "exit":
            return False
        elif "." in command:
            content = read_content(command)
            if content:
                site_filename = command#.rsplit('.', 1)[0]#.replace('.', '_')
                save_site(site_filename, content)
                user_urls.append(command)
                print(content)
            else:
                print("Error: Incorrect URL")
        elif command in user_urls:
            read_file(command)
        else:
            print("Error: Incorrect URL")
        command = input()


def save_site(s, c):
    with open(filename(s), "w") as f:
        f.write(c)


def show_last():
    user_urls.pop()
    if user_urls:
        last = user_urls.pop()
        read_file(last)


def read_file(s):
    try:
        content_file = open(filename(s))
        print(content_file.read())
    except FileNotFoundError:
        print("Error open file", s)


def read_content(s):
    try:
        if not s.startswith("http"):
            command = "http://" + s
        r = requests.get(command, verify=False)
        soup = BeautifulSoup(r.content, 'html.parser')
        result = [x.text for x in soup.find_all(['p', 'a', 'ul', 'ol', 'li']) + soup.find_all(re.compile('^h[1-6]$'))]
        return Fore.BLUE + '/n'.join(result)
    except requests.exceptions.ConnectionError:
        return False


def filename(f):
    return os.path.join(dirName, f + ".txt")


user_urls = []
dirName = sys.argv[1]
if not os.path.exists(dirName):
    os.mkdir(dirName)
browser()
