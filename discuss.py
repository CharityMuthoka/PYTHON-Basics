#ask the user to enter marks
maths=float(input("Enter maths marks:"))
eng=float(input("Enter english marks:"))
kisw=float(input("Enter Kiswahili marks:"))
geo=float(input("Enter geography marks:"))

#Calculate the average
total=maths+eng+kisw+geo
avg=total/4

#determine the grade
if 0<= avg<=39:
    grade="D"

elif 40<=avg<60:
    grade="C"

elif 60<=avg<80:
    grade="B"

elif 80 <= avg <= 100:
    grade = "A"

else:
    grade = "Invalid"

    #print the results
    print(f"Average is{avg}")
    print(f"Your grade is {grade}")