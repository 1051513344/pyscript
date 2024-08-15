


if __name__ == "__main__":
    import re
    with open("view.sql", "r", encoding='utf-8') as f:
        view = f.read()
    column_nums = []
    for row in view.split("\n"):
        if row.startswith("select ") and row.endswith(" from dual"):
            row_ = row.replace("select ", "")
            # print(row_)
            # print(re.findall("  ", row_))
            column_num = len(re.findall("  ", row_))
            if column_num == 25:
                print(row_)
            # column_num = len(re.findall("\w+,|\w+ from dual", row_))
            if column_num not in column_nums:
                column_nums.append(column_num)
    print(column_nums)