# Time Complexity: O(n)
# 
# Args:
#   namelist: a Python list of names
#   num: the number of times a potato is passed through the queue
# Returns:
#   The name of the last person remaining after repetitive counting by num.

# 1. First, we create a queue and add all the names in the namelist to the queue.
# 2. Then, we print the name at the front of the queue (which is the first name in the namelist).
# 3. Then, we loop through the num (7) which is passed into the function.
# 4. For each iteration, we dequeue the first name and enqueue it back to the end of the queue.
# 5. We print the name at the front of the queue.
# 6. After the 7th iteration, we dequeue the front name, which is ‘BILL’ and print it.
# 7. We repeat steps 3-6 until there is only one name left in the queue, which is the winner of the raffle.
from Queue import Queue
def hoyPotato(namelist,num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
    print(simqueue.look())
    # Time Complexity: O(n)
    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
            print(simqueue.look())
        simqueue.dequeue()
        print(simqueue.look())
    # print(simqueue.dequeue())
hoyPotato(['BILL','DAVID','SUSAN','JANE','KENT','BRAD'],3)