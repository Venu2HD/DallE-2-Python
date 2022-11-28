from os import mkdir, getcwd, remove, listdir, name
from os.path import exists, isdir
from requests import get

def ensurefolders():
    if exists("Results") and isdir("Results"):
        pass
    else:
        mkdir("Results")
    if exists("temp") and isdir("temp"):
        pass
    else:
        mkdir("temp")

def saveimgoutput(image_binary:bytes, output_filename:str, save_output:bool):
    if save_output:
        if name == "nt":
            with open(f"Results\\{output_filename}", "wb") as output_file:
                output_file.write(image_binary)
        else:
            with open(f"Results/{output_filename}", "wb") as output_file:
                output_file.write(image_binary)
        if name == "nt":
            print(f"\nSaved output at: {getcwd()}\\Results\\{output_filename}")
        else:
            print(f"\nSaved output at: {getcwd()}/Results/{output_filename}")

def getimgoutput(url:str):
    return get(url = url).content

def savetextoutput(final_text:str, output_filename:str, save_output:bool):
    if save_output:
        if final_text.replace(final_text[4:], "") == "\n\n":
            final_text = final_text[4:]
        elif final_text.replace(final_text[2:], "") == "\n":
            final_text = final_text[2:]
        if name == "nt":
            with open(f"Results\\{output_filename}", "w") as output_file:
                output_file.write(final_text)
        else:
            with open(f"Results/{output_filename}", "w") as output_file:
                output_file.write(final_text)
        if name == "nt":
            print(f"\nSaved output at: {getcwd()}\\Results\\{output_filename}")
        else:
            print(f"\nSaved output at: {getcwd()}/Results/{output_filename}")

def removetemp(tempfolder:str = "temp"):
    for item in listdir(tempfolder):
        if name == "nt":
            remove(f"{tempfolder}\\{item}")
        else:
            remove(f"{tempfolder}/{item}")
