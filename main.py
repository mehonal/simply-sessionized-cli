import requests
from getkey import getkey
import random

class Session():
    name: str
    session: requests.Session

    def __init__(self,name):
        self.name = name
        self.session = requests.Session()


sessions = []

def session_exists(name: str):
    "Removes the session provided by name"
    if sessions and sessions is not None:
        for session in sessions:
            if session.name == name:
                return True
    return False

def init_session(name: str | None = None):
    if name == None:
        name = random.randint(100_000, 999_999)
        while session_exists(name):
            name = random.randint(100_000, 999_999)
    session = Session(name)
    sessions.append(session)
    print("Successfully initialized session:")
    return session

def remove_session(name: str):
    "Removes the session provided by name"
    if sessions and sessions is not None:
        for session in sessions:
            if session.name == name:
                sessions.remove(session)
                return True
    return False

def get_session(name: str | None = None):
    "Returns the session provided by name"
    if sessions and sessions is not None:
        if name == None:
            return sessions[-1]
        for session in sessions:
            if session.name == name:
                return session
    return None

def list_sessions():
    "Returns the session provided by name"
    if sessions and sessions is not None:
        for session in sessions:
            print(session.name)
    else:
        print("You have no active sessions.")


def send_web_request(session: Session):
    print("Example input: https://somewebsite.com/")
    url = input("URL: ")
    print("Example input: GET")
    method = input("Method: ")
    print("Sending web request...")
    if method.lower() == 'get':
        resp = session.session.get(url)
    elif method.lower() == 'post':
        resp = session.session.get(url)
    print("Successfully got a response.")
    return resp

def response_menu(resp: requests.Response):
    while True:
        print(
            f"""
Currently working with: {resp.url}

1) View Response Text
2) View Response Headers
3) View Response Encoding
4) View Response Cookies
5) View Response Elapsed
6) View Response History
7) View Response JSON
8) View Response Status Code
9) Return to session
q) Quit program
Please press a valid key to proceed: """, end = ""
        )
        selection = getkey()
        print(selection)
        if selection == "q":
            print("Quitting Simply Sessionized.")
            exit()
        elif selection == "1":
            print(resp.text)
        elif selection == "2":
            print(resp.headers)
        elif selection == "3":
            print(resp.encoding)
        elif selection == "4":
            print(resp.cookies)
        elif selection == "5":
            print(resp.elapsed)
        elif selection == "6":
            print(resp.history)
        elif selection == "7":
            try:
                print(resp.json())
            except:
                print("Seems like no JSON was returned.")
        elif selection == "8":
            print(resp.status_code)
        elif selection == "9":
            return False

def session_menu(session_name: str):
    if not session_exists(session_name):
        print("No session named \"" + session_name + "\" exists.")
        return False
    else:
        session = get_session(session_name)
        while True:
            print(
                f"""
Currently logged onto "{session_name}"

1) Send Web Request
2) Log out of session
q) Quit program
Please press a valid key to proceed: """, end = ""
            )
            selection = getkey()
            print(selection)
            if selection == "q":
                print("Quitting Simply Sessionized.")
                exit()
            elif selection == "1":
                resp = send_web_request(session)
                response_menu(resp)
            elif selection == "2":
                return False

def main_menu():
    print(
        """
1) Initialize new sesison
2) Log onto session
l) List sessions
q) Quit program
Please press a valid key to proceed: """, end = ""
    )

    selection = getkey()
    print(selection)
    if selection == "q":
        print("Quitting Simply Sessionized.")
        exit()
    elif selection == "l":
        list_sessions()
    elif selection == "1":
        session_name = input('Enter new session name: ')
        init_session(session_name)
    elif selection == "2":
        session_name = input('Enter session name: ')
        session_menu(session_name)


print("Simply Sessionized Started.")

while True:
    main_menu()