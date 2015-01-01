#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

BLOCKS = [
    [
        [1, 1, 1],
        [1, 1, 0]
    ],
    [
        [0, 2, 0],
        [2, 2, 2],
        [0, 2, 0]
    ],
    [
        [0, 3, 0],
        [3, 3, 3],
        [0, 0, 3]
    ],
    [
        [4, 4, 0, 0],
        [0, 4, 4, 4]
    ],
    [   [5, 5, 0],
        [0, 5, 5],
        [0, 0, 5]
    ]
]

for block in BLOCKS:
    print block

print "---------------------"

def block_size(block):
    return len(block), len(block[0])

def turn90(block):    
    #mat = np.matrix(block)
    #__import__("pdb").set_trace()
    n, m = block_size(block)
    new_block =[]
    for j in range(m):
        new_row = []
        for i in reversed(range(n)):
            new_row.append(block[i][j])
        new_block.append(new_row)
    #print np.matrix(block)
    #print np.matrix(new_block)
    return new_block

def turn_over(block):
    n, m = block_size(block)
    new_block = [] 
    for i in reversed(range(n)):
        new_block.append(block[i])
    return new_block

for block in BLOCKS:
    print '------'
    print np.matrix(block)
    print np.matrix(turn90(block))
    print np.matrix(turn_over(block))
#turn90(BLOCKS[0])



