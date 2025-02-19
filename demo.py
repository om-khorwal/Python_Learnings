import pandas as pd
import numpy as np
from collections import Counter,defaultdict
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
c=0
file = open('/home/om/file.txt','r')
content = file.read()
lines = content.split("\n")
words = content.split()

# for total lines,letters,words:
# a = len(words)
# c+=a
# print("total words",len(words))
# print("total lines",len(lines))
# print("total characters",c)

# wordfreq={}
# for word in words:
#     if word in wordfreq:
#      wordfreq[word]+=1
#     else:
#      wordfreq[word] = 1
# print(wordfreq)

letter={}
for word in words:
 for i in word:
   if i in letter:
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
# data = {
#     'Name' : [ 'Jon' , 'Marry' , 'Tani','Kin'],
#     'Age' : [20,50,40,34],
#     'Dep':['store','field','logistic',np.nan]
# }
# a = pd.DataFrame(data)

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

# b=a.fillna(0)
# c=a.dropna()
# print(c)

#used for merging of 2 dataframes
# df1 = pd.DataFrame({'Key': ['A', 'B'], 'Value': [100, 200]})
# df2 = pd.DataFrame({'Key': ['A', 'B'], 'Score': [50, 60]})

# merged_df = pd.merge(df1, df2, on='Key')
# print(merged_df)

#counter function
# s = ['red','blue','black','black','red','black','blue','blue']
# a = Counter(s) # it counts the total elements directly
# b = Counter(content)
# c = Counter(lines)
# d = Counter(words)
# for word in s:
#     a[word] += 1
# print(a)
# print(b)
# print(c)
# print(d)

# w = Counter('abracadabra').most_common(3) #return the most common elements as asked here are top 3 

# c = Counter(a=4, b=2, c=0, d=-2)
# sorted(c.elements()) #it will return the elements in the expanded format as order 

# c = Counter(a=4, b=2, c=10, d=-2)
# d = Counter(a=1, b=2, c=3, d=4)
# c.subtract(d)  #it will subtract from 2 data
# e=c.total() # it will make the total out of them
# print(c)

# c.total()                       # total of all counts
# c.clear()                       # reset all counts
# list(c)                         # list unique elements
# set(c)                          # convert to a set
# dict(c)                         # convert to a regular dictionary
# c.items()                       # access the (elem, cnt) pairs
# Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
# c.most_common()[:-n-1:-1]       # n least common elements
# +c                              # remove zero and negative counts

#using defaultdict to count people in departments

# data = [
#     {"Name": "Alice", "Department": "HR"},
#     {"Name": "Bob", "Department": "IT"},
#     {"Name": "Charlie", "Department": "HR"},
#     {"Name": "David", "Department": "IT"},
#     {"Name": "Eve", "Department": "Finance"},
# ]

# df = pd.DataFrame(data)
# dept_count = defaultdict(int)
# for dep in df['Department']:
#     dept_count[dep]+=1

# total = (list(dept_count.items()))
# print(pd.DataFrame(total))

#this is made without using defaultdict
# count_character = {}
# for w in content:
#     if w in count_character:
#      count_character[w] += 1
#     else:
#       count_character[w] =1
# print(count_character)

#this is made using default dict
 