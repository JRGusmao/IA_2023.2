import openai
import pyttsx3
import speech_recognition as sr

openai.api_key = "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"

engine = pyttsx3.init()

voices = engine.getProperty('voices')
portuguese_voice = None
for voice in voices:
    if 'portuguese' in voice.languages:
        portuguese_voice = voice
        break
if portuguese_voice is not None:
    engine.setProperty('voice', portuguese_voice.id)
else:
    print("Não foi encontrado o pacote de linguagem")


def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio, language="pt-BR")
    except sr.UnknownValueError:
        print('Erro: Não foi possível entender a fala')
    except sr.RequestError as e:
        print(f'Erro de reconhecimento de fala: {e}')


def generate_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=4000,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response['choices'][0]['text']
    except openai.OpenAIError as e:
        print(f'Erro na solicitação à API da OpenAI: {e}')


def speak_text(text):
    engine.say(text)
    engine.runAndWait()


def main():
    listening = False
    while True:
        if not listening:
            activation_phrase = input("Digite 'dino' para começar a escutar: ")
            if activation_phrase.lower() == 'dino':
                listening = True
                print("Começando a escutar para perguntas...")
        else:
            print("Modo de escuta ativado. Diga sua pergunta ou digite 'parar' para sair...")
            with sr.Microphone() as source:
                recognizer = sr.Recognizer()
                source.pause_threshold = 1
                audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                filename = "input.wav"
                with open(filename, "wb") as f:
                    f.write(audio.get_wav_data())
                text = transcribe_audio_to_text(filename)
                if text:
                    print(f"Você disse: {text}")
                    response = generate_response(text)
                    print(f"DINO disse: {response}")
                    speak_text(response)
                user_input = input("Diga sua próxima pergunta ou digite 'parar' para sair: ")
                if user_input.lower() == 'parar':
                    listening = False


if __name__ == '__main__':
    main()
