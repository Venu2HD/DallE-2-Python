from io import BufferedReader
import openai

def genimage(image_prompt:str, api_key:str, image_width:int = 1024, image_height:int = 1024, image_amount:int = 1):
    openai.api_key = api_key
    return openai.Image.create(prompt = image_prompt, n = image_amount, size = f"{image_width}x{image_height}")["data"][0]["url"]

def variateimage(image_opened:BufferedReader, api_key:str, image_amount:int = 1):
    openai.api_key = api_key
    return openai.Image.create_variation(image = image_opened, n = image_amount, size = f"1024x1024")["data"][0]["url"]

def textcomplete(text_prompt:str, model:str, length:int, api_key:str, temperature:float = 0.5):
    openai.api_key = api_key
    return openai.Completion.create(model = model, prompt = text_prompt, max_tokens = length, temperature = temperature)["choices"][0]["text"]