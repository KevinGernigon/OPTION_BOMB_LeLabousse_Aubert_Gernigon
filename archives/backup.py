
#contrôles joueur 1
    pressed_keys = pygame.key.get_pressed()
    if (player.rect.x >= 48 and player.rect.x <= 624 and player.rect.y > 48) and not (player.rect.x >= 144 and player.rect.x < 192 and player.rect.y == 144) and not (player.rect.x > 48 and player.rect.x < 144 and player.rect.y == 192) and not (player.rect.x > 288 and player.rect.x < 384 and player.rect.y == 144) and not (player.rect.x > 480 and player.rect.x < 624 and player.rect.y == 144) and not (player.rect.x > 528 and player.rect.x < 624 and player.rect.y == 192) and not (player.rect.x > 240 and player.rect.x < 432 and player.rect.y == 240) and not (player.rect.x > 48 and player.rect.x < 240 and player.rect.y == 384) and not (player.rect.x > 432 and player.rect.x < 624 and player.rect.y == 384) and not (player.rect.x > 240 and player.rect.x < 432 and player.rect.y == 528) and not (player.rect.x > 48 and player.rect.x < 192 and player.rect.y == 624) and not (player.rect.x > 288 and player.rect.x < 384 and player.rect.y == 624) and not (player.rect.x > 480 and player.rect.x < 624 and player.rect.y == 624):  
        if pressed_keys[K_UP]:
            player.rect.move_ip(0,-1)

    if (player.rect.x >= 48 and player.rect.x <= 624 and player.rect.y < 624) and not (player.rect.x > 48 and player.rect.x < 192 and player.rect.y == 48) and not (player.rect.x > 288 and player.rect.x < 384 and player.rect.y == 48) and not (player.rect.x > 480 and player.rect.x < 624 and player.rect.y == 48) and not (player.rect.x > 240 and player.rect.x < 432 and player.rect.y == 144) and not (player.rect.x > 48 and player.rect.x < 240 and player.rect.y == 288) and not (player.rect.x > 432 and player.rect.x < 624 and player.rect.y == 288) and not (player.rect.x > 240 and player.rect.x < 432 and player.rect.y == 432) and not (player.rect.x > 48 and player.rect.x < 144 and player.rect.y == 480) and not (player.rect.x > 96 and player.rect.x < 192 and player.rect.y == 528) and not (player.rect.x > 288 and player.rect.x < 384 and player.rect.y == 528) and not (player.rect.x > 480 and player.rect.x < 624 and player.rect.y == 528) and not (player.rect.x > 528 and player.rect.x < 624 and player.rect.y == 480):
            if pressed_keys[K_DOWN]:
                player.rect.move_ip(0, 1)

    if (player.rect.x > 48 and player.rect.y >= 48 and player.rect.y <= 624) and not (player.rect.x == 192 and player.rect.y > 48 and player.rect.y < 144) and not (player.rect.x == 144 and player.rect.y > 96 and player.rect.y < 192) and not (player.rect.x == 384 and player.rect.y > 48 and player.rect.y < 144) and not (player.rect.x == 624 and player.rect.y > 48 and player.rect.y < 192) and not (player.rect.x == 432 and player.rect.y > 144 and player.rect.y < 240) and not (player.rect.x == 240 and player.rect.y > 288 and player.rect.y < 384) and not (player.rect.x == 624 and player.rect.y > 288 and player.rect.y < 384) and not (player.rect.x == 432 and player.rect.y > 432 and player.rect.y < 528) and not (player.rect.x == 144 and player.rect.y > 480 and player.rect.y < 624) and not (player.rect.x == 192 and player.rect.y > 528 and player.rect.y < 624) and not (player.rect.x == 384 and player.rect.y > 528 and player.rect.y < 624) and not (player.rect.x == 624 and player.rect.y > 480 and player.rect.y < 624):
        if pressed_keys[K_LEFT]:
            player.rect.move_ip(-1, 0)

    if (player.rect.x < 624 and player.rect.y >= 48 and player.rect.y <= 624) and not (player.rect.y > 48 and player.rect.y < 192 and player.rect.x == 48) and not (player.rect.x > 288 and player.rect.x < 384 and player.rect.y > 48 and player.rect.y < 144) and not (player.rect.x > 480 and player.rect.x < 624 and player.rect.y > 48 and player.rect.y < 144) and not (player.rect.x > 528 and player.rect.x < 624 and player.rect.y > 96 and player.rect.y < 192) and not (player.rect.x > 240 and player.rect.x < 288 and player.rect.y > 144 and player.rect.y < 240) and not (player.rect.x == 48 and player.rect.y > 288 and player.rect.y < 384) and not (player.rect.x == 432 and player.rect.y > 288 and player.rect.y < 384) and not (player.rect.x == 240 and player.rect.y > 432 and player.rect.y < 528) and not (player.rect.x == 48 and player.rect.y > 480 and player.rect.y < 624) and not (player.rect.x == 288 and player.rect.y > 528 and player.rect.y < 624) and not (player.rect.x == 480 and player.rect.y > 528 and player.rect.y < 624) and not (player.rect.x == 528 and player.rect.y > 480 and player.rect.y < 624):
        if pressed_keys[K_RIGHT]:
            player.rect.move_ip(1, 0)

