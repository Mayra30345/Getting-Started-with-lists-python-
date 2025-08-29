def match_words(words):
    ctr=0
    lst=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr +=1
            lst.append(word)
    print("List of words with first and last chracter as the same \n",lst)
    return ctr
count=match_words(["abc","cbc","1221","xyv","lst"])
print("Number of words which have the same first and last character are: ",count)
