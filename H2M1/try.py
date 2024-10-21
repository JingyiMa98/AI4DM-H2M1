 # Use a pipeline as a high-level helper
from transformers import pipeline


def img2text(imgUrl):
    img_to_text_pipe = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")
    text = img_to_text_pipe(imgUrl)[0]["generated_text"]
    return text
scenario = img2text('luke-miller-s6w_b3RFzy0-unsplash.jpg')