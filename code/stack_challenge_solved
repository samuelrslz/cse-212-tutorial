tortillas = [1, 2, 3]   # The tortillas' stack with three initial tortillas.

def make_tortilla(tortillas):
    if len(tortillas) == 0:
        new_tortilla = 1
    else:
        new_tortilla = len(tortillas) + 1
    tortillas.append(new_tortilla)   # Append will add at the top of the stack.

def take_tortilla(tortillas):
    if len(tortillas) == 0:
        print("There are no tortillas left.")
    else:
        return tortillas.pop()   # When we use pop() we're also deleting the last item.


### TESTS ###

make_tortilla(tortillas)
make_tortilla(tortillas)
print(tortillas) # [1, 2, 3, 4, 5]
top_tortilla = take_tortilla(tortillas)
print(top_tortilla) # 5
print(tortillas) # [1, 2, 3, 4]
take_tortilla(tortillas)
take_tortilla(tortillas)
take_tortilla(tortillas)
take_tortilla(tortillas)
take_tortilla(tortillas) # Message saying that there are no tortillas left.