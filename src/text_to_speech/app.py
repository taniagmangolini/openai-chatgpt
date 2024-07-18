import whisper
import api
from logger import Logger


logger = Logger().get_logger()


if __name__ == "__main__":
    try:

        with open("text_to_speech/data/example.txt", 'r') as file:
            response = api.convert_text_to_speech("alloy", file.read())
            response.stream_to_file("text_to_speech/data/example.mp3")

    except Exception as e:
        logger.info(f"Error: {e}")
