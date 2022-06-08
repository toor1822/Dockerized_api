from time import sleep
import threading


def main():
    threads = [
        threading.Thread(target=greater, args=('Vlad', 3), daemon=True),
        threading.Thread(target=greater, args=('Mika', 3), daemon=True),
        threading.Thread(target=greater, args=('Kristina', 3), daemon=True),
    ]
    [thread.start() for thread in threads ]
    print('hello from main')
    [thread.join() for thread in threads]
    print('Done')


def greater(name: str, time: int):
    for i in range(0, time):
        print('Hello my best friend {} !!!'.format(name))
        sleep(1)


if __name__ == "__main__":
    main()