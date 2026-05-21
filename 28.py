import colorsys
def rgb_to_hsl(r, g, b):
    r /= 255.0
    g /= 255.0
    b /= 255.0
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return int(h * 360), int(s * 100), int(l * 100)
r = int(input("Enter the red value (0-255): "))
g = int(input("Enter the green value (0-255): "))
b = int(input("Enter the blue value (0-255): "))
h, s, l = rgb_to_hsl(r, g, b)
print(f"HSL: ({h}, {s}%, {l}%)")