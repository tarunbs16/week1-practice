text = input("Enter text: ")

uppercase_count = 0
lowercase_count = 0
digit_count = 0
space_count = 0
other_count = 0

for char in text:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char.isspace():
        space_count += 1
    else:
        other_count += 1

print(f"\nUppercase Letters: {uppercase_count}")
print(f"Lowercase Letters: {lowercase_count}")
print(f"Digits: {digit_count}")
print(f"Spaces: {space_count}")
print(f"Other Characters: {other_count}")
