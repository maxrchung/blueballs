import pygame, sys
import random

Play = True
GameOver = False
lightBlue = False

class SimpleSprite(pygame.sprite.Sprite):
    def __init__(self, imagePath, dimension, positions):
        imageSurface = pygame.image.load(imagePath)
        imageSurface.set_colorkey( (0, 0, 0) )
        self.surfaces = []
        for pos in positions:
            rect = pygame.Rect(pos[0], pos[1], dimension[0], dimension[1])
            self.surfaces.append(imageSurface.subsurface(rect))
        self.index = 0
        self.image = self.surfaces[self.index]

    def update(self):
        self.index = self.index + 1
        if self.index == (len(self.surfaces) - 1):
            self.index = 0
        self.image = self.surfaces[self.index]

wasd = pygame.image.load('./wasd.png')
wasdX = 1280/7 - wasd.get_width()/2
wasdY = 720/2 - wasd.get_height()/2
arrows = pygame.image.load('./arrows.png')
arrowsX = 1280*6/7 - wasd.get_width()/2
arrowsY = 720/2 - wasd.get_height()/2
lightBlueWins = pygame.image.load('./lightBlueWins.png')
darkBlueWins = pygame.image.load('./darkBlueWins.png')
back = pygame.image.load('./blueBallsBackdrop.png')
backX = 1280/2 - back.get_width()/2
backY = 720/2 - back.get_height()/2
ball1 = SimpleSprite('./ball1.png', (25, 25), [[0, 0]])
ball2 = SimpleSprite('./ball2.png', (25, 25), [[0, 0]])
safety_paddle = SimpleSprite('./safety_paddle.png', (1280, 15), [[0, 0]])
platform1 = SimpleSprite('./platform1.png', (125, 15), [[0, 0]])
platform2 = SimpleSprite('./platform2.png', (125, 15), [[0, 0]])
platform3 = SimpleSprite('./platform3.png', (125, 15), [[0, 0]])
platform4 = SimpleSprite('./platform4.png', (125, 15), [[0, 0]])
platform5 = SimpleSprite('./platform5.png', (125, 15), [[0, 0]])
platform6 = SimpleSprite('./platform6.png', (125, 15), [[0, 0]])
platform7 = SimpleSprite('./platform7.png', (125, 15), [[0, 0]])
platform8 = SimpleSprite('./platform8.png', (125, 15), [[0, 0]])
platform9 = SimpleSprite('./platform9.png', (125, 15), [[0, 0]])
platform0 = SimpleSprite('./platform0.png', (125, 15), [[0, 0]])

pygame.init()
pygame.key.set_repeat(1, 1)

_display = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Blue Balls')

