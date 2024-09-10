















if __name__ == "__main__":

    with open("NurseWorkExperienceDO.java", "r", encoding='utf-8') as f:
        DO = f.read()
    with open("InWorkRespDTO.java", "r", encoding='utf-8') as f:
        DTO = f.read()
    propertyForDOList = []
    for row in DO.split("\n"):
        if "private" in row:
            property = row.split(" ")[len(row.split(" ")) - 1][:-1]
            propertyForDOList.append(property)
    propertyForDTOList = []
    for row in DTO.split("\n"):
        if "private" in row:
            property = row.split(" ")[len(row.split(" ")) - 1][:-1]
            propertyForDTOList.append(property)
    propertyList = [p for p in propertyForDOList if p in propertyForDTOList]
    for p in propertyList:
        print(f"nurseWorkExperienceDO.set{p[0].upper()+p[1:]}(inWorkRespDTO.get{p[0].upper()+p[1:]}());")
        # print(f"empRespDTO.set{p[0].upper()+p[1:]}(nurseDossierDO.get{p[0].upper()+p[1:]}());")
