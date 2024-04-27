from google.cloud import speech
import pvporcupine
import pyaudio
import wave
import pvcobra
import struct
import pygame

# Keys
picovoice_key = open('Sens/Picovoice.txt').readline().strip()
google_cloud = speech.SpeechClient.from_service_account_file('Sens/GoogleCloudkey.json')

# Constants
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
FRAME_LENGTH = 512
SILENCE_SECONDS = 5  # Seconds of silence until recording stops
SILENCE_THRESHOLD = 2  # Seconds of silence after speaking until recording stops
MAXIMUM_SECONDS = 15  # Max time for a voice command
VAD_THRESHOLD = 0.5  # Adjust as needed
WAVE_OUTPUT_FILENAME = "output.wav"

# Initialize PyAudio
microphone = pyaudio.PyAudio()
microphone_stream = microphone.open(format=FORMAT,
                                    channels=CHANNELS,
                                    rate=RATE,
                                    input=True,
                                    frames_per_buffer=FRAME_LENGTH)

# Cobra is used to detect when a person is speaking
cobra = pvcobra.create(access_key=picovoice_key)
hotword_model_path = "Hey-Ratchet_en_windows_V3_0_0.ppn"


# Used for playing sounds
def play_sound(sound_file):
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


# Function to start recording when hearing speech
def wait_for_speech():
    did_speak = False
    frames = []

    # Allow the user an allowed amount of time to start giving the command
    for i in range(int(RATE / FRAME_LENGTH * SILENCE_SECONDS)):
        data = microphone_stream.read(FRAME_LENGTH)
        new_data = struct.unpack('h' * cobra.frame_length, data)

        voice_probability = cobra.process(new_data)
        if voice_probability > VAD_THRESHOLD and i > 5:  # Allows time to calibrate to correct level
            did_speak = True
            frames.append(data)
            break

    return did_speak, frames


# Method to record audio until user goes silent
def record_audio(frames):
    silent_time = 0
    for i in range(int(RATE / FRAME_LENGTH * MAXIMUM_SECONDS)):
        data = microphone_stream.read(FRAME_LENGTH)
        frames.append(data)

        new_data = struct.unpack('h' * cobra.frame_length, data)
        voice_probability = cobra.process(new_data)

        if voice_probability < VAD_THRESHOLD:
            silent_time += 1 / (RATE / FRAME_LENGTH)
        else:
            silent_time = 0

        if silent_time > SILENCE_THRESHOLD:
            break

    return frames


def save_audio(frames):
    # Saves the voice command as a file.
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(microphone.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


# Function to transcribe audio using Google Cloud Speech-to-Text
def transcribe_audio():
    try:
        file_name = "output.wav"

        with open(file_name, 'rb') as f:
            audio_data = f.read()

        audio_file = speech.RecognitionAudio(content=audio_data)

        config = speech.RecognitionConfig(
            sample_rate_hertz=RATE,  # Adjusted sample rate to match the WAV file
            enable_automatic_punctuation=False,
            language_code='en-US'
        )

        response = google_cloud.recognize(
            config=config,
            audio=audio_file
        )

        result = response

        return result
        # print('\nResult:', response.results[0].alternatives[0].transcript)

    except Exception as e:
        print("Error:", e)


def listen_for_hotword():
    # Initialize Porcupine used for hot word recognition
    porcupine = pvporcupine.create(
        access_key=picovoice_key,
        keyword_paths=[hotword_model_path]
    )

    while True:
        pcm = microphone_stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
        keyword_index = porcupine.process(pcm)
        if keyword_index >= 0:  # If hot word is detected
            return True


def get_command_text():
    did_speak, frames = wait_for_speech()
    if did_speak:
        frames = record_audio(frames)
        play_sound('Sounds/StopChime.wav')
        save_audio(frames)
        return transcribe_audio()
    else:
        print("No speech")


def listen_for_commands():
    while True:
        print("Listening for 'Hey Ratchet'...")
        if listen_for_hotword():
            print("Wake up word 'Hey Ratchet' detected!")
            play_sound('Sounds/StartChime.wav')
            result = get_command_text()
            print('Done listening')
            return '\nResult:' + result.results[0].alternatives[0].transcript
