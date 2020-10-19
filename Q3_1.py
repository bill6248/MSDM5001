count=0
with open("blocklist.txt", "r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        if re.search( r'blockID="[ig].*[0-9]"', line):
            count=count+1
            print(line)
