

with open("医保码表.txt", "r", encoding="utf-8") as f:
    txt = f.read()

for line in txt.split("\n"):
    if line.lower().startswith("dscg_way" + "	"):
        print(line)
        # p = line.split("\t")
        # print(p[0] + p[1] + "(" + "\"{}\"".format(p[1]) + ", " + "\"{}\"".format(p[2]) + "),")