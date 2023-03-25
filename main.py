import requests
from getkey import getkey

class Session():
    name: str
    session: requests.Session

    def __init__(self,name):
        self.name = name
        self.session = requests.Session()


sessions = []

session = Session("Session 1")
print("Session \"Session 1\" has been initialized.")

sessions.append(session)

def init_session(name: str | None = None):
    session = Session(name)
    sessions.append(session)
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

def menu():
    print(
        """
        1) Initialize new sesison
        2) Send Web Request
        3) Quit
        q) Quit program

        Please press a valid key to proceed: """, end = ""
    )

    selection = getkey()
    print(selection)


print("Simply Sessionized Started.")