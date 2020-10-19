count=0
with open("blocklist.txt", "r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        stat=0
        if 'blockID' in line:
            if re.search(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)',line):
                str='\/^'
                for i in str:
                    if i in line:
                        stat=1
                    else:
                        pass
                if stat==0:
                    print(line)
                    count=count+1
