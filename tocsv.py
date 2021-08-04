"""

parse data like this that print from mysql cli to csv file

+----+---------+------------+------------+---------+---------------------+---------------------+
| id | user_id | product_id | pay_amount | status  | add_time            | last_update_time    |
+----+---------+------------+------------+---------+---------------------+---------------------+
| 19 |       1 |          1 |         20 | SUCCESS | 2021-02-04 11:28:36 | 2021-04-01 14:24:56 |
| 23 |       2 |          1 |          1 | SUCCESS | 2021-02-04 11:33:09 | 2021-02-04 11:33:09 |
| 24 |       2 |          1 |          1 | SUCCESS | 2021-02-04 11:34:51 | 2021-02-04 11:34:51 |
| 25 |       1 |          1 |          1 | SUCCESS | 2021-02-04 11:42:13 | 2021-02-04 11:42:18 |
| 26 |       2 |          1 |          1 | SUCCESS | 2021-02-04 11:42:18 | 2021-02-04 11:42:18 |
| 27 |       3 |          1 |          1 | SUCCESS | 2021-02-04 11:46:39 | 2021-02-04 11:46:39 |
| 28 |       1 |          1 |          1 | SUCCESS | 2021-02-04 11:47:01 | 2021-02-04 11:47:08 |
| 29 |       3 |          1 |          1 | SUCCESS | 2021-02-04 11:47:08 | 2021-02-04 11:47:08 |
| 30 |       2 |          1 |          1 | SUCCESS | 2021-02-04 11:47:08 | 2021-02-04 11:47:09 |
| 31 |       1 |          1 |          1 | SUCCESS | 2021-02-04 11:48:00 | 2021-02-04 11:48:22 |
+----+---------+------------+------------+---------+---------------------+---------------------+



"""
import csv
import re

headLineList = []
data = []
def readFile(originFilePath):
    with open(originFilePath, "r") as f:
        i = 0
        while True:
            line = f.readline()
            if not line:
                break
            matchObj = re.match(r'\+--', line)
            if matchObj:
                continue
            line_list = line.split("|")
            line_list = line_list[1:-1]

            if len(line_list) == 0:
                continue

            i += 1
            line_list_new = []
            for str in line_list:
                str = str.strip()
                if str == "NULL":
                    str = ""
                line_list_new.append(str)
            if i == 1:
                headLineList.extend(line_list_new)
            else:
                data.append(line_list_new)

def writeCsvFile(csvFilePath):
    with open(csvFilePath, "w") as csvfile:
        writer = csv.writer(csvfile)

        # 字段名称
        writer.writerow(headLineList)
        # 数据
        writer.writerows(data)

if __name__ == '__main__':

    originFilePath = "./data/data.txt"
    csvFilePath = "./data/data.csv"
    readFile(originFilePath)
    writeCsvFile(csvFilePath)
