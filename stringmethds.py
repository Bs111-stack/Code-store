""" a=input()
print("my name is",a) """
b="uiui"#strings are immutable..
print(b.upper())#small to upper case of text...
c="HELLOs"
print(c.lower())
#rstrip is used to remove the unwanted content means it will not print..
h="quantum******"
print(h.rstrip("*"))
#if you want to replce the text like if written (a)and want i in the place of a use replace...
o="thy"
print(o.replace("thy","hyi"))
#split used to make a list..
l="my world is a good"
print(l.split(" "))
# want to capitalize the first letter of text use this... use capitalize,it also change all characters into lower case...
mnk="introduction To python"
print(mnk.capitalize())
#wanna to make text into center...
str="welcome to this course"
print(str.center(40))#40 is about the space in the front of starting character not applies to all characters...
#want to know how many times a character is repating in a variable or identifier..
ioi="harrry harrry harrry"
print(ioi.count("harrry"))
#if you want to know whether the charactrers are and with what....
nb=" welcoem vnn kwj ."
print(nb.endswith("-"))#if ends give true otherwise false..#same as startswith..
# want to find dthe index of a given text in the collection of characters..
robin="he is the the leader of this team"
print(robin.find("of"))
# want to know whether the characters is alphanumeric or not...
po="weLcometokiu"
print(po.isalnum())#alphanumeric means no spaces between characters...
#isalpha gives true or false if character has numbers gives false if no gives true...
rtr="welcome34"
print(rtr.isalpha())
#islower gives that your character is made of purely small character if yes gives true other wise false...
iop="hello iujjka"
print(iop.islower())#same as isupper
#isprintable shows whether the characters are printable or not if yes give true otherwise false when there is a unprintable character...
joi="hello my joi\n"#this is printable until i add any unwanted text like i write \n...
print(joi.isprintable())
#isspace tells only in true or false if there is any space or not but there is a condition it works only when there is no character only space space space..
zon="     "
print(zon.isspace())
#istitle uses when we want to know that our first letter of every character is capital or not if capital gives yes otherwise false
yoy="The Dora And The Boots "#gives true
print(yoy.istitle())
#swapcase changes upper case character into a lower case and lower case to upper case..
ror="hell world kese ho app sabhi log"
print(ror.swapcase())
#title used in a situation when we want our first letter of every charcters is lower case to upper case...
naruto="rashingun kamaihaamaii hey ya"
print(naruto.title())