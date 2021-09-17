import subprocess
import os

class openShellscript():
    def __init__(self):
        self.returncode = None
        self.shellscript = None
        self.displayPath = os.path.abspath("bin/displaySoftware.sh")
        self.removePath = os.path.abspath("bin/remove.sh")
        self.installPath = os.path.abspath("bin/install.sh")
        self.updatePath = os.path.abspath("bin/update.sh")

    def displaySoftware(self):
        self.shellscript = subprocess.Popen([self.displayPath], shell=True, stdin=subprocess.PIPE )
        self.shellscript.stdin.write('yes\n'.encode("utf-8"))
        self.shellscript.stdin.close()
        self.returncode = self.shellscript.wait()

    def deleteSoftware(self):
        self.shellscript = subprocess.Popen([self.removePath], shell=True, stdin=subprocess.PIPE )
        self.shellscript.stdin.write('yes\n'.encode("utf-8"))
        self.shellscript.stdin.close()
        self.returncode = self.shellscript.wait()
        self.securityDelete = open(self.removePath, 'r+')
        self.securityDelete.truncate(0)
        self.securityDelete.close

    def installSoftware(self):
        self.shellscript = subprocess.Popen([self.installPath], shell=True, stdin=subprocess.PIPE )
        self.shellscript.stdin.write('yes\n'.encode("utf-8"))
        self.shellscript.stdin.close()
        self.returncode = self.shellscript.wait()
        self.securityDelete = open(self.installPath, 'r+')
        self.securityDelete.truncate(0)
        self.securityDelete.close

    def update(self):
        self.shellscript = subprocess.Popen([self.updatePath], shell=True, stdin=subprocess.PIPE )
        self.shellscript.stdin.write('yes\n'.encode("utf-8"))
        self.shellscript.stdin.close()
        self.returncode = self.shellscript.wait()
        self.securityDelete = open(self.updatePath, 'r+')
        self.securityDelete.truncate(0)
        self.securityDelete.close

OpenShellscript = openShellscript()