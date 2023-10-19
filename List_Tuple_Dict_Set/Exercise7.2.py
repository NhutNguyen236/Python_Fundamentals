string = "I am a teacher and I love to inspire and teach people"

# convert a string into a list 
list = string.split()

count_dict = [[element, list.count(element)] for element in list]

only = []
print(count_dict)

for i in count_dict:
    if(i[1] == 1):
        only.append(i[0])
        
print(only)