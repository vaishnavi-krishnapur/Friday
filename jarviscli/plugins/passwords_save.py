import cryptocode
import csv
import os.path

from plugin import plugin

@plugin("savepassword")
class SavePassword():
    def __call__(self, jarvis, s):
        user = jarvis.input('Who are you: ')
        website = jarvis.input('enter the website: ')
        username = jarvis.input('enter username : ')
        password = jarvis.input('enter password : ')
        #output = [user,website, username, password]
        self.newOrExistingUser(user, website, username, password)
        jarvis.say("website details saved")

    def newOrExistingUser(self,user, website, username, password):
        fileName = "Passwords_"+ user.lower() + ".csv"
        if os.path.exists(fileName):
            #print("user exists.adding details")
            self.addOrUpdateDetails(user,website, username, password)
        else:
            #print("user doesnt exists. adding user")
            self.createCsv(user,website, username, password)

    def createCsv(self,user, website, username, password):
        print(os.getcwd())
        fileName = "Passwords_"+ user.lower() + ".csv"
        csvFile = open(fileName, 'w')
        self.addOrUpdateDetails(user,website, username, password)


    def addOrUpdateDetails(self,user, website, username, password):
        password_encrypted = self.encrypt_password(user, password)
        fileName = "Passwords_"+ user.lower() + ".csv"
        replace = False
        csvRead = open(fileName, 'r')
        reader = csv.reader(csvRead)
        for line in reader:
            if website in line:
                line[1] = username
                line[2] = password_encrypted
                replace = True
        csvRead.close()

        if replace == False:
            csvFile = open(fileName, 'a')
            writer = csv.writer(csvFile)
            writer.writerow([website, username, password_encrypted])
            csvFile.close()

    def encrypt_password(self, user, password):
        #encrypting the password using username as key
        return cryptocode.encrypt(password,user)
