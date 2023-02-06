# SCAN and C-SCAN algorithms representations in Python

# Iterates through a sorted list of unique integers representing the waiting disk requests
# from a certain point in the middle (disk arm position) removing the elements. When reaches 
# the end of the list, iterates backwards until it reaches the beginning of the list, 
# answering to all the requests in the list.

# Iterates through a sorted list of unique integers representing the waiting disk requests
# from a certain point in the middle (disk arm position) removing the elements. When reaches 
# the end of the list, goes back to start of the list and iterates again through the remaining 
# elements, answering to all the requests in the list.

# index.

from datetime import datetime
import random

with open("requests.txt", "r") as f:
    lines = f.readlines()

requests = [int(line.strip()) for line in lines]
requests.sort()

def SCAN(requests, position_element):
    if position_element in requests: position = requests.index(position_element)
    else: return 'Invalid initial position'

    path = ''

    # iterates from the position to the start of the list
    for i in range(position, -1, -1):
        path += str(requests[i]) + '->'
        requests.pop(i)

    # iterates from the start of the list (position that
    # the first iteration ended to the end of the list
    for i in range(len(requests)):
        path += str(requests[i]) + '->'

    return path


def CSCAN(requests, position_element):
    if position_element in requests: position = requests.index(position_element)
    else: return 'Invalid initial position'

    path = ''

    # iterates from the position to the start of the list
    for i in range(position, -1, -1):
        path += str(requests[i]) + '->'
        requests.pop(i)

    # goes to the end of the list and iterates backwards again
    for i in range(len(requests) - 1, -1, -1):
        path += str(requests[i]) + '->'

    return path


def run(requests):
    start_position = requests[random.randint(0, len(requests) - 1)]
    requests_copy = requests.copy()

    before = datetime.now().timestamp()
    SCAN(requests, start_position)
    scan_time = (datetime.now().timestamp() - before) * 1000
    # print(f'\nSCAN time: {datetime.now() - before}')

    before = datetime.now().timestamp()
    CSCAN(requests_copy, start_position)
    cscan_time = (datetime.now().timestamp() - before) * 1000
    # print(f'\nCSCAN time: {datetime.now() - before}')

    return {'requests': requests, 'start_position': start_position,
     'scan_time': scan_time, 'cscan_time': cscan_time}

# print(run())

# def run():
#     start_position = requests[random.randint(0, len(requests) - 1)]

#     before = datetime.now().timestamp()
#     SCAN(requests, start_position)
#     scan_time = (datetime.now().timestamp() - before) * 1000
#     # print(f'\nSCAN time: {datetime.now() - before}')

#     before = datetime.now().timestamp()
#     CSCAN(requests, start_position)
#     cscan_time = (datetime.now().timestamp() - before) * 1000
#     # print(f'\nCSCAN time: {datetime.now() - before}')

#     return {'requests': requests, 'start_position': start_position,
#      'scan_time': scan_time, 'cscan_time': cscan_time}