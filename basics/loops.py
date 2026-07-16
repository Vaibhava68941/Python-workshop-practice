#list -> data structure that can hold multiple values of multiple types
#array -> data structure that can hold multiple values of the same type
list_of_cloud = ["AWS", "Azure", "GCP", "Digital Ocean", "Oracle Cloud", "IBM Cloud"]

print(list_of_cloud)

#added alibaba at the end of the list
list_of_cloud.append("Alibaba Cloud")

print(list_of_cloud)

#added salesforce cloud at index 3
list_of_cloud.insert(3, "Salesforce Cloud")

print(list_of_cloud)
print(len(list_of_cloud))  

for cloud in list_of_cloud:
    print(" ")
    print(cloud)
    
for i in range(1,11):
    print(i)