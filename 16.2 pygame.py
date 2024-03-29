import sys, pygame

pygame.init()

size = width, height = 700, 300
speed = [2, 2]
background = 255, 255, 255

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Srishti python exp 16 Bouncing ball")

ball = pygame.image.load('/Users/srishtikumar/desktop/3RD SEM/ball.jpg')
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(background)
    screen.blit(ball, ballrect)
    pygame.display.flip()
