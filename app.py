import gradio as gr
import whisper


# Translate speech to braille

def transcribe_audio(audio, state=None, lang=None):
    if state is None:
        state = {}

    model = whisper.load_model('base')
    result = model.transcribe(audio, language=lang)

    state['transcription'] = result['text']

    return state['transcription'], state, \
           f"Detected language: {result['language']}"

def generate_braille():
    pass

# Setup gradio interface

title = "Speech to Braille Translator"
transcription_tb = gr.Textbox(label="Transcription", lines=10, max_lines=20)
detected_lang = gr.outputs.HTML(label="Detected Language")
state = gr.State({"transcription": ""})

demo = gr.Interface(fn=transcribe_audio,
             inputs=[
                 gr.Audio(source="microphone", type="filepath",
                          streaming=False),
                 state,
             ],
             outputs=[
                 transcription_tb,
                 state,
                 detected_lang,
             ],
             # live=True,
             allow_flagging='never',
             title=title,
             )

# Launch gradio app
demo.launch()
