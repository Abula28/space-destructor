# 🌌 Space Destructor

Space Destructor is a thrilling 2D arcade-style game built with Python and Pygame. Your mission: destroy as many enemy spaceships as possible by firing bullets while avoiding deadly collisions. The game intensifies as the number of enemies grows with your score. Are you ready for the challenge?

---

## 🚀 Features

- **🎮 Player Movement:** Navigate your spaceship left and right using the arrow keys.
- **🔫 Shooting Bullets:** Fire powerful bullets with the spacebar to obliterate enemy spaceships.
- **📈 Dynamic Difficulty:** The game grows harder as new enemies appear every time you score 3 points.
- **💀 Game Over State:** The game ends when you collide with an enemy, displaying a "Game Over" message and your final score.
- **🏆 Score Display:** Track your current score on the screen as you progress.

---

## 🛠️ Prerequisites

Before playing, ensure you have the following installed:

- Python 3.6 or higher
- Pygame library

Install Pygame with:

```bash
pip install pygame
```

---

## 🎮 How to Play

1. Clone or download the repository to your computer.
2. Make sure these assets are in the same directory as the game script:
   - `background.jpg`: Game background image.
   - `player.png`: Image of the player's spaceship.
   - `enemy.png`: Image of enemy spaceships.
   - `bullet.png`: Image of bullets.
3. Run the game script with Python:

```bash
python3 space_destructor.py
```

---

## 🎛️ Controls

- **⬅️ Left Arrow Key:** Move the player spaceship to the left.
- **➡️ Right Arrow Key:** Move the player spaceship to the right.
- **⏹️ Spacebar:** Fire bullets.

---

## ⚙️ Game Mechanics

1. **🕹️ Player Movement:**
   - The player can move horizontally within the screen's boundaries.

2. **💥 Shooting Bullets:**
   - Fire bullets from your spaceship to destroy enemies.
   - Only one bullet can be active at a time.

3. **👾 Enemies:**
   - Enemies move horizontally and descend vertically when they reach the screen's edges.
   - Colliding with an enemy ends the game.

4. **📊 Score and Difficulty:**
   - Gain 1 point for each destroyed enemy.
   - Every 3 points, an additional enemy spawns to increase the difficulty.

5. **⚠️ Game Over:**
   - Colliding with an enemy stops the game and displays your final score alongside a "Game Over" message.

---

## 📸 Screenshots

### Gameplay in Action

![Gameplay Screenshot](https://github.com/user-attachments/assets/14b66e30-8aed-4e3d-815b-6ace657bcc14)
![Enemies Approaching](https://github.com/user-attachments/assets/0a2ccb7b-7634-49e5-9702-e839d0d103c8)
![Game Over](https://github.com/user-attachments/assets/9ebb7d04-8646-4a1d-a3e1-64d386ed8a09)

---

## 🌟 Future Improvements

- Introduce multiple levels with escalating difficulty.
- Add exciting power-ups to aid the player.
- Implement sound effects for shooting, destruction, and collisions.
- Create a main menu and pause functionality for better user experience.
- Develop a high score tracking system to save and display top scores.

---

## 🙏 Acknowledgments

- Built with ❤️ using [Pygame](https://www.pygame.org/).
- Inspired by classic arcade games that defined a generation of fun.

---

🎉 Enjoy Space Destructor and may your reflexes guide you to victory!

