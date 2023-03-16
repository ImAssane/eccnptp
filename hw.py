#!/bin/python3
print("Welcome To Empire CyberSecurity \n")
print("Our Certfications: \n")
print("Ethical Hacking e Pentest \n")
print("Web Application Penetration Test \n")
print("Network Pentesting Advanced \n")
print("Network Defender \n")
print("Web Application Defender")
print("\n"*5)
print("All certifications costs 13500 \n")

name=input("Enter your Full name \n")
age=int(input("Enter your age \n"))

if(age<18):
 print("Sorry, But You are not old enough to do this certification")
else:
 curso=input("Enter the Certification \n")
 money=input("Enter the fee you paid (MZN) \n")
 print("")
 if(money>="13500"):
  print("CONGRATULATIONS "+ name+ ", You've paid the first month fee " +money+" Meticais "+"for the Certification:"+curso)
  
 else:
  print(name+"You haven't paid this Certification's first month fee, please do it")
  
print("_"*100)
