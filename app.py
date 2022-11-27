import gradio as gr
import whisper
from pybraille import convertText


# Translate speech to braille
def speech_to_text(audio):
    """

    :param audio: Speech data
    :return: Transcript of speech data
    """
    model = whisper.load_model('base')

    return model.transcribe(audio, language=lang)


def transcribe_audio(audio, store=None):
    """

    :param audio: Speech data from gradio interface
    :param store: Container for user data
    :return: Detected language, transcript text, braille translation, session state
    """
    if store is None:
        store = {}

    result = speech_to_text(audio)
    store['transcription'] = result['text']
    store['braille'] = convertText(store['transcription'])

    return f"Detected language: {result['language']}", store[
        'transcription'], store['braille'], store


# Setup gradio interface
title = "Speech to Braille Translator"
transcription_tb = gr.Textbox(label="Transcription", lines=10, max_lines=20)
detected_lang = gr.outputs.HTML(label="Detected Language")
transcription_braille = gr.Textbox(label="Braille", lines=10, max_lines=20)

state = gr.State({"transcription": ""})

demo = gr.Interface(fn=transcribe_audio,
                    inputs=[
                        gr.Audio(source="microphone", type="filepath",
                                 streaming=False),
                        state
                    ],
                    outputs=[
                        detected_lang,
                        transcription_tb,
                        transcription_braille,
                        state,
                    ],
                    # live=True,
                    allow_flagging='never',
                    title=title,
                    )

# Launch gradio app
demo.launch()
