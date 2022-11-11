# coding: utf-8
import pandas as pd
from preprocessData import preprocessData
from getRecommendResult import getResult
#需求信息
#encoding="unicode_escape"
dataDemandSameIndustry=pd.io.parsers.read_csv('C:/Users/zhongxing/Desktop/lan/data/需求信息同.csv',encoding='gbk')
dataDemandNotSameIndustry=pd.io.parsers.read_csv('C:/Users/zhongxing/Desktop/lan/data/需求信息非同.csv',encoding='gbk')

#企业是否认证
isCertified=True
#企业是否已承接过需求
isTakeDemand=False
#同行业需求
demandSameIndustry=preprocessData(dataDemandSameIndustry)
#非同行业需求
demandNotSameIndustry=preprocessData(dataDemandNotSameIndustry)
#企业相关性产品
businessProducts=''
#经营范围
businessScope='玻璃制品加工、销售；玻璃制品购销；普通货物及技术的进出口；废旧玻璃回收。(依法须经批准的项目，经相关部门批准后方可开展经营活动)'
##主导产品
businessLeadingProduct=''
businessId='b12'
resultNotSameIndustry={}
resultSameIndustry={}
resultAll={}

getResult(isCertified,isTakeDemand,businessId,businessScope,businessLeadingProduct,demandNotSameIndustry,demandSameIndustry)