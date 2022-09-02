from stegano import lsb
import getpass
inImgPNG = 'dog.png'
outImgPNG = 'secret.png'
msg = 'The quick fox jumped over the lazy dog'
username = input("Enter the username:")
passwd = getpass.getpass("Enter the password:")
lsb.hide(inImgPNG, message=msg).save(outImgPNG)
message = lsb.reveal(outImgPNG)

if username == "nova" and passwd == "kali":
    print(f"The hidden message is : {message}")
else:
    print("The pssword or the username is incorrect")


