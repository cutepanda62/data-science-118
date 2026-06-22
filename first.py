#1.waf to remove last word from  string
#2.waf to remove words if vawel present from string
#3.waf to 
str1="This is python code in vs"
#4.wof to extract only numbers for string
str1="This is python code in vs version-35 address noida-11096"


text="This is python code in vs"
def remove_last_word(s):
    words = s.split()
    return " ".join(words[:-1])

print(remove_last_word(text))