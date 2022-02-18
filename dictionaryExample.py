ogrenciler = {
    '120' : {
        'ad': 'Ali',
        'soyad' : 'Yilmaz',
        'telefon' : '532 000 00 01'
    },
    '125' : {
        'ad': 'Can',
        'soyad' : 'Korkmaz',
        'telefon' : '532 000 00 02'
    },
    '128' : {
        'ad': 'Volkan',
        'soyad' : 'Yukselen',
        'telefon' : '532 000 00 03'
    }
}

studentNumber = input('Ogrenci numarasi giriniz : ')
print(ogrenciler[studentNumber])

newStudentNumber = input('Yeni ogrenci numarasi giriniz : ')
newStudentName = input('Yeni ogrenci adi giriniz : ')
newStudentSurname = input('Yeni ogrenci soyadi giriniz : ')
newStudentTelephoneNumber = input('Yeni ogrenci telefon numarasi giriniz : ')

ogrenciler[newStudentNumber] = {
    'ad' : newStudentName,
    'soyad' : newStudentSurname,
    'telefon' : newStudentTelephoneNumber
}

print(ogrenciler)