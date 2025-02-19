import pandas as pd
import numpy as np
# n= int(input("enter number"))
# a,b=0,1
# c=0

# iterative
# for _ in range(n):
#     print(a)  
#     c =a + b
#     a = b
#     b=c

#recursive 
# def func(a,b,c):
#     if c ==n:
#      return
#     print(a)
#     return func(b,a+b,c+1)
# func(a,b,c)

# FIzzBuzz
# for i in range (n):
#  if i%5==0 and i%3==0:
#    print("Fizz buzz")
#  elif i%5==0:
#     print("buzz")
#  elif i%3==0:
#     print("Fizz")
#  else:
#    print (i)

#reading file
# c=0
file = open('/home/om/file.txt','r')
content = file.read()
lines = content.split("\n")
words = content.split()
for i in words:
    a = len(i)
    c+=a
print("total words",len(words))
print("total lines",len(lines))
print("total characters",c)

wordfreq={}
for word in words:
    if word in wordfreq:
     wordfreq[word]+=1
    else:
     wordfreq[word] = 1
print(wordfreq)

letter={}
for word in words:
 for i in word:
   if i in letter.keys():
     letter[i] += 1
   else:
     letter[i] =1
print(letter)

#reading CSV data
# p = pd.read_csv('/home/om/data.csv')
# print(p.to_string())


#create series-1D data and dataframes-2D data 
# s = pd.Series([1,2,3,np.nan,5,7,9])
# s = [1,3,4,2,4,44]
# df= pd.DataFrame(s)
# print(df)
# listdata= [['a','b','v'],['c','d'],['e','f']]
# b = pd.DataFrame(listdata,columns=['X','Y','Z'])
# print(b)
data = {
    'Name' : [ 'Jon' , 'Marry' , 'Tani','Kin'],
    'Age' : [20,50,40,34],
    'Dep':['store','field','logistic',np.nan]
}
a = pd.DataFrame(data)

#Data to CSV file and Aditional parameters
# a.to_csv('output.csv', sep=',',index=False,header=False,columns=['Name','Age'])
# readnewfile = pd.read_csv('/home/om/output.csv')
# print(readnewfile)

# print(a[["Name",'Age']])
# print(a["Name"])

#Selecting data from database
# print(a.iloc[0]) ##getting data by position
# print(a[a['Age']>20]) #filter
# print(a.loc[1:2,['Name','Age']]) ##getting data by label and specific column

# b=a.sort_values(by='Age',ascending=False) #sorting the data
# print(b)

# c= a[a['Age']>20] #filtering the data
# print(c)

# a['c'] = a['Name'] + a['Dep'] #joining 2 columns
# print(a)

b=a.fillna(0)
c=a.dropna()
print(c)