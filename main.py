a = str(input("Enter a word "))
char = str(input("Enter a alphabet "))
i = 0
count = 0
while i<len(a):
    if a[i]==char:
        count = count+1
    i = i+1
print(count)       