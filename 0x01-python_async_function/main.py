'''
Test file for printing the correct output of the wait_n coroutine
'''
measure_time = __import__('2-measure_runtime').measure_time

n = 5
max_delay = 9

print(measure_time(n, max_delay))
