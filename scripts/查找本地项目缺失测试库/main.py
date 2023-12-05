
import os

if __name__ == "__main__":

    for dir in os.listdir("D:\DataConfig"):
        if dir.startswith("NIS_"):
            with open(f"D:/DataConfig/{dir}/conf/resources.properties", "r", encoding="utf-8-sig", errors="ignore") as f:
                if "192.168.10.239:1521:orcl" not  in f.read():
                    print(dir)


