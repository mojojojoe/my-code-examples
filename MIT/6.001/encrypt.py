def get_key(passwd):
    hsh = hash(passwd)
    return hsh % 541

def process_password(key):
    passwd = input("Please enter password")
    pass_key = get_key(passwd)
    print(pass_key)
    if pass_key != key:
        print("Passwords don't match")
        return False
    elif pass_key == key:
        print("Passwords match")
        return True
    else:
        print("should never get here")
        exit(0)

def loop_for_password(key):
    j = 0
    while j < 3:
        i = process_password(key)
        if not i:
            j += 1
        else:
            j = 3

def __main__():
    _KEY = get_key("Peter")
    loop_for_password(_KEY)

if __name__ == '__main__':
    __main__()
