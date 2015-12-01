#!/usr/bin/python2.4 -tt
import sys

def Cat(filename):
    f = open(filename, 'rU')
    text = f.read()
    tuples = text.split()
    tuples_pair = {}
    counted_tuple = {}
    index = 0
    sorted_tuples = sorted(tuples)
    for item in sorted_tuples:
        tuples_pair[index] = item
        #print(item)
        index = index + 1
    #print(tuples_pair)
    f.close()
    
    single_word_counter = 1
    for x in range(0, index-1):
        print("_____________")
        print(tuples_pair[x])
        print(tuples_pair[x+1])
        if tuples_pair[x] == tuples_pair[x+1]:
            single_word_counter = single_word_counter + 1
        else:
            counted_tuple[tuples_pair[x]] = single_word_counter
            single_word_counter = 1
    print("Counted Tuple") 
    print(counted_tuple)


def main():
	Cat(sys.argv[1])

if __name__ == '__main__':
	main()
