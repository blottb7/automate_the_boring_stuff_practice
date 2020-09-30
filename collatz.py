#Practice problem at end of Chapter 3:

def collatz(number):
    try:
        if number % 2 == 0:
            return print(number)
        else:
            return print(3 * number + 1)
    except TypeError:
        print("Please type an integer.")

collatz(3)
collatz(10)
collatz(5)
collatz(16)
collatz(8)
collatz(4)
collatz(2)
collatz(1)
collatz("bug")
