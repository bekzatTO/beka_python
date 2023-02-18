# import os,sys


# cwd = os.path.dirname(os.path.abspath(sys.argv[0]))

# my_file = os.path.join(cwd,"ids.txt")

# header=[]
# body=[]


# with open(my_file,"r") as red:
#     for i in red.read().splitlines():
#         if i.startswith("#"):
#             header.append(i)
#         elif i.startswith("/"):
#             body.append(i)

# d={}

# for i in body:
#     disk=i.split(":")[0].strip()
#     value=i.split(":")[1].strip()
#     d[disk]=value




# for k,v in d.items():
#     if k == "/dev/sda3":
#         disk3=v.split(",")
#     elif k == "/dev/sda4":
#         disk4=v.split(",")




# d3=disk3[1]
# d4=disk4[1]


# disk3[1]=d4
# disk4[1]=d3

# first=d4[0]
# second=d4[1]


# disk4.pop(0)

# disk4.insert(1,first)


# disk4[0]=disk4[0].replace("size","start").strip()
# disk4[1]=disk4[1].replace("start"," size")


# print(disk4)


# d["/dev/sda3"]=",".join(disk3)
# d["/dev/sda4"]=",".join(disk4)



# body=[]
# for k,v in d.items():
#     body.append(k+" : "+v)

# l=[""]
# t=''
# for i in header+l+body:
#     t+=i+"\n"




# with open("new.txt","w+") as w:
#     w.write(t)

# with open("new.txt","r") as r:
#     print(r.read())

# filename = __name__








# import start

# p1=start.Buy(2006,11,18,18,16)
# # print(p1.shirt_fit())

# print(dir(start))


fruit = ["apple","banana","peach"]
ppl=["Azat","Beka","Apa"]

# Zip allows you to loop multiple lists
for k,v in zip(fruit,ppl): 
    print(f"{v} likes to eat {k}")



