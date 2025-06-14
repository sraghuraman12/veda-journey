import logging
import argparse

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
    parser = argparse.ArgumentParser(description="Greet the user in different languages.")
    parser.add_argument('--name', type=str, default="SR", help='Name of the user')
    parser.add_argument('--lang', type=str, default="en", help='Language code (en, hi, ta, es)')
    args = parser.parse_args()
    logging.info(greet(args.name, args.lang))
