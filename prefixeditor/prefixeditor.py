import os


def main():
    prefixchanged = False
    #get the directory from user input
    directory = input("Enter the directory: ")

    #get the previoud prefix from user input
    oldprefix = input("Enter the target prefix: ")

    #get the new prefix from user input
    newprefix = input("Enter the new prefix: ")


    #alter correct files in the directory to the new prefix
    for filename in os.listdir(directory):
        if filename.startswith(oldprefix):
            os.rename(os.path.join(directory, filename), os.path.join(directory, filename.replace(oldprefix, newprefix)))
            prefixchanged = True
        else:
            print("No files with the prefix " + oldprefix + " found in the directory " + directory)


    if prefixchanged:
        print("Prefixes '" + oldprefix + "' successfully changed to '" + newprefix + "' in the directory '" + directory + "'")


main()



if __name__ == "__main__":
    main()