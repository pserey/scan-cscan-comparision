import time
import pandas as pd
import random
import sys

import matplotlib.pyplot as plt
from algorithms import CSCAN, SCAN, run
from generator import generate

def scan(requests, position):
    # implementation of algorithm 1
    start_time = time.time()
    SCAN(requests, position)
    end_time = time.time()
    return end_time - start_time

def cscan(requests, position):
    # implementation of algorithm 2
    start_time = time.time()
    CSCAN(requests, position)
    end_time = time.time()
    return end_time - start_time

# def compare_algorithms(inputs, algorithm1, algorithm2):
def compare_algorithms(inputs):
    results = []
    for requests in inputs:
        results.append(run(requests, sys.argv[1]))
        # time_scan = scan(requests, start_position)
        # time_cscan = cscan(requests, start_position)
        # results.append({'requests': requests, 'start_position': start_position,
        #                 'scan_time': time_scan, 'cscan_time': time_cscan})
    return results

def plot_results(results):
    df = pd.DataFrame(results)
    df.sort_values(by='start_position', inplace=True)
    max_scan_time = df['scan_time'].max()
    max_cscan_time = df['cscan_time'].max()
    max_time = max(max_scan_time, max_cscan_time)
    window_size = 500  # Define the size of the moving average window
    scan_moving_average = df['scan_time'].rolling(window=window_size, min_periods=1).mean()
    cscan_moving_average = df['cscan_time'].rolling(window=window_size, min_periods=1).mean()
    fig, ax1 = plt.subplots()
    color = 'tab:red'
    ax1.set_xlabel('Input size')
    ax1.set_ylabel('Normalized Time', color=color)
    ax1.plot(df['start_position'], scan_moving_average / max_time, color=color, label='scan')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.set_ylim(0, 1)
    ax2 = ax1.twinx() 
    color = 'tab:blue'
    ax2.set_ylabel('Normalized Time', color=color)
    ax2.plot(df['start_position'], cscan_moving_average / max_time, color=color, label='cscan')
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.set_ylim(0, 1)
    fig.tight_layout()
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    plt.show()

# def plot_results(results):
#     df = pd.DataFrame(results)
#     df.sort_values(by='start_position', inplace=True)
#     max_scan_time = df['scan_time'].max()
#     max_cscan_time = df['cscan_time'].max()
#     max_time = max(max_scan_time, max_cscan_time)
#     fig, ax1 = plt.subplots()
#     color = 'tab:red'
#     ax1.set_xlabel('Input size')
#     ax1.set_ylabel('Normalized Time', color=color)
#     ax1.plot(df['start_position'], df['scan_time'] / max_time, color=color, label='scan')
#     ax1.tick_params(axis='y', labelcolor=color)
#     ax1.set_ylim(0, 1)
#     ax2 = ax1.twinx() 
#     color = 'tab:blue'
#     ax2.set_ylabel('Normalized Time', color=color)
#     ax2.plot(df['start_position'], df['cscan_time'] / max_time, color=color, label='cscan')
#     ax2.tick_params(axis='y', labelcolor=color)
#     ax2.set_ylim(0, 1)
#     fig.tight_layout()
#     ax1.legend(loc='upper left')
#     ax2.legend(loc='upper right')
#     plt.show()


def generate_requests(num):
    generate(num)

    with open("requests.txt", "r") as f:
        lines = f.readlines()

    requests = [int(line.strip()) for line in lines]
    requests.sort()
    
    return requests

def random_start_position_element(requests):
    random_index = random.randint(0, len(requests) - 1)
    return requests[random_index]


def generate_inputs():
    inputs = []

    for i in range(1, 100):
        requests = generate_requests(10*i)
        # start_element = random_start_position_element(requests)

        # inputs.append((requests, start_element))
        inputs.append(requests)

    return inputs



inputs = generate_inputs()
# results = compare_algorithms(inputs, scan, cscan)
results = compare_algorithms(inputs)
# for e in results:
#     if e['scan_time'] < e['cscan_time']: print('x')
#     else: print('.')
# for r in results:
#     print(r)
plot_results(results)