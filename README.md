# ⚓ Sank - Python GUI Naval Battle Game

Sank is a desktop naval battle game (similar to Battleship) built entirely in Python using `tkinter`. Challenge a smart computer opponent in this visually rich, interactive game experience.

![image](https://github.com/user-attachments/assets/4eb30b89-1853-42e2-ba71-c9e37970e8de)

---

## 🎮 Game Features

- **Dual 7x7 Grid Boards**:
  - Your Fleet board shows your ships (🚢), enemy hits (💥), and misses (💧).
  - Enemy Waters board allows targeting with a crosshair cursor.
- **Turn-based Gameplay**:
  - Fire at enemy waters and watch the computer respond.
  - Auto computer turns after a miss.
- **Win Conditions**:
  - Sink all 4 enemy ships before they sink yours.
  - Game over screen with replay option.

---

## 🎨 Visual Design

- **Naval theme** with ocean blue gradients.
- **Color-coded grid cells**:
  - Green: 🚢 Your Ship  
  - Red: 💥 Hit  
  - Gray: 💧 Miss  
  - Dark: ⬜ Unknown
- **Interactive Buttons**:
  - Hover effects and crosshair cursor for enemy waters.
- **Legend and Status Bar**:
  - Shows symbol meaning and real-time game messages.

---

## ⚓ Gameplay

- Click on the enemy board to fire.
- Visual feedback: 💥 for hits, 💧 for misses, 🚢 for ships.
- Computer uses a simple AI to shoot back automatically.
- The game ends when all 4 ships of either side are sunk.

---

## 🔧 Controls

- `🔄 New Game`: Restart the game with new ship placements.
- `❌ Quit`: Exit the game.
- **Auto prompt to replay** when game ends.

---

## 💻 Technical Details

- **Written in Python 3** using only the built-in `tkinter` library.
- Responsive GUI with status updates.
- Clean and modular codebase.
- Proper error handling for repeated shots and edge cases.

---

## 🖥️ Installation & Usage

1. **Install Python 3.x** if not already installed.
2. **Clone this repo**:

  ```bash
   git clone https://github.com/Kalharapasan/Sank_Naval_Battle_Game_Using_python.git
   cd Sank_Naval_Battle_Game_Using_python
 ```
🚀 Future Improvements (optional)
Smarter AI with strategy-based targeting

Sound effects and animations

Multiplayer (local or online)

📄 License
This project is licensed under the MIT License.

🧑‍💻 Author
Your Name
Made with ❤️ in Python
GitHub
