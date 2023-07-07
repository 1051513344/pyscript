


with open("EnrollApplyBo.java", "r", encoding="utf-8") as f:
    content = f.read()

lines = content.split("\n")


print("{")
for line in lines:
    if line.startswith("    private ") and not line.startswith("    private static final ") and not "Date" in line:
        if "Integer" in line:
            param = line.split(" ")[-1][:-1]
            print("    \"{}\": 1,".format(param))
        if "String" in line:
            param = line.split(" ")[-1][:-1]
            print("    \"{}\": \"\",".format(param))
        if "Double" in line:
            param = line.split(" ")[-1][:-1]
            print("    \"{}\": 0.0,".format(param))
print("}")
