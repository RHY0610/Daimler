# -*- coding: utf-8 -*-
def search(li,item):
  
  mid = len(li)//2
  if len(li)==0:
    return False
  if item == li[mid]:
    return True
  elif item > li[mid]:
    return search(li[mid+1:],item)
  else:
    return search(li[:mid],item)

if __name__ == '__main__':
   while(True):
        print('Please input your array:')
        x = input()
        xlist = x.split(",")
        xlist = [int(xlist[i]) for i in range (len(xlist))] 
        xlist.sort()
        print(xlist)
        print("Tell me which number do you want:")
        num = input()
        a=search(xlist,int(num))
        print(a)
    