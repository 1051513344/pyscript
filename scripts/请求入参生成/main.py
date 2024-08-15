













if __name__ == "__main__":

    import json
    # params = ""
    # with open("params.txt", "r", encoding='utf-8') as f:
    #     params = f.read()
    #
    # dict = {}
    # for i in params.split("\n"):
    #     if ": " in i:
    #         dict[i.split(": ")[0]] = i.split(": ")[1]
    #     else:
    #         pass
    # # dict['month'] = 2
    # # dict['nurseGroupId'] = "955c74b1c1d94b768fede92babaf4494"
    # # dict['qcPlanId'] = "e0a57d78b43b478cb50a58ac2844541c"
    # # dict['wardId'] = "beb0087e54354baa9305a4067bd4b14e"
    # print(json.dumps(dict, ensure_ascii=False))


    dict = {}
    classTxt = ""
    with open("class.java", "r", encoding='utf-8') as f:
        classTxt = f.read()

    propertyList = [i for i in classTxt.split("\n") if i.startswith("    private")]

    for property in propertyList:
        field = property.split(" ")[-1].replace(";", "")
        dict[field] = "1"

    print(json.dumps(dict))







