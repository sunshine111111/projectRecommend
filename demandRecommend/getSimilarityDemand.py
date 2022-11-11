from sentence_transformers.util import cos_sim
from sentence_transformers import SentenceTransformer as SBert

#businessScope:单条企业经营范围，demandContents：多条需求信息
def getSimilarityDemand(businessId,businessScope,demandContents,dataDemandId,getIdWithScore):
    model = SBert('paraphrase-multilingual-MiniLM-L12-v2')
    ##这里考虑到模型网站访问失败的情况，也可以直接将模型下载到本地使用
    # model = SBert('C:\\Users\zhongxing\Desktop\lan\project\paraphrase-multilingual-MiniLM-L12-v2')
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
    if getIdWithScore:
        return result_temp
    else:
        return result