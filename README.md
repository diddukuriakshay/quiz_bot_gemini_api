# Quiz_bot(Gemini API)

## what it does

the bot takes the input from user(topic) and sends to gemini-flash model and recieves questions related to that topic.
Again it sends the user's answers to gemini and receives the marks

## How it works

bot takes topic and converts it into prompt(give 3 questions on "topic") and sends that prompt.
after receiving, it prints text of the generated content, and then takes user's input(answers) and sends back to gemini along with question(by converting into prompt), then gemini sends the result.

## Tech used

- python
- google gemini API
- python-dotenv

## How to run
1. Install packages:
```
pip install google-genai python-dotenv
```
2. Create a `.env` file with:
```
GEMINI_API_KEY=your_key_here
```
3. Run:
```
python quiz.py
```

## what i learned

i just learned how to use APIs, this is my first project using APIs.