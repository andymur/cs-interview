#!/usr/bin/python3

# Abbreviation task
# https://www.hackerrank.com/challenges/abbr/problem


# should be YES but NO now
#beFgH
#EFH

# result abc, cdeafabcasd should be 5 but abc, cdeabd should be -1
def substring_nouppercase(a, b):
    inda = 0
    syma = a[inda]
    match_started = False
    indb = 0
    result = -1

    for symb in b:
        #print("symb {0} indb {1}".format(symb, indb))
        if symb.lower() == syma.lower():
            if match_started:
                if len(a) <= inda + 1:
                    return result
                else:
                    inda += 1
                    syma = a[inda]
            else:
                result = indb
                match_started = True
                if len(a) <= inda + 1:
                    return result
                else:
                    inda += 1
                    #print(inda)
                    syma = a[inda]
        else:
            match_started = False
            result = -1
            inda = 0
            syma = a[inda]
        indb = indb + 1

    return -1

#rename me
def start_and_end_of_substring(a, b):
    index = substring_nouppercase(b, a) 
    
    if index > -1:
        return (index, index + len(b))
    else:
        return (-1,-1)

def yes_or_no(a, b):
    
    if a == b:
        return "YES"
    start_index, end_index = start_and_end_of_substring(a, b)



    if start_index > -1:
        #substr = a[start_index:end_index]
        prefix = a[:start_index]
        postfix = a[end_index:]
    
        if prefix.lower() == prefix and postfix.lower() == postfix:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"


def abbreviation(a,b):
    yes_or_no(a,b)

if __name__ == "__main__":
    #print("A")
    #print(substring_nouppercase("abc", "adbccdesfAbc"))
    print(yes_or_no("AbCdE", "AFE"))
    #print(index_and_length_of_substring("AbCdE", "AFE"))
