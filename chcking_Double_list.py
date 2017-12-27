mylist=["habibi","ahmed","majid","khalid","immad","choyee","kammo","maryam","rajjo","shahzad","Ali"]
'''friends_list=[]
for friends_list in mylist:
    if "a" in mylist:
        friends_list.append(mylist)
    else:
        print("you dont have a name which start with a")'''
############################or############################
print([x for x in mylist if x[0].lower()=="a"])

