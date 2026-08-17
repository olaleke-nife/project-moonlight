import tkinter as tk
import random

stories = [
    "{name} fought a giant {animal} using a {object}.",
    "{name} married a {animal} because it loved {food}.",
    "{name} accidentally threw {food} at a {animal}.",
    "{name} cried the day a {animal} crawled on him and ate the {food}",
    "{name} woke up one morning to discover a giant {animal} sleeping in the backyard. Armed with nothing but a {object}, {name} carefully approached it. To everyone's surprise, the {animal} only wanted some {food}, and by sunset the two had become unlikely friends.",

    "{name} entered a village where every {animal} could talk. The chief {animal} demanded that {name} prove their courage using only a {object}. After a series of ridiculous challenges and a feast of {food}, {name} was declared an honorary citizen.",

    "{name} spent weeks searching for a legendary {object} said to grant incredible luck. Instead, the journey led to a clever {animal} guarding a mountain of {food}. The two struck an unusual bargain that changed {name}'s life forever.",

    "{name} accidentally dropped a {object} into a river, waking an enormous {animal}. Instead of attacking, the creature insisted that {name} prepare its favorite {food}. The meal turned into the strangest picnic anyone had ever seen.",

    "{name} found an abandoned {object} glowing deep inside the forest. The moment it was picked up, a mysterious {animal} appeared and claimed it had been protecting it for centuries. The only way to keep the treasure was to share some {food}.",

    "{name} challenged a fearless {animal} to a contest. The prize was a magical {object} and a lifetime supply of {food}. What started as a competition quickly became an adventure filled with unexpected twists and hilarious mistakes.",

    "{name} discovered that every time a {object} was used, a tiny {animal} magically appeared asking for {food}. Before long, hundreds of hungry creatures surrounded {name}, creating complete chaos in the neighborhood.",

    "{name} was hired to deliver a rare {food} across the kingdom. Along the way, a mischievous {animal} kept stealing pieces of the delivery while a mysterious {object} seemed to make the journey even stranger.",

    "{name} wandered into a hidden cave where an ancient {animal} guarded a powerful {object}. Instead of fighting, the creature invited {name} to share {food} while telling stories that had been forgotten for generations.",

    "{name} invented a strange {object} that could understand animals. The first creature to test it was a grumpy {animal}, whose only request was an endless supply of {food}.",

    "{name} opened the front door to find a tiny {animal} balancing a gigantic {object} on its head. The creature politely asked for some {food} before revealing a secret that nobody would believe.",

    "{name} entered a cooking competition against a famous {animal}. The secret ingredient was {food}, but the only cooking tool allowed was a {object}. The judges had never seen such a ridiculous contest.",

    "{name} inherited an old {object} from a mysterious relative. Every full moon, it transformed into a friendly {animal} that searched the house for {food} before disappearing at sunrise.",

    "{name} built a machine using a {object} that accidentally switched places with a curious {animal}. Suddenly, {name} had to survive in the wild while the {animal} enjoyed eating {food} at home.",

    "{name} rescued a lost {animal} during a storm. As thanks, the creature gifted a magical {object} that could create unlimited {food}, but only if it was used with kindness.",

    "{name} was exploring an old castle when a noisy {animal} stole the only {object} needed to escape. The chase led through secret passages filled with delicious {food} and unexpected surprises.",

    "{name} entered a mysterious market where every {animal} traded unusual treasures. One offered a magical {object} in exchange for a single piece of {food}, but the deal came with an unexpected catch.",

    "{name} decided to train a wild {animal} for the annual festival. Training required patience, a sturdy {object}, and plenty of {food}. By the end of the week, they had become the stars of the celebration.",

    "{name} discovered a map hidden inside a dusty {object}. It led to a forgotten island where a gigantic {animal} protected an endless garden of {food}.",

    "{name} accidentally wished upon a magical {object}. The next morning, every {animal} within miles gathered outside the house expecting a grand feast of {food}.",

    "{name} accepted a dare to spend one night in an abandoned cabin. The only company was a talking {animal}, an enchanted {object}, and a mysterious basket filled with {food}.",

    "{name} woke to find that a playful {animal} had rearranged the entire house. The only clue left behind was a missing {object} and a trail of scattered {food}.",

    "{name} entered a tournament where contestants had to tame a wild {animal} using only a {object}. The grand prize included enough {food} to feed an entire kingdom.",

    "{name} found a tiny village where every resident was a different {animal}. Their annual celebration could only begin after someone recovered the missing {object} and prepared the legendary {food}.",

    "{name} received a mysterious letter inviting them to dinner with a royal {animal}. The invitation required bringing a rare {object} and a basket of {food}, though nobody explained why.",

    "{name} was chased through the jungle by a giant {animal}. Every clever escape involved an unusual {object}, while a bag of {food} somehow made the adventure even more chaotic.",

    "{name} stumbled upon a magical library where books came alive as {animal}s. The librarian handed over a glowing {object} and warned that only {food} could calm the enchanted creatures.",

    "{name} dreamed of becoming the greatest explorer alive. The journey began with a trusty {object}, a backpack full of {food}, and an unexpected guide—a surprisingly clever {animal}.",

    "{name} accidentally shrank to the size of a mouse after touching a magical {object}. Suddenly, an ordinary {animal} looked enormous, and even a crumb of {food} seemed like a giant feast.",

    "{name} discovered a hidden door beneath a pile of {food}. Beyond it lived an ancient {animal} protecting a legendary {object}. Together they uncovered a secret that had remained hidden for centuries."

]

def generate_story():
    name = name_entry.get()
    animal = animal_entry.get()
    food = food_entry.get()
    obj = object_entry.get()

    story = random.choice(stories)

    story = story.format(
        name=name,
        animal=animal,
        food=food,
        object=obj
    )

    output.config(text=story)


window = tk.Tk()
window.title("Funny Story Generator")
window.geometry("500x400")

tk.Label(window, text="Name").pack()
name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text="Animal").pack()
animal_entry = tk.Entry(window)
animal_entry.pack()

tk.Label(window, text="Food").pack()
food_entry = tk.Entry(window)
food_entry.pack()

tk.Label(window, text="Object").pack()
object_entry = tk.Entry(window)
object_entry.pack()

tk.Button(window, text="Generate Story", command=generate_story).pack(pady=10)

output = tk.Label(window, text="", wraplength=450)
output.pack()

window.mainloop()
