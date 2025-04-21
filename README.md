# 🎮 Tic-Tac-Toe AI

This project is focused on building an AI agent that plays Tic-Tac-Toe optimally using the **Minimax algorithm**.

---

## 🧠 Project Overview

This AI is designed for a **deterministic**, **perfect-information**, **zero-sum** game environment — exactly the kind of scenario foundational to many classic AI problems.

The AI agent uses **recursive adversarial search** (Minimax) to simulate every possible game state, evaluate outcomes, and always choose the best guaranteed move assuming an optimal opponent.

> ⚠️ It will either win or draw — **never lose.**

This project puts into practice key AI principles that scale to more complex problems like:

- Chess and Go engines
- Real-time strategy AI
- Tactical planning agents
- Search-based decision systems

---

## 🛠️ Features

- ✅ Intelligent AI using Minimax
- ✅ Recursive evaluation of game trees
- ✅ Interactive gameplay via Pygame UI
- ✅ Core functions written from scratch

---

## 🧪 AI Concepts Applied

| Concept                  | Description                                                 |
|--------------------------|-------------------------------------------------------------|
| **Minimax Algorithm**    | Explores all possible game outcomes to minimize loss        |
| **Adversarial Search**   | Assumes opponent plays optimally                            |
| **Game Trees**           | Builds complete decision paths for each player              |
| **Utility Evaluation**   | Assigns numeric scores to terminal states                   |
| **Turn-Based Simulation**| Alternates player turns based on board state                |

---

## 📁 Project Structure

| File            | Description                                 |
|-----------------|---------------------------------------------|
| `tictactoe.py`  | AI logic, game rules, and core functionality|
| `runner.py`     | Simple UI to play against the AI (via Pygame)|
| `requirements.txt` | Project dependencies (mainly `pygame`)   |

---

## 🚀 Getting Started

Follow these steps to set up and run the project on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/tic-tac-toe-ai.git
cd tic-tac-toe-ai
```

### 2. Create a Virtual Environment (Recommended)

```bash
python3 -m venv .venv
```

### 3. Activate the Virtual Environment

```bash
source .venv/bin/activate
```
On Windows, use:
```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Game

```bash
python3 runner.py
```