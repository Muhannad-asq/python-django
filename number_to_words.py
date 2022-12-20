from num2words import num2words

print(num2words(36))

# Other variants, according to the type of article.
print(num2words(1000100, to = 'ordinal'))
print(num2words(36, to = 'ordinal_num'))
print(num2words(36, to = 'year'))
print(num2words(36, to = 'currency'))

# Language Support.
print(num2words(36, lang ='es'))
