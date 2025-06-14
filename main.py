import logging

logging.basicConfig(
    format='%(asctime)s - %(message)s',
    level=logging.INFO
)

def greet(name):
    return f"Hello, {name}! You're on your AI journey with Veda. 🚀"

if __name__ == "__main__":
    logging.info(greet("SR"))
