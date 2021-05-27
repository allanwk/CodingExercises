import numpy as np
from math import log, floor, ceil
np.set_printoptions(threshold=np.inf, linewidth=np.nan)
import sys
import xlsxwriter

def general_square_sum(d, m, l):
    return m*((((d+m-1)*(d+m))-((d-1)*d))/2)

def loss(d, m, l, s):
    if l == 0:
        return s
    elif l >= d + m - 1:
        return 0
    elif l <= d:
        return s - m*m*l
    return s - m*(l*(d+m-l) + (((l-1)*l)-((d-1)*d))/2)

def extended_sum(d, m, n_lines, l, s):
        sum = n_lines*((s + 8**(log(m, 2)))/m)
        if l >= d + (2*m) - 1:
            return 0
        elif d <= d + m:
            return sum - n_lines*l*m
        return sum - (n_lines*((l*(d+(2*m)-l)) + (((l-1)*l)-((d+m-1)*(d+m)))/2))

total = [0]
depth = [0]

def calc_block(m, n, d, l):
    depth[0] += 1
    #print(total[0])
    if m == 0 or n == 0:
        return

    #Align the main axis of the matrix horizontally
    block_sums = {}
    x = max(m,n)
    y = min(m,n)
    k = 2**(floor(log(y, 2)))
   #print(x, y, d, k)
    increment = 8**(log(k, 2))
    block_sums = {0: general_square_sum(d, k, l)}
   #print("Adding",loss(d, k, l, block_sums[0]))
    total[0] += loss(d, k, l, block_sums[0])

    #Computing blocks on the first row
    first_row_blocks = ceil(x/k)
    for i in range(1, first_row_blocks):
        block_sums[i] = block_sums[i-1] + increment
        if i != first_row_blocks - 1:
           #print("Adding",loss((k*i)+d, k, l, block_sums[i]))
            total[0] += loss((k*i)+d, k, l, block_sums[i])
   #print(block_sums)
    last_block_lines = x % k
    #If we have no excess block lines, but we have not computed all blocks,
    #we have to add the entire last block
    if x / k > len(block_sums) - 1 and last_block_lines == 0 and x/k !=1:
       #print("Adding",loss(k*(first_row_blocks-1)+d, k, l, block_sums[first_row_blocks-1]))
        total[0] += loss(k*(first_row_blocks-1)+d, k, l, block_sums[first_row_blocks-1])
    
    #Otherwise just add the necessary portion of the last block
    else:
       #print("Else Adding", last_block_lines, k*(first_row_blocks-1)+d,(loss(k*(first_row_blocks-1)+d, k, l, block_sums[first_row_blocks-1])/k)*last_block_lines)
        total[0] += (loss(k*(first_row_blocks-1)+d, k, l, block_sums[first_row_blocks-1])/k)*last_block_lines

    #Calculate the second row if necessary
    print(k, x, y, first_row_blocks)
    lines_under = y - k
    if(lines_under > 0):
        #Generation of XOR pattern of block indices for this row
        indexes = [i for i in range(first_row_blocks)]
        for i in range(1, first_row_blocks, 2):
            aux = indexes[i]
            indexes[i] = indexes[i-1]
            indexes[i-1] = aux
        if(first_row_blocks % 2 != 0):
            indexes[-1] += 1
        #Adding those blocks using the results from the first row
        for i in indexes[:-1]:
            if i not in block_sums:
                block_sums[i] = general_square_sum((i*k)+d, k, l)
           #print("Adding",(loss((i*k)+d, k, l, block_sums[i])/k)*lines_under)
            total[0] += (loss((i*k)+d, k, l, block_sums[i])/k)*lines_under
            
        if x%k == 0 and x/k != 1:
            i = indexes[-1]
            if i not in block_sums:
                block_sums[i] = general_square_sum((i*k)+d, k, l)
           #print("Adding",(loss((i*k)+d, k, l, block_sums[i])/k)*lines_under)
            total[0] += (loss((i*k)+d, k, l, block_sums[i])/k)*lines_under
        else:
            calc_block(m%k, n%k, (indexes[-1]*k)+d, l)

def elder_age(m,n,l,t):
    
    total[0] = 0
    calc_block(m,n,0,l)
    

    #arr = np.array([[0 for i in range(m)] for j in range(n)])
    #for y in range(n):
    #    for x in range(m):
    #        arr[y][x] = x^y
    #print(arr)   
    #
    #workbook = xlsxwriter.Workbook('output.xlsx')
    #worksheet = workbook.add_worksheet()
    #row = 0
    #for col, data in enumerate(arr):
    #    worksheet.write_column(row, col, data)
    #workbook.close()
    return total[0]%t

print(elder_age(28827050410, 35165045587, 7109602, 13719506))
print(depth[0])
#m = 443
#n = 494
#arr = np.array([[0 for i in range(m)] for j in range(n)])
#for y in range(n):
#    for x in range(m):
#        arr[y][x] = x^y
##print(arr)   
#
#workbook = xlsxwriter.Workbook('output.xlsx')
#worksheet = workbook.add_worksheet()
#row = 0
#for col, data in enumerate(arr):
#    worksheet.write_column(row, col, data)
#workbook.close()

