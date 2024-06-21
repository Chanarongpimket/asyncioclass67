# extending the Thread class
from time import sleep, ctime
#extending the Thread class
from threading import Thread

#custom thread class
class CustomThread(Thread):
    def run(self):
        #block for a moment
        sleep(1)
        # display a message
        print(f"{ctime()} This is coming from another thread")

#create the thread
thread = CustomThread()

# start the thread
thread.start()

#wait for the thread to finish
thread.join()
print(f"{ctime()} Waiting for the thread to finish")
