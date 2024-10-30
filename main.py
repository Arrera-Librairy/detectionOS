from dectectionOS import *

def main():
    sytem = OS()
    print("Windows : ",sytem.osWindows())
    print("Linux : ",sytem.osLinux())

if __name__ == '__main__':
    main()