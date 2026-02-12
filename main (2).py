a={
    "name": ["Ravi","anu","ammu"," bharani"],
     "roll":["45","56","46","58",]
}
int= input(" enter name to search ")
if int in a["name"]:
    place=a[" name"].index( int)
    print("name found")
    print("rollno",a[" roll"][place])
else:
   print(" not found")
   b= input(" enter roll number ")
   a["name"].append (int)
   a["roll"].append(b)
   print("data added ")
   print(a)