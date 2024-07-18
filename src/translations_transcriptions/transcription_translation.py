import whisper
from logger import Logger

print(whisper.__file__)

logger = Logger().get_logger()

if __name__ == "__main__":

    try:
        model = whisper.load_model("base")
    except Exception as e:
        logger.info(e)
        exit(1)

    try:
        audio_file = "translations_transcriptions/data/Winston_Church.ogg"

        logger.info("Transcription (original language):")
        transcription = model.transcribe(audio_file)
        logger.info(transcription["text"])

        logger.info("Transcription (portugues):")
        transcription_pt = model.transcribe(audio_file, language="pt")
        logger.info(transcription_pt["text"])
    except Exception as e:
        logger.info(f"Transcription error: {e}")
