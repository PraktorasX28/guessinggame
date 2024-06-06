# Το chatgpt το Χρησιμοποίησα σε κάποια σημία ώστε να κάνει ποιό καλογρμένο το κώδικα
from flask import Flask, render_template, request, session
import random
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
results_file = 'results.txt'
x = random.randint(0, 128)

# Όπως εδω
my_list1 = [x - i for i in range(1, 11)]
my_list2 = [x + i for i in range(1, 11)]
my_list3 = [x - i for i in range(1, 6)]
my_list4 = [x + i for i in range(1, 6)]


def check_guess(x, y):
    if y == x:
        message = f"Συγχαρητήρια! Ο αριθμός ήταν {x}"
        with open(results_file, 'a') as file:
            file.write(f"Μάντεψες τον αριθμο {x} σωστά !\n")

    elif y < 0 or y > 128:
        message = "Ο αριθμός είναι ανάμεσα στο 0 και το 128"

    elif 9 < x < 100 and (y < 10 or y >= 100):
        message = "Ο αριθμός είναι διψήφιος"

    elif x >= 100 and y < 100:
        message = "Ο αριθμός είναι τριψήφιος"

    elif x < 10 and y >= 10:
        message = "Ο αριθμός είναι μονοψήφιος"

    elif x > y:
        if y in my_list1:
            message = "Ο αριθμός βρισκέται μέσα σε κλίμακα των 10"
            if y in my_list3:  # Όπως εδω
                message += f" Και ο αριθμός είναι  {'άρτιος' if x % 2 == 0 else 'περιττός'}"
        else:
            message = "Ο αριθμός σου είναι μικρότερος απο το τυχαίο"

    elif x < y:
        if y in my_list2:
            message = "Ο αριθμός βρισκέται μέσα σε κλίμακα των 10"
            if y in my_list4:  # Όπως εδω
                message += f" Και ο αριθμός είναι  {'άρτιος' if x % 2 == 0 else 'περιττός'}"
        else:
            message = "Ο αριθμός σου είναι μεγαλύτερος απο το τυχαίο"

    return message


@app.route('/', methods=["GET", "POST"])
def guessthenumber():
    message = ""
    
    if request.method == "POST":
        try:
            y = int(request.form["guess"])
            message = check_guess(x, y)
        except ValueError:
            message = "Εισάγεται έναν έγκυρο αριθμό."
            
    return render_template("guess.html", message=message)

if __name__ == '__main__':
    app.run(debug=True)