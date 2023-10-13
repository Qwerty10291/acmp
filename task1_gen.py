from random import randint, choice


with open(input("введите название файла:"), "w") as file:
    ids = sorted(set(randint(1, 10000000) for _ in range(1000000)))
    cards = list(set(randint(1, 50000000) for _ in range(2000000)))[:len(ids)]
    for i in range(50):
        print(choice(ids))
    file.write("\n".join(f"{i} {c}"  for i, c in zip(ids, cards)))