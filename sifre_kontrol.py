# Kullanıcıdan şifre alma ve temel güvenlik kontrolü

sifre = input("Lütfen test etmek istediğiniz şifreyi girin: ")

# Şifre uzunluğunu len() fonksiyonu ile kontrol ediyoruz
if len(sifre) < 8:
    print("Zayıf Şifre: Şifreniz en az 8 karakter uzunluğunda olmalıdır.")
elif "123" in sifre or "admin" in sifre:
    print("Zayıf Şifre: Şifreniz '123' veya 'admin' gibi kolay tahmin edilen ifadeler içeremez.")
else:
    print("Güçlü Şifre: Temel güvenlik kriterlerini sağlıyor.")
