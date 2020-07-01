from threading import Thread,Lock



lock=Lock()
def main():

   def ru1(sen):

               lock.acquire()

               print("user entered string:",sen)
               lock.release()



   def ru(sen):

           lock.acquire()

           print("reverse of user input:",sen[::-1])
           lock.release()


   sen=input(" enter string to be reversed")
   p=Thread(target=ru1,args=(sen,))
   p.start()
   q=Thread(target=ru,args=(sen,))
   q.start()
   p.join()
   q.join()
   rest=input(" ").lower()
   if rest=="yes":
       main()
   else:
       exit()

main()

