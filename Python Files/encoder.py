import codecs
import time
text = input("Enter the phrase that you want to encode in hexadecimal. ")
text2 = text.encode()
print(codecs.encode(text2,"hex"))
time.sleep(5)
