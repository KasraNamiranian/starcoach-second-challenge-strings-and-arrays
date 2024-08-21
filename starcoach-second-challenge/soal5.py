import string
n= input()

def remove_punctuation(text):
    return text.translate(str.maketrans(string.punctuation,  ' ' * len(string.punctuation)))


clean_text = remove_punctuation(n)
words = clean_text.split()
filtered_words = [word for word in words if not word.isupper()]

t=0
for i in filtered_words:
    for j in i:
        if j not in ('a','e','i','o','u','y','A','E','I','O','U','Y'):
            t=t+1
            if t>=5:
                print(i,end=" ")
                break
        else:
            t=0
    t=0