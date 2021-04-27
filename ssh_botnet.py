

import argparse
from pexpect import pxssh

botnet=[]

class Client:
    def __init__(self,host,user,password,port):
        self.host=host
        self.user=user
        self.password=password
        self.port=port
        self.session = self.connect()
    def connect(self):
        try:
            s=pxssh.pxssh()
            s.login(self.host,self.user,self.password,self.port)
            return s
        except Exception as e:
            print(e)
            print("[-] Error Connecting")

    def send_command(self,cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before.decode("utf-8")

    
def botnetcmd(cmd):
    for client in botnet:
        output=client.send_command(cmd)
        print("[*] Output from  " + client.host)
        print("[+] " + output + "\n")


def addclient(host,user,password,port):
    client= Client(host,user,password,port)
    botnet.append(client)



def main():
    paser=argparse.ArgumentParser(description="A SSH Botnet that connects throungh multiple servers ")

    paser.add_argument("-H",required=True,dest="host",help="Enter the target host to connect")
    paser.add_argument("-U",required=True,dest="user",help="Enter the username")
    paser.add_argument("-p",required=True,dest="password",help="Enter the password")
    paser.add_argument("-C",required=True, dest="cmd",help="Enter any command to want to add")
    paser.add_argument("-P",required=True,dest="port",help="Enter the port if required")

    args = paser.parse_args()
    
    host=args.host.split(",")
    user=args.user.split(",")
    password=args.password.split(",")
    port=args.port.split(",")
    cmd = args.cmd.split(",")

    for data in range(0,len(host)):
        addclient(host[data],user[data],password[data],port[data])

    for commnd in cmd:
        botnetcmd(commnd)
        

   

if __name__=="__main__":
    main()
