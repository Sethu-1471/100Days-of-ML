import statistics;
print("---------------------------")
class Dataset:
    def add(a, b):
        return a+b

x = int(input("enter first number"))
y = int(input("enter second number"))
print(Dataset.add(x,y))

print("---------------------------")

a=[2,3,4,5,6,7,8,9,0,1]
b = statistics.mean(a)

print(b)
print("---------------------------")


