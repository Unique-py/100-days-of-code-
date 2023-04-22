Student_data ={
   "Harry":45,
   "Hermonie":100,
   "Ron":45,
   "Nevil":90
   }

for students in Student_data:
    score = Student_data[students]
    if score <90:
        Student_data[students] ="OS"
    elif score < 80:
        Student_data[students] = "OP"
    else:
        Student_data[students] ="OG"  
