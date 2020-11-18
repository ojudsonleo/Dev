from time import *
import sys
import os

while True:
    i = os.system("bash")

    if i == "compose file":
        print("connecting...")
        sleep(12)
        print("activating..")
        sleep(12)
        input("length: ")
        sleep(3)
        print("completed")
        print("lisense: Rs")
        i = input("lisense: ")

        if i == "Rs":
            print("sucessfully finshed")

        else:
            print("wrong lisence")

        sys.exit()
