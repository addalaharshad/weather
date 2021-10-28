import requests
import torch

MODEL_URL = 'https://github.com/vmc99/animal-face-classifier/releases/download/1.0.0-alpha/animal-face-detection_new.pth'
# r = requests.get(MODEL_URL)
# model = r.content
# print(type(model))
# filename.write_bytes(r.content)

# import wget
# wget.download(MODEL_URL)

# r = requests.get(MODEL_URL, allow_redirects=True)

# open('model.pth', 'wb').write(r.content)

state_dict = torch.hub.load_state_dict_from_url(MODEL_URL)

    # state_dict = torch.hub.load_state_dict_from_url(MODEL_URL)
    # # PATH = 'animal-face-classifier_new.pth'
    # model.load_state_dict(state_dict)
