import openai
import os
from datetime import datetime

start_time = datetime.now()

openai.api_key = os.getenv("OPENAI_API_KEY")
model_name = "gpt-4"
# model_name = "gpt-3.5-turbo"

question = "discord bot の作り方について教えて"

response = openai.ChatCompletion.create(
    model=model_name,
    messages=[
        {"role": "user", "content": question},
    ],
)

end_time = datetime.now()

print(response.choices[0]["message"]["content"].strip())
print(f"elapsed time: {end_time - start_time}")

# write to output-${yyyymmddthhmmss}.txt
with open(f"output-{model_name}-{datetime.now().strftime('%Y%m%dT%H%M%S')}-{question}.txt", "w") as f:
    f.write(f"model: {model_name}\n")
    f.write("time: " + str(end_time - start_time) + "\n")
    f.write("question: " + question + "\n")
    f.write("answer: " + response.choices[0]["message"]["content"].strip() + "\n")