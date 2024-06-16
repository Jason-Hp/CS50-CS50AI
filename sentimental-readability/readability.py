# TODO
import cs50

counter = 0
space = 0
sent = 0

text = cs50.get_string("Text: ")
text = text.lower()

for i in range(len(text)):
    if text[i] > 'z' or text[i] < 'a' :
        counter += 1
    if text[i] == ' ':
        space += 1
    if text[i] == '.' or text[i] == '?' or text == '!':
        sent += 1

a = round(0.0588 * ((len(text)-counter)/(space+1)*100) - 0.296 * (sent/(space+1)*100) - 15.8)

if a < 1:
    print("Before Grade 1")
elif a > 16:
    print("Grade 16+")
else :
    print(f"Grade {a}")