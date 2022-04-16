import re
s = """Hello from student1@jsm.com
to CSstudent2@gmail.com about the meeting @2PM"""
lst = re.findall('\S+@\S+', s)
print(lst)