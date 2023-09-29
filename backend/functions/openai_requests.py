
from decouple import config
import assemblyai as aai
import torch
from functions.database import get_recent_messages
from transformers import (
  AutoTokenizer,
  AutoModelForCausalLM,
)

MODEL_NAME = "TheFuzzyScientist/diabloGPT_open-instruct"
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
tokenizer.pad_token = tokenizer.eos_token


# Convert audio to text
def convert_audio_to_text(audio_file):
  try:
# replace with your API token
    aai.settings.api_key = config("ASSEMBLY_AI_KEY")
    transcriber = aai.Transcriber()
    message_text = transcriber.transcribe(audio_file).text
    return message_text
  except Exception as e:
    return


# Convert audio to text
def get_chat_response(message_input):

  messages = get_recent_messages()
  user_message = {"role": "user", "content": message_input + " Only say two or 3 words in Spanish if speaking in Spanish. The remaining words should be in English"}
  messages.append(user_message)
  

  try:
   
    inputs = tokenizer.encode(message_input, return_tensors='pt')
    outputs = model.generate(inputs, max_length=64, pad_token_id=tokenizer.eos_token_id)
    generated = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated[:generated.rfind('.')+1]
  except Exception as e:
    return
