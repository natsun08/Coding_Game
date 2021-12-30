"""
Daily problems 17th
Author: Tran Quang Phuc
"""
def scrabble_score_file(filename):
    '''Print the result of the calculation: total value of letters / number of words'''
    TILE_SCORES = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4,
    "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1,
    "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1,
    "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8,
    "y": 4, "z": 10}
    '''The library which specifies the value of each letter'''
    summary = 0
    count = 0
    in_file = open(filename,'r')
    for line in in_file:
        words = line.split()
        for i in words:
            count += 1
            for j in i:
                if j in TILE_SCORES:
                    summary += TILE_SCORES[j]
    in_file.close()
    return(summary/count)
def compute_dna_distance(dna):
    '''print out a list which contains the distance of each pair of DNA strand'''
    distances = []
    for pair in dna:
        strand = pair.split()
        count = 0
        for i in range(min(len(strand[0]),len(strand[1]))):
            if (strand[0][i]!='-') and (strand[1][i]!='-'): 
                if strand[0][i] != strand[1][i]:
                    count += 1
        count += abs(len(strand[0])-len(strand[1]))
        distances.append(count)
    return(distances)
        