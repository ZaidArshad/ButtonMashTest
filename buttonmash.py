import pygame

pygame.init()
pygame.joystick.init()
clock = pygame.time.Clock()

print("Joysticks connected:", pygame.joystick.get_count())
for id in range(pygame.joystick.get_count()):
    print("Joystick #%s: %s" % (id, pygame.joystick.Joystick(id).get_name()))

stickID = input("Controller ID: ")
stick = pygame.joystick.Joystick(int(stickID))
stick.init()

presses = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONUP and event.button == 0:
            presses +=1
    print(presses)
    clock.tick(1)
    presses = 0