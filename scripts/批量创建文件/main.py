# -*- coding: gbk -*-


method = "getBedsByGroup"
methodName = "获取床位分组病人"
methodNameMethod = f'{methodName}{method}'


def main():
    with open(methodNameMethod+".txt", "w") as f:
        f.write('')
    with open(f"{methodNameMethod} - sql查询.txt", "w") as f:
        f.write('')
    with open(f"{methodNameMethod} - json出参.txt", "w") as f:
        f.write('')


if __name__ == "__main__":

    main()