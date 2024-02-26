import os
import time

from path import Path
from getch import pause
import tkinter as tk
from tkinter import filedialog
from tqdm import tqdm,trange

root = tk.Tk()
root.withdraw()

filetypes = (
        ('Text Files', '*.txt'),
        ('All files', '.')
    )

file_path = filedialog.askopenfilename(title='Lütfen Liste Dosyanızı seçiniz', filetypes=filetypes)


dosya = open(file_path, "r")
lines = dosya.readlines()
lsit = []

for line in lines:
    if not line.strip():
        continue
    lsit.append(line.replace("\n", ""))
dosya.close()

def fonksiyon(x):
    return list(dict.fromkeys(x))
mylist = list(dict.fromkeys(lsit))
print(mylist)

KAYNAK = "path"  # kaynak dosya
HEDEF = "path"  # hedef dosya

k = Path(KAYNAK)  # KAYNAK Adlı değişken string bir ifadedir . Bu ifadeyi Path tipine dönüştürüyoruz .
h = Path(HEDEF)  # HEDEF Adlı değişken string bir ifadedir . Bu ifadeyi Path tipine dönüştürüyoruz .

print("\n\nKAYNAK adlı değişkenin tipi : %s" % type(KAYNAK))
print("k adlı değişkenin tipi : %s " % type(k))

print("\n\nHEDEF adlı değişkenin tipi", type(HEDEF))
print("h adlı değişkenin tipi", type(h))

myliste = mylist



def transfer():
    print("\n\nDosyalar %s adresinden %s adresine kopyalanıyor !!\n" % (k, h))
    dosya_sayisi = 0
    for j in mylist:

        time.sleep(2)
        for i in k.walk():  # dizinin içindek dosyaları gez
            if i.isfile() and i.endswith(j): # eğer mevcut indiste bir  uzantılı dosya var ise
                if os.path.exists("{}\\{}".format(HEDEF, j)):
                    print("Dosya zaten mevcut : ", j)
                else:
                    dosya_sayisi += 1  # dosya sayısını artır
                    print("Kopyalanıyor %s" % i)
                    bar=tqdm(mylist)
                    bar.set_description("Kopyalanıyor {}".format(i))
                    time.sleep(1)
                    i.copy(h)  # hedefe mevcut indisteki  uzantılı dosyayı kopyala

                    if (dosya_sayisi == 0):
                        print("Mevcut dizinde  dosya bulunamadı ! ")
                    else:
                        print("\n%s adet dosya başarılı şekilde kopyalandı" % dosya_sayisi)
                    if (dosya_sayisi == 0):
                        print("Mevcut dizinde  uzantılı dosya bulunamadı ! ")
                    else:
                        print("\n%s adet dosya başarılı şekilde kopyalandı" % dosya_sayisi)



if __name__ == "__main__":
    if (os.path.exists(KAYNAK)):
        transfer()
    else:
        print("\n\nDosya Yolu Bulunamadı")

pause('Press Any Key To Exit.')
pause_exit(0, 'Press Any Key To Exit.')