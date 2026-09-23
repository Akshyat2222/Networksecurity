import hashlib
text = "Hi how are you"
with open("message.txt","w") as file:
    file.write(text)
original_hash = hashlib.sha256(text.encode()).hexdigest()
with open("original_hash","w") as file:
   file.write(original_hash)

reciever_message = "Hi how are you"
reciever_hash = hashlib.sha256(reciever_message.encode()).hexdigest()

if original_hash == reciever_hash:
    print("Message is Not altered")
else:
    print("Message is altered")
