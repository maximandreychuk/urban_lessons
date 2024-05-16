"""«Равные части»."""

stroke, l = input()
l = len(stroke)
print(f'{stroke[(l//2):l]}{stroke[0:l//2]}')