#DSA-Assgn-1

def merge_list(list1, list2):
    merged_data=""
    list2.reverse()
    for i in range(len(list1)):
        if(list1[i] is not None):
            merged_data=merged_data+list1[i]
        if(list2[i] is not None):
            merged_data=merged_data+list2[i]
        merged_data+=' '
    #write your logic here
    resultant_data=merged_data.strip()
    return resultant_data

#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)

    

print(merged_data)
