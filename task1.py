# 1.1
a = "My name is WEIWEI."
print(a)
print("-" * 60)

# 1.2
print(a[0])
print("-" * 60)

# 1.3
print(a[-1])
print("-" * 60)

# 1.4
print(a[4:10])
print("-" * 60)

# 1.5
print(a.lower())
print("-" * 60)

# 1.6
b = "tutu on the tuki-kata."
print(b.replace("tu", "ta"))
print("-" * 60)

# 1.7
# Predict output: 0    
string = "Hello world!"
position = string.find("a")
print(position)  
# Actual output: -1
# Reason: The character "a" is not found in the string, so find() returns -1.
print("-" * 60)

#1.8
# Predict output: jhfdb -> jhfdb -> bdfhj -> hj
p = "abcdefghij"
print(p[::-2][:5][::-1][3:])
print("-" * 60)

#1.9
p = "abcdefghij"
step1 = p[::-2]
step2 = step1[:5]
step3 = step2[::-1]
step4 = step3[3:]
print(step1, "->", step2, "->", step3, "->", step4)
print("-" * 60)

#1.10
print(a * 10)
print("-" * 60)

#1.11
print("hello" + str(42))
print("-" * 60)