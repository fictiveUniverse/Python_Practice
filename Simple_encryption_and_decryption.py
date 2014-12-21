input = raw_input("Enter Message:")

encrypted_text = ""
plain_text = ""
for c in input:
    x = ord(c)  # ord get the ascii value
    x = x + 7  # add 7 to the Ascii
    c2 = chr(x)  # convert back to character
    encrypted_text = encrypted_text + c2
print("Encrypted Message: " + encrypted_text)

for i in encrypted_text:
    x = ord(i)
    x = x - 7
    c2 = chr(x)
    plain_text = plain_text + c2
print("Decrypted Message: " + plain_text)


