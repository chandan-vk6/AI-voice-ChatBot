
from decouple import config
import assemblyai as aai
import os
from dotenv import load_dotenv
from groq import Groq
import torch
from functions.database import get_recent_messages
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

# you can also use openAI whishper which is much more efficient and faster
# Convert audio to text
def convert_audio_to_text(audio_file):
  try:
# replace with your API token
    aai.settings.api_key = config("ASSEMBLY_AI_KEY")
    transcriber = aai.Transcriber()
    message_text = transcriber.transcribe(audio_file).text
    # print(F"message_text ============> {message_text}")
    return message_text 
  except Exception as e:
    return 

# what i have implemented is i ha ve model and  iam  getting response from that which is  very /
# slow respones instead you can get it from openai or another using api which is faster
# Convert audio to text
def get_chat_response(message_input):


  # messages = get_recent_messages()
  # user_message = {"role": "user", "content": message_input + " Only say two or 3 words in Spanish if speaking in Spanish. The remaining words should be in English"}
  # messages.append(user_message)
  

  try: 

    chat_completion = client.chat.completions.create(
        messages=[
           {
              "role": "system",
              "content": "you are a helpful spanish language Teaching assistant."
            },
            {
                "role": "user",
                "content": message_input,
            }
        ],
        model="mixtral-8x7b-32768",
    )
    print(chat_completion.choices[0].message.content)
    return chat_completion.choices[0].message.content

    # return output[0]['generated_text'].split('\n', 1)[1]
  except Exception as e:
    return
