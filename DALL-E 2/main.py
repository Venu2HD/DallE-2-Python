from scripts.output_handler import saveimgoutput, getimgoutput, removetemp, ensurefolders, savetextoutput
from scripts.input_gatherer import getinput, getimagesavepref, gettextsavepref
from scripts.generate import genimage, variateimage, textcomplete
from scripts.check_requirements import check_requirements
from scripts.install import install_requirements
from scripts.get_settings import getsettings
from PIL.Image import open as open_pillow
from os.path import isdir, exists
from os import mkdir, name

install_requirements(check_requirements())

ensurefolders()

settings = getsettings()
api_key = settings["api_key"]

if exists("temp") and isdir("temp"):
    pass
else:
    mkdir("temp")

input_from_user = getinput()

print("\nYour content is being generated...\n")
if input_from_user["action"] == "Generate image":
    image_url = genimage(input_from_user["image_prompt"], api_key)
elif input_from_user["action"] == "Generate image variation":
    image_url = variateimage(input_from_user["image_opened"], api_key)
elif input_from_user["action"] == "Generate text":
    final_text = textcomplete(input_from_user["text_prompt"], input_from_user["text_model"], input_from_user["length"], api_key, temperature = input_from_user["temperature"])

if "Generate image" in input_from_user["action"]:
    image_binary = getimgoutput(image_url)
    if name == "nt":
        with open("temp\\tmpimg.png", "wb") as tmpimg:
            tmpimg.write(image_binary)
        image_pillow = open_pillow("temp\\tmpimg.png")
    else:
        with open("temp/tmpimg.png", "wb") as tmpimg:
            tmpimg.write(image_binary)
        image_pillow = open_pillow("temp/tmpimg.png")
    image_save_pref = getimagesavepref(image_pillow)
    saveimgoutput(image_binary, image_save_pref["image_save_name"], image_save_pref["save_output"])
    removetemp()
elif "Generate text" in input_from_user["action"]:
    text_save_pref = gettextsavepref(final_text)
    savetextoutput(final_text, text_save_pref["filename"], text_save_pref["save_text"])