import PIL.Image

#Our ASCII characters
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";"]

#Resize image to fit the ASCII characters
def resize_image(image, new_width=100):
    width, height = image.size
    new_height = int(new_width * (height / width))
    resize_image = image.resize((new_width, new_height))
    return (resize_image)

#Convert each pixel to grayscale
def graytify(image):
    grayscale_image = image.convert("L")
    return (grayscale_image)

#Convert each pixels to ASCII characters
def covert(image):
    new_image = resize_image(image)
    new_image = graytify(image)
    pix = new_image.load()
    #create a grid of ASCII characters that coresponding to the image size
    ascii_image = []  
    for i in range(new_image.height):
        ascii_image.append(["X"] * new_image.width)

    #populate grid with ASCII characters
    #so bassically it checks for the the brightness of the picture and give the corresponding ASCII character
    for y in range(image.height):
        for x in range(image.width):
            if pix[x, y] == 0:
                ascii_image[y][x] = "@"
            elif pix[x,y] in range(1,100):
                ascii_image[y][x] = "X"
            elif pix[x,y] in range(100,200):
                ascii_image[y][x] = "#"
            elif pix[x,y] in range(200,300):
                ascii_image[y][x] = "S"
            elif pix[x,y] in range(300,400):
                ascii_image[y][x] = "%"
            elif pix[x,y] in range(400,500):
                ascii_image[y][x] = "?"
            elif pix[x,y] in range(500,600):
                ascii_image[y][x] = "*"
            elif pix[x,y] in range(600,700):
                ascii_image[y][x] = "+"
            elif pix[x,y] in range(700,750):
                ascii_image[y][x] = ";"
            else:
                ascii_image[y][x] = " "    
    return ascii_image


def main():
    path = input("Enter the path of the image: ")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "not valid to convert to ASCII")

    ascii_image = covert(image)


    with open("ascii_image.txt", "w") as f:
        for row in ascii_image:
            f.write("".join(row) + "\n")

main()