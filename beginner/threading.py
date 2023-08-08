# thread = a flow of execution. like a separate order of instruction.
#                   however each thread takes a turn running to achieve concurrency
#                   GIL = (global interpreter lock),
#                   allows only one thread to hold the control of the python interpreter at any one time

# cpu bound = program/task spends most of its time waiting for internal events (cpu intensive)
#              use multiprocessing

# io bound = program/task spends most of its time waiting for external events( user input,web scraping)
#             use multithreading


import threading
import time

#def eat_breakfast():
#    time.sleep(3)
#    print("You eat the breakfast")

#def drink_coffee():
#    time.sleep(4)
#    print("you drink coffee")

#def study():
#    time.sleep(5)
#    print("you finsih studying")

#x= threading.Thread(target=eat_breakfast,args=())
#x.start()

#y= threading.Thread(target=drink_coffee,args=())
#y.start()

#z= threading.Thread(target=study,args=())
#z.start()

#x.join()
#y.join()
#z.join()


#eat_breakfast()
#drink_coffee()
#study()

#print(threading.active_count())
#print(threading.enumerate())
#print(time.perf_counter())


# daemon thread = a thread that runs in the background, not important for program to run
#                 your program will not wait for daemon threads to complete before exiting
#                 non-daemon threads cannot normally be killed,stay alive until task is complete

#                 ex. background tasks, garbage collection, waiting for input,long running process


def timer():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ", count, "seconds")

x = threading.Thread(target=timer, deamon=True)
x.start()

x.setDeamon(True)
print(x.is Deamon)
answer = input("Do you wish to exit?")







