import csv
import cryptocode
import os.path
from plugin import plugin

@plugin("getpassword")
class getPassword():
    def __call__(self, jarvis, s):
        user = jarvis.input('Who are you: ')
        website = jarvis.input('enter which website details to be retrieved: ')
        self.authenticate(user, website)
        #jarvis.say(output)

    def authenticate(self, user, website):
        key= input("enter the password to decrypt :")
        if key==user:
            self.get_passwords(user, website)
        else:
             print("Key is incorrect. Cant retrieve the password")


    def get_passwords(self, user, website):
        fileName = "C:\\Users\\vaish\\Desktop\\Friday\\Passwords_"+ user.lower() + ".csv"
        if os.path.exists(fileName):
            csvFile=open(fileName,'r')
            content=csv.reader(csvFile)
            username=0
            for lines in content:
                if website in lines:
                    username = lines[1]
                    password = self.decrypt_password(user,lines[2])
            if username==0:
                print("website not saved before. Please save before retrieve")
            else:
                print("user name is ",username, ". Password is ", password)
        else :
            print("user doesnt exists")


    def decrypt_password(self, user,password):
        return cryptocode.decrypt(password, user)