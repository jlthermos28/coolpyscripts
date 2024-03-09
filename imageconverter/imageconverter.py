from PIL import Image
import os
def main():
    imagefile = input("Enter the path of the image (PNG or JPG) file you want to convert: ").strip('"')
    #PNG detected
    if imagefile[-2] ==  'n':
        input("PNG detected, press enter to convert to JPG...")
        img = Image.open(imagefile)
        rgb_im = img.convert('RGB')
        rgb_im.save(imagefile.replace("png", "jpg"))
        os.remove(imagefile) #remove the original PNG file
        print("Image converted to JPG")
    #JPG detected
    elif imagefile[-2] == 'p':
        input("JPG detected, press enter to convert to PNG...")
        img = Image.open(imagefile)
        img.save(imagefile.replace("jpg", "png"))
        os.remove(imagefile) #remove the original JPG file
        print("Image converted to PNG")    
    else:
        print("Image file must be either a PNG or JPG")
        main()
main()




#loop
if __name__ == "__main__":
    main()



