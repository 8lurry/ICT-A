def replace_in_string(string):
    return string.replace(' ', '-')

def char_last_in_string(string, char):
    for i in range(len(string)-1, -1, -1):
        if string[i] == char:
            return i

def prime_factors(num):
    factors = []
    for i in range(2, num + 1):
        if num % i == 0:
            prime = True
            for j in range(2, i // 2 + 1):
                if i % j == 0:
                    prime = False
                    break
            if prime:
                factors.append(i)
    return factors

def swap_num(x, y):
    return y, x

def separate_odd_even(num_list):
    odd = []
    even = []
    for num in num_list:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd

if __name__=="__main__":
    import sys
    select = input("""\
Please select which function you wish to execute....
Hint: Provide an integer value corresponding to the function in the order given below.
>>> 
>>> 1 Replace empty space with hyphen in a string
>>> 2 Find last occurrence of a character in a string
>>> 3 Find prime factors of a number
>>> 4 Swap two numbers
>>> 5 put even and odd numbers in separate list
>>>
.......: """)
    if select == '1':
        string = input("""\
        Please give your string to act upon:
        .......: """)
        print(replace_in_string(string))
    elif  select == '2':
        string = input("""\
        Please give your string to act upon
        .......: """)
        char = input("""\
        Please give the charater to find its last occurrence
        .......: """)
        print(f"At the last occurrence, the index of {char} is {char_last_in_string(string, char)}")
    elif select == '3':
        num = int(input("""\
        Please give a number to find its prime factors
        .......: """))
        print(f"Prime factors of {num} are: {prime_factors(num)}")
    elif select == '4':
        inp = input("""\
        Please give two comma (,) separated numbers to swap
        .......: """)
        ls = inp.split(',')
        x, y = int(ls[0]), int(ls[1])
        print(f"Swapped Numbers: {swap_num(x, y)}")
    elif select == '5':
        inp = input("""\
        Please give comma (,) separated numbers to put in to even and odd lists
        .......: """)
        num_list = [int(i) for i in inp.split(',')]
        even, odd = separate_odd_even(num_list)
        print(f"List of evens: {even}, and odds: {odd}")
    else:
        print("Incorrect Input! You are suppose to give a integer number between 1 and 5 (inclusive)")
