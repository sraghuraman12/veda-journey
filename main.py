import logging

logging.basicConfig(
    format='%(asctime)s - %(message)s',
    level=logging.INFO
)

def greet(name, lang="en"):
    try:
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        greetings = {
            "en": "Hello",
            "hi": "Namaste",
            "ta": "Vanakkam",
            "es": "Hola"
        }
        return f"{greetings.get(lang, 'Hello')}, {name}! You're on your AI journey with Veda. 🚀"
    except Exception as e:
        logging.error(f"Error in greet: {e}")
        raise

if __name__ == "__main__":
    logging.info(greet("SR", "ta"))
