



import pandas as pd
import re


def getFreightFormulaConfigValue(truckLength):
    if truckLength == "4.2":
        return """
def getTruckLength():
    return 4.2
def getTruckFreight(distance, tolls, pathNum):
    if pathNum > 0:
        pathNum = pathNum - 1
    # 总运费
    totalFee = 0
    # 起步费
    initFee = 150
    totalFee = initFee
    if distance <= 20:
        totalFee = totalFee + tolls
        totalFee = totalFee + pathNum*50
    if distance > 20 and distance <= 200:
        totalFee = totalFee + (distance-20)*2.25
        totalFee = totalFee + tolls
        totalFee = totalFee + pathNum*50
    if distance > 200:
        totalFee = totalFee + (distance-20)*2.25
        totalFee = totalFee + tolls
        totalFee = totalFee + pathNum*50
    return totalFee
def getFreightFormula(distance, tolls, pathNum):
    if pathNum > 0:
        pathNum = pathNum - 1
    # 总运费
    totalFee = 0
    # 起步费
    initFee = 150
    result = str(initFee)
    totalFee = initFee
    if distance <= 20:
        totalFee = totalFee + tolls
        result = result + " + " + f'{tolls}'
        totalFee = totalFee + pathNum*50
        result = result + " + " + f'{pathNum}*50'
    if distance > 20 and distance <= 200:
        totalFee = totalFee + (distance-20)*2.25
        result = result + " + " + f'({distance}-20)*2.25'
        totalFee = totalFee + tolls
        result = result + " + " + f'{tolls}'
        totalFee = totalFee + pathNum*50
        result = result + " + " + f'{pathNum}*50'
    if distance > 200:
        totalFee = totalFee + (distance-20)*2.25
        result = result + " + " + f'({distance}-20)*2.25'
        totalFee = totalFee + tolls
        result = result + " + " + f'{tolls}'
        totalFee = totalFee + pathNum*50
        result = result + " + " + f'{pathNum}*50'
    return result + " = " + str(round(totalFee, 2))
        """
    if truckLength == "6.8":
        return """
def getTruckLength():
    return 6.8
def getTruckFreight(distance, tolls, pathNum):
    if pathNum > 0:
        pathNum = pathNum - 1
    # 总运费
    totalFee = 0
    # 起步费
    initFee = 300
    totalFee = initFee
    if distance <= 20:
        totalFee = totalFee + tolls
        totalFee = totalFee + pathNum*50
    if distance > 20 and distance <= 200:
        totalFee = totalFee + (distance-20)*3.1
        totalFee = totalFee + tolls
        totalFee = totalFee + pathNum*50
    if distance > 200:
        totalFee = totalFee + (200-20)*3.1
        totalFee = totalFee + (distance-200)*1.7
        totalFee = totalFee + tolls
        totalFee = totalFee + pathNum*50
    return totalFee
def getFreightFormula(distance, tolls, pathNum):
    if pathNum > 0:
        pathNum = pathNum - 1
    # 总运费
    totalFee = 0
    # 起步费
    initFee = 300
    result = str(initFee)
    totalFee = initFee
    if distance <= 20:
        totalFee = totalFee + tolls
        result = result + " + " + f'{tolls}'
        totalFee = totalFee + pathNum*50
        result = result + " + " + f'{pathNum}*50'
    if distance > 20 and distance <= 200:
        totalFee = totalFee + (distance-20)*3.1
        result = result + " + " + f'({distance}-20)*3.1'
        totalFee = totalFee + tolls
        result = result + " + " + f'{tolls}'
        totalFee = totalFee + pathNum*50
        result = result + " + " + f'{pathNum}*50'
    if distance > 200:
        totalFee = totalFee + (200-20)*3.1
        result = result + " + " + f'(200-20)*3.1'
        totalFee = totalFee + (distance-200)*1.7
        result = result + " + " + f'({distance}-200)*1.7'
        totalFee = totalFee + tolls
        result = result + " + " + f'{tolls}'
        totalFee = totalFee + pathNum*50
        result = result + " + " + f'{pathNum}*50'
    return result + " = " + str(round(totalFee, 2))
        """
    if truckLength == "13" or truckLength == "13.5":
        return """
def getTruckLength():
    return 13.5
def getTruckFreight(distance, tolls, pathNum):
    if pathNum > 0:
        pathNum = pathNum - 1
    # 总运费
    totalFee = 0
    # 起步费
    initFee = 700
    totalFee = initFee
    if distance <= 40:
        pass
    if distance > 40 and distance <= 200:
        totalFee = totalFee + (distance-40)*2.75
        totalFee = totalFee + tolls
        totalFee = totalFee + pathNum*50
    if distance > 200:
        totalFee = totalFee + (200-40)*2.75
        totalFee = totalFee + (distance-200)*2
        totalFee = totalFee + tolls
        totalFee = totalFee + pathNum*50
    return totalFee
def getFreightFormula(distance, tolls, pathNum):
    if pathNum > 0:
        pathNum = pathNum - 1
    # 总运费
    totalFee = 0
    # 起步费
    initFee = 700
    result = str(initFee)
    totalFee = initFee
    if distance <= 40:
        pass
    if distance > 40 and distance <= 200:
        totalFee = totalFee + (distance-40)*2.75
        result = result + " + " + f'({distance}-40)*2.75'
        totalFee = totalFee + tolls
        result = result + " + " + f'{tolls}'
        totalFee = totalFee + pathNum*50
        result = result + " + " + f'{pathNum}*50'
    if distance > 200:
        totalFee = totalFee + (200-40)*2.75
        result = result + " + " + f'(200-40)*2.75'
        totalFee = totalFee + (distance-200)*2
        result = result + " + " + f'({distance}-200)*2'
        totalFee = totalFee + tolls
        result = result + " + " + f'{tolls}'
        totalFee = totalFee + pathNum*50
        result = result + " + " + f'{pathNum}*50'
    return result + " = " + str(round(totalFee, 2))
        """



