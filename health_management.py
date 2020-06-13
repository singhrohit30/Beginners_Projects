# Health Management System for logging and retrieving diet and exercise for clients
# The clients are Rohit Sush and Ritika
# Change clients according to ur needs
import datetime


def log_entry_diet(name, value):
    if name == 'rohit':
        with open('Rohit_deit.txt', 'a') as f:
            f.write(f'[{datetime.datetime.now()}] ' + value + "\n")
            print('Item Added Successfully')

    elif name == 'sush':
        with open('Sush_diet.txt', 'a') as f:
            f.write(f'[{datetime.datetime.now()}] ' + value + "\n")
            print('Item Added Successfully')

    elif name == 'ritika':
        with open('Ritika_diet.txt', 'a') as f:
            f.write(f'[{datetime.datetime.now()}] ' + value + "\n")
            print('Item Added Successfully')

    else:
        print('Client not found....404')


def log_entry_exercise(name, value):
    if name == 'rohit':
        with open('Rohit_exercise.txt') as f:
            f.write(f'[{datetime.datetime.now()}] ' + value + "\n")
            print('Item Added Successfully')

    elif name == 'sush':
        with open('Sush_exercise.txt') as f:
            f.write(f'[{datetime.datetime.now()}] ' + value + "\n")
            print('Item Added Successfully')

    elif name == 'ritika':
        with open('Ritika_exercise.txt') as f:
            f.write(f'[{datetime.datetime.now()}] ' + value + "\n")
            print('Item Added Successfully')

    else:
        print('Client not found....404')


def retrieve(name, choice):
    if name == 'rohit':
        if choice == 'diet':
            with open('Rohit_deit.txt') as f:
                lst = f.read()
                print(lst)

        elif choice == 'exercise':
            with open('Rohit_exercise.txt') as f:
                lst = f.read()
                print(lst)

    if name == 'sush':
        if choice == 'diet':
            with open('Sush_diet.txt') as f:
                lst = f.read()
                print(lst)

        elif choice == 'exercise':
            with open('sush_exercise.txt') as f:
                lst = f.read()
                print(lst)

    if name == 'ritika':
        if choice == 'diet':
            with open('Ritika_diet.txt', 'r') as f:
                lst = f.read()
                print(lst)

        elif choice == 'exercise':
            with open('Ritika_exercise.txt') as f:
                lst = f.read()
                print(lst)


while True:
    clients = ['rohit', 'sush', 'ritika']
    name = input('Enter the name: ').lower()
    if name not in clients:
        print('404....No Such client!!!....Try Again..')
    else:
        log_retrieve = input('Enter Log or Retrieve: ').lower()
        choice = input('Diet or Exercise: ').lower()

        if log_retrieve == 'log':
            if choice == 'diet':
                add = input('Enter the food item: ')
                log_entry_diet(name, add)
            elif choice == 'exercise':
                add = input('Enter the Exercise: ')
                log_entry_exercise(name, add)
            else:
                print(f'Class Type {choice} not Found...404')
        elif log_retrieve == 'retrieve':
            if choice == 'diet':
                retrieve(name, choice)
            elif choice == 'exercise':
                retrieve(name, choice)
            else:
                print(f'Class Type {choice} not found...404')
        else:
            print('Input Error...Try Again!!!')

    try_again = input('\n Do you want to continue: ').lower()
    if try_again == 'yes':
        continue
    else:
        break
