#!/usr/bin/env python3

def print_fibonacci(length):
    sequence = [0,1]

    if length <=2:
        print(sequence[:length])
    else:
        while len(sequence)< length:
            next_number = sequence [-1] + sequence[-2]
            sequence.append(next_number)

        print(sequence)    
    pass