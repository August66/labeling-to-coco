import xml.dom.minidom

def getkey(filename):

    dir="/home/zbp/wzh_workspace/detction-benchmark/data/image/"

    dom=xml.dom.minidom.parse(dir+filename+".xml")
    root=dom.documentElement

    filenames=root.getElementsByTagName("filename")
    filename=filenames[0].firstChild.data
    #print(filename)

    x=[]
    y=[]
    x1=[]
    y1=[]
    names=[]
    name=root.getElementsByTagName("name")
    xmin=root.getElementsByTagName("xmin")
    ymin=root.getElementsByTagName("ymin")
    xmax=root.getElementsByTagName("xmax")
    ymax=root.getElementsByTagName("ymax")
    for i in range(len(name)):
        s=name[i].firstChild.data
        if ' ' not in s:
            names.insert(i, name[i].firstChild.data)
            x.insert(i, xmin[i].firstChild.data)
            y.insert(i, ymin[i].firstChild.data)
            x1.insert(i, xmax[i].firstChild.data)
            y1.insert(i, ymax[i].firstChild.data)

    # print(names)
    # print(x)
    # print(y)
    # print(x1)
    # print(y1)
    return names, x, y, x1, y1




import os
#提取文件夹下的地址+文件名，源文件设定排序规则
def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.jpg' or os.path.splitext(file)[1] == '.JPG':
                L.append( file)
    t = []
    for i in L:
        t.append(i.split('.')[0])
    return L, t
#print(file_name(dir))

def printf(str):
    dir = "/home/zbp/wzh_workspace/detction-benchmark/coco/"
    fh=open(dir+'classes.txt', 'a', encoding='UTF-8')
    fh.write(str+'\n')
    fh.close()

def printdata(str_image,str_cl_id,x,y,x1,y1):
    dir = "/home/zbp/wzh_workspace/detction-benchmark/coco/"
    fh = open(dir + 'annos.txt', 'a')
    fh.write(str_image)
    fh.write('*')
    fh.write('%d' %str_cl_id)
    fh.write('*')
    fh.write(x + '*')
    fh.write(y + '*')
    fh.write(x1 + '*')
    fh.write(y1 + '\n')
    fh.close()

# #提取类别
dir="/home/zbp/wzh_workspace/detction-benchmark/data/image"
l, t=file_name(dir)
names=[]
for i in t:
    name, _, _, _, _ =getkey(i)
    for j in range(len(name)):
        if name[j] not in names:
             #print(name[j])
             names.append(name[j])
            # printf(name[j])
print(names)

# #提取BBox 图片名字 classid x y x1 y2
for i in range(len(l)):
    str_image=l[i]

    name, x, y, x1, y1 = getkey(t[i])
    #print(name)
    for j in range(len(name)):
        str_cl_id=names.index(name[j])
        #printdata(str_image,str_cl_id,x[j],y[j],x1[j],y1[j])
