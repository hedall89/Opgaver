
#Opgave 1a)
List = [5,6,8,9,10,11,13,18,19,20]
print(len(List))
print(type(List))

#opgave 2a)

def ListSortUE(List):

 var_uligetal = [tal for tal in List
                 if tal % 2 == 1]
 var_ligetal = [tal for tal in List
                if tal % 2 == 0]
 return var_uligetal, var_ligetal



print(ListSortUE(List))

