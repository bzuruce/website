from openai import OpenAI
from flask import Flask, render_template, request
app = Flask()
app.route("/")
def app():
  return render_template("get.html")
def ask_gpt(content):
  client = OpenAI()
  response = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=content,
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  return response.choices[0].message.content