while True:
    if Play:
        lightBlue = False
        mainClock = pygame.time.Clock()
        ball1X = (1280 - 25 + 25) / 2
        ball1Y = 0 - 25
        ball1MotionY = 0.20
        ball2X = (1280 - 25 - 25) / 2
        ball2Y = 0 - 25
        ball2MotionY = 0.20
        safety_paddleX = 0
        safety_paddleY = 720 - 15
        platform1X = random.choice([0 - 125, 1280])
        platform1Y = 50+60 + random.randint(-5, 5)
        platform1Speed = random.randint(3, 10)
        platform2X = random.choice([0 - 125, 1280])
        platform2Y = 50+60*2 + random.randint(-5, 5)
        platform2Speed = random.randint(3, 10)
        platform3X = random.choice([0 - 125, 1280])
        platform3Y = 50+60*3 + random.randint(-5, 5)
        platform3Speed = random.randint(2, 9)
        platform4X = random.choice([0 - 125, 1280])
        platform4Y = 50+60*4 + random.randint(-5, 5)
        platform4Speed = random.randint(2, 9)
        platform5X = random.choice([0 - 125, 1280])
        platform5Y = 50+60*5 + random.randint(-5, 5)
        platform5Speed = random.randint(2, 9)
        platform6X = random.choice([0 - 125, 1280])
        platform6Y = 50+60*6 + random.randint(-5, 5)
        platform6Speed = random.randint(2, 9)
        platform7X = random.choice([0 - 125, 1280])
        platform7Y = 50+60*7 + random.randint(-5, 5)
        platform7Speed = random.randint(1, 8)
        platform8X = random.choice([0 - 125, 1280])
        platform8Y = 50+60*8 + random.randint(-5, 5)
        platform8Speed = random.randint(1, 8)
        platform9X = random.choice([0 - 125, 1280])
        platform9Y = 50+60*9 + random.randint(-5, 5)
        platform9Speed = random.randint(1, 8)
        platform0X = random.choice([0 - 125, 1280])
        platform0Y = 50+60*10 + random.randint(-5, 5)
        platform0Speed = random.randint(1, 8)
        platform1Direction = 1
        platform2Direction = 1
        platform3Direction = 1
        platform4Direction = 1
        platform5Direction = 1
        platform6Direction = 1
        platform7Direction = 1
        platform8Direction = 1
        platform9Direction = 1
        platform0Direction = 1

        if platform1X < 0:
            platform1Direction = -1
        if platform2X < 0:
            platform2Direction = -1
        if platform2X < 0:
            platform2Direction = -1
        if platform3X < 0:
            platform3Direction = -1
        if platform4X < 0:
            platform4Direction = -1
        if platform5X < 0:
            platform5Direction = -1
        if platform6X < 0:
            platform6Direction = -1
        if platform7X < 0:
            platform7Direction = -1
        if platform8X < 0:
            platform8Direction = -1
        if platform9X < 0:
            platform9Direction = -1
        if platform0X < 0:
            platform0Direction = -1

        jump1Counter = 0
        canJump1 = False
        jump1 = False
        jump2Counter = 0
        canJump2 = False
        jump2 = False
        display1 = random.randint(0, 255)
        display2 = random.randint(0, 255)
        display3 = random.randint(0, 255)
        display2Get = True
        display1Get = True

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key==pygame.K_F4:
                        if pygame.get.get_pressed()[K_RALT] or pygame.key.get_pressed()[K_LALT]:
                            pygame.quit()
                            sys.exit()

            platform1X -= platform1Speed * platform1Direction
            platform2X -= platform2Speed * platform2Direction
            platform3X -= platform3Speed * platform3Direction
            platform4X -= platform4Speed * platform4Direction
            platform5X -= platform5Speed * platform5Direction
            platform6X -= platform6Speed * platform6Direction
            platform7X -= platform7Speed * platform7Direction
            platform8X -= platform8Speed * platform8Direction
            platform9X -= platform9Speed * platform9Direction
            platform0X -= platform0Speed * platform0Direction

            if platform1X < -125:
                platform1X = random.choice([0 - 125, 1280])
                platform1Y = 50+60 + random.randint(-5, 5)
                platform1Speed = random.randint(3, 10)
                platform1Direction = 1
                if platform1X < 0:
                    platform1Direction = -1
            elif platform1X > 1280:
                platform1X = random.choice([0 - 125, 1280])
                platform1Y = 50+60 + random.randint(-5, 5)
                platform1Speed = random.randint(3, 10)
                platform1Direction = 1
                if platform1X < 0:
                    platform1Direction = -1
            if platform2X < -125:
                platform2X = random.choice([0 - 125, 1280])
                platform2Y = 50+60*2 + random.randint(-5, 5)
                platform2Speed = random.randint(3, 10)
                platform2Direction = 1
                if platform2X < 0:
                    platform2Direction = -1
            elif platform2X > 1280:
                platform2X = random.choice([0 - 125, 1280])
                platform2Y = 50+60*2 + random.randint(-5, 5)
                platform2Speed = random.randint(3, 10)
                platform2Direction = 1
                if platform2X < 0:
                    platform2Direction = -1
            if platform3X < -125:
                platform3X = random.choice([0 - 125, 1280])
                platform3Y = 50+60*3 + random.randint(-5, 5)
                platform3Speed = random.randint(2, 9)
                platform3Direction = 1
                if platform3X < 0:
                    platform3Direction = -1
            elif platform3X > 1280:
                platform3X = random.choice([0 - 125, 1280])
                platform3Y = 50+60*3 + random.randint(-5, 5)
                platform3Speed = random.randint(2, 9)
                platform3Direction = 1
                if platform3X < 0:
                    platform3Direction = -1
            if platform4X < -125:
                platform4X = random.choice([0 - 125, 1280])
                platform4Y = 50+60*4 + random.randint(-5, 5)
                platform4Speed = random.randint(2, 9)
                platform4Direction = 1
                if platform4X < 0:
                    platform4Direction = -1
            elif platform4X > 1280:
                platform4X = random.choice([0 - 125, 1280])
                platform4Y = 50+60*4 + random.randint(-5, 5)
                platform4Speed = random.randint(2, 9)
                platform4Direction = 1
                if platform4X < 0:
                    platform4Direction = -1
            if platform5X < -125:
                platform5X = random.choice([0 - 125, 1280])
                platform5Y = 50+60*5 + random.randint(-5, 5)
                platform5Speed = random.randint(2, 9)
                platform5Direction = 1
                if platform5X < 0:
                    platform5Direction = -1
            elif platform5X > 1280:
                platform5X = random.choice([0 - 125, 1280])
                platform5Y = 50+60*5 + random.randint(-5, 5)
                platform5Speed = random.randint(2, 9)
                platform5Direction = 1
                if platform5X < 0:
                    platform5Direction = -1
            if platform6X < -125:
                platform6X = random.choice([0 - 125, 1280])
                platform6Y = 50+60*6 + random.randint(-5, 5)
                platform6Speed = random.randint(2, 9)
                platform6Direction = 1
                if platform6X < 0:
                    platform6Direction = -1
            elif platform6X > 1280:
                platform6X = random.choice([0 - 125, 1280])
                platform6Y = 50+60*6 + random.randint(-5, 5)
                platform6Speed = random.randint(2, 9)
                platform6Direction = 1
                if platform6X < 0:
                    platform6Direction = -1
            if platform7X < -125:
                platform7X = random.choice([0 - 125, 1280])
                platform7Y = 50+60*7 + random.randint(-5, 5)
                platform7Speed = random.randint(1, 8)
                platform7Direction = 1
                if platform7X < 0:
                    platform7Direction = -1
            elif platform7X > 1280:
                platform7X = random.choice([0 - 125, 1280])
                platform7Y = 50+60*7 + random.randint(-5, 5)
                platform7Speed = random.randint(1, 8)
                platform7Direction = 1
                if platform7X < 0:
                    platform7Direction = -1
            if platform8X < -125:
                platform8X = random.choice([0 - 125, 1280])
                platform8Y = 50+60*8 + random.randint(-5, 5)
                platform8Speed = random.randint(1, 8)
                platform8Direction = 1
                if platform8X < 0:
                    platform8Direction = -1
            elif platform8X > 1280:
                platform8X = random.choice([0 - 125, 1280])
                platform8Y = 50+60*8 + random.randint(-5, 5)
                platform8Speed = random.randint(1, 8)
                platform8Direction = 1
                if platform8X < 0:
                    platform8Direction = -1
            if platform9X < -125:
                platform9X = random.choice([0 - 125, 1280])
                platform9Y = 50+60*9 + random.randint(-5, 5)
                platform9Speed = random.randint(1, 8)
                platform9Direction = 1
                if platform9X < 0:
                    platform9Direction = -1
            elif platform9X > 1280:
                platform9X = random.choice([0 - 125, 1280])
                platform9Y = 50+60*9 + random.randint(-5, 5)
                platform9Speed = random.randint(1, 8)
                platform9Direction = 1
                if platform9X < 0:
                    platform9Direction = -1
            if platform0X < -125:
                platform0X = random.choice([0 - 125, 1280])
                platform0Y = 50+60*10 + random.randint(-5, 5)
                platform0Speed = random.randint(1, 8)
                platform0Direction = 1
                if platform6X < 0:
                    platform0Direction = -1
            elif platform0X > 1280:
                platform0X = random.choice([0 - 125, 1280])
                platform0Y = 50+60*10 + random.randint(-5, 5)
                platform0Speed = random.randint(1, 8)
                platform0Direction = 1
                if platform0X < 0:
                    platform0Direction = -1

            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                ball1X -= 6
            elif key[pygame.K_RIGHT]:
                ball1X += 6
            if key[pygame.K_a]:
                ball2X -= 6
            elif key[pygame.K_d]:
                ball2X += 6
            if canJump2:
                if key[pygame.K_w]:
                    jump2Counter = 2.38
                    canJump2 = False
                    jump2 = True
                    display2Get = True
            if canJump1:
                if key[pygame.K_UP]:
                    jump1Counter = 2.38
                    canJump1 = False
                    jump1 = True
                    display1Get = True

            safety_paddleRect = pygame.Rect(safety_paddleX, safety_paddleY, 1280, 15)
            platform1Rect = pygame.Rect(platform1X, platform1Y, 125, 15)
            platform2Rect = pygame.Rect(platform2X, platform2Y, 125, 15)
            platform3Rect = pygame.Rect(platform3X, platform3Y, 125, 15)
            platform4Rect = pygame.Rect(platform4X, platform4Y, 125, 15)
            platform5Rect = pygame.Rect(platform5X, platform5Y, 125, 15)
            platform6Rect = pygame.Rect(platform6X, platform6Y, 125, 15)
            platform7Rect = pygame.Rect(platform7X, platform7Y, 125, 15)
            platform8Rect = pygame.Rect(platform8X, platform8Y, 125, 15)
            platform9Rect = pygame.Rect(platform9X, platform9Y, 125, 15)
            platform0Rect = pygame.Rect(platform0X, platform0Y, 125, 15)

            ball1Y += ball1MotionY
            ball1MotionY += 0.60
            ball2Y += ball2MotionY
            ball2MotionY += 0.60

            if ball1MotionY >= 7:
                ball1MotionY = 7
            if ball2MotionY >= 7:
                ball2MotionY = 7

            if jump1:
                ball1MotionY -= jump1Counter
                jump1Counter -= 0.15
                if ball1MotionY > 0.20:
                    jump1 = False
            else:
                if safety_paddleRect.collidepoint(ball1X + 25/2, ball1Y+25):
                    ball1Y = safety_paddleY - 25
                    ball1MotionY = 0
                    canJump1 = True
                elif platform1Rect.collidepoint(ball1X + 25/2, ball1Y+25):
                    ball1Y = platform1Y - 25
                    ball1MotionY = 0
                    canJump1 = True
                    if display1Get:
                        display1Get = False
                        display1 += 10
                        display2 += 10
                        display3 += 10
                elif platform2Rect.collidepoint(ball1X + 25/2, ball1Y+25):
                    ball1Y = platform2Y - 25
                    ball1MotionY = 0
                    canJump1 = True
                    if display1Get:
                        display1Get = False
                        display1 += 9
                        display2 += 9
                        display3 += 9
                elif platform3Rect.collidepoint(ball1X + 25/2, ball1Y+25):
                    ball1Y = platform3Y - 25
                    ball1MotionY = 0
                    canJump1 = True
                    if display1Get:
                        display1Get = False
                        display1 += 8
                        display2 += 8
                        display3 += 8
                elif platform4Rect.collidepoint(ball1X + 25/2, ball1Y+25):
                    ball1Y = platform4Y - 25
                    ball1MotionY = 0
                    canJump1 = True
                    if display1Get:
                        display1 += 7
                        display2 += 7
                        display3 += 7
                        display1Get = False
                elif platform5Rect.collidepoint(ball1X + 25/2, ball1Y+25):
                    ball1Y = platform5Y - 25
                    ball1MotionY = 0
                    canJump1 = True
                    if display1Get:
                        display1 += 6
                        display2 += 6
                        display3 += 6
                        display1Get = False
                elif platform6Rect.collidepoint(ball1X + 25/2, ball1Y+25):
                    ball1Y = platform6Y - 25
                    ball1MotionY = 0
                    canJump1 = True
                    if display1Get:
                        display1 += 5
                        display2 += 5
                        display3 += 5
                        display1Get = False
                elif platform7Rect.collidepoint(ball1X + 25/2, ball1Y+25):
                    ball1Y = platform7Y - 25
                    ball1MotionY = 0
                    canJump1 = True
                    if display1Get:
                        display1 += 4
                        display2 += 4
                        display3 += 4
                        display1Get = False
                elif platform8Rect.collidepoint(ball1X + 25/2, ball1Y+25):
                    ball1Y = platform8Y - 25
                    ball1MotionY = 0
                    canJump1 = True
                    if display1Get:
                        display1 += 3
                        display2 += 3
                        display3 += 3
                        display1Get = False
                elif platform9Rect.collidepoint(ball1X + 25/2, ball1Y+25):
                    ball1Y = platform9Y - 25
                    ball1MotionY = 0
                    canJump1 = True
                    if display1Get:
                        display1 += 2
                        display2 += 2
                        display3 += 2
                        display1Get = False
                elif platform0Rect.collidepoint(ball1X + 25/2, ball1Y+25):
                    ball1Y = platform0Y - 25
                    ball1MotionY = 0
                    canJump1 = True
                    if display1Get:
                        display1 += 1
                        display2 += 1
                        display3 += 1
                        display1Get = False
            if jump2:
                ball2MotionY -= jump2Counter
                jump2Counter -= 0.15
                if ball2MotionY > 0.20:
                    jump2 = False
            else:
                if safety_paddleRect.collidepoint(ball2X + 25/2, ball2Y+25):
                    ball2Y = safety_paddleY - 25
                    ball2MotionY = 0
                    canJump2 = True
                elif platform1Rect.collidepoint(ball2X + 25/2, ball2Y+25):
                    ball2Y = platform1Y - 25
                    ball2MotionY = 0
                    canJump2 = True
                    if display2Get:
                        display2Get = False
                        display1 -= 10
                        display2 -= 10
                        display3 -= 10
                elif platform2Rect.collidepoint(ball2X + 25/2, ball2Y+25):
                    ball2Y = platform2Y - 25
                    ball2MotionY = 0
                    canJump2 = True
                    if display2Get:
                        display2Get = False
                        display1 -= 9
                        display2 -= 9
                        display3 -= 9
                elif platform3Rect.collidepoint(ball2X + 25/2, ball2Y+25):
                    ball2Y = platform3Y - 25
                    ball2MotionY = 0
                    canJump2 = True
                    if display2Get:
                        display2Get = False
                        display1 -= 8
                        display2 -= 8
                        display3 -= 8
                elif platform4Rect.collidepoint(ball2X + 25/2, ball2Y+25):
                    ball2Y = platform4Y - 25
                    ball2MotionY = 0
                    canJump2 = True
                    if display2Get:
                        display2Get = False
                        display1 -= 7
                        display2 -= 7
                        display3 -= 7
                elif platform5Rect.collidepoint(ball2X + 25/2, ball2Y+25):
                    ball2Y = platform5Y - 25
                    ball2MotionY = 0
                    canJump2 = True
                    if display2Get:
                        display2Get = False
                        display1 -= 6
                        display2 -= 6
                        display3 -= 6
                elif platform6Rect.collidepoint(ball2X + 25/2, ball2Y+25):
                    ball2Y = platform6Y - 25
                    ball2MotionY = 0
                    canJump2 = True
                    if display2Get:
                        display2Get = False
                        display1 -= 5
                        display2 -= 5
                        display3 -= 5
                elif platform7Rect.collidepoint(ball2X + 25/2, ball2Y+25):
                    ball2Y = platform7Y - 25
                    ball2MotionY = 0
                    canJump2 = True
                    if display2Get:
                        display2Get = False
                        display1 -= 4
                        display2 -= 4
                        display3 -= 4
                elif platform8Rect.collidepoint(ball2X + 25/2, ball2Y+25):
                    ball2Y = platform8Y - 25
                    ball2MotionY = 0
                    canJump2 = True
                    if display2Get:
                        display2Get = False
                        display1 -= 3
                        display2 -= 3
                        display3 -= 3
                elif platform9Rect.collidepoint(ball2X + 25/2, ball2Y+25):
                    ball2Y = platform9Y - 25
                    ball2MotionY = 0
                    canJump2 = True
                    if display2Get:
                        display1 -= 2
                        display2 -= 2
                        display3 -= 2
                        display2Get = False
                elif platform0Rect.collidepoint(ball2X + 25/2, ball2Y+25):
                    ball2Y = platform0Y - 25
                    ball2MotionY = 0
                    canJump2 = True
                    if display2Get:
                        display1 -= 1
                        display2 -= 1
                        display3 -= 1
                        display2Get = False

            if ball1X < 0:
                ball1X = 0
            elif ball1X > 1280 - 25:
                ball1X = 1280 - 25

            if ball2X < 0:
                ball2X = 0
            elif ball2X > 1280 - 25:
                ball2X = 1280 - 25

            if display1 >= 255 and display2 >= 255 and display3 >= 255:
                display1 = random.randint(0, 255)
                display2 = random.randint(0, 255)
                display3 = random.randint(0, 255)
                Play = False
                GameOver = True
                lightBlue = True
                break
            elif display1 <= 0 and display2 <= 0 and display3 <= 0:
                display1 = random.randint(0, 255)
                display2 = random.randint(0, 255)
                display3 = random.randint(0, 255)
                Play = False
                GameOver = True
                break
            if display1 >= 255:
                display1 = 255
            elif display1 <= 0:
                display1 = 0
            if display2 >= 255:
                display2 = 255
            elif display2 <= 0:
                display2 = 0
            if display3 >= 255:
                display3 = 255
            elif display3 <= 0:
                display3 = 0

            _display.fill((display1, display2, display3))
            _display.blit(back, (backX, backY))
            _display.blit(wasd, (wasdX, wasdY))
            _display.blit(arrows, (arrowsX, arrowsY))
            _display.blit(ball1.image, (ball1X, ball1Y))
            _display.blit(ball2.image, (ball2X, ball2Y))
            _display.blit(safety_paddle.image, (safety_paddleX, safety_paddleY))
            _display.blit(platform1.image, (platform1X, platform1Y))
            _display.blit(platform2.image, (platform2X, platform2Y))
            _display.blit(platform3.image, (platform3X, platform3Y))
            _display.blit(platform4.image, (platform4X, platform4Y))
            _display.blit(platform5.image, (platform5X, platform5Y))
            _display.blit(platform6.image, (platform6X, platform6Y))
            _display.blit(platform7.image, (platform7X, platform7Y))
            _display.blit(platform8.image, (platform8X, platform8Y))
            _display.blit(platform9.image, (platform9X, platform9Y))
            _display.blit(platform0.image, (platform0X, platform0Y))

            pygame.display.flip()
            mainClock.tick(60)

    elif GameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key==pygame.K_F4:
                    if pygame.get.get_pressed()[K_RALT] or pygame.key.get_pressed()[K_LALT]:
                        pygame.quit()
                        sys.exit()
                elif event.key==pygame.K_SPACE:
                    GameOver = False
                    Play = True

        _display.fill((0,0,0))
        if lightBlue:
            _display.blit(lightBlueWins, (0,0))
        else:
            _display.blit(darkBlueWins, (0,0))

        pygame.display.flip()
        mainClock.tick(60)
            
