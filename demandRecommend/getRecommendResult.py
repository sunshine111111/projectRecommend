from getSimilarityDemand import getSimilarityDemand

def getResultByIsCertified(businessId,companyBusiness,demandNotSameIndContents,demandNotSameIndId,demandSameIndContents,demandSameIndId):
    resultAlltemp={}
    resultItem=[]
    ##粗选
    resultNotSameIndustryTemp = getSimilarityDemand(businessId, companyBusiness, demandNotSameIndContents,
                                                    demandNotSameIndId, True)
    resultNotSameIndList = resultNotSameIndustryTemp[0:len(resultNotSameIndustryTemp) // 4:1]

    resultSameIndustryTemp = getSimilarityDemand(businessId, companyBusiness, demandSameIndContents,
                                                 demandSameIndId, True)
    resultSameIndustryTemp.extend(resultNotSameIndList)
    resultAllTemp = resultSameIndustryTemp
    # 过滤
    resultAllTempFilter = list(filter(lambda x: x[1] >= 0.4, resultAllTemp))
    ##排序
    result_temp = sorted(resultAllTempFilter, key=lambda x: x[1], reverse=True)
    if result_temp:
        for item in result_temp:
            resultItem.append(item[0])
    else:
        resultItem = ["None"]
    resultAlltemp[businessId] = resultItem
    return resultAlltemp

def getResult(isCertified,isTakeDemand,businessId,businessScope,businessLeadingProduct,demandNotSameIndustry,demandSameIndustry):
    resultAll={}
    if isCertified:
        if not isTakeDemand:
            resultAll=getResultByIsCertified(businessId, businessScope, demandNotSameIndustry['demandContent'], demandNotSameIndustry['uuid'],demandSameIndustry['demandContent'], demandSameIndustry['uuid'])
        else:
            resultAll = getResultByIsCertified(businessId, businessLeadingProduct,
                                                           demandNotSameIndustry['demandContent'],
                                                           demandNotSameIndustry['uuid'],demandSameIndustry['demandContent'], demandSameIndustry['uuid'])
    return resultAll