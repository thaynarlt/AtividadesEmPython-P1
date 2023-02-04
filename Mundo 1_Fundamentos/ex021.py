#Faça um prograimport pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('midnightcity.mp3')
pygame.mixer.music.play()
pygame.event.wait()
