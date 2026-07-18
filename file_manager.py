# DG AI File Manager System


def save_file(filename, content):

    file = open(filename, "w")

    file.write(content)

    file.close()


    print("File saved:", filename)



def read_file(filename):

    try:

        file = open(filename, "r")

        data = file.read()

        file.close()


        return data


    except:

        return "File not found"



def delete_file(filename):

    import os


    if os.path.exists(filename):

        os.remove(filename)

        print("File deleted:", filename)


    else:

        print("File does not exist")