def main():
    truckFreightResultDict, freightFormulaResultDict = getData()
    truckFreightResultList = []
    freightFormulaResultList = []
    with pd.ExcelFile("（已下架，2024年初-7月24日）运输车辆出车申请-吴政哲1736315946593.xlsx") as xls:
        df = pd.read_excel(xls, "202407241910000340")
        for row_index, row in df.iterrows():
            if row[0] in truckFreightResultDict and row[0] in freightFormulaResultDict:
                truckFreightResultList.append(truckFreightResultDict[row[0]])
                freightFormulaResultList.append(freightFormulaResultDict[row[0]])
            else:
                truckFreightResultList.append(None)
                freightFormulaResultList.append(None)

    # 创建一个简单的DataFrame
    df = pd.read_excel("（已下架，2024年初-7月24日）运输车辆出车申请-吴政哲1736315946593.xlsx")
    # 假设我们要添加的数据是一个新的列
    truckFreightResultdata = truckFreightResultList
    df['运费'] = truckFreightResultdata
    freightFormulaResultdata = freightFormulaResultList
    df['运费公式'] = freightFormulaResultdata
    # 将更新后的DataFrame保存回Excel文件，这里使用原来的文件名和路径
    df.to_excel("（已下架，2024年初-7月24日）运输车辆出车申请-吴政哲1736315946593.xlsx", sheet_name='202407241910000340',  index=False)
def getData():
    r1 = {}
    r2 = {}
    with pd.ExcelFile("（已下架，2024年初-7月24日）运输车辆出车申请-吴政哲1736315946593.xlsx") as xls:
        df = pd.read_excel(xls, "202407241910000340")
        for row_index, row in df.iterrows():
            # print(row, sep='\n')
            truckLength = re.findall("(\d+?.?\d+).*?米", row[13])
            if len(truckLength) > 0:
                truckLength = truckLength[0]
                distance = re.findall("距离（(.*?)公里.*）", row[13])
                distance2 = re.findall("约 (\d+)公里", row[13])
                if len(distance) > 0 or len(distance2) > 0:
                    if len(distance) > 0:
                        distance = float(distance[0]) if "红绿灯" not in distance[0] else 0
                    if len(distance2) > 0:
                        distance = float(distance2[0])
                    # print(distance)
                    pathNum = re.findall("（“.*?”）", row[13])
                    pathNum2 = re.findall("途经点个数：(\d+)", row[13])
                    if len(pathNum) > 0 or len(pathNum2) > 0:
                        if len(pathNum) > 0:
                            pathNum = len(pathNum) - 1
                        if len(pathNum2) > 0:
                            pathNum = int(pathNum2[0]) + 1
                        tolls = re.findall("过路费（.*?(\d+)元）", row[13])
                        tolls2 = re.findall("预计道路费用约：￥(\d+)", row[13])
                        tolls3 = re.findall("预计道路费用约：过路费(\d+)", row[13])
                        if len(tolls) > 0 or len(tolls2) > 0 or len(tolls3) > 0:
                            if len(tolls) > 0:
                                tolls = float(tolls[0])
                            if len(tolls2) > 0:
                                tolls = float(tolls2[0])
                            if len(tolls3) > 0:
                                tolls = float(tolls3[0])
                            # print(tolls, row[0])
                            truckFreightFormula = {}
                            freightFormula = getFreightFormulaConfigValue(truckLength)
                            result = {}
                            source_code = freightFormula
                            exec(source_code, {}, result)
                            getTruckLength = result['getTruckLength']
                            truckFreightFormula[getTruckLength()] = result

                            sourceCodeFunc = truckFreightFormula[float(truckLength) if truckLength != "13" else 13.5]
                            getTruckFreight = sourceCodeFunc['getTruckFreight']
                            getFreightFormula = sourceCodeFunc['getFreightFormula']
                            truckFreightResult = round(getTruckFreight(distance, tolls, pathNum), 2)
                            truckFreightResult = str(truckFreightResult) + "元"
                            freightFormulaResult = getFreightFormula(distance, tolls, pathNum)
                            print(row[0], truckFreightResult, freightFormulaResult)
                            r1[row[0]] = truckFreightResult
                            r2[row[0]] = freightFormulaResult
                        else:
                            print("error4 {} {} ====================================================".format(row[0], row[13]))
                    else:
                        print("error3 {} {} ====================================================".format(row[0], row[13]))
                else:
                    print("error2 {} {} ====================================================".format(row[0], row[13]))
            else:
                print("error1 {} {} ====================================================".format(row[0], row[13]))
    return r1,r2



def test():
    # 创建一个简单的DataFrame
    df = pd.read_excel("output.xlsx")

    # 假设我们要添加的数据是一个新的列
    new_column_data = ["X", "X", "XXX"]
    df['CC1'] = new_column_data

    # 将更新后的DataFrame保存回Excel文件，这里使用原来的文件名和路径
    df.to_excel("output.xlsx", index=False)





if __name__ == "__main__":
    main()
