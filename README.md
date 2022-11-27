# Speech to Braille translator

## Overview
The demo for this project is hosted on Hugging Face spaces [here](https://huggingface.co/spaces/Azuremis/Speech2Braille).

It currently translates English speech into Braille.

The speech-text translation is done using OpenAI's [Whisper](https://openai.com/blog/whisper/) [model](https://github.com/openai/whisper). The text-braille translation is done using 
the [PyBraille](https://pypi.org/project/pybraille/) library.

## How to use
1. Go to the [demo](https://huggingface.co/spaces/Azuremis/Speech2Braille) on Hugging Face spaces
2. Click the record button and accept the browswer request for microphone access
3. Speak a few sentences then click the stop button when done.
4. Click the submit button to see both the English trascript and the Braille translation

![demo_screen](demo_screen.jpg?raw=true "DemoScreen")

## Disclaimer
This is a demo so I don't advise using it for any serious purpose!

## Credits

Thank you to [Dave](), I used his [RememberThis](https://github.com/AdBanacho/GPT-3-Hackathon) code to help me grok
how to use the OpenAI's whisper. I also found LabLab's Whisper [guides](https://lablab.ai/tech/whisper) really helpful. 