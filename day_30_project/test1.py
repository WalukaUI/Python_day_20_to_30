fruits = ["apple", "cherry", "coco"]

def make_pie(idx):
    try:
        fruit = fruits[idx]
    except IndexError as err:
        print(f"{err} sdfsf")
    else:
        print(fruit + " pie")


make_pie(2)