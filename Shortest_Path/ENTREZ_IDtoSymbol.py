'''
将ENTREZ_id转换成Symbol
'''
f1 = open("Mapping_ubiquinone.txt","r")
f1.readline()
f2 = open("Gene.txt")
f2.readline()

Symbol_list = []
Entrez_ID = []
for i in f1 :
    text1 = i.rstrip('\n').split('\t')
    if text1[1] not in Entrez_ID:
        Entrez_ID.append(text1[1])
'''for w in Entrez_ID:
    print(w)'''

#for j in Entrez_ID:
for k in f2:
    text2 = k.rstrip('\n').split('\t')
    #print("j=%s,text2[4]=%s" %(j,text2[4]))
    if text2[0] in Entrez_ID:
        if text2[4] not in Symbol_list:
            Symbol_list.append(text2[4])
'''for d in Symbol_list:
    print(d)'''
'''for i in f1:
    text1 = i.rstrip('\n').split("\t")
    for j in f2:
        text2 = j.rstrip('\n').split("\t")
        if (text1[1] == text2[0]):
            if text2[4] not in Symbol_list:
                print(text1,text2)'''
'''count  = 0
for i in f1:
    text1 = i.rstrip('\n').split("\t")
    print(text1[1])
    count = count + 1'''





f3 = open("ubiquinone_symbol.txt","w")

for k in Symbol_list:
    f3.write(k+"\n")
    print(k)
    #print(len(Symbol_list))
f3.close()
