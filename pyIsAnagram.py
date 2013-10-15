import os,sys,collections, optparse

# Banner
def Banner():
    print("=================================================")
    print("Anagram v0.1                                     ")
    print("=================================================")
    
# Checks whether input strings, S1 & S2 are anagram.
def is_anagram(S1, S2):
    bAnagram = False
    if len(S1) == len(S2):
        d = collections.defaultdict(int)
        for x in S1:
            d[x] += 1
        for x in S2:
            d[x] -= 1
        bAnagram = not any(d.itervalues())
    return bAnagram

if __name__=="__main__":
    Banner()
    parser = optparse.OptionParser()
    parser.add_option('-i', '--in1', dest='s1', help='Input string 1')
    parser.add_option('-j', '--in2', dest='s2', help='Input string 2')
    
    (options,args) = parser.parse_args()
    
    if options.s1 and options.s2:
        szRes = is_anagram(options.s1, options.s2)
        if szRes==True:
            print("The 2 strings, %s and %s are anagram." % (options.s1, options.s2))
        else:
            print("The 2 strings, %s and %s are not anagram." % (options.s1, options.s2))
    elif len(args) != 3:
        parser.error("wrong number of arguments")
        print options
        print args