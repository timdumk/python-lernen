print("Hello World")
age = int(input("How old are you? "))
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

for _ in range(3):
    print("Tim")
    films = ["hobbit", "star wars", "james bond"]
    print(films[1])
def add(a, b):
    print(a + b)
add(5, 7)
add(10, 15)

i=0
while i <= 10:
    print(i)
    i += 1  
films = []
films.append("The Matrix")
films.append("Inception")
films.append("Interstellar")

print(len(films))

