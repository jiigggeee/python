from Question import Question

question_prompts = [
    "What day of the week is named after the Norse god Odin?\n(a) Monday\n(b) Tuesday\n(c) Wednesday\n(d) Sunday\n\n",
    "Who is the god of thunder?\n(a) Baldur \n(b) Snorri\n(c) Thor\n(d) Fenrir\n\n",
    "What group of people inhabited the island of Crete?\n(a) Minoans\n(b) Phoenicians\n(c) Trojans\n(d) Spartans\n\n"
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + " / " + str(len(questions)) + " correct")

run_test(questions)