#!/usr/bin/python
def print_path(dir, count):
    for _ in range(count):
        print(dir)
        
def find_answer():
    max = int( input() )
    for i in range(0, max):
        row = input().strip()
        #nothing is going to be stripped and is just making a copy
        if row.find('m') != -1:
            mario = [i, row.find('m')]
        if row.find('p') != -1:
            peach = [i, row.find('p')]
    result = [p - m for p, m in zip(peach, mario)]
    # x = [1, 2, 3]
    # y = [4, 5, 6]
    # zipped = zip(x, y)
    # list(zipped)
    # [(1, 4), (2, 5), (3, 6)]
    # what zip() does 
    # is negative when mario is above peach or when mario is to
    # the left of peach
    direction = ['DOWN', 'RIGHT']
    
    if result[0] < 0:
        direction[0] = 'UP'
        result[0] *= -1 
    if result[1] < 0:
        direction[1] = 'LEFT'
        result[1] *= -1
    # the multiply by -1 is to make it positive
    print_path(direction[0], result[0])
    # you are finding UP/DOWN
    print_path(direction[1], result[1])
    # you are finding LEFT/RIGHT
find_answer()
