def zad2(imie, nazwisko):
    nazwa = (imie[0].capitalize() + ". " + nazwisko.capitalize())
    return nazwa

imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")

print(zad2(imie, nazwisko))
