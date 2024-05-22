from flask import Flask, render_template
import random

app = Flask(__name__)

#Lista de las imagenes de gatos
images = [
    "https://media.tenor.com/images/043a3299edb9161b14a71b87afacf54f/tenor.gif",
    "https://media.tenor.com/images/ebb65bb0ca7bdd155c198a066ecfcb92/tenor.gif",
    "https://media.tenor.com/images/eff22afc2220e9df92a7aa2f53948f9f/tenor.gif",
    "https://media.tenor.com/images/29bcbdd10695e7ac46817f63c068dade/tenor.gif",
    "https://media.tenor.com/images/f21e8e1a608e8521fc239a5e7265413a/tenor.gif",
    "https://media.tenor.com/images/2ef32c5ee9c6153dc5a6354cff7c670b/tenor.gif",
    "https://media.tenor.com/images/815a7cd9ba42f91700acfc5579bee3ee/tenor.gif",
    "https://media.tenor.com/images/48a21a706669aeb55db4bbe07034d252/tenor.gif",
    "https://media.tenor.com/images/3cbb1811e8e58938bf65ea67c028988f/tenor.gif",
    "https://media.tenor.com/images/c35c83e1b5e9b5d3c30c5d7b0f0bc738/tenor.gif",
    "https://media.tenor.com/images/eab17a80e1c0558c1a10246413de37a3/tenor.gif",
    "https://media.tenor.com/images/232c7dbbb9bdd0ff16f2504685f3d718/tenor.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")