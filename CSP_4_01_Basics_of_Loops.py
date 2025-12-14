#All questions must use a loop for full points.

def oddNumbers(n:int) ->str:
    """
    Print out all odd numbers from 1 to n(inclusive) in a single string seperated by spaces.
    example oddNumbers(5) -> "1 3 5"
    example oddNumbers(8) -> "1 3 5 7"
    example oddNumbers(-8) -> ""
    """
    answer = ""
    for i in range(1, n+1, 2):
        answer += str(i) + " "
    answer = answer[0 : len(answer) - 1]
    return answer
print(oddNumbers(5))


def backwards(n)-> int:
    """
    modify the below function such that it prints out all the numbers from n to 1
    inclusive starting at n and counting down to 1
    example backwards(5) -> "5 4 3 2 1"
    example backwards(8) -> "8 7 6 5 4 3 2 1"
    example backwards(-2) -> ""
    """
    answer = ""
    while n>= 1:
        answer += str(n) + " "
        n -= 1
    answer = answer[0 : len(answer) - 1]
    return answer
print(backwards(5))

import random

def randomRepeating():
    """
    Print out a random number from 1-10 until you get a 10. Then print out how many
    times it took to roll a 10
    NOTE: Given randomness no test for this question
    :return:
    """

    iteration = 0
    i = 0
    while i != 10:
        i = random.randint(1, 10)
        iteration += 1
    print(f"it took {iteration} tries roll a 10")
randomRepeating()



def randomRange(n):
    """
    Generate a random number from 1 to 100 n number of times. Then after that is
    done print out what the highest number and the lowers number was from the rolled numbers.
    NOTE: Given randomness no test for this question
    :param n:
    :return:
    """
    low = 101
    high = 0
    for i in range(n):
        num = random.randint(1,100)
        if num < low:
            low = num
        if num > high:
            high = num
    print(f"your high is {high} your low is {low}")
randomRange(5)





def reverse(word:str)->str:
    """
    Takes in a string as an argument and return the given string in reverse.
    example reverse("cat") -> "tac"
    example reverse("Hello") -> "olleH"
    """

    answer = ""
    for i in range(len(word)-1, -1, -1):
        answer = answer + word[i]
    return(answer)
reverse("cat")



def fizzBuzzContinuous(n):
    """
    Modify the function such that it does the fizzbuzz operation on all numbers
    from 1 to n(inclusive).
    Fizz buzz is defined as
    if the number is divisible by 3 print fizz
    if the number is divisible by 5 print buzz
    if the number is divisible by both 3 and 5 print fizzbuzz
    if none of the above apply print the number.

    As with above questions add each answer to a string and return the final string.
    :param n:
    :return:
    """

    answer = ""
    for f in range(1, n+1):
        if f%3 and f%5 == 0:
            answer = answer + "fizzbuzz "
        elif f%5 == 0:
            answer = answer + "buzz "
        elif f%3 == 0:
            answer = answer + "fizz "
        else:
            answer = answer + str(f) + " "
    answer = answer[0:len(answer)-1]
    return answer
print(fizzBuzzContinuous(16))




def collatz(n):
    """
    Modify this function such that it mimics the collatz conjecture starting at n
    and prints out each number.
    The collatz conjecture is that if n is an even number divide it by 2. if n is
    an odd number multiply it by 3 and add 1.
    Repeat this process until n == 1.
    :param n:
    :return:
    """

    answer = ""
    while n != 1:
        if n%2==0:
            n=n/2
            answer = answer + str(int(n)) + " "
        else:
            n=(3*n)+1
            answer = answer + str(int(n)) + " "
    answer = answer[0:len(answer)-1]
    return answer
print(collatz(5))

def fibonacci(n):
    """
    for the given argument n print out the first n numbers of the fibonacci
    sequence in a single string sperated by spaces.
    The fibonacci sequence is defined as a sequence that starts with 0 then 1 as
    the first two numbers. Every subsequent number is the prior two numbers added together.
    Example fibonacci(6) -> "0 1 1 2 3 5"
    Example fibonacci(10) -> "0 1 1 2 3 5 8 13 21 34"
    Example fibonacci(1) -> "0"
    :param n:
    :return:
    """

    answer = ""
    previous = 0
    current = 1
    if n==0:
        pass
    elif n==1:
        answer += "0 "
    elif n==2:
        answer += "0 1 "
    elif n > 2:
        answer += "0 1 "
        for i in range(2, n):
            new = previous + current
            previous = current
            current = new
            answer += str(new) + " "
    answer = answer[0:len(answer)-1]
    return answer
print(fibonacci(300))