# This script was written by Pierce Jamieson in Python 3.6
# The purpose of this script is to replace geneIDs in .nwk files.
# .nwk files are used to make phylogenetic trees.

import random
import math as maths
import re


def nwkReplace(nwkInput, geneIDs, replacementIDs):
    geneIDs.replace(" ", "")
    replacementIDs.replace(" ", "")
    geneIDarray = geneIDs.split(",")
    replacementIDarray = replacementIDs.split(",")
    if len(replacementIDarray) != len(geneIDarray):
        print("Error, lists are of different lengths")
    counter = 0
    for ID in geneIDarray:
        position = nwkInput.find(ID)
        length = len(ID)
        if position != -1:
            nwkInput = nwkInput[:position] + \
                replacementIDarray[counter] + nwkInput[(position + length):]
            counter = counter + 1
        else:
            counter = counter + 1

        if counter == len(geneIDarray):
            print(nwkInput)


nwkInput = input("Please paste the .nwk file into the terminal: ")
geneIDs = input(
    "Please paste the list of geneIDs found in your newick file into the terminal separated by commas: ")
replacementIDs = input(
    "Please paste the list of IDs you would like to replace those IDs with in corresponding order separated by commas: ")
nwkReplace(nwkInput, geneIDs, replacementIDs)
