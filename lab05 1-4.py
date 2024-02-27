#Q1.1
list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)
#Q1.2
list1 = ["M", "na", "i", "Ke"] 
list2 = ["y", "me", "s", "lly"]
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)
#Q2.1
numbers = [1, 2, 3, 4, 5, 6, 7]
res = []
for i in numbers:
    res.append(i * i)
print(res)
#Q2.2
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

res = [x + y for x in list1 for y in list2]
print(res)
#Q3.1
dict1 = {'Ten': 10, 'twenty':20, 'thirty':30}
dict2 = {'thirty': 30, 'forty':40, 'fifty':50}
dict3 = {**dict1, **dict2}
print(dict3)
#Q3.2
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict['class']['student']['marks']['history'])
#Q3.3
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

res = dict.fromkeys(employees, defaults)
print(res)

print(res["Kelly"])
#Q4.1
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])

#Q4.2
tuple1 = (10, 20, 30, 40)
a, b, c, d = tuple1
print(a)
print(b)
print(c)
print(d)
#Q4.3
tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1, tuple2 = tuple2, tuple1
print(tuple2)
print(tuple1)



