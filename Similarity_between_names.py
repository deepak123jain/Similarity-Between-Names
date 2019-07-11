
from whoswho import who as w
from fuzzywuzzy import process as p

# List of all the names

choices=['krishan mohan singh','krishna mohan','K.M. singh','kM Singh','K m singh','krishan singh','Krishan','Krishna mohan singh','kris']

# The names which should be used as reference for matching.
s1='Krishan mohan singh'
s2='krishan mohan'

# Find matching score on basis both the reference names 
# using process from fuzzywuzzy (python library)
s=p.extract(s1, choices,limit=len(choices))
q=p.extract(s2, choices,limit=len(choices))

# a flag
error=0

# aggregate count for all the names in list when compared with 1st reference name
d1=0
print(s,q)
for i in s:
    d1+=i[1]
    
    # if score is somewhere less than 70, use whoswho library
    # since if acronym is there for some name then whoswho gives better result
    if i[1]<70:
        q1=(w.ratio(s1,i[0]))
        q2=(w.ratio(s2,i[0]))
        print(i[0])
        # if score is still <60 then block the user
        if q1<60 and q2<60:
            print('blocked')
            error=1
            break
        else:
            # if score >=60 
            # decrement fuzzywuzzy score and add whoswho score
            d1-=i[1]
            d1+=max(q1,q2)
            error=0
        
        
# is all the names passed successfully from 1st reference name, repeat same process for second reference name


if error==0:
    d2=0
    for i in q:
        d2+=i[1]
        if i[1]<70:
            q1=(w.ratio(s1,i[0]))
            q2=(w.ratio(s2,i[0]))
            print(i[0])
            if q1<60 and q2<60:
                print('blocked')
                error=1
                break
            else:
                d2-=i[1]
                d2+=max(q1,q2)
                error=0
        
        
        
# if both the all the names are passed with both the reference names
if error==0:
    # Find Mean Score for both the reference name
    f1=d1/len(choices)
    f2=d2/len(choices)
    
    
    # if the avereage of both the mean scores is greater than threshold(here 75) than accept the user else block the user.
    if ((f1+f2)/2)>=75:
        print('Pass with score=',(f1+f2)/2)
    else:
        print('Blocked')

    





