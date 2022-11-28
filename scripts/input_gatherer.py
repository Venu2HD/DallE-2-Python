from tkinter.filedialog import askopenfilename
from inquirer import List, prompt
from PIL.Image import Image

def getinput():
    for _ in range(1):
        action = prompt([List(message = "Pick sommething", name = "action", choices = ["Generate image", "Generate image variation", "Generate text"])])

        if action["action"] == "Generate image":
            while True:
                image_prompt = input("What should the image be inspired by?\n")
                if image_prompt != "":
                    break
            return {"action": action["action"], "image_prompt": image_prompt}
        elif action["action"] == "Generate image variation":
            print("Please pick an image")
            while True:
                image_path = askopenfilename(title = "Please pick an image")
                try:
                    image_opened = open(image_path, "rb")
                except FileNotFoundError:
                    continue
                else:
                    break
            return {"action": action["action"], "image_opened": image_opened, "image_path": image_path}
        elif action["action"] == "Generate text":
            while True:
                text_prompt = input("Text prompt:\n")
                if text_prompt != "":
                    break
            text_model = prompt([List(message = "Text model", name = "text_model", choices = ["Text Davinci 002", "Text Curie 001", "Text Babbage 001", "Text Ada 001", "Advanced"])])["text_model"].lower().replace(" ", "-", -1)
            if text_model == "Advanced":
                text_model = prompt([List(message = "Advanced text model", name = "text_model", choices = ["Text Davinci 001", "Davinci Instruct Beta", "Davinci", "Curie Instruct Beta", "Curie", "Babbage", "Ada"])])["text_model"].lower().replace(" ", "-", -1)
            while True:
                try:
                    temperature = float(input("What should the temperature be?\nLess temperature = More deterministic.\nMore temperature = More random.\n"))
                except ValueError:
                    continue
                else:
                    if temperature >= 0:
                        break
            while True:
                try:
                    length = round(int(input("\nHow long should the created text maximum be?\n(In characters)\n")) / 4)
                except TypeError or ValueError:
                    continue
                else:
                    if length <= 0:
                        print("\nLength too low")
                        continue
                    else:
                        break
                    
            return {"action": action["action"], "text_prompt": text_prompt, "text_model": text_model, "temperature": temperature, "length": length}

def getimagesavepref(image_pillow:Image, show_image:bool = True):
    if show_image:
        print("\nShowing image\n")
        image_pillow.show()
    image_save_pref = prompt([List(message = "Should the image be saved", name = "image_save_pref", choices = ["Yes", "No"])])
    if image_save_pref["image_save_pref"] == "Yes":
        while True:
            image_save_name = "{}.png".format(input("What should the image be saved as? (Exclude the file extension)\n"))
            if image_save_name == ".png":
                continue
            else:
                break
        save_image = True
    else:
        save_image, image_save_name = False, ""
    return {"image_save_name": image_save_name, "save_output": save_image}

def gettextsavepref(final_text:str, show_text:bool = True):
    if show_text:
        if final_text.replace(final_text[4:], "") == "\n\n":
            print(f"{final_text[4:]}{'{}'}".format("\n"))
        elif final_text.replace(final_text[2:], "") == "\n":
            print(f"{final_text[2:]}{'{}'}".format("\n"))
        else:
            print(f"{final_text}{'{}'}".format("\n"))
    save_text = {"Yes": True, "No": False}[prompt([List(message = "Should the text be saved?", name = "save_text", choices = ["Yes", "No"])])["save_text"]]
    if save_text:
        while True:
            filename = "{}.txt".format(input("What should the text be saved as? (Exclude the file extension)\n"))
            if filename != "":
                break
    else:
        filename = ""
    return {"save_text": save_text, "filename": filename}
