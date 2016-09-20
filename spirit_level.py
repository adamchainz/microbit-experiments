from microbit import Image, accelerometer, display


def main():
    while True:
        x = normalize(accelerometer.get_x())
        y = normalize(accelerometer.get_y())
        image = generate_image(x, y)
        display.show(image)


def normalize(value, width=200):
    value = max(-width, min(width, value))
    return value / (width * 2)


def generate_image(x, y):
    image = grid(5, 5)
    x_pixel = int((x * 2) + 2)
    y_pixel = int((y * 2) + 2)
    image[y_pixel][x_pixel] = 9
    return imageify(image)


def grid(width, height):
    return [
        [0 for _ in range(width)]
        for __ in range(height)
    ]


def imageify(image):
    string = ''
    for line in image:
        string += ''.join(str(x) for x in line)
        string += ':'
    return Image(string)


if __name__ == '__main__':
    main()
