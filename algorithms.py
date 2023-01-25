# SCAN and C-SCAN algorithms representations in Python

# SCAN:
# Iterates through a sorted list of unique integers representing the waiting disk requests
# from a certain point in the middle (disk arm position) removing the elements. When reaches 
# the end of the list, iterates backwards until it reaches the beginning of the list, 
# answering to all the requests in the list.

# C-SCAN:
# Iterates through a sorted list of unique integers representing the waiting disk requests
# from a certain point in the middle (disk arm position) removing the elements. When reaches 
# the end of the list, goes back to start of the list and iterates again through the remaining 
# elements, answering to all the requests in the list.

# OBS: iterating is done 'backwards' in the list for easier removal (pop) of the elements by
# index.

from datetime import datetime

with open("requests.txt", "r") as f:
    lines = f.readlines()

requests = [int(line.strip()) for line in lines]
requests.sort()

def SCAN(requests, position_element):
    if position_element in requests: position = requests.index(position_element)
    else: return 'Invalid initial position'

    # iterates from the position to the start of the list
    for i in range(position, -1, -1):
        print(requests[i], end='->')
        requests.pop(i)

    # iterates from the start of the list (position that
    # the first iteration ended to the end of the list
    for i in range(len(requests)):
        print(requests[i], end='->')


def CSCAN(requests, position_element):
    if position_element in requests: position = requests.index(position_element)
    else: return 'Invalid initial position'

    # iterates from the position to the start of the list
    for i in range(position, -1, -1):
        print(requests[i], end='->')
        requests.pop(i)

    # goes to the end of the list and iterates backwards again
    for i in range(len(requests) - 1, -1, -1):
        print(requests[i], end='->')


start_position = requests[(len(requests) // 2) + 324]

before = datetime.now()
SCAN(requests, start_position)
print(f'\nSCAN time: {datetime.now() - before}')

before = datetime.now()
CSCAN(requests, start_position)
print(f'\nCSCAN time: {datetime.now() - before}')
