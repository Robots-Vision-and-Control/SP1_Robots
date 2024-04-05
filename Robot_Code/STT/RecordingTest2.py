from google.cloud import speech
import pvporcupine
import pyaudio
import wave
import pvcobra
import struct
from playsound import playsound

# Constants
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 256
SILENCE_SECONDS = 5  # Seconds of silence until recording stops
SILENCE_THRESHOLD = 2  # Seconds of silence after speaking until recording stops
MAXIMUM_SECONDS = 15  # Time before the user is cut off
VAD_THRESHOLD = 0.5  # Adjust as needed
WAVE_OUTPUT_FILENAME = "output.wav"


# Function to record audio
def record_command():
    playsound('Sounds/ListeningChime.wav')
    # Voice activity detection object
    picovoice_key = open('../Sens/Picovoice.txt').readline().strip()
    cobra = pvcobra.create(access_key=picovoice_key)
    CHUNK = cobra.frame_length
    RATE = cobra.sample_rate

    # Recording Audio object
    audio = pyaudio.PyAudio()
    audio_stream = audio.open(format=FORMAT, channels=CHANNELS,
                              rate=cobra.sample_rate, input=True,
                              frames_per_buffer=cobra.frame_length)

    print("Recording...")

    frames = []
    did_speak = False

    # Allows the user an allowed amount of time to start giving the command
    for i in range(0, int(RATE / CHUNK * SILENCE_SECONDS)):
        data = audio_stream.read(CHUNK)
        new_data = struct.unpack('h' * cobra.frame_length, data)

        voice_probability = cobra.process(new_data)
        #print(voice_probability)
        if voice_probability > VAD_THRESHOLD and i > 5:  # Allows time to calibrate to correct level
            did_speak = True
            frames.append(data)
            break

    # If the user started talking record audio until they go silent
    if did_speak:
        silent_time = 0
        for i in range(0, int(RATE / CHUNK * MAXIMUM_SECONDS)):
            data = audio_stream.read(CHUNK)
            frames.append(data)

            new_data = struct.unpack('h' * cobra.frame_length, data)
            voice_probability = cobra.process(new_data)
            #print('Section 2 -', voice_probability)
            if voice_probability < VAD_THRESHOLD:
                silent_time += 1 / (RATE / CHUNK)
            else:
                silent_time = 0

            if silent_time > SILENCE_THRESHOLD:
                break

    print("Finished recording.")

    # End audio Stream
    audio_stream.stop_stream()
    audio_stream.close()
    audio.terminate()
    cobra.delete()

    # Make the output wave file
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    transcribe_audio()


# Function to transcribe audio using Google Cloud Speech-to-Text
def transcribe_audio():
    try:
        client = speech.SpeechClient.from_service_account_file('../Sens/GoogleCloudkey.json')
        file_name = "output.wav"

        with open(file_name, 'rb') as f:
            audio_data = f.read()

        audio_file = speech.RecognitionAudio(content=audio_data)

        config = speech.RecognitionConfig(
            sample_rate_hertz=16000,  # Adjusted sample rate to match the WAV file
            enable_automatic_punctuation=True,
            language_code='en-US'
        )

        response = client.recognize(
            config=config,
            audio=audio_file
        )

        print('\nResult:', response.results[0].alternatives[0].transcript)
        playsound('Sounds/StopChime.wav')

    except Exception as e:
        print("Error:", e)



# Main function
def main():
    while True:
        input("Press Enter to start recording. Speak your command...")
        record_command()
        print("Done!")
        transcribe_audio()


def hotword():
    # Path to Porcupine keyword file
    keyword_file_path = "Hey-Ratchet_en_windows_V3_0_0.ppn"
    picovoice_key = open('../Sens/Picovoice.txt').readline().strip()

    #print(keyword_file_path)

    # Initialize Porcupine
    porcupine = pvporcupine.create(
        access_key=picovoice_key,
        keyword_paths=[keyword_file_path]
    )

    # Initialize PyAudio
    pa = pyaudio.PyAudio()
    audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length)

    #print(pyaudio.PyAudio().get_default_input_device_info())

    try:
        print("Listening for 'Hey Ratchet'...")

        while True:
            pcm = audio_stream.read(porcupine.frame_length)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
            keyword_index = porcupine.process(pcm)
            if keyword_index >= 0:
                print("Wake up word 'Hey Ratchet' detected!")
                record_command()

    except KeyboardInterrupt:
        print("Stopping...")
        playsound('Sounds/StopChime.wav')

    finally:
        audio_stream.close()
        pa.terminate()
        porcupine.delete()


if __name__ == "__main__":
    hotword()