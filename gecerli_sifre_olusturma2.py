import string


    
def gecerliSifre():
    
    while True:
        y=1
        sifre = input("Oluşturmak istediğiniz parolayı giriniz: ")
        if len(sifre) < 4:
            print( "Şifreniz çok kısa")
            y=0
        if not any(char.isdigit() for char in sifre):
            print( "Şifreniz sayı içermek zorundadır.")
            y=0
        if not any(char.isupper() for char in sifre):
            print( "Şifreniz büyük harf içermek zorundadır.")
            y=0
        if not any(char.islower() for char in sifre):
            print( "Şifreniz küçük harf içermek zorundadır.")
            y=0
        if not any(char in string.punctuation for char in sifre):
            print( "Şifreniz sembol içermek zorundadır.")
            y=0
        if y == 1:
            esb= "Bu şifreyi kullanabilirsiniz."
            print(esb)
            break
        
        
gecerliSifre()