# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 11:02:01 2018

@author: jenkinscc
"""
###Opens the fasta file you want to explore entry by entry
def read_FASTA_strings(fasta):
    with open(fasta) as file:
        return file.read().split('>')[1:]

###Matches the accession number to fasta and entry and separates sequence from header
def match_accession(fasta):
    for value in read_FASTA_strings(fasta):
        if accession_number in value:
            return value.partition('\n')
###removes white space characters if any in fasta file        
def rm_ws(fasta):
    return [[value.replace('\n', '')] for value in match_accession(fasta)]
###asks for user input
accession_number = input("What is the Accession Number?")
sequence = input("What is the Sequence of Interest?")
species = input("What is the Species?")
###If human input, uses the current human database on MS_Drive
if species.upper() == 'HUMAN':
    fasta = 'I:/FASTA_Databases/2016/2016_01 Human UniProt.fasta'
###If mouse input, uses the current mouse database on MS_Drive   
if species.upper() == 'MOUSE':  
    fasta = 'I:/FASTA_Databases/2016/2016_01 Mouse UniProt.fasta'

###Had to choose the sequence and pop the string out of the list with [0]
protein_sequence = (rm_ws(fasta)[2])[0]

###Search sequence of interest to protein sequence (+1 due to python counting)            
beginning_location =  protein_sequence.find(sequence.upper())+1

end_location = beginning_location + len(sequence) - 1    
   
print('\n', "Sequence Begins At Residue: ", beginning_location, '\n', "Sequence Ends At Residue: ", end_location)





