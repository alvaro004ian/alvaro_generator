from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        name1 = request.form.get("name1")
        name2 = request.form.get("name2")
        sentences = [
            f"{name1} and {name2} are going on a date. {name2} spills coffee on {name1}, and {name1} says: 'Oh fuck!' 😂",
            f"{name1} and {name2} tried cooking together. The fire alarm went off, but they called it 'modern art cuisine'.",
            f"{name1} and {name2} went shopping. {name1} bought socks with bananas, {name2} pretended it was high fashion.",
            f"{name1} and {name2} played video games. {name2} lost badly, but claimed the controller was possessed.",
            f"{name1} and {name2} took a selfie. A random dog photobombed them, and now it’s their profile picture forever.",
            f"{name1} and {name2} went to a fancy dinner. {name2} stole fries from {name1}'s plate, and {name1} declared war.",
            f"{name1} and {name2} tried baking cookies. {name2} ate the dough raw, {name1} called them a cookie criminal.",
            f"{name1} and {name2} went shopping. {name2} hid in the changing room and scared {name1} so badly they dropped all the clothes.",
            f"{name1} and {name2} played truth or dare. {name2} dared {name1} to sing in public, and strangers actually tipped them.",
            f"{name1} and {name2} went to karaoke. {name2} sang so badly the machine begged for mercy, {name1} laughed until they cried.",
            f"{name1} and {name2} tried cooking pasta. {name2} threw noodles at the wall, {name1} said: 'That's art now.'",
            f"{name1} and {name2} went to the movies. {name2} whispered spoilers, {name1} threw popcorn at them in revenge.",
            f"{name1} and {name2} played hide and seek. {name2} hid in the fridge, {name1} almost fainted when they found them.",
            f"{name1} and {name2} went to the beach. {name2} buried {name1} in sand and drew a mustache on their face.",
            f"{name1} and {name2} joined a dance class. {name2} spun too hard and crashed into {name1}, everyone clapped like it was choreography.",
            f"{name1} and {name2} tried yoga. {name2} fell asleep in downward dog, {name1} posted it online.",
            f"{name1} and {name2} went ice skating. {name2} fell every 3 seconds, {name1} pretended to be a coach yelling 'style points!'",
            f"{name1} and {name2} went bowling. {name2} threw the ball backwards, {name1} screamed louder than the crowd.",
            f"{name1} and {name2} tried painting. {name2} painted a mustache on {name1}, and called it modern art.",
            f"{name1} and {name2} went camping. {name2} scared {name1} with fake ghost noises, then tripped over the tent rope.",
            f"{name1} and {name2} played video games. {name2} unplugged {name1}'s controller, {name1} chased them around the room.",
            f"{name1} and {name2} went roller skating. {name2} crashed into a trash can, {name1} laughed until they joined inside.",
            f"{name1} and {name2} tried baking a cake. {name2} added salt instead of sugar, {name1} called it 'revenge dessert'.",
            f"{name1} and {name2} went swimming. {name2} splashed {name1} nonstop, until {name1} dunked them under water playfully."
        ]
        result = random.choice(sentences)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
