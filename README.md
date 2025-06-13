

## 🕹️ Hangman Game – Python Terminal Version

Welcome to the classic **Hangman** game implemented in Python!
Try to guess the secret word one letter at a time before you run out of tries.

---

### 📁 Files Included

* `hangman.py` – The main Python script to run the game.

---

### 🛠️ Requirements

* Python 3.x installed on your machine
* No additional libraries required (only built-in modules)

---

### ▶️ How to Run

1. **Clone or Download** this repository.
2. Open a terminal and navigate to the directory.
3. Run the following command:

```bash
python hangman.py
```

---

### 🎮 How to Play

* The game randomly selects a word from a predefined list.
* You have **6 tries** to guess the correct word.
* Enter one letter at a time.
* The game will show your progress using underscores (`_`) for unguessed letters.
* If you guess all letters correctly, you win!
* If you run out of tries, the game ends and reveals the word.

---

### ✏️ Example

```
Welcome to Hangman!

Word: _ _ _ _ _ _
Tries left: 6
Guess a letter: a
Correct!

Word: _ a _ _ _ _
Tries left: 6
Guess a letter: z
Wrong guess.
```

---

### 📌 Notes

* Only single alphabetic characters are accepted.
* Repeating a guessed letter will show a warning.
* Words are currently chosen from a small built-in list.

---

### 📃 License

This project is provided for educational and personal use.

