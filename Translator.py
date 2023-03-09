from googletrans import Translator
sen = str(input('Enter the sentence :'))
Trans = Translator()
lang=str(input('your language:'))
convert =str(input('Language You Want To Convert:'))
output= Trans.translate(sen,src=lang,dest=convert)
print(output.text)