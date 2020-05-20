import time


class Timer:
    def __init__(self):
        self.working_time = 0

    def __enter__(self):
        self.begin = time.monotonic()
        print(f'{self.begin}: начало работы.\n')

    def calculate_time(self):
        self.working_time = self.end - self.begin
        return self.working_time

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f'error: {exc_val}')
        self.end = time.monotonic()
        print(f'{self.end}: конец работы.')
        print(f'{self.calculate_time()}: общее время работы.')


def eratosthenes(n):
    primes = []
    for number in range(2, n + 1):
        for prime_number in primes:
            if number % prime_number == 0:
                break
        else:
            primes.append(number)
    print(primes, '\n')


if __name__ == '__main__':
    with Timer() as timer:
        eratosthenes(100000)
