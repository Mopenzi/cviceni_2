zamestnanci = ['František', 'Anna', 'Jakub', 'Klára']
print("Zaměstnanci na začátku: " + str(zamestnanci))
zamestnanci_a = zamestnanci.copy()
zamestnanci_a.extend(("Bruno", "Anežka"))
print("Nová jména přidána: " + str(zamestnanci_a))
zamestnanci_b = zamestnanci.copy()
zamestnanci_b.insert(1, "Bruno")
print("Nová jména vložena: " + str(zamestnanci_b))
