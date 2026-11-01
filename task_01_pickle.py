"""Defines CustomObject, which can be serialized and deserialized with pickle."""
import pickle


class CustomObject:
    """A simple object holding a name, an age and student status."""

    def __init__(self, name, age, is_student):
        """Initialise the object's attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize this instance to filename using pickle."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PicklingError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return a CustomObject from filename, or None on failure."""
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
        except (OSError, EOFError, pickle.UnpicklingError,
                AttributeError, ImportError, IndexError, TypeError,
                ValueError):
            return None
        if not isinstance(obj, cls):
            return None
        return obj