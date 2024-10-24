# Open the file with UTF-8 encoding
with open('kiosk2.txt', 'r', encoding='utf-16') as file:
    text = file.readlines()

# Print the contents
print(type(text))
print(text)

i = 1
suma = 0
strsuma = 0
zamsuma = 0
centsuma = 0
print(type(text[i]))
while i < len(text):
    nla = text[i].split("\t")
    suma = suma + int(nla[4])
    if str(nla[5]) == "Стрийська":
        strsuma = strsuma + int(nla[4])
    elif str(nla[5]) == "Замарстинівська":
        zamsuma = zamsuma + int(nla[4])
    elif str(nla[5]) == "Замарстинівська":
        centsuma = centsuma + int(nla[4])
    i = i + 1
print(strsuma)
print(zamsuma)
print(centsuma)
print(suma)
