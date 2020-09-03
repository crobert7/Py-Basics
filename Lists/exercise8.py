# break - example

print("Break instruction:")
for i in range(1,6):
    if i == 3:
        break
    print("In the loop.", i)
print("Out the loop.")

# continaue - example

print("\nContinue instruction:")
for i in range(1,6):
    if i == 3:
        continue
    print("In the loop", i)
print("Out the loop.")