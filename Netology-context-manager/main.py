import datetime


class Timer:
    def __enter__(self):
        self.begin = datetime.datetime.utcnow()
        print(f'{self.begin}: начало работы.\n')

    def calculate_time(self):
        self.working_time = self.end - self.begin
        return self.working_time

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f'error: {exc_val}')
        self.end = datetime.datetime.utcnow()
        print(f'{self.end}: конец работы.')
        print(f'{self.calculate_time()}: общее время работы.')


def eratosthenes(n):
    simples = []
    for number in range(2, n + 1):
        for simple_number in simples:
            if number % simple_number == 0:
                break
        else:
            simples.append(number)
    print(simples, '\n')


if __name__ == '__main__':
    with Timer() as timer:
        eratosthenes(100000)
