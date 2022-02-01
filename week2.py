Places = ["SF", "Greece", "Canada", "Amsterdam", "LA"]
print(Places)#Prints list in original state
print(sorted(Places))#Prints list in alphabetical order
print(sorted(Places, reverse=True))#Prints list in reverse alphabetical order
print(Places)#prints in original state to show not permanently sorted
Places.reverse()#Reverses the original list
print(Places)#Prints the list now reversed
Places.reverse()#Reverses the list to the original
print(Places)#Prints the list reversed again 