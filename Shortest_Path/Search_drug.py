import pymongo
from pymongo import MongoClient
import re
import json
import Disease_gene as dg

def searchdrug(disease,address = "39.97.240.2", port = 27017):
    client = pymongo.MongoClient(address, port)
    db = client['admin']
    db.authenticate("root", "@nenu_icb_2019_2022@")
    collection = client['Biodata']["DrugBank"]
    '''for i in iter:
        collection.insert(i)
        print('sucess', i)'''
    x = collection.find({"description": {"$regex": ".%s"%disease}})
    #return x
    target_list = []
    for i in x:
        if "targets" in i:
            if i["targets"] is not None:
                if type(i["targets"]["target"]) is dict:
                    #print(i["targets"]["target"]["polypeptide"]["gene-name"])
                    if "polypeptide" in i["targets"]["target"]:
                        if "gene-name" in i["targets"]["target"]["polypeptide"]:
                            if i["targets"]["target"]["polypeptide"]["gene-name"] not in target_list:
                                target_list.append(i["targets"]["target"]["polypeptide"]["gene-name"])

                if type(i["targets"]["target"]) is list:
                    #print(i["targets"]["target"])
                    #print(len(i["targets"]["target"]))
                    for j in i["targets"]["target"]:
                        #print(i["targets"]["target"][j])
                        if "polypeptide" in j:
                            if "gene-name" in j["polypeptide"]:
                                #print(i["targets"]["target"][j]["polypeptide"]["gene-name"])
                                if j["polypeptide"]["gene-name"] not in target_list:
                                    target_list.append(j["polypeptide"]["gene-name"])
                        '''else:
                            #print("F")
                            print(i["targets"]["target"][j])'''
                    '''for j in range(len(i["targets"]["target"])):
                        print(i["targets"]["target"][j]["polypeptide"]["gene-name"])
                        if i["targets"]["target"][j]["polypeptide"]["gene-name"] not in target_list:
                            target_list.append(i["targets"]["target"][j]["polypeptide"]["gene-name"])'''

    '''print("target_list中元素包含：")
    for i in range(len(target_list)):
        print(target_list[i])
        print(len(target_list))'''
    return target_list


#print(type(searchdrug("Parkinson")))
#A = DataSearch()
#调用

#for i in searchdrug("Liver"):
#    print(i)
#for i in searchdrug("Parkinson"):
#    print(i)
'''def json_to_dict(s):
    dict = json.loads(s)
    return dict'''
'''
target_list = []
#for i in searchdrug("Schizophrenia"):
for i in searchdrug("Parkinson"):
    if "targets" in i:
        if i["targets"] is not None:
            if type(i["targets"]["target"]) is dict:
                print(i["targets"]["target"]["polypeptide"]["gene-name"])
                if i["targets"]["target"]["polypeptide"]["gene-name"] not in target_list:
                    target_list.append(i["targets"]["target"]["polypeptide"]["gene-name"])
            '''
'''
            if type(i["targets"]["target"]) is list:
                #print(i["targets"]["target"])
                #print(len(i["targets"]["target"]))
                for j in range(len(i["targets"]["target"])):
                    #print(i["targets"]["target"][j])
                    if "polypeptide" in i["targets"]["target"][j]:
                        if "gene-name" in i["targets"]["target"][j]["polypeptide"]:
                            print(i["targets"]["target"][j]["polypeptide"]["gene-name"])
                            if i["targets"]["target"][j]["polypeptide"]["gene-name"] not in target_list:
                                target_list.append(i["targets"]["target"][j]["polypeptide"]["gene-name"])
                    '''
'''            
                    else:
                        #print("F")
                        print(i["targets"]["target"][j])'''
'''                 for j in range(len(i["targets"]["target"])):
                    print(i["targets"]["target"][j]["polypeptide"]["gene-name"])
                    if i["targets"]["target"][j]["polypeptide"]["gene-name"] not in target_list:
                        target_list.append(i["targets"]["target"][j]["polypeptide"]["gene-name"])'''
'''
print("target_list中元素包含：")
for i in range(len(target_list)):
    print(target_list[i])
    print(len(target_list))'''
#for i in searchdrug("Parkinson"):

'''for i in searchdrug("schizophrenia"):
    if "targets" in i:
        if i["targets"] is not None:'''
            #if type(i["targets"]["target"]) is dict:
                #print(i["targets"]["target"]["polypeptide"]["gene-name"])
                #print(i["targets"]["target"]["polypeptide"]["gene-name"])
                #print(type(i["targets"]["target"]))'''
            #if type(i["targets"]["target"]) is list:
                #for j in range(len(i["targets"]["target"])):
                    #print(j)
                    #print(type(i["targets"]["target"][j]))
                #print(len(i["targets"]["target"]))
                    #print(i["targets"]["target"][j]["polypeptide"]["gene-name"])'''
