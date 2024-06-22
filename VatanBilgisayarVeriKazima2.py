# Gerekli Kütüphanelerin Yüklenmesi
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Kazıma işlemi sonucunda, verilerimi bir tabloya kaydetmek istiyorum. Excel formatında dışarı çıkartacağım.
# Bu işlem için, for döngüsü sonucunda çıkan değerleri boş bir listeye kaydetmem gerekiyor.
LaptopModels = []
LaptopIsims = []
LaptopFiyats = []
LaptopYildizs = []
LaptopYorumSayisis = []

for sayfa in range(1, 12):
    
    print(f"{sayfa}. sayfanın veri kazımasına başlanıyor...")
    time.sleep(2)
    
    Url = f"https://www.vatanbilgisayar.com/notebook/?page={sayfa}"
    Response = requests.get(Url)
    # print(Response) Response 200 döndü. Olumlu dönüş.
    Soup = BeautifulSoup(Response.text, "html.parser")
    AnaTablo = Soup.find("div", {"class": "wrapper-product wrapper-product--list-page clearfix"}).find_all("div", {"class": "product-list product-list--list-page"})
    # AnaTablo ile, çekmek istediğim veriler liste halinde. For ile hepsinin içerisinde girip, verileri kazıyabilirim.

    for i in AnaTablo:
        
        LaptopModel = i.find("div", {"class": "product-list__content"}).find("a", {"class": "product-list__link"}).find("div", {"class": "product-list__product-code"}).text.strip()
        LaptopIsim = i.find("div", {"class": "product-list__content"}).find("a", {"class": "product-list__link"}).find("div", {"class": "product-list__product-name"}).text.strip()
        LaptopFiyat = i.find("div", {"class": "product-list__content"}).find("div", {"class": "product-list__cost"}).find("div", {"class": "productList-camp"}).find("span", {"class": "product-list__price"}).text.strip()
        LaptopFiyat = LaptopFiyat.replace(".","")
        LaptopFiyat = int(LaptopFiyat)
        LaptopYildiz = i.find("div", {"class": "product-list__content"}).find("div", {"class": "wrapper-star"}).find("span", {"class": "score"})
        LaptopYildiz = LaptopYildiz["style"].split(":")[1].replace(";","").strip()
        LaptopYorumSayisi = i.find("div", {"class": "product-list__content"}).find("div", {"class": "wrapper-star"}).find("a", {"class": "comment-count"}).text.strip().replace("(","").replace(")","")
        if LaptopYildiz == "100%":
            LaptopYildiz = "5"
        elif LaptopYildiz == "80%":
            LaptopYildiz = "4"
        elif LaptopYildiz == "60%":
            LaptopYildiz = "3"
        elif LaptopYildiz == "40%":
            LaptopYildiz = "2"
        elif LaptopYildiz == "20%":
            LaptopYildiz = "1"
        elif LaptopYildiz == "0%":
            LaptopYildiz = "0"
        LaptopModels.append(LaptopModel)
        LaptopIsims.append(LaptopIsim)
        LaptopFiyats.append(LaptopFiyat)
        LaptopYorumSayisis.append(LaptopYorumSayisi)
        LaptopYildizs.append(LaptopYildiz)
    
    print(f"{sayfa}. sayfanın veri kazıması bitti...")
    time.sleep(2)
     
Df = pd.DataFrame({
    "Laptop Modeli": LaptopModels,
    "Laptop İsmi" : LaptopIsims,
    "Laptop Fiyatı": LaptopFiyats,
    "Laptop Yorum Sayısı": LaptopYorumSayisis,
    "Laptop Yıldızı": LaptopYildizs
})

excel_adi = "C:/Users/Mehmet Akif/Desktop/vatan_laptop_verileri.xlsx"
Df.to_excel(excel_adi, index=False)
    
    
    
    
    
    

