a = "AAAAA"
b = "BBBBB"
c = 1.1
string = "a = {nome1}, b = {nome2} e c = {nome3:.2f}"
formato = string.format(nome1=a, nome2=b, nome3=c)

print(formato)