from englisttohindi.englisttohindi import EngtoHindi
 
# message to be translated
# message = "Yes, I am geeks"
message = input("Enter value to change to hindi: ")
 
# creating a EngtoHindi() object
res = EngtoHindi(message)
 
# displaying the translation
print(res.convert)