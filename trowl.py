#!/usr/bin/python

import twitter
import Growl
from time import sleep



def getLatestUpdate(timeline, user):
    for t in timeline:
        if (t.GetUser().screen_name != user):
            return t

def growlLatestUpdate(status, growl):
    growl.notify("update", status.GetUser().GetName(), status.GetText())

def compareStatus(a, b):
    if a is None:
        return False
    return a.GetId() == b.GetId()


def main():
    user = "username"
    password = "password"
    check_term = 1 #minutes
    curr = None
    
    #set up twitter
    api = twitter.Api(user, password)

    #set up growl
    g = Growl.GrowlNotifier("Trowl", ["update"])
    g.register()
    
    while 1:
        try:
            prev = curr
            curr = getLatestUpdate(api.GetFriendsTimeline(), user)
            if not compareStatus(prev, curr):
                growlLatestUpdate(curr, g)
            sleep(check_term * 60)
        except KeyboardInterrupt:
            print "\nTerminating..."
            break

    print "Good bye."


if __name__ == "__main__":
    main()


