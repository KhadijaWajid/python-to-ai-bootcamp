# message = "hello im akif"

# print(message[2])
# print(message[-1])

# print(message[0:5])

# print(message)

# # string_name[start : stop]

# # methods
# print(message.upper())
# print(message.title())

# st = "   a    "
# print(st.strip())
# print(st.lstrip())
# print(st.rstrip())

# print(message.replace("hello", "Hey!"))

# s = "a,b,c"
# print(s.split(","))



#practice
raw_course_title = "   python to ai bootcamp   "
cleaned_title = raw_course_title.strip().title()
tokens = cleaned_title.split()
new_title = cleaned_title.replace("Gdg", "GDG CUI Wah")

print("Cleaned:", cleaned_title)
print("Tokens:", tokens)
print("Replaced:", new_title)

marks_list = [45, 78, 92, 33, 88, 105, 60]
for mark in marks_list:
    if mark > 100:
        print(f"Skipping invalid mark: {mark}")
        continue  
    
    if mark >= 50:
        print(f"Mark: {mark} -> Status: Pass")
    else:
        print(f"Mark: {mark} -> Status: Fail")
















