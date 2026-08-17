from tkinter import *

root = Tk()
root.title("Dictionary")
root.geometry("500x400")

# ---------------- WORD MEANINGS ----------------

word_meanings = {
    "happy": "Feeling or showing pleasure and joy.",
    "sad": "Feeling unhappy or sorrowful.",
    "angry": "Feeling strong annoyance or displeasure.",
    "beautiful": "Pleasant or attractive to look at.",
    "brave": "Having courage and not being afraid of danger.",
    "clever": "Quick to understand, learn, or solve problems.",
    "strong": "Having great physical or mental power.",
    "weak": "Not physically or mentally strong.",
    "fast": "Moving or happening quickly.",
    "slow": "Moving or happening at a low speed.",
    "smart": "Having a good ability to learn and understand things.",
    "kind": "Being friendly, caring, and helpful.",
    "honest": "Always telling the truth and being trustworthy.",
    "friendly": "Kind and pleasant toward other people.",
    "important": "Having great value or significance.",
    "easy": "Something that does not require much effort.",
    "difficult": "Something that requires a lot of effort or skill.",
    "dangerous": "Likely to cause harm or injury.",
    "safe": "Protected from danger or harm.",
    "powerful": "Having great strength, influence, or ability.",
    "computer": "An electronic machine that processes and stores information.",
    "python": "A popular programming language used to build software, websites, and applications.",
    "program": "A set of instructions that tells a computer what to do.",
    "code": "Instructions written for a computer to perform a task.",
    "software": "Programs and applications that run on a computer.",
    "hardware": "The physical parts of a computer or electronic device.",
    "internet": "A worldwide network that connects computers and devices.",
    "website": "A collection of web pages available on the internet.",
    "application": "A software program designed to perform a particular task.",
    "developer": "A person who creates and maintains software.",
    "technology": "The use of scientific knowledge to create useful tools and systems.",
    "artificial": "Something made or created by humans rather than occurring naturally.",
    "intelligence": "The ability to learn, understand, and solve problems.",
    "artificial intelligence": "Computer technology that allows machines to perform tasks that normally require human intelligence.",
    "database": "An organized collection of information that can be stored and accessed.",
    "data": "Information collected for a particular purpose.",
    "algorithm": "A set of steps used to solve a problem or complete a task.",
    "function": "A block of code designed to perform a specific task.",
    "variable": "A named place used to store a value in a program.",
    "dictionary": "A collection of words and their meanings; in Python, it is also a data structure storing key-value pairs.",
    "student": "A person who is learning or studying something.",
    "teacher": "A person who helps others learn.",
    "school": "A place where people receive education.",
    "knowledge": "Information and understanding gained through learning or experience.",
    "education": "The process of learning knowledge and skills.",
    "success": "The achievement of a desired goal.",
    "failure": "The lack of success in achieving a goal.",
    "goal": "Something that a person wants to achieve.",
    "dream": "A strong hope or ambition for the future.",
    "future": "The time that has not happened yet.",
    "present": "The current time or moment.",
    "past": "The time that has already happened.",
    "learn": "To gain knowledge or a skill through study or experience.",
    "teach": "To help someone gain knowledge or learn a skill.",
    "build": "To create or construct something.",
    "create": "To make or produce something new.",
    "develop": "To create, improve, or grow something.",
    "improve": "To make something better.",
    "practice": "Repeated activity done to improve a skill.",
    "focus": "To concentrate attention on something.",
    "motivation": "The reason or desire that encourages someone to take action.",
    "confidence": "Belief in your own abilities.",
    "challenge": "A difficult task that requires effort or skill.",
    "opportunity": "A favorable chance to do or achieve something.",
    "experience": "Knowledge or skill gained by doing something.",
    "problem": "A situation or question that needs to be solved.",
    "solution": "An answer or method for solving a problem.",
    "idea": "A thought, plan, or suggestion about something.",
    "business": "An organization or activity created to provide goods or services.",
    "company": "An organization that provides goods or services.",
    "startup": "A newly created business, often focused on developing a new product or service.",
    "money": "A medium used to buy goods and services.",
    "price": "The amount of money required to buy something.",
    "customer": "A person who buys or uses a product or service.",
    "product": "Something created or sold to satisfy a need or want.",
    "service": "An activity performed for someone in exchange for payment or benefit.",
    "market": "A place or system where buyers and sellers exchange goods or services.",
    "profit": "Money gained after subtracting costs from revenue.",
    "team": "A group of people working together toward a common goal.",
    "leader": "A person who guides or directs others.",
    "leadership": "The ability to guide, influence, or manage a group.",
    "communication": "The process of sharing information, thoughts, or ideas.",
    "friend": "A person whom you know and like.",
    "family": "A group of people related to one another.",
    "love": "A strong feeling of affection or care for someone or something.",
    "respect": "A feeling of admiration or consideration for someone.",
    "help": "To make something easier for someone or assist them.",
    "trust": "A strong belief that someone or something is reliable.",
    "time": "The ongoing sequence in which events happen.",
    "day": "A period of 24 hours.",
    "night": "The period of darkness between evening and morning.",
    "morning": "The early part of the day.",
    "energy": "The ability to do work or cause change.",
    "health": "The general condition of a person's physical and mental well-being.",
    "exercise": "Physical activity performed to improve or maintain fitness.",
    "food": "Something eaten or drunk to provide nutrition.",
    "book": "A written or printed work containing information, stories, or ideas.",
    "language": "A system of communication using words and symbols.",
    "word": "A unit of language with meaning.",
    "meaning": "What something represents, expresses, or refers to.",
    "question": "A sentence or phrase asking for information.",
    "answer": "A response to a question.",
    "life": "The condition that distinguishes living organisms from non-living things.",
    "world": "The earth and all the people, places, and things on it."
}


# ---------------- LOOKUP FUNCTION ----------------

def lookup():

    # Clear the text box
    my_text.delete(1.0, END)

    # Get the word entered by the user
    word = my_entry.get().lower().strip()

    # Check our dictionary
    if word in word_meanings:

        definition = word_meanings[word]

        my_text.insert(END, word.capitalize() + "\n\n")
        my_text.insert(END, definition)

    else:

        my_text.insert(
            END,
            "Word not found."
        )


# ---------------- GUI ----------------

my_labelframe = LabelFrame(
    root,
    text="Dictionary",
    padx=10,
    pady=10
)

my_labelframe.pack(pady=20)

# Enter word label
my_label = Label(
    my_labelframe,
    text="Enter word"
)

my_label.grid(row=0, column=0, padx=10, pady=10)

# Entry box
my_entry = Entry(
    my_labelframe,
    font=("Helvetica", 24)
)

my_entry.grid(
    row=0,
    column=1,
    padx=10,
    pady=10
)

# Translate / Search button
my_button = Button(
    my_labelframe,
    text="Translate",
    command=lookup
)

my_button.grid(
    row=1,
    column=0,
    columnspan=2,
    padx=10,
    pady=10
)

# Text box
my_text = Text(
    root,
    width=50,
    height=15,
    wrap=WORD
)

my_text.pack(pady=20)

# Start the GUI
root.mainloop()
