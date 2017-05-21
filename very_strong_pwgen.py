import string
from random import choice

letters = string.ascii_letters
specials = 'ÆÄØÖÅËÏÖÜŸÂÊÎÔÛŶÃẼĨÕŨỸæäøöåëïöüÿâêîôûŷãẽĩõũỹ'
digits = string.digits
symbols = string.punctuation
chars = letters + specials + digits + symbols

length = 64
password = "".join(choice(chars) for x in range(length))
print(password)


