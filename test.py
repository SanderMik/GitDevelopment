# Het spel steen, papier en schaar (Voor het eerst uitgewerkt (werkend))

from random import choice

user = input("Kies een wapen (steen, papier of schaar): ")
comp = choice(["steen", "papier", "schaar"])

print("De gebruiker (jij) koos", user)
print("De computer (ik) koos", comp)

if user == "steen" and comp == "papier":
    print("Haha! Eigenlijk koos ik papier! Ik heb gewonnen!")
elif user == "schaar" and comp == "papier":
    print("Je had mij door...")
elif user == "steen" and comp == "schaar":
    print("Je had mij door...")
elif user == "papier" and comp == "schaar":
    print("Haha! Eigenlijk koos ik schaar! Ik heb gewonnen!")
elif user == "papier" and comp == "steen":
    print("Je had mij door...")
elif user == comp:
    print("Het is gelijkspel!")
else:
    print("Haha! Eigenlijk koos ik steen! Ik heb gewonnen!")

# print("Hopelijk heb je de volgende keer meer geluk...")


