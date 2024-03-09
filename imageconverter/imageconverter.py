from PIL import Image

def main():
    imagefile = input("Enter the name of the image file you want to convert: ")
    if imagefile[-1] ==  'g':
        input("PNG detected, press enter to convert to JPG...")
        img = Image.open(imagefile)
        img.save(imagefile.replace("png", "jpg"))
        print("Image converted to JPG")
    elif imagefile[-1] == 'g':
        input("JPG detected, press enter to convert to PNG...")
        img = Image.open(imagefile)
        img.save(imagefile.replace("jpg", "png"))
        print("Image converted to PNG")    
    else:
        print("Image file must be either a PNG or JPG")
        main()
main()





if __name__ == "__main__":
    main()



