import search_drug as sd
import Disease_gene as dg
import read_json as rj
import networkx as nx
def call(disease):
    #初始化字典
    dic = {}
    list = []#字典的key值存为list用于判断路径上的元素是否有字典中的元素，用于后面统计频率
    f = open("ubiquinone_symbol.txt","r")
    for key in f:
        line = key.rstrip('\n')
        list.append(line)
        #print(list)
        dic[line] = 0
    #print(list)

    #遍历字典
    #for key in dic.items():
        #print(key)

    for i in sd.searchdrug(disease):#药物靶标列表
        #print(sd.searchdrug(disease)[i])
        for j in dg.disease_gene(disease):#致病基因列表
            #print(dg.disease_gene(disease)[j])
            #print(sd.searchdrug(disease)[i],dg.disease_gene(disease)[j])
            try:
                # 做疾病基因和药物靶标的全连接，找全连接的最短路径
                path = nx.shortest_path(rj.read_json_file("dkw.json"),i, j)

                for ele in path:#ele:最短路径上的元素
                    if ele in list:#路径元素属于列表中的元素
                        dic[ele]= dic[ele]+1#统计频率
                        #print(ele,dic[ele])#元素，出现次数
                #打印最短路径
                #print("%s疾病中的药物靶标%s和致病基因%s的最短路径为：%s" %(disease,i,j,path))

            except Exception:
                pass
                #print("药物靶标%s或致病基因%s有一个及以上不存在！" %(i,j))
    file = open("Frequence of %s.txt" %disease,"w")
    for key in dic.items():
        print(key)
        file.write(key[0]+" : "+key[1]+"\n")
    file.close()

call("Parkinson")
#call("Alzheimer")
#call("Liver")
#call("Huntington")
#call("")

