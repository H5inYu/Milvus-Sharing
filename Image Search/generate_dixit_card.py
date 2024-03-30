import requests
from openai import OpenAI

client = OpenAI()

for i in [5, 32, 33]:
    response = client.images.generate(
        model="dall-e-3",
        prompt="fighting with stories, fancy style",
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    img_data = requests.get(image_url).content
    with open(f'Dixit Card/{i}.png', 'wb') as handler:
        handler.write(img_data)
