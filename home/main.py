from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
import requests
import random

#CST 205 Final Project
#Project Name: Adopt a Paw
#Authors: Jamie Maniulit, Isaiah Bueno, Calvin Chan
#Contributers: Jamie - worked on main.py functions, API implementation,
#and all template html classes.

#Project Github Link: https://github.com/jamiellem/CST205_FinalProject

app = Flask(__name__)
bootstrap = Bootstrap(app)

#Requests to get image and breed data from API
images = requests.get("https://dog.ceo/api/breed/hound/images")
imgData = images.json()['message']
breeds = requests.get("https://dog.ceo/api/breed/hound/list")
breedData = breeds.json()['message']

#Renders home page, this function also randomizes the dog pics
#shown each time the user reloads the page.
@app.route('/')
def home():
    firstBreed = random.choice(imgData)
    secondBreed = random.choice(imgData)
    thirdBreed = random.choice(imgData)
    return render_template('home.html',data1=firstBreed,data2=secondBreed,data3=thirdBreed)

#Renders find pet page and passes breed and image data from API
@app.route('/findPet')
def petFind():
    breed1 = breedData[0]
    img1 = imgData[0]
    breed2 = breedData[1]
    img2 = imgData[242]
    breed3 = breedData[2]
    img3= imgData[416]
    breed4 = breedData[3]
    img4 = imgData[609]
    breed5 = breedData[4]
    img5 = imgData[760]
    breed6 = breedData[5]
    img6 = imgData[953]
    return render_template('findPet.html', b1=breed1, i1=img1,b2=breed2, i2=img2,
                           b3=breed3, i3=img3,b4=breed4, i4=img4,b5=breed5, i5=img5, b6=breed6, i6=img6)

#Renders Sign Up page
@app.route('/signUp')
def CreateAcc():
    return render_template('CreateAcc.html')

#Renders Login page
@app.route('/login')
def Login():
    return render_template('Login.html')

#Renders Adopt page
@app.route('/Adopt')
def Adopt():
    return render_template('Adopt.html')