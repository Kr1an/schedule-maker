import os
import json
import random
from utils.helpers.property_writer import *
from utils.helpers.property_reader import *

INPUT_FILE_PATH = os.path.abspath(
    os.path.join(
        __file__,
        "..",
        "..",
        "input",
        "input.json"
    )
)


def generate_schedule():
    info = json.load(open(INPUT_FILE_PATH, 'r'))
    print(get_property(info, 'subjects')[0]['title'])
