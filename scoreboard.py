from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("lawngreen")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-120,250)
        self.write("Player 1 ", align="center", font=("Bahnschrift", 40, "normal"))
        self.goto(150,250)
        self.write("Player 2 ", align="center", font=("Bahnschrift", 40, "normal"))
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Bahnschrift", 40, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Bahnschrift", 40, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
    
    def display_winner(self, winner):
        self.goto(0, 0)
        self.write("{} wins!".format(winner), align="center", font=("Bahnschrift", 36, "bold"))

class Scoreboard_ai(Turtle):
    def __init__(self):
        super().__init__()
        self.color("lawngreen")
        self.penup()
        self.hideturtle()
        self.player_score = 0
        self.computer_score = 0
        self.update_scoreboard_ai()

    def update_scoreboard_ai(self):
        self.clear()
        self.goto(-120,250)
        self.write("Computer ", align="center", font=("Bahnschrift", 40, "normal"))
        self.goto(150,250)
        self.write("Player ", align="center", font=("Bahnschrift", 40, "normal"))
        self.goto(-100, 200)
        self.write(self.computer_score, align="center", font=("Bahnschrift", 40, "normal"))
        self.goto(100, 200)
        self.write(self.player_score, align="center", font=("Bahnschrift", 40, "normal"))
    
    def computer_point(self):
        self.computer_score += 1
        self.update_scoreboard_ai()

    def player_point(self):
        self.player_score += 1
        self.update_scoreboard_ai()
    
    def display_winner_ai(self, winner):
        self.goto(0, 0)
        self.write("{} wins!".format(winner), align="center", font=("Bahnschrift", 36, "bold"))