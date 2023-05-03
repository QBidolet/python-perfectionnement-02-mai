import sched
import time

s = sched.scheduler(time.monotonic, time.sleep)
# s = sched.scheduler(time.time, time.sleep)

def sum_n(n):
    sum = 0
    for i in range(n + 1):
        sum += i
    print(f"le résultat du processus avec n ={n}  est: {sum} ")


if __name__ == '__main__':
    s.enter(10, 1, sum_n, argument=(100,))
    s.enter(5, 2, sum_n, argument=(200,))
    s.run()
