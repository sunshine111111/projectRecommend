
def preprocessData(dataDemand):
    ##需求标题
    dataDemand['demandTitle'] = dataDemand['demandTitle'].fillna('')
    # 需求描述
    dataDemand['demandDescription'] = dataDemand['demandDescription'].fillna('')
    # 需求内容(考虑到需求描述不完善的情况下，将需求标题考虑进去)
    dataDemand['demandContent'] = dataDemand['demandTitle'] + dataDemand['demandDescription']
    return dataDemand
