'''s="emma is good girl, emma is a writer"
count=s.count("emma")
print(count)'''
def count_emma(statement):
    print("Given String: ", statement)
    count = 0
    for i in range(len(statement) - 1):
        count += statement[i: i + 4] == 'Emma'
    print(len(statement[i:i+4]))  
    #return count

count = count_emma("Emma is good developer. Emma is a writer")

print("Emma appeared ", count, "times")