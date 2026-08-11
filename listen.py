def listen():

    print("\n🎙️ JARVIS is listening...")
    print("Speak now...")

    try:

        audio = sd.rec(
            int(DURATION * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="int16",
            device=MIC_DEVICE
        )

        sd.wait()

        wav.write(
            "temp_audio.wav",
            SAMPLE_RATE,
            audio
        )

        recognizer = sr.Recognizer()

        with sr.AudioFile("temp_audio.wav") as source:

            recorded_audio = recognizer.record(source)

        text = recognizer.recognize_google(
            recorded_audio,
            language="en-IN"
        )

        print("\n🧠 JARVIS understood:")
        print(text)

        return text

    except sr.UnknownValueError:

        print("\n❌ I couldn't understand what you said.")

        return None

    except sr.RequestError as error:

        print("\n❌ Speech recognition service error:")
        print(error)

        return None

    except Exception as error:

        print("\n❌ Microphone error:")
        print(error)

        return None