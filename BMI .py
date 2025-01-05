H = float (input("enter the height in cm"))
W = float (input("enter the weight in kg"))
BMI = W / (H/100)**2
print (BMI)
if BMI <= 18.4 : 
    print ("underweight")
elif BMI <= 24.9 :
    print ("healthy")
elif BMI <= 29.9 :
    print ("overweight")
elif BMI <= 34.9 :
    print ("severly overweight")
elif BMI <= 39.9 :
    print ("obese")
else :
    print ("severly obese")


