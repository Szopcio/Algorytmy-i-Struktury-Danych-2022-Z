def zad4(imie, nazwisko, zad2):
    return zad2(imie, nazwisko)

def zad2(imie, nazwisko):
    nazwa = (imie[0].capitalize() + ". " + nazwisko.capitalize())
    return nazwa


imie = ("jan")
nazwisko = ("kowalski")

print(zad4(imie, nazwisko, zad2))
