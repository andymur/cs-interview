#!/usr/bin/python3

# Abbreviation task
# https://www.hackerrank.com/challenges/abbr/problem


# should be YES but NO now // fixed
#beFgH
#EFH

#eFgH
#EFH

    #FgH
    #FH
    #--
    #FgH
    #EFH

# should be YES but NO now

# ERreEerR
# ERRER
    #eEerR
    #RER
    #--
    #eEerR
    #ER


def another_attempt(longer, shorter, level = 0):
    short_idx = 0
    long_idx = 0
    short_len = len(shorter)
    long_len = len(longer)
    if (level > 1000):
        print("RECURSION!")
        return False
    #print("===== ENTER ====")
    #print("longer: {0}, shorter: {1}, level: {2}".format(longer, shorter, level))
    print("longer: {0}, shorter: {1}, level: {2}".format(len(longer), len(shorter), level))
    while short_idx < short_len and long_idx < long_len:
        
        short_symbol = shorter[short_idx]
        long_symbol = longer[long_idx]
        #print("long symbol: {1}, short symbol: {0}".format(short_symbol, long_symbol))
        if short_symbol == long_symbol:
            short_idx+=1
            long_idx+=1
        elif short_symbol == long_symbol.upper():
            return another_attempt(longer[long_idx + 1:], shorter[short_idx:], level+1) or another_attempt(longer[long_idx + 1:], shorter[short_idx + 1:], level+1)
        elif long_symbol.isupper():
            return False
        else:
            long_idx+=1

    if long_idx < long_len:
        return longer.lower() == longer

    return short_idx >= short_len

# result abc, cdeafabcasd should be 5 but abc, cdeabd should be -1
def substring_nouppercase(a, b):
    print("a: {0}, b: {1}".format(a, b))
    inda = 0
    syma = a[inda]
    match_started = False
    indb = 0
    result = -1
    size = 0

    returnabind = (-1, -1)

    while indb < len(b):
        symb = b[indb]
        print("symb {0} indb {1} syma {2}, inda {3}".format(symb, indb, syma, inda))
        if symb.lower() == syma.lower():            
            if match_started:
                if len(a) <= inda + 1:
                    return result, len(a) + size
                else:
                    inda += 1
                    syma = a[inda]
            else:
                result = indb
                match_started = True
                if len(a) <= inda + 1:
                    return result, len(a) + size
                else:
                    inda += 1
                    print(inda)
                    syma = a[inda]
            # store information for potential return
            if symb.islower():
                print("storing inda {0}, indb {1}".format(inda - 1, indb))
                returnabind = inda - 1, indb
        else:
            
            #skip lower symbol cause it could be deleted
            if symb.islower():
                size += 1
            # we can try to restore the indices
            elif returnabind != (-1, -1):
                print("resetting")
                inda, indb = returnabind
                syma = a[inda]
                size += 1
                #not exactly needed symb = a[indb]
            #reset a position                
            else:
            	match_started = False
            	result = -1
            	inda = 0
            	syma = a[inda]           
        indb = indb + 1

    return (-1, -1)

#rename me
def start_and_end_of_substring(a, b):
    index, length = substring_nouppercase(b, a) 
    
    if index > -1:
        return (index, index+length)
    else:
        return (-1,-1)

def yes_or_no(a, b):
    
    if a == b:
        return "YES"
    start_index, end_index = start_and_end_of_substring(a, b)


    #print("start index: {0}, end index: {1}".format(start_index, end_index))
    if start_index > -1:
        #substr = a[start_index:end_index]
        prefix = a[:start_index]
        postfix = a[end_index:]
        #print(prefix + " " + postfix)
        if prefix.lower() == prefix and postfix.lower() == postfix:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"


def abbreviation(a,b):
    return yes_or_no(a,b)

def read_and_run():
    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        #result = abbreviation(b, a)
        result = substring_nouppercase(b, a)
        print(result)

