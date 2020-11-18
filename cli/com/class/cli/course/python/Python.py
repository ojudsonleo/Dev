from time import sleep


from time import *
class DATA(object):
    @staticmethod
    def store(Data, Doc=False):
        import time

        print("creating data..")

        time.sleep(9)

        if Doc == True:
            print("put any data to store in the main storage")

        if Doc == False:
            pass

        data = {Data}

        print("data{")
        print(data)
        print("}")

    @staticmethod
    def delete(Data):
        print("deleting data...")
        sleep(5)
        print("deleted")

    @staticmethod
    def deleteall():
        print("deleting all from data...")
        sleep(6)
        print("deleted all")

    @staticmethod
    def Reload():
        print("reloading..")
        sleep(2)
        print("")
        print("reloaded")

    @staticmethod
    def cleardata():
        print("clearingdata..")
        sleep(4)
        print("cleared")
    

DATA.store(12)