#contrôles joueur 2
    if abs(self._motion[0]) > abs(self._motion[1]): #Empêche le joueur de se déplacer en diagonale
            self._motion[1] = 0
    
    if (player2.rect.x >= 48 and player2.rect.x <= 624 and player2.rect.y > 48) and not (player2.rect.x >= 144 and player2.rect.x < 192 and player2.rect.y == 144) and not (player2.rect.x > 48 and player2.rect.x < 144 and player2.rect.y == 192) and not (player2.rect.x > 288 and player2.rect.x < 384 and player2.rect.y == 144) and not (player2.rect.x > 480 and player2.rect.x < 624 and player2.rect.y == 144) and not (player2.rect.x > 528 and player2.rect.x < 624 and player2.rect.y == 192) and not (player2.rect.x > 240 and player2.rect.x < 432 and player2.rect.y == 240) and not (player2.rect.x > 48 and player2.rect.x < 240 and player2.rect.y == 384) and not (player2.rect.x > 432 and player2.rect.x < 624 and player2.rect.y == 384) and not (player2.rect.x > 240 and player2.rect.x < 432 and player2.rect.y == 528) and not (player2.rect.x > 48 and player2.rect.x < 192 and player2.rect.y == 624) and not (player2.rect.x > 288 and player2.rect.x < 384 and player2.rect.y == 624) and not (player2.rect.x > 480 and player2.rect.x < 624 and player2.rect.y == 624):  
        if self._motion[0] > 0.25:
            player2.rect.move_ip(0,-1)

    if (player2.rect.x >= 48 and player2.rect.x <= 624 and player2.rect.y < 624) and not (player2.rect.x > 48 and player2.rect.x < 192 and player2.rect.y == 48) and not (player2.rect.x > 288 and player2.rect.x < 384 and player2.rect.y == 48) and not (player2.rect.x > 480 and player2.rect.x < 624 and player2.rect.y == 48) and not (player2.rect.x > 240 and player2.rect.x < 432 and player2.rect.y == 144) and not (player2.rect.x > 48 and player2.rect.x < 240 and player2.rect.y == 288) and not (player2.rect.x > 432 and player2.rect.x < 624 and player2.rect.y == 288) and not (player2.rect.x > 240 and player2.rect.x < 432 and player2.rect.y == 432) and not (player2.rect.x > 48 and player2.rect.x < 144 and player2.rect.y == 480) and not (player2.rect.x > 96 and player2.rect.x < 192 and player2.rect.y == 528) and not (player2.rect.x > 288 and player2.rect.x < 384 and player2.rect.y == 528) and not (player2.rect.x > 480 and player2.rect.x < 624 and player2.rect.y == 528) and not (player2.rect.x > 528 and player2.rect.x < 624 and player2.rect.y == 480):
            if self._motion[0] < -0.25:
                player2.rect.move_ip(0, 1)

    if (player2.rect.x > 48 and player2.rect.y >= 48 and player2.rect.y <= 624) and not (player2.rect.x == 192 and player2.rect.y > 48 and player2.rect.y < 144) and not (player2.rect.x == 144 and player2.rect.y > 96 and player2.rect.y < 192) and not (player2.rect.x == 384 and player2.rect.y > 48 and player2.rect.y < 144) and not (player2.rect.x == 624 and player2.rect.y > 48 and player2.rect.y < 192) and not (player2.rect.x == 432 and player2.rect.y > 144 and player2.rect.y < 240) and not (player2.rect.x == 240 and player2.rect.y > 288 and player2.rect.y < 384) and not (player2.rect.x == 624 and player2.rect.y > 288 and player2.rect.y < 384) and not (player2.rect.x == 432 and player2.rect.y > 432 and player2.rect.y < 528) and not (player2.rect.x == 144 and player2.rect.y > 480 and player2.rect.y < 624) and not (player2.rect.x == 192 and player2.rect.y > 528 and player2.rect.y < 624) and not (player2.rect.x == 384 and player2.rect.y > 528 and player2.rect.y < 624) and not (player2.rect.x == 624 and player2.rect.y > 480 and player2.rect.y < 624):
        if self._motion[1] > 0.25:
            player2.rect.move_ip(-1, 0)

    if (player2.rect.x < 624 and player2.rect.y >= 48 and player2.rect.y <= 624) and not (player2.rect.y > 48 and player2.rect.y < 192 and player2.rect.x == 48) and not (player2.rect.x > 288 and player2.rect.x < 384 and player2.rect.y > 48 and player2.rect.y < 144) and not (player2.rect.x > 480 and player2.rect.x < 624 and player2.rect.y > 48 and player2.rect.y < 144) and not (player2.rect.x > 528 and player2.rect.x < 624 and player2.rect.y > 96 and player2.rect.y < 192) and not (player2.rect.x > 240 and player2.rect.x < 288 and player2.rect.y > 144 and player2.rect.y < 240) and not (player2.rect.x == 48 and player2.rect.y > 288 and player2.rect.y < 384) and not (player2.rect.x == 432 and player2.rect.y > 288 and player2.rect.y < 384) and not (player2.rect.x == 240 and player2.rect.y > 432 and player2.rect.y < 528) and not (player2.rect.x == 48 and player2.rect.y > 480 and player2.rect.y < 624) and not (player2.rect.x == 288 and player2.rect.y > 528 and player2.rect.y < 624) and not (player2.rect.x == 480 and player2.rect.y > 528 and player2.rect.y < 624) and not (player2.rect.x == 528 and player2.rect.y > 480 and player2.rect.y < 624):
        if self._motion[1] < -0.25:
            player2.rect.move_ip(1, 0)

    def setMotion(self, axis, value):   #_motion récupère l'axe et la valeur du stick
        self._motion[axis] = value