import itertools as t
import pyfiglet
import colorama
from colorama import Fore, Back, Style

print(Fore.RED)
ascii_banner = pyfiglet.figlet_format("ARCHLİST")
print(ascii_banner)

print(Fore.RED)
print("Kişiye özel Wordlist oluşturma yazısına hoşgeldiniz.")
print(Fore.BLUE)
colorama.init(autoreset=True)
print("Kurban hakkında özel bilgileri girdiğinizde özel bir wordlist oluşturur.")
colorama.init(autoreset=True)
print(Fore.RED + Back.YELLOW + " Hiçbir şekilde sorumluluk kabul edilmemektedir.")
print(Style.RESET_ALL)
print(Fore.RED + Fore.CYAN	+ "Bu yazılım archzets tarafından kodlanmıştır.")

chars = input("Kurban Hakkında Bilgi :")
min = int(input("Kurban Hakkında Sayı Gir En Az :"))
max = int(input("Kurban Hakkında Sayı Gir En Fazla :"))
output = input("Dosya İsmi Giriniz :")

if output == "" or output is None:
    file = open(chars+".txt",'w')
else:
    file = open(output,'w')
if min == max:
    for i in range(min, max + 1):
        for a in t.product(chars, repeat= i):
            s = "".join(a)
            file.write(s+"\n")
        file.close()

elif min < max:
    for i in range(min, max + 1):
        for a in t.product(chars, repeat= i):
            s = "".join(a)
            file.write(s+"\n")
        file.close()
else:
    print("Maksimum tekrar, minimum tekrardan büyük olmalıdır")
    exit
if output == "" or output is None:
    print("Dosyayı adına göre kaydedildi :"+chars+".txt")
else:
    print("Dosyayı adına göre kaydedildi :"+output)
