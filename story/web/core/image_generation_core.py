import pickle
import openai
import requests
import json


SD_API_URL = "https://stablediffusionapi.com/api/v3/text2img"
INIT_IMAGE_LINK = "https://raw.githubusercontent.com/CompVis/stable-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo.png"
MASK_IMAGE_LINK = "https://raw.githubusercontent.com/CompVis/stable-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo_mask.png"


def write_prompt(prompt):
    openai.api_key = "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"
    messages = [
        {"role": "system", "content": "Given a text, your task is to assist users in creating prompts for a text-to-image model (stable diffusion) to generate an illustration for the story.\n- The prompt should be concise and exclude unnecessary details.\n- Aim to preserve the main character's visual appearance.\n- Avoid using quotation marks.\n- Avoid using characters' names.\n -An example of a prompt is 'a man holding a beer on the moon, elephants over the fence'\n\nHere's the format:\nStory: ...\n\nAction: ...\n\nPrompt: ... (This is where you write the prompt)."},
        {"role": "system", "content": f"Story: {prompt}\n\nPrompt: "},
    ]

    prompt = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=32,
        messages=messages,
    )["choices"][0]["message"]["content"]

    return prompt


def generate_image(
    prompt,
    url=SD_API_URL,
    guidance_scale=7.5,
):
    prompt = write_prompt(prompt)
    print(prompt)
    payload = json.dumps({
        "key": "H7ycSgt7QhMcB7KVmgVgMJkrl4I6qIUejt6RKBLAYqgoomMlSQZpTpp73WNE",
        "prompt": prompt,
        "negative_prompt": None,
        "width": "512",
        "height": "448",
        "samples": "1",
        "num_inference_steps": "20",
        "seed": None,
        "guidance_scale": guidance_scale,
        "safety_checker": "no",
        "multi_lingual": "no",
        "panorama": "no",
        "self_attention": "no",
        "upscale": "no",
        "webhook": None,
        "track_id": None
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    response_dict = json.loads(response.text)
    print(response_dict["output"][0])
    return response_dict["output"][0]
