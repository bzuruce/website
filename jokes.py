from random import randint
from flask import Flask, render_template

def jokes():
    jokes = ["What do you call a magic dog? \n\nA labracadabador!", 
             "What do you call a pony with a cough \n\nA little horse!", 
             "Why can't you hear a pterodactyl go to the bathroom? \n\nBecause the 'P' is silent!",
             "Why did the frog take the bus to work today? \n\nBecause his car got toad!",
             "What did the buffalo say when his son left for college? \n\nBison!",
             "What is an alien's favorite part of a computer? \n\nThe space bar!",
             "Why did the yogurt go to the art exhibition? \n\nBecause it was cultured!"]
    chosen = randint(0,len(jokes)-1)
    return [str(chosen+1), str(jokes[chosen])]