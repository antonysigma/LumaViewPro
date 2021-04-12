# USED TO GENERATE PROtOCOL JSON FILE

# Protocol Layout
protocol = {
    "microscope": 'LS620',
    "frame_width": 2592,
    "frame_height": 1944,
    "objective": 'Canon 55mm',
    "period": 0.17,
    "duration": 0.17,
    "BF": {
        "save_folder": "./capture",
        "file_root": "W_",
        "ill": 100,
        "gain": 0.,
        "exp": 50.,
        "false_color": False,
        "acquire": True
    },
    "Blue": {
        "save_folder": "./capture",
        "file_root": "B_",
        "ill": 100,
        "gain": 0.,
        "exp": 50,
        "false_color": True,
        "acquire": True
    },
    "Green": {
        "save_folder": "./capture",
        "file_root": "G_",
        "ill": 100,
        "gain": 0.,
        "exp": 50,
        "false_color": True,
        "acquire": True
    },
    "Red": {
        "save_folder": "./capture",
        "file_root": "R_",
        "ill": 1000,
        "gain": 0.,
        "exp": 50,
        "false_color": True,
        "acquire": True
    },
    "Composite": {
        "acquire": False
    }
}

import json

with open("./data/default.json", "w") as write_file:
    json.dump(protocol, write_file)
