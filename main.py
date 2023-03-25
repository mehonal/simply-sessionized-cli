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

def use_session(name: str | None = None):
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

def menu():
    print(
        """
1) Initialize new sesison
2) Send Web Request
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
        pass
        


print("Simply Sessionized Started.")

while True:
    menu()