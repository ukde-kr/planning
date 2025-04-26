import os
from dotenv import load_dotenv
from google.cloud import speech

# Load environment variables from .env file
load_dotenv()

def transcribe_with_diarization_from_gcs(gcs_uri, language_code="en-GB", output_file_path=None):
    """Transcribes an audio file from Google Cloud Storage with speaker diarization."""
    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.MP3,  # Adjust based on audio format
        sample_rate_hertz=16000,  # Adjust based on audio sample rate
        language_code=language_code,
        diarization_config=speech.SpeakerDiarizationConfig(
            enable_speaker_diarization=True,
            min_speaker_count=2, 
            max_speaker_count=2, 
        ),
        model="latest_long", # Or specify a more specific model if needed
    )

    print(f"Waiting for operation to complete for audio at: {gcs_uri}")
    operation = client.long_running_recognize(config=config, audio=audio)
    response = operation.result(timeout=2700)  # Adjust timeout as needed

    segments = []
    current_speaker = None
    current_sentence = []

    for result in response.results:
        for segment in result.alternatives[0].words:
            word = segment.word
            speaker_tag = segment.speaker_tag

            if current_speaker is None:
                current_speaker = speaker_tag
                current_sentence.append(word)
            elif current_speaker == speaker_tag:
                current_sentence.append(word)
            else:
                segments.append((current_speaker, " ".join(current_sentence)))
                current_speaker = speaker_tag
                current_sentence = [word]

    # Add the last segment
    if current_sentence:
        segments.append((current_speaker, " ".join(current_sentence)))

    if output_file_path:
        with open(output_file_path, "w") as outfile:
            for speaker, sentence in segments:
                outfile.write(f"Speaker {speaker}: {sentence}\n")
        print(f"Transcription with speaker labels per turn saved to: {output_file_path}")
    else:
        for speaker, sentence in segments:
            print(f"Speaker {speaker}: {sentence}")

    return segments

if __name__ == "__main__":
    gcs_audio_uri = "gs://llm-study-bucket/full-output.mp3"
    language = "en-GB" 
    output_file = "transcription_output_from_gcs.txt"

    # Set the GOOGLE_APPLICATION_CREDENTIALS environment variable from .env
    credential_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    if credential_path:
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_path
    else:
        print("Error: GOOGLE_APPLICATION_CREDENTIALS environment variable not found in .env file.")
        exit()

    transcribe_with_diarization_from_gcs(gcs_audio_uri, language, output_file)