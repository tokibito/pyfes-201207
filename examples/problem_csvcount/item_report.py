# coding: utf-8
import csv


def main():
    f = open("items.csv")
    reader = csv.reader(f)
    count_data = {}
    for row in reader:
        name = row[1].decode('cp932')
        count = int(row[2])
        if name in count_data:
            count_data[name] += count
        else:
            count_data[name] = count
    f.close()
    for kv in count_data.items():
        print u"%s %d個" % kv

if __name__ == '__main__':
    main()
