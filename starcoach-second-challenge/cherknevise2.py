import string

def replace_punctuation_with_space(sentence):
    # ایجاد یک جدول ترجمه برای جایگزین کردن علائم نگارشی با فاصله
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    # استفاده از جدول ترجمه برای جایگزین کردن علائم نگارشی
    new_sentence = sentence.translate(translator)
    return new_sentence

sentence = "سلام، من یک جمله هستم!"
print(replace_punctuation_with_space(sentence))