if __name__ == "__main__":
    print(another_attempt("ERreEerREeerErrrrRRyeReErrerrereEEeRRErRrrereeeeerErereerReRereeeeCrreErREreeerrRrRERreeererererEeEEeerrerrereeRRerreeerrreRererereeSerEeeRereerrReErrrereErrerrrreererrsRRecerEreeRrrreRereerErrRRrrEeEererRrrreRerReRrereererereEeereEereesrERreReeerReErEeeeeRererReereRereerRrrRRerrerreeereEeeereerrEreeERreReRrEErRRerEereeeRreeErReerrEerEeEreerrTeeeEErreRErrerreeeeereeEeerERErRrereerreerRrrreerEreeRrErreeeRReRerrreerrEreerrerEeEeerreeeeEeerRrrerrsrerrereReREerEerrRerRErereRreerRreRReEeeeRerRereeerRerererrerrrreeReeERereeeesrrEerrrreeeeerrrrereeeeeerRrRrreeereRrreeseERrrrerReeeerreeeeereEerErrrRrreeeerRerrrrrErRreREeeerrrrrrrErrreerrRrereerrRrEEErsREeeerReEeErrrrRrRererereeererreereeRreerrerREeEReereerrrrrrereereeeerEeeeerreerSrReererrRereREreereErEReEReeeerrerEeeEeeRreeeRreeeEreeeeEreerrrEeereeerrrrERrRERReeerreEeJEEeSEeeeEeEeeRrRrrreeeRerrreerEreeererEereeeeRRrreReRrEerreEreeeerEErRrRrrrrerrereeEERErerreerrRrrreeeErEeErEreRrErRrErrreeeereeerrrrSeReeeeRerrrrerrEreerEeeeeeeerrreerreRerrREr", 
        "ERREREERERRREERREERRERRREEEERRREREEECEREERRRERREEEERRREERRERRRRSERERERERERERRRRRREERREREERRREEERERRRRRRREREEESEREREREEEERRERERRRERRRRREEREREERERREERRERRERREREEEERRTEEEEREEREEEEEEEERERRRRERREERREREERRREREREEREEREEERRRERERERREEREERRERRERERERRRREEERRREERRRRREREREREEEEERRRRRRRREERRERRERRRERERRREEERRRRERRERERRRERRRREREERREEESREEREERRRERREEEERRERERREEREREEREERREEEEEERRRSRERREREEEERERREREEERRERREEEEEEEREEERERRERREREEJEESEEEEEEERRRREEREREEEEEERERRRRRRREEEEREERRREEREEERRREEEEREERRERRERRRSREEERERREERRRRER"))
    #print(another_attempt("ERreEerREeer", "ERREREE"))
    #read_and_run()
    #print("A")
    #beFgH
    #EFH
    #print(substring_nouppercase("ABC", "AbbbBC"))
    #print(substring_nouppercase("EFH", "beFgH"))
    #print(substring_nouppercase("ERreEerREeerErrrrRRyeReErrerrereEEeRRErRrrereeeeerErereerReRereeeeCrreErREreeerrRrRERreeererererEeEEeerrerrereeRRerreeerrreRererereeSerEeeRereerrReErrrereErrerrrreererrsRRecerEreeRrrreRereerErrRRrrEeEererRrrreRerReRrereererereEeereEereesrERreReeerReErEeeeeRererReereRereerRrrRRerrerreeereEeeereerrEreeERreReRrEErRRerEereeeRreeErReerrEerEeEreerrTeeeEErreRErrerreeeeereeEeerERErRrereerreerRrrreerEreeRrErreeeRReRerrreerrEreerrerEeEeerreeeeEeerRrrerrsrerrereReREerEerrRerRErereRreerRreRReEeeeRerRereeerRerererrerrrreeReeERereeeesrrEerrrreeeeerrrrereeeeeerRrRrreeereRrreeseERrrrerReeeerreeeeereEerErrrRrreeeerRerrrrrErRreREeeerrrrrrrErrreerrRrereerrRrEEErsREeeerReEeErrrrRrRererereeererreereeRreerrerREeEReereerrrrrrereereeeerEeeeerreerSrReererrRereREreereErEReEReeeerrerEeeEeeRreeeRreeeEreeeeEreerrrEeereeerrrrERrRERReeerreEeJEEeSEeeeEeEeeRrRrrreeeRerrreerEreeererEereeeeRRrreReRrEerreEreeeerEErRrRrrrrerrereeEERErerreerrRrrreeeErEeErEreRrErRrErrreeeereeerrrrSeReeeeRerrrrerrEreerEeeeeeeerrreerreRerrREr", 
    #    "ERREREERERRREERREERRERRREEEERRREREEECEREERRRERREEEERRREERRERRRRSERERERERERERRRRRREERREREERRREEERERRRRRRREREEESEREREREEEERRERERRRERRRRREEREREERERREERRERRERREREEEERRTEEEEREEREEEEEEEERERRRRERREERREREERRREREREEREEREEERRRERERERREEREERRERRERERERRRREEERRREERRRRREREREREEEEERRRRRRRREERRERRERRRERERRREEERRRRERRERERRRERRRREREERREEESREEREERRRERREEEERRERERREEREREEREERREEEEEERRRSRERREREEEERERREREEERRERREEEEEEEREEERERRERREREEJEESEEEEEEERRRREEREREEEEEERERRRRRRREEEEREERRREEREEERRREEEEREERRERRERRRSREEERERREERRRRER"))
    #print(yes_or_no("AbCdE", "AFE"))
    #print(index_and_length_of_substring("AbCdE", "AFE"))
