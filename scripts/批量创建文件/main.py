# -*- coding: gbk -*-


method = "getBedsByGroup"
methodName = "��ȡ��λ���鲡��"
methodNameMethod = f'{methodName}{method}'


def main():
    with open(methodNameMethod+".txt", "w") as f:
        f.write('')
    with open(f"{methodNameMethod} - sql��ѯ.txt", "w") as f:
        f.write('')
    with open(f"{methodNameMethod} - json����.txt", "w") as f:
        f.write('')


if __name__ == "__main__":

    main()