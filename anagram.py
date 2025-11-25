def anagram(s1, s2):
    a1={}
    a2={}

    for i in range (len(s1)):
        if s1[i] in a1:
            a1[s1[i]]+=1
        else:
            a1[s1[i]]=1
    
    for j in range (len(s2)):
        if s2[j] in a2:
            a2[s2[j]]+=1
        else:
            a2[s2[j]]=1
    if a1==a2:
        return True
    else:
        return False
    
s1=input("String1: ")
s2=input("String2: ")   
print(anagram(s1,s2))