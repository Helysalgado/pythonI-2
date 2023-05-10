'''
NAME
	Count_nucleotids.py
    
VERSION
    1.0
    
AUTHOR 
	Ethan Marcos Galindo Raya

DESCRIPTION
	It shows the quantity of each nucleotids of a given sequence

CATEGORY
	
USAGE 

'''

# IMPORTS
import re  # Detection of sequence cases

# Message to the user asking for the rute 
print('Please, enter the rute that contains the dna sequence:')
rute = input()
dna =   open(rute).read()

# we identify if is fastA to make proper changes
dna = dna.split('\n')
if re.search(r'.fna$', rute):
    dna = dna[1:]
dna = ''.join(''.join(dna).split(' ')).upper()

# Comprobation of correct sequence
if re.search(r'[^ATCG]', dna) or dna == '':
    raise ValueError(f'\nThe sequence has an error in it')

# Count A, T, C, G
As = dna.count('A')
Ts = dna.count('T')
Cs = dna.count('C')
Gs = dna.count('G')

# Messages with results
print(f'The dna sequence has the following quantity of aminoacids:\n\
    \tA: {As}\tT: {Ts}\tC: {Cs}\tG: {Gs}')
