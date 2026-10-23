from google import genai
from dotenv import load_dotenv
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
model = "gemini-3.5-flash"

topic = input("enter a topic: ")

prompt1 = "give 3 mcq questions on " + topic + " with options a to d. number them 1 to 3. dont give answers."
res1 = client.models.generate_content(model=model, contents=prompt1)
questions = res1.text
print(questions)

ans = input("enter your answers (eg: a,c,b): ")

prompt2 = "questions:\n" + questions + "\nmy answers: " + ans + "\ncheck each answer, tell right or wrong with correct answer and short reason. give score out of 3."
res2 = client.models.generate_content(model=model, contents=prompt2)
print(res2.text)

