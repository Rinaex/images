import os

def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            yield f

def main(txt,path):
    f = open(txt,'a')
    base = path
    for i in findAllFile(base):
        f.writelines(i+'\n')
        print(i)
    f.close()





if __name__ == '__main__':
    main('./pc.txt','./pc')
    main('./mobile.txt','./mobile')
