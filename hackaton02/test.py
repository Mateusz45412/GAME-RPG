# def menu():
#     new = input("czy chcesz rozpocząć nową grę y/n ?").lower()
#     if new == "y":
#         print("Nowa gra")
#     elif new == "n":
#         conti = input("chcesz kontynuować grę y/n ?").lower()
#         if conti == "y":
#             pass
#         elif conti == "n":
#             print("Koniec gry")
import energy_module
start_energy = 100
energy = 100
energy_module.energies(energy, start_energy)
