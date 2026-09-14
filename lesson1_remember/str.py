s = "cat"
s = s.upper()
print(s)
s1 = "Hello"
s2 = 'Hello'
s3 = """ Line one
                       Line two """
print(s1)
print(s2)
print(s3)

#len() 123456      #index  - [] 012345
s = "Hello my group!"
print(len(s))
print(s[0])
print(s[14])
print(s[-1])

#slicing - my_string[start:end:step]
s1 = "Python"
print(s1[2:4])
print(s1[:4]) #from start to ind 4 exclusive
print(s1[4:]) #from ind 4 to the end of string
print(s1[:])
print(s1[::2]) #every 2 symbol
print(s1[::-1]) #reverse
print(s1[2:100])

name = "Helen"
last_name = "Paltiy"
age = 25
print(name+ " " +last_name + "-" + str(age))
print(f"Hi my name is {name} and my last name {last_name} and i`m {age}")


#upper() / lower()
raw = "  Automation QA   "
print(raw.upper())
print(raw.lower())

#strip
print(raw.strip())
print(raw.strip().upper())

#split() / join()
cvs_line = "Login:Cart,Checkout,Mama,Papa"
parts = cvs_line.split(",") #['Login:Cart', 'Checkout', 'Mama', 'Papa']
print(parts)
print(" - ".join(parts))

print()
#replace()
msg = "Test failed: element not found"
print(msg.replace("failed", "passed"))

#find() and index()
#find() -  -1 if substring is not found
#index - ValueError if substring is not found


s = "banana"
print(s.find("na"))
print(s.index("na"))

print(s.find("wer"))

#print(s.index("wer"))

#count()
print(s.count("na"))
















