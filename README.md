# 🃏 Blackjack Card Counter — Hi-Lo System

> Terminal-based blackjack card counter using the Hi-Lo system. Enter card ranks as they're dealt — get live running count, true count, and betting signals.

---

## 📌 Overview

A Python-based simulation of Blackjack enhanced with the **Hi-Lo card counting strategy**. It demonstrates how statistical techniques can be applied to track card distributions and gain a strategic edge in decision-making.

Enter cards by rank as you see them dealt at the table, and the counter tracks your running count, true count, and gives you a live betting signal in real time.

---

## 🧠 How It Works — Hi-Lo System

The Hi-Lo system assigns a value to every card:

| Cards          | Count Value |
|----------------|-------------|
| 2, 3, 4, 5, 6  | +1          |
| 7, 8, 9        | 0           |
| 10, J, Q, K, A | −1          |

- **Running Count** — cumulative sum of all card values seen so far
- **True Count** — running count divided by decks remaining (adjusts for deck penetration)
- **Betting Signal** — actionable suggestion based on the true count

---

## ⚙️ Features

- 🎮 Simulates standard Blackjack gameplay
- 🔢 Real-time running count calculation
- 📊 True count conversion for better accuracy
- ♠️ Single-deck shoe simulation with card tracking
- 🧮 Deck awareness — warns when a rank is exhausted

---

## 🛠️ Tech Stack

- Python 3.6+
- Standard libraries only (`random`) — no installs needed

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/blackjack-hilo.git
```

2. Navigate to the project folder:

```bash
cd blackjack-hilo
```

3. Run the script:

```bash
python blackjack_hilo.py
```

### Interactive Session

Once running, type a card rank and press Enter to register it:

```
> A        # Ace dealt
> 10       # Ten dealt
> J        # Jack dealt
> 5        # Five dealt
```

**Valid ranks:** `A  2  3  4  5  6  7  8  9  10  J  Q  K`  
Suits are not needed — they have no effect on the Hi-Lo count.

### Commands

| Input          | Action                                        |
|----------------|-----------------------------------------------|
| `A`, `2` … `K` | Register a card by rank                       |
| `?`            | Show how many of each rank remain in the deck |
| `r`            | Shuffle a fresh deck and reset all counts     |
| `q`            | Quit                                          |

---

## 🎮 Demo Mode

Auto-deals a set number of cards and prints the full count progression:

```bash
python blackjack_hilo.py --demo          # deals 20 cards
python blackjack_hilo.py --demo 35       # deals 35 cards
```

Sample output:

```
  Card   Value   Running     True  Signal
  ───────────────────────────────────────────────────────
  K         -1        -1    -1.04  🔴
  5         +1         0    +0.00  ⚪
  3         +1        +1    +1.05  🟡
  A         -1         0    +0.00  ⚪
```

---

## 📈 Betting Signals

| Signal | True Count | Advice                  |
|--------|------------|-------------------------|
| 🔴     | < 0        | Bet minimum or sit out  |
| ⚪     | 0 – 1      | Flat bet, no clear edge |
| 🟡     | 1 – 2      | Consider a small raise  |
| 🟢     | 2 – 3      | Raise your bet          |
| 🔵     | 3+         | Max bet!                |

---

## 🔮 Future Improvements

- Add GUI (Tkinter / Pygame / Streamlit)
- Implement advanced strategies (e.g., Wonging)
- Add betting strategy simulation
- Visualize count trends using graphs
- Multi-deck shoe support

---

## 📚 Learning Outcomes

- Applied probability concepts in a real-world scenario
- Implemented game logic and simulation in Python
- Understood statistical advantage in card games
- Practised clean, modular Python design

---

## 📁 File Structure

```
blackjack_hilo.py   # Main script — all logic in one file
README.md           # This file
```

---

## ⚠️ Disclaimer

This project is for **educational purposes only** and does not promote or encourage gambling.

---
