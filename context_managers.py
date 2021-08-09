# context managers : structures that allow for allocating and releasing resources upon use

# Basic example - open is the context manager
with open("text.txt") as file:
    print(file.read() + "\n")

# Custom context manager as a class
class TranslationResource(object):
    def __init__(self, text):
        self.open = True
        self.text = text
    
    def french(self):
        self.request_translation()
        return "Bonjour"

    def spanish(self):
        self.request_translation()
        return "Hola"
    
    def english(self):
        self.request_translation()
        return "Hello"
    
    def request_translation(self):
        if not self.open:
            raise RuntimeError("Resource is closed")

    def close(self):
        self.open = False
        return True

print(TranslationResource("Hello").french())

# Every context manager must have __enter__ and __exit__ methods
class TranslationResourceContextManager(object):
    def __init__(self, text):
        self.translation_resource = TranslationResource(text)

    def __enter__(self):
        return self.translation_resource

    def __exit__(self, type, value, traceback): # must have arguments type, value and traceback
        print("Closed Translation Resource")
        return self.translation_resource.close()

with TranslationResourceContextManager("Hello") as resource:
    print(resource.spanish())

with TranslationResourceContextManager("Hello") as resource: 
    print(resource.nonexistantlanguage()) # if __exit__ does not handle exceptions by returning True, exception is raised by with block
    print("This will not be printed - resource will be closed on the exception from the previous instruction")


# Custom context manager as a generator with contextlib.contextmanager
from contextlib import contextmanager

@contextmanager
def TranslationResourceContextManager2(text):
    resource = TranslationResource(text)
    try:
        yield resource
    except:
        print("Error: Failed to translate.")
        resource.close()
    finally:
        resource.close()

with TranslationResourceContextManager2("Hello") as resource:
    print(resource.spanish())

with TranslationResourceContextManager2("Hello") as resource: 
    print(resource.nonexistantlanguage())
    print("This will not be printed - resource will be closed on the exception from the previous instruction")