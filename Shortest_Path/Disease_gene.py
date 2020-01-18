'''
根据疾病名寻找致病基因
'''
def disease_gene(disease):
    f = open("all_gene_disease_associations.txt","r")
    #text = disease
    gene_list = []
    f.readline()
    for line in f:
        text = line.rstrip('\n').split("\t")
        #text1 = line.rstrip("\t")
        #print(text[0].split("/t")[0].split("/t")[0].split("/t")[0].split("/t")[0].split("/t")[0])
        #print(text1)
        if disease in text[5]:
            if text[1] not in gene_list:
                gene_list.append(text[1])
    return gene_list
'''
for i in range(len(disease_gene("Parkinson"))):
    print(disease_gene("Parkinson")[i])#致病基因'''
#disease_gene("Parkinson's disease")
#disease_gene()
