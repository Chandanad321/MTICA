##sample_set={"red","blue","green"}
##sample_list=["white","block","orange"]
##sample_set.update(sample_list)
##print(sample_set)
##
####unhansable type cannot be set member
####for i in sample_list:
###     sample_set.add(i)


set1={10,20,30}
set2={30,40,50}
set1.difference_update(set2)
print(set1)

