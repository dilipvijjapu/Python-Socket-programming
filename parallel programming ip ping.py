import os
import re
from threading import Thread


class testit(Thread):
   def __init__ (self,ip):
      Thread.__init__(self)
      self.ip = ip
      self.status = -1
   def run(self):
        pingaling = os.popen("ping -q -c2 "+self.ip,"r")
     # while 1:
        line = pingaling.readline()#used to read ip address statistics


        igot = re.findall(testit.lifeline,line)#it is used to find 1st parameter in the line
        if igot:
           self.status = int(igot[0])

testit.lifeline = re.compile(r"(\d) received")# basically it is used to match patterns
report = ("No response","Partial Response","Alive")

#MAX_PARALLEL = 15


pinglist = []
top = 25



for host in range(1,4):
   ip = "172.217.167."+str(host)
   current = testit(ip)
   pinglist.append(current)
   current.start()

   """waitfor = 0
   if len(pinglist) > MAX_PARALLEL: waitfor = 1
   if host == top: waitfor = len(pinglist)"""

   for pingle in pinglist:
       """pingle = pinglist[0]
       pinglist = pinglist[1:]"""
       pingle.join()
       print("Status from ",pingle.ip,"is",report[pingle.status])


