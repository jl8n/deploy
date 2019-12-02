import os, base64


# Use cookies appropriately to associate the session ID with the user agent.
# Upon successful authentication, use the session store to persist the user’s authenticated state and identity.
# Do not add superfluous data to the session store.


class SessionStore:

  def __init__(self):
    # self.sessions is a dictionary (of dictionaries)
    self.sessions = {}

  # add a new session to the session store
  def createSession(self):
    newSessionId = self.generateSessionId()
    self.sessions[newSessionId] = {}
    return newSessionId

  # retrieve an existing session from the session store
  def getSession(self, sessionId):
    if sessionId in self.sessions:
      return self.sessions[sessionId]
    else:
      return None

  # create a new session ID
  def generateSessionId(self):
    rnum = os.urandom(32)
    rstr = base64.b64encode(rnum).decode("utf-8")
    return rstr

