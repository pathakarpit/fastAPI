import time
from timeit import default_timer as timer

def run_task(name, seconds):
    print(f'{name} started at: {timer()}')
    time.sleep(seconds)
    print(f'{name} completed at: {timer()}')

start = timer()
run_task('Task 1', 2)
run_task('Task 1', 1)
run_task('Task 1', 3)

print(f'total time taken: {timer() - start:.2f} seconds')