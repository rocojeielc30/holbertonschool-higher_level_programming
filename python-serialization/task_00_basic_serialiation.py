#!/usr/bin/env python3
"""Serializes a dictionary to a JSON file and deserializes it back."""
import json

def serialize_and_save_to_file(data, filename):
    """Serialize data to JSON."""
    with open(filename, 'w', encoding="utf=8") as file:
        json.dump(data, file)
    pass

def load_and_deserialize(filename):
    """Deserialize data to JSON."""
    with open(filename, 'r', encoding="utf=8") as file:
        return json.load(file)
    pass