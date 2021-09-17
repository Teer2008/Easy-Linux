import ShellScriptHandeler
import sys, os
from bullet import Password

class shell():
    def __init__(self):
        self.runShell = None
        self.ShellInput = None
        self.delPack = None
        self.savedDelPack = None
        self.enterdPassword = False

    def mainLoop(self):
        self.runShell = True
        while self.runShell == True:
            self.ShellInput = input(str("(help for Command-List)M A I N  I N P U T-->:"))

            if self.ShellInput == "help":
                # ADD COMMAND LIST HERE
                print("\nlist\nexit\nclear\npassword\ndelete\ninstall\nupdate\n")

            if self.ShellInput == "list":
                ShellScriptHandeler.OpenShellscript.displaySoftware()

            if self.ShellInput == "exit":
                os.system("clear")
                self.runShell = False
                sys.exit()

            if self.ShellInput == "clear":
                os.system("clear")

            if self.ShellInput == "delete":
                    if self.enterdPassword == True:
                        self.delPack = input(str("Package Name: "))
                        self.fullRemove = "echo " + self.userPassword + " | sudo -S apt-get -y --purge remove " + self.delPack
                        with open(os.path.abspath("bin/remove.sh"), 'w') as self.removeShell:
                            self.removeShell.write(self.fullRemove + "\necho " + self.userPassword + " | sudo -S apt-get -y autoremove" + "\necho " + self.userPassword + " | sudo -S apt-get -y clean\n")
                            self.removeShell.close()
                            print("SOFTWARE IS NOW READY")
                            ShellScriptHandeler.OpenShellscript.deleteSoftware()

                    if self.enterdPassword == False:
                        print("You have to ENTER youre Password first using the command password")

            if self.ShellInput == "password":
                self.passwordInput = Password(prompt="Password: ", hidden='*')
                print("Youre Password is only Saved while youre using the Program")
                self.userPassword = self.passwordInput.launch()
                self.enterdPassword = True

            if self.ShellInput == "install":
                    if self.enterdPassword == True:
                        self.instPack = input(str("Package Name: "))
                        self.fullInstall = "echo " + self.userPassword + " | sudo -S apt -y install " + self.instPack
                        with open(os.path.abspath("bin/install.sh"), 'w') as self.installShell:
                            self.installShell.write(self.fullInstall)
                            self.installShell.close()

                            print("SOFTWARE IS NOW READY")
                            ShellScriptHandeler.OpenShellscript.installSoftware()

                    if self.enterdPassword == False:
                        print("You have to ENTER youre Password first using the command password")

            if self.ShellInput == "update":
                if self.enterdPassword == True:
                    self.fullUpdate = "echo " + self.userPassword + " | sudo apt update && sudo apt upgrade -y\necho " + self.userPassword + " | sudo apt autoremove"
                    with open(os.path.abspath("bin/update.sh"), 'w') as self.updateShell:
                        self.updateShell.write(self.fullUpdate)
                        self.updateShell.close()
                        ShellScriptHandeler.OpenShellscript.update()

                if self.enterdPassword == False:
                    print("You have to ENTER youre Password first using the command password")

Shell = shell()
Shell.mainLoop()