


with open("bean/ResidentStudentVo.java", "r", encoding="utf-8") as f:
    Vo = f.read()

with open("bean/TurnInterStdPlan.java", "r", encoding="utf-8") as f:
    Do = f.read()

VoDict = {}
for row in Vo.split("\n"):
    if row.startswith("    private"):
        rl = row.replace("    private ", "").replace(";", "").split(" ")
        VoDict[rl[1]] = rl[0]

DoDict = {}
for row in Do.split("\n"):
    if row.startswith("    private"):
        rl = row.replace("    private ", "").replace(";", "").split(" ")
        DoDict[rl[1]] = rl[0]


for k,v in DoDict.items():
    if k in VoDict:
        if DoDict[k] != VoDict[k]:
            print(k, VoDict[k], DoDict[k])

