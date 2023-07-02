import turtle
import random

# Pencereyi oluşturma
window = turtle.Screen()
window.title("Turtle Oyunu")
window.bgcolor("white")
window.setup(width=800, height=600)
window.tracer(0)

# Skorları ve süreyi başlatma
score = 0
time_left = 20

# Skorboard'u oluşturma
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("black")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(-380, 260)
scoreboard.write("Puan: 0   Süre: 20", align="left", font=("Courier", 16, "normal"))

# Turtle'ı oluşturma
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()

# Puan alma fonksiyonu
def increase_score():
    global score
    score += 1
    scoreboard.clear()
    scoreboard.write("Puan: {}   Süre: {}".format(score, time_left), align="left", font=("Courier", 16, "normal"))

# Turtle'ın tıklandığında puanı artırma
def on_click(x, y):
    if player.distance(x, y) < 20:
        increase_score()

# Fare tıklamalarını dinleme
turtle.onscreenclick(on_click, 1)

# Turtle'ı rastgele yerlere hareket ettirme
def move_turtle():
    global time_left
    x = random.randint(-380, 380)  # Rastgele x koordinatı
    y = random.randint(-280, 280)  # Rastgele y koordinatı
    player.goto(x, y)
    time_left -= 0.5
    scoreboard.clear()
    scoreboard.write("Puan: {}   Süre: {}".format(score, int(time_left)), align="left", font=("Courier", 16, "normal"))
    if time_left <= 0:
        end_game()
    else:
        window.ontimer(move_turtle, 500)

# Oyunu bitirme
def end_game():
    scoreboard.clear()
    scoreboard.goto(0, 0)
    scoreboard.write("Oyun Bitti!", align="center", font=("Courier", 24, "bold"))

# Oyun döngüsünü başlatma
move_turtle()

# Ana döngü
while True:
    window.update()
