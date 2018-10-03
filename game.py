
from player import *
from platform import *


class Game:
    def __init__(self):
        """Setup our game app"""
        pygame.display.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode(RATIO)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 24)
        self.running = False
        self.restartButton = pygame.K_r
        self.jumpKey = pygame.K_UP
        self.minWin = 1
        self.winTimer = 0
        self.countDownTimer = 10




    def newGame(self):
        """Setup a new game"""


        self.allSprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.player = Player(self)
        self.allSprites.add(self.player)

        self.readState = open(str("save.txt"), "r")

        if self.readState.read() == "return":
            self.player.rTimes = 7
            self.readState.close()
        else:
            self.readState.close()

        self.saveState = open(str("save.txt"), "w")


        for plat in PLATFORM_LIST:
            #Create a new platform
            p = Platform(*plat)
            self.allSprites.add(p)
            self.platforms.add(p)


    def run(self):
        """Run our app"""
        self.running = True
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0
            self.input()
            self.update(dt)
            self.draw()

    def input(self):
        """Process Input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_ESCAPE:
                    # self.running = False
                if event.key == self.jumpKey:
                    self.player.jump()
                if event.key == self.restartButton:
                    self.player.timer = 0
                    self.player.image.fill(PLAYER_COLOR)
                    self.player.rTimes += 1




    def update(self, dt):
        """We update our vars"""
        if self.player.rTimes > 14 or self.player.timer > 30:
            self.running = False

        if self.player.rTimes == 14:
            self.medal = pygame.image.load("medal.png")
            self.medal.convert_alpha()
            self.player.killTime = 999

        if 14 > self.player.rTimes > 9:
            self.player.killTime = 0.5

        if self.player.rTimes == 9:
            self.player.killTime = 7.5
            self.image = pygame.image.load("image.jpg")

        if self.player.rTimes == 8:
            self.player.killTime = 21.5
            if self.player.timer > 6:
                self.countDownTimer -= 1 * dt

        self.winTimer += 1 * dt
        self.allSprites.update(dt)

        if self.player.vel.y > 0: #If player is falling

            hits = pygame.sprite.spritecollide(self.player,\
                                               self.platforms,\
                                               False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
        if self.player.rTimes > 2:
            self.restartButton = pygame.K_i
        if self.player.timer > 10 and self.player.rTimes > 3:
                self.player.leftButton = pygame.K_a
                self.player.rightButton = pygame.K_d
                self.jumpKey = pygame.K_w
        if self.player.rTimes >= 7:
            self.player.leftButton = pygame.K_a
            self.player.rightButton = pygame.K_d
            self.jumpKey = pygame.K_w




# =========================================================
# =========================================================
# =========================================================

    def FirstStage(self):
        if 10 > self.player.timer > 5:
            self.werd_blit_cent(PSM, GREEN)
        elif self.player.timer > 10:
            self.werd_blit_cent(IWU, GREEN)

    def SecondStage(self):
        if self.player.timer < 5:
            self.werd_blit_cent(BRUH, GREEN)
        elif 10 > self.player.timer > 5:
            self.werd_blit_cent(YKNO, GREEN)
        elif self.player.timer > 10:
            self.werd_blit_cent(SEE, GREEN)

    def ThirdStage(self):
        if self.player.timer < 5:
            self.werd_blit_cent(RESTART, GREEN)
        elif 10 > self.player.timer > 5:
            self.werd_blit_cent(BUTTONCHANGE, GREEN)
        elif self.player.timer > 10:
            self.werd_blit_cent(FACE, GREEN)

    def FourthStage(self):
        if self.player.timer < 2.5:
            self.werd_blit_cent(YOU, RED)
        elif 5 > self.player.timer > 2.5:
            self.werd_blit_cent(BUTT, RED)
        elif 10 > self.player.timer > 5:
            self.werd_blit_cent(FINE, GREEN)
        elif self.player.timer > 10:
            self.werd_blit_cent(CHANGECONTROLS, GREEN)

    def FifthStage(self):
        if 1.25 < self.player.timer < 3.5:
            self.werd_blit_cent(SMART, GREEN)
        elif 5.5 > self.player.timer > 3.5:
            self.werd_blit_cent(KTHEN, GREEN)
            self.winTimer = 0
        elif 10 > self.player.timer > 5.5:
            self.werd_blit_cent(BYE, GREEN)
        elif self.player.timer > 10 and self.winTimer < 20:
            pygame.display.iconify()
            self.minWin -= 1

    def SixthStage(self):
        if 1.25 < self.player.timer < 2.5:
            self.werd_blit_cent(HOW, GREEN)
        elif 5 > self.player.timer > 2.5:
            self.werd_blit_cent(LOOK, GREEN)
        elif 7.5 > self.player.timer > 5:
            self.werd_blit_cent(GUESS, GREEN)
        elif 10 > self.player.timer > 7.5:
            self.werd_blit_cent(QUIT, RED)
        elif self.player.timer > 10:
            self.saveState.write("return")
            self.saveState.close()
            self.running = False

    def SeventhStage(self):
        if self.player.timer < 2.5:
            self.werd_blit_cent(PERSISTENT, GREEN)
        elif 5 > self.player.timer > 2.5:
            self.werd_blit_cent(UGH, GREEN)
        elif 7.5 > self.player.timer > 5:
            self.werd_blit_cent(LET, GREEN)
        elif self.player.timer > 8:
            self.werd_blit_cent(PSM2, GREEN)

    def EighthStage(self):
        if self.player.timer < 2.5:
            self.werd_blit_cent(KEEP, GREEN)
        elif 5 > self.player.timer > 2.5:
            self.werd_blit_cent(ILL, GREEN)
        elif 16 > self.player.timer > 5:
            self.werd_blit_cent(str(int(self.countDownTimer)), RED)
        elif 18.5 > self.player.timer > 16:
            self.werd_blit_cent(EMPTY, GREEN)
        elif 19 > self.player.timer > 18.5:
            self.werd_blit_cent(DOT, GREEN)
        elif 19.5 > self.player.timer > 19:
            self.werd_blit_cent(DOTDOT, GREEN)
        elif 20 > self.player.timer > 19.5:
            self.werd_blit_cent(DOTDOTDOT, GREEN)

        elif 20.5 > self.player.timer > 20:
            self.werd_blit_cent(DOT, GREEN)
        elif 21 > self.player.timer > 20.5:
            self.werd_blit_cent(DOTDOT, GREEN)
        elif 21.5 > self.player.timer > 21:
            self.werd_blit_cent(DOTDOTDOT, GREEN)
        elif self.player.timer > 21.5:
            self.werd_blit_cent(STOP, RED)

    def NinthStage(self):
        if self.player.timer < 1.5:
            self.werd_blit_cent(UGH, GREEN)
        elif 2.5 > self.player.timer > 1.5:
            self.werd_blit_cent(AGAIN, GREEN)
        elif 5.5 > self.player.timer > 3.5:
            self.werd_blit_cent(KILLME, GREEN)
        elif 7 > self.player.timer > 5.5:
            self.screen.blit(self.image, (WIDTH / 2 - self.image.get_size()[0] / 2, HEIGHT / 2 - self.image.get_size()[1] / 2))
        elif self.player.timer > 7.5:
            pass

    def TenthStage(self):
        self.werd_blit_cent(JUST, RED)

    def EleventhStage(self):
        self.werd_blit_cent(GIVE, RED)

    def TwelvethStage(self):
        self.werd_blit_cent(ME, RED)

    def ThirteenthStage(self):
        self.werd_blit_cent(STOPYOU, RED)

    def Fourtheenth(self):
        if self.player.timer < 2:
            self.werd_blit_cent(WANT, GREEN)
        elif 3 > self.player.timer > 2:
            self.werd_blit_cent(MEDAL, GREEN)
        elif 5 > self.player.timer > 3:
            self.werd_blit_cent(HERE, GREEN)
        elif self.player.timer > 5:
            string = self.font.render(WIN, 1, BLUE)
            stringSize = self.font.size(WIN)

            string2 = self.font.render(THEEND, 1, BLUE)
            string2Size = self.font.size(THEEND)
            self.screen.blit(self.medal,
                             (WIDTH / 2 - self.medal.get_size()[0] / 2, HEIGHT / 2 - self.medal.get_size()[1] / 2))

            self.screen.blit(string, (WIDTH / 2 - stringSize[0] / 2, HEIGHT / 2 - 50))
            self.screen.blit(string2, (WIDTH / 2 - string2Size[0] / 2, HEIGHT / 2 - 25))



    def draw(self):
        """Draw the game scene"""
        self.screen.fill(BGCOLOR)
        #Draw all game objects
        self.allSprites.draw(self.screen)

        if self.player.rTimes == 1:
            self.FirstStage()
        if self.player.rTimes == 2:
            self.SecondStage()
        if self.player.rTimes == 3:
            self.ThirdStage()
        if self.player.rTimes == 4:
            self.FourthStage()
        if self.player.rTimes == 5:
            self.FifthStage()
        if self.player.rTimes == 6:
            self.SixthStage()
        if self.player.rTimes == 7:
            self.SeventhStage()
        if self.player.rTimes == 8:
            self.EighthStage()
        if self.player.rTimes == 9:
            self.NinthStage()
        if self.player.rTimes == 10:
            self.TenthStage()
        if self.player.rTimes == 11:
            self.EleventhStage()
        if self.player.rTimes == 12:
            self.TwelvethStage()
        if self.player.rTimes == 13:
            self.ThirteenthStage()
        if self.player.rTimes == 14:
            self.Fourtheenth()


        pygame.display.update()

    def werd_blit_cent(self, s1, color):
        string = self.font.render(s1, 1, color)
        stringSize = self.font.size(s1)

        self.screen.blit(string, (WIDTH / 2 - stringSize[0] / 2, HEIGHT / 2 - stringSize[1] / 2))
