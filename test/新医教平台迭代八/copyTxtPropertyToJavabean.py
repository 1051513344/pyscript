





if __name__ == "__main__":

    with open("bean/ResidentStudentVo.java", "r", encoding="utf-8") as f:
        Vo = f.read()

    rows = Vo.split("\n")

    with open("bean/ResidentStudentIdTxtConvert.java", "w", encoding="utf-8") as f:
        for row in rows[:15]:
            f.write(row.replace("ResidentStudentVo", "ResidentStudentIdTxtConvert") + "\n")

        for row in [r for r in rows if r.startswith("    private ")]:
            if row.endswith("Txt;"):
                f.write(row.replace("Txt;", ";") + "\n\n")
                f.write(row + "\n\n")

        f.write("}")

