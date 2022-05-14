import time
hexstring = input("Enter hex string that you want to decode. ")
a_string = bytes.fromhex(hexstring)
a_string = a_string.decode("ascii")
print("The decoded string is "+a_string)
time.sleep(5)
