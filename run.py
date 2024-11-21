import devices


def startup():
    a = input('Do you want to load the demo config? (Y/n) > ')
    if a.lower() == 'Y':
        demo()
    else:
        start()

def demo():
    pass

def start():
    pass