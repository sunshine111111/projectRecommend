# coding: utf-8
import sys
import pandas as pd
from sentence_transformers.util import cos_sim
from sentence_transformers import SentenceTransformer as SBert

#需求信息
#encoding="unicode_escape"
dataDemand=pd.io.parsers.read_csv('C:/Users/zhongxing/Desktop/lan/data/需求信息.csv',encoding='gbk')
resultFile = "C:/Users/zhongxing/Desktop/lan/data/result.txt"
out_to_file=True
##fillna()是一个用来填补数据集中的缺失值或不完整值的方法。
#企业经营范围
#dataDemand['businessScope']=dataDemand['businessScope'].fillna('')
##需求标题
dataDemand['demandTitle']=dataDemand['demandTitle'].fillna('')
#需求描述
dataDemand['demandDescription']=dataDemand['demandDescription'].fillna('')
#需求内容(考虑到需求描述不完善的情况下，将需求标题考虑进去)
dataDemand['demandContent']=dataDemand['demandTitle']+dataDemand['demandDescription']

#model = SBert('paraphrase-multilingual-MiniLM-L12-v2')
##这里考虑到模型网站访问失败的情况，直接将模型下载到本地使用
model = SBert('C:\\Users\zhongxing\Desktop\lan\project\paraphrase-multilingual-MiniLM-L12-v2')

#businessScope:单条企业经营范围，demandContents：多条需求信息
def getDemand(businessId,businessScope,demandContents,dataDemandId):
    sentencesBusiness = businessScope
    demandSim_total = {}
    resultItem = []
    result = {}
    if len(demandContents)>0:
        for id,demandContent in zip(dataDemandId,demandContents):
            sentencesDemand = demandContent
            embeddingsBusiness = model.encode(sentencesBusiness)
            embeddingsDemand = model.encode(sentencesDemand)
            cosine_scores = cos_sim(embeddingsBusiness, embeddingsDemand)
            demandSim_total[id]=cosine_scores
            #print(id,cosine_scores.numpy())
        result_temp = []
        result_temp=sorted(demandSim_total.items(),key=lambda x:x[1],reverse=True)
        #print(result_temp)
        if result_temp:
            for item in result_temp:
                resultItem.append(item[0])
        else:
            resultItem = ["None"]
    print(resultItem)
    result[businessId]=resultItem
    if out_to_file:
        export=open(resultFile,'w')
        for item in resultItem:
            export.write(str(item)+'\n')
        export.close()
    else:
        return result

businessScope='玻璃制品加工、销售；玻璃制品购销；普通货物及技术的进出口；废旧玻璃回收。(依法须经批准的项目，经相关部门批准后方可开展经营活动)'
businessId='b12'
getDemand(businessId,businessScope,dataDemand['demandContent'],dataDemand['uuid'])
