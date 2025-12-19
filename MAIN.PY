from igbo import igbo
from hausa import hausa
from egbira import egbira
from tiv import tiv
from yoruba import yoruba

print("COS 101 LANGUAGE TRANSLATOR")
print("1. Igbo")
print("2. Hausa")
print("3. Egbira")
print("4. Tiv")
print("5. Yoruba")

choice = input("Choose language (1-5): ")
word = input("Enter English word: ").lower()

if choice == "1":
    print(igbo.get(word, "Word not found"))
elif choice == "2":
    print(hausa.get(word, "Word not found"))
elif choice == "3":
    print(egbira.get(word, "Word not found"))
elif choice == "4":
    print(tiv.get(word, "Word not found"))
elif choice == "5":
    print(yoruba.get(word, "Word not found"))
else:
    print("Invalid choice")
