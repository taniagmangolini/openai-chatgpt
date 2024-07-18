import whisper
import api
from logger import Logger


logger = Logger().get_logger()


if __name__ == "__main__":
    try:
        audio_file = "translations_transcriptions/data/Winston_Church.ogg"
        logger.info("Transcription by API:")
        text = api.transcribe_audio(audio_file)

        system_prompt = """You are a movie specialist. 
        Your role is to correct the transcription of 
        the audio file and summarize it"."""

        response = api.create_chat_completion(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text},
            ],
        )
        logger.info(response)

    except Exception as e:
        logger.info(f"Transcription error: {e}")
