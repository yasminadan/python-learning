#print("Goodbye World!")

#firstname = input("Enter your first name:")
#lastname = input("Enter your last name:")

#print("Your names are:" + firstname + lastname)

 nums = range(11)
num_list = list(nums)
#print(num_list)

nums2 = range(0,11,2)
num_list2 = list(nums2)
#print(num_list2)

index_listnames = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
index_list = enumerate(index_listnames, 10)
index_list_list = list(index_list)
#print(index_list_list)

names =  ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

names_map = map(str.upper, names)
names_map_list = list(names_map)
#print(names_map_list) 


