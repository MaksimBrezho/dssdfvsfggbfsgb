import math
import matplotlib.pyplot as plt

def calculate_polygons(startx, starty, endx, endy, radius):
    sl = (2 * radius) * math.tan(math.pi / 6)
    p = sl * 0.5
    b = sl * math.cos(math.radians(30))
    w = b * 2
    h = 2 * sl
    endx = endx - w
    endy = endy - h
    origx = startx

    xoffset = b
    yoffset = 3 * p
    polygons = []
    row = 1

    while starty < endy:
        if row % 2 == 0:
            startx = origx + xoffset
        else:
            startx = origx
        while startx < endx:
            p1x = startx
            p1y = starty + p
            p2x = startx
            p2y = starty + (3 * p)
            p3x = startx + b
            p3y = starty + h
            p4x = startx + w
            p4y = starty + (3 * p)
            p5x = startx + w
            p5y = starty + p
            p6x = startx + b
            p6y = starty

            poly = [
                (p1x, p1y),
                (p2x, p2y),
                (p3x, p3y),
                (p4x, p4y),
                (p5x, p5y),
                (p6x, p6y),
                (p1x, p1y)]
            polygons.append(poly)

            startx += w
        starty += yoffset
        row += 1

    return polygons

def main():
    start_x = float(input("Введите начальную координату X: "))
    start_y = float(input("Введите начальную координату Y: "))
    end_x = float(input("Введите конечную координату X: "))
    end_y = float(input("Введите конечную координату Y: "))
    radius = float(input("Введите радиус: "))

    polygons = calculate_polygons(start_x, start_y, end_x, end_y, radius)
    for i, polygon in enumerate(polygons, 1):
        print(f"Шестиугольник {i}: {polygon}")
    fig, ax = plt.subplots()
    for polygon in polygons:
        poly = plt.Polygon(polygon, edgecolor='black', lw=2, fill=False)
        ax.add_patch(poly)

    plt.axis('equal')
    plt.show()

if __name__ == "__main__":
    main()
