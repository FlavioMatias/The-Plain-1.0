try:
    import pygame
except:
    print("por favor instale as bibliotecas necessarias")
try:
    from player import Player, projectiles
    from enemies import *
    from buttons import Button
    from aud.audios import *
    from config import *
    from itens import *

    pygame.init()
    pygame.mouse.set_visible(False)
    potion_cura = Potions.Cura()
    pause_screen = pygame.image.load("sprites/pause_screen.png")
    option = pygame.image.load("sprites/options.png")
    bg_menu = pygame.image.load("sprites/back 1.png")
    bg = pygame.image.load("sprites/backgroud_glass.png")
    cursor_img = pygame.image.load("sprites/cursor.png")
    cursor_img = pygame.transform.scale(cursor_img, (30, 30))
    
    
    while Run:
        mouse_pos = pygame.mouse.get_pos()
        arma = Arsenal.get_weapon(arma_atual)
        arma_drop = Arsenal.drop_weapon(arma_atual)
        
        if arma_atual == "magic_book":
             x_proj, y_proj = 30, 30
             Player.atk = 50
        else:
            x_proj, y_proj = 15, 15
            Player.atk = 35
            
        if paused:
            mouse_pos = pygame.mouse.get_pos()
            menu_p = Button.menupause.rect.collidepoint(mouse_pos)
            reset_p = Button.resetpause.rect.collidepoint(mouse_pos)
            resume_p = Button.resume.rect.collidepoint(mouse_pos)
                
            if pause_start_time == 0:
                pause_start_time = pygame.time.get_ticks()
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_TAB:
                        button_sound.play()
                        paused = False
                        total_pause_time += pygame.time.get_ticks() - pause_start_time
                        pause_start_time = 0
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if menu_p:
                            button_sound.play()
                            state = "menu" 
                            paused = False
                            total_pause_time += pygame.time.get_ticks() - pause_start_time
                            pause_start_time = 0
                            start_ticks = pygame.time.get_ticks()
                            
                        if reset_p:
                            button_sound.play()
                            state = "init"
                            paused = False
                            total_pause_time += pygame.time.get_ticks() - pause_start_time
                            pause_start_time = 0
                            start_ticks = pygame.time.get_ticks()
                            
                        if resume_p:
                            button_sound.play()
                            paused = False
                            total_pause_time += pygame.time.get_ticks() - pause_start_time
                            pause_start_time = 0
                            
                            
                        
            screen.blit(pause_screen,(190,70))
            
            screen.blit(Button.resume.img,Button.resume.rect)
            screen.blit(Button.resetpause.img,Button.resetpause.rect)
            screen.blit(Button.menupause.img,Button.menupause.rect)
            
            screen.blit(cursor_img, mouse_pos)
            pygame.display.flip()
            clock.tick(64)
            continue
            
        if state in ["wave1", "wave2", "wave3"]:
            if music_state != "battle":
                pygame.mixer.music.load("aud/batalha.wav")
                pygame.mixer.music.play(-1)
                music_state = "battle" 
                
        else:
            if music_state != "menu":
                pygame.mixer.music.load("aud/music-menu.wav")
                pygame.mixer.music.play(-1)
                music_state = "menu"

        difficulty = dif_select[dif_cursor]
        
        match difficulty:
            case "easy":
                goblin_S = 3000
                magic_S = 5000
                golem_S = 20000
            
            case "medium":
                goblin_S = 2000
                magic_S = 4000
                golem_S = 18000
                
            case "hard":
                goblin_S = 1500
                magic_S = 3000
                golem_S = 16000
        
        
        match state:
            
            case "init":

                pygame.time.set_timer(Create_goblin, goblin_S)
                pygame.time.set_timer(Create_ranged, magic_S)
                pygame.time.set_timer(Create_golem, golem_S)  
                
                start_ticks = pygame.time.get_ticks()
                arma_atual = "magic_book"
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            pygame.quit()
                                
                    if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                atk_sound.play()
                                new_proj = Arsenal.projetil(arma.rect.centerx, arma.rect.centery, angle, x_proj, y_proj)
                                if arma_atual == "steff":
                                    new_proj_top = Arsenal.projetil(arma.rect.centerx, arma.rect.centery, angle+15,x_proj, y_proj)
                                    new_proj_bot = Arsenal.projetil(arma.rect.centerx, arma.rect.centery, angle-15,x_proj, y_proj)
                                    projectiles.append(new_proj_top)
                                    projectiles.append(new_proj_bot)
                                projectiles.append(new_proj)

                                
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            button_sound.play()
                            start_ticks = pygame.time.get_ticks() 
                            state = "wave1"
                            for bullet in enemy_projectiles:
                                enemy_projectiles.remove(bullet)
                            
                        if event.key == pygame.K_TAB:
                            paused = True
                            
                enemies = []
                # if state ==  "init":
                #     enemy_projectiles = []
                
                angle, mousex = mouse()
                screen.blit(bg,(-4,0))
                wave2 = font.render(f"Press [ENTER] to start", True, (250, 250, 255)) 
                screen.blit(wave2, (Tela.width - 900, Tela.height - 150)) 
                
                if state == "init":
                    start_ticks = pygame.time.get_ticks()
                    
                Player.hp = 400
                keys = pygame.key.get_pressed()
                Player.move(keys)
                    
                arma.rect.x = Player.rect.x + 50
                arma.rect.y = Player.rect.y + 50  
                
                if  mousex < Player.rect.x:
                    arma.rect.x -= 55
                    screen.blit(Player.sprite_flipped, (Player.rect.x, Player.rect.y))
                    arma.rotate_pistol(arma.sprite_flipped_close, screen, angle)
                else: 
                    screen.blit(Player.sprite, (Player.rect.x, Player.rect.y))
                    arma.rotate_pistol(arma.sprite_close, screen, angle)
                
                for proj in projectiles[:]:
                    proj.up()
                    proj.draw(screen)
                
                screen.blit(cursor_img, mouse_pos)
                pygame.display.flip()
                clock.tick(64)
                
            case "wave1":
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            pygame.quit()
                                
                    if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                atk_sound.play()
                                new_proj = Arsenal.projetil(arma.rect.centerx, arma.rect.centery, angle, x_proj,y_proj)
                                projectiles.append(new_proj)
                                if arma_atual == "steff":
                                    new_proj_top = Arsenal.projetil(arma.rect.centerx, arma.rect.centery, angle+15, x_proj,y_proj)
                                    new_proj_bot = Arsenal.projetil(arma.rect.centerx, arma.rect.centery, angle-15, x_proj,y_proj)
                                    projectiles.append(new_proj_top)
                                    projectiles.append(new_proj_bot)
                                    
                    if event.type == Create_goblin:
                            newgoblin = goblin(Player)
                            enemies.append(newgoblin)
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_TAB:
                            button_sound.play()
                            paused = True
                
                            
                screen.blit(bg,(-4,0))
                
                angle, mousex = mouse()
                seconds = (pygame.time.get_ticks() - start_ticks - total_pause_time) / 1000
                
                secondst = int(70 - (seconds))
                
                texthp = f"LIFE: {Player.hp}/ 400"
                draw_hp(texthp,screen)
                
                wave1 = font.render(f"proxima wave: {secondst:02}", True, (255, 255, 255)) 
                screen.blit(wave1, (Tela.width - 250, 15)) 
                
                if Player.hp <= 0:
                    state = "lose"
                if seconds >= 60:
                    enemies = []
                    if seconds >= 70 and state == "wave1":
                        start_ticks = pygame.time.get_ticks()
                        state = "wave2"
                        
                        
                keys = pygame.key.get_pressed()
                Player.move(keys)
                    
                arma.rect.x = Player.rect.x + 50
                arma.rect.y = Player.rect.y + 45  
                

                if  mousex < Player.rect.x:
                    arma.rect.x -= 50
                    screen.blit(Player.sprite_flipped, (Player.rect.x, Player.rect.y))
                    arma.rotate_pistol(arma.sprite_flipped, screen, angle)
                    if Player.is_damaged:
                        screen.blit(Player.flip_red, (Player.rect.x, Player.rect.y))
                        arma.rotate_pistol(arma.sprite_flipped, screen, angle)
                        
                else: 
                    screen.blit(Player.sprite, (Player.rect.x, Player.rect.y))
                    arma.rotate_pistol(arma.sprite, screen, angle)
                    if Player.is_damaged:
                        screen.blit(Player.sprite_red, (Player.rect.x, Player.rect.y))
                        arma.rotate_pistol(arma.sprite, screen, angle)
                
                if Player.is_damaged:
                    Player.damage_timer -= 1
                    if Player.damage_timer <= 0:
                        Player.is_damaged = False        
                
                for proj in projectiles[:]:
                    proj.up()
                    proj.draw(screen)

                        
                for enemy in enemies[:]:
                    enemy.move()
                    enemy.draw(Player, screen)
                    enemy.atack(Player)
                    if enemy.hp <= 0:
                        enemies.remove(enemy)
                    
                for proj in projectiles[:]:
                    for enemy in enemies[:]:
                        if proj.colid(enemy):
                            projectiles.remove(proj)
                            enemy.hp -= Player.atk
                            break  
                
                screen.blit(cursor_img, mouse_pos)
                pygame.display.flip()
                clock.tick(64)
                    
            case "wave2":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            pygame.quit()
                                
                    if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                atk_sound.play()
                                new_proj = Arsenal.projetil(arma.rect.centerx, arma.rect.centery, angle, x_proj,y_proj)
                                projectiles.append(new_proj)
                                
                    if event.type == Create_goblin:
                            newgoblin = goblin(Player)
                            enemies.append(newgoblin)
                            
                    if event.type == Create_ranged:
                            newgoblin = ranged(Player)
                            enemies.append(newgoblin)
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_TAB:
                            button_sound.play()
                            paused = True
                            
                        if event.key == pygame.K_e and potion_cura.colid(Player) and Player.hp < 400:
                            button_sound.play()
                            Player.hp += 50
                            spw_potion = True
                            break
                        
                screen.blit(bg,(-4,0))
                
                angle, mousex = mouse()
                seconds2 = (pygame.time.get_ticks() - start_ticks - total_pause_time) / 1000
                seconds2t = int(70 - (seconds2))
                
                texthp = f"LIFE: {Player.hp}/ 400"
                
                draw_hp(texthp,screen)
                wave2 = font.render(f"proxima wave: {seconds2t:02}", True, (255, 255, 255)) 
                screen.blit(wave2, (Tela.width - 250, 15)) 
                if Player.hp <= 0:
                    state = "lose"
                    
                if seconds2 >= 60:
                    enemies = []
                    if seconds2 >= 70 and state == "wave2":
                        start_ticks = pygame.time.get_ticks()
                        state = "wave3"            
                    
                keys = pygame.key.get_pressed()
                Player.move(keys)
                    
                arma.rect.x = Player.rect.x + 50
                arma.rect.y = Player.rect.y + 45         
                if not spw_potion: 
                    screen.blit(potion_cura.sprite,potion_cura.rect)
                
                if  mousex < Player.rect.x:
                    arma.rect.x -= 50
                    screen.blit(Player.sprite_flipped, (Player.rect.x, Player.rect.y))
                    arma.rotate_pistol(arma.sprite_flipped, screen, angle)
                    if Player.is_damaged:
                        screen.blit(Player.flip_red, (Player.rect.x, Player.rect.y))
                        arma.rotate_pistol(arma.sprite_flipped, screen, angle)
                        
                else: 
                    screen.blit(Player.sprite, (Player.rect.x, Player.rect.y))
                    arma.rotate_pistol(arma.sprite, screen, angle)
                    if Player.is_damaged:
                        screen.blit(Player.sprite_red, (Player.rect.x, Player.rect.y))
                        arma.rotate_pistol(arma.sprite, screen, angle)
                
                if Player.is_damaged:
                    Player.damage_timer -= 1
                    if Player.damage_timer <= 0:
                        Player.is_damaged = False        
                
                
                for proj in projectiles[:]:
                    proj.up()
                    proj.draw(screen)

                        
                for enemy in enemies[:]:
                    enemy.move()
                    enemy.draw(Player, screen)
                    enemy.atack(Player)
                    if enemy.hp <= 0:
                        enemies.remove(enemy)
                    
                for proj in projectiles[:]:
                    for enemy in enemies[:]:
                        if proj.colid(enemy):
                            projectiles.remove(proj)
                            enemy.hp -= Player.atk
                            break 
                        
                for bullet in enemy_projectiles[:]:
                    bullet.move()
                    bullet.draw(screen)
                    if bullet.colid(Player): 
                        damage_sound.play()
                        Player.is_damaged = True
                        Player.damage_time = 9000
                        Player.hp -= bullet.atk
                        enemy_projectiles.remove(bullet)
                screen.blit(cursor_img, mouse_pos)  
                pygame.display.flip()
                clock.tick(64)
                
            case "wave3":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            pygame.quit()
                                
                    if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                player_center = Player.rect.center
                                mouse_pos = pygame.mouse.get_pos()
                                angle = math.degrees(math.atan2(mouse_pos[1] - player_center[1], mouse_pos[0] - player_center[0]))

                                atk_sound.play()
                                new_proj = Arsenal.projetil(arma.rect.centerx, arma.rect.centery, angle, x_proj, y_proj)
                                if arma_atual == "steff":
                                    new_proj_top = Arsenal.projetil(arma.rect.centerx, arma.rect.centery, angle+10, x_proj, y_proj)
                                    new_proj_bot = Arsenal.projetil(arma.rect.centerx, arma.rect.centery, angle-10, x_proj, y_proj)
                                    projectiles.append(new_proj_top)
                                    projectiles.append(new_proj_bot)
                                projectiles.append(new_proj)
                                
                    if event.type == Create_goblin:
                            newgoblin = goblin(Player)
                            enemies.append(newgoblin)
                            
                    if event.type == Create_ranged:
                            newgoblin = ranged(Player)
                            enemies.append(newgoblin)
                            
                    if event.type == Create_golem:
                            newgoblin = golem(Player)
                            enemies.append(newgoblin)
                            
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_e and Player.rect.colliderect(arma_drop.rect):
                            match arma_atual:
                                case "steff":
                                    arma_atual = "magic_book"
                                    
                                case "magic_book":
                                    arma_atual = "steff"
                            
                        if event.key == pygame.K_TAB:
                            button_sound.play()
                            paused = True
                
                screen.blit(bg,(-4,0))
                
                angle, mousex = mouse()
                seconds3 = (pygame.time.get_ticks() - start_ticks - total_pause_time) / 1000
                
                seconds3t = int(70 - (seconds3))
                texthp = f"LIFE: {Player.hp}/ 400"
                
                draw_hp(texthp,screen)
                
                wave3 = font.render(f"vitoria: {seconds3t:02}", True, (255, 255, 255)) 
                screen.blit(wave3, (Tela.width - 250, 15))
                
                if Player.hp <= 0:
                    state = "lose"
                    
                if seconds3 >= 60:
                    enemies = []
                    if seconds3 >= 70 and state == "wave3":
                        state = "win" 
                    
                keys = pygame.key.get_pressed()
                Player.move(keys)
                if arma_atual == "magic_book":
                    arma.rect.x = Player.rect.x + 50
                    arma.rect.y = Player.rect.y + 45  
                elif arma_atual == "steff":
                    arma.rect.x = Player.rect.x + 65
                    arma.rect.y = Player.rect.y + 45
                    
                if arma_atual == "magic_book":
                    screen.blit(Arsenal.steff.sprite,Arsenal.steff.rect)
                else:
                    screen.blit(Arsenal.Pistol.sprite_close,Arsenal.Pistol.rect)
                    
                if  mousex < Player.rect.x:
                    if arma_atual == "magic_book":
                        arma.rect.x -= 50
                    else:
                        arma.rect.x -= 55
                        
                    screen.blit(Player.sprite_flipped, (Player.rect.x, Player.rect.y))
                    arma.rotate_pistol(arma.sprite_flipped, screen, angle)
                    if Player.is_damaged:
                        screen.blit(Player.flip_red, (Player.rect.x, Player.rect.y))
                        arma.rotate_pistol(arma.sprite_flipped, screen, angle)
                        
                else: 
                    screen.blit(Player.sprite, (Player.rect.x, Player.rect.y))
                    arma.rotate_pistol(arma.sprite, screen, angle)
                    if Player.is_damaged:
                        screen.blit(Player.sprite_red, (Player.rect.x, Player.rect.y))
                        arma.rotate_pistol(arma.sprite, screen, angle)
                
                if Player.is_damaged:
                    Player.damage_timer -= 1
                    if Player.damage_timer <= 0:
                        Player.is_damaged = False        
                
                
                for proj in projectiles[:]:
                    proj.up()
                    proj.draw(screen)

                        
                for enemy in enemies[:]:
                    enemy.move()
                    enemy.draw(Player, screen)
                    enemy.atack(Player)
                    if enemy.hp <= 0:
                        enemies.remove(enemy)
                    
                for proj in projectiles[:]:
                    for enemy in enemies[:]:
                        if proj.colid(enemy):
                            projectiles.remove(proj)
                            enemy.hp -= Player.atk
                            break  
                        
                for bullet in enemy_projectiles[:]:
                    bullet.move()
                    bullet.draw(screen)
                    if bullet.colid(Player): 
                        damage_sound.play()
                        Player.is_damaged = True
                        Player.damage_time = 9000
                        Player.hp -= bullet.atk
                        enemy_projectiles.remove(bullet) 
                
                screen.blit(cursor_img, mouse_pos)
                pygame.display.flip()
                clock.tick(64)
                
            case "lose":
                pygame.mixer.music.pause()
                lose_sound.play()
                mouse_pos = pygame.mouse.get_pos()
                reset_game = Button.reset.rect.collidepoint(mouse_pos)
                menu = Button.menu.rect.collidepoint(mouse_pos)


                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        lose_sound.stop()
                        button_sound.play()
                        if reset_game:
                            pygame.mixer.music.play(-1)
                            start_ticks = pygame.time.get_ticks()
                            Player.hp = 400
                            state = "init"
                            projectiles = []
                            enemies = []
                            
                        if menu:
                            pygame.mixer.music.play(-1)
                            state = 'menu'

                bg_lose = pygame.image.load("sprites/backgroud_glass.png")
                
                lose = pygame.image.load("sprites/derrota.png")
                
                screen.blit(bg_lose,(-4,0))
                screen.blit(lose,(400,150))
                
                if menu:
                    screen.blit(Button.menu.img_hover,Button.menu.rect)
                else:
                    screen.blit(Button.menu.img,Button.menu.rect)
                    
                if reset_game:
                    screen.blit(Button.reset.img_hover,Button.reset.rect)
                else:
                    screen.blit(Button.reset.img,Button.reset.rect)

                screen.blit(cursor_img, mouse_pos)
                pygame.display.flip()
                clock.tick(64)
                
            case "menu":
                mouse_pos = pygame.mouse.get_pos()
                
                start = Button.Start.rect.collidepoint(mouse_pos)
                options = Button.Option.rect.collidepoint(mouse_pos)
                close = Button.Exit.rect.collidepoint(mouse_pos)
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        button_sound.play()
                        if start:
                            Player.rect.x, Player.rect.y  = 600, 300
                            enemies = []
                            state = 'init'
                            
                        if options:
                            state = "options"
                            
                        if close:
                            pygame.quit()
                            
                titulo = pygame.image.load("sprites/Endless Horde.png")
                
                                            
                bg_menu = pygame.image.load("sprites/back 1.png")
                
                screen.blit(bg_menu,(0,0))
                screen.blit(titulo,(535,125))
                if close:
                    screen.blit(Button.Exit.img_hover,Button.Exit.rect)
                else:
                    screen.blit(Button.Exit.img,Button.Exit.rect)
                
                
                if start:
                    screen.blit(Button.Start.img_hover,Button.Start.rect)
                else:
                    screen.blit(Button.Start.img,Button.Start.rect)
                    
                if options:
                    screen.blit(Button.Option.img_hover,Button.Option.rect)
                else:
                    screen.blit(Button.Option.img,Button.Option.rect)
                    
                if close:
                    screen.blit(Button.Exit.img_hover,Button.Exit.rect)
                else:
                    screen.blit(Button.Exit.img,Button.Exit.rect)
                    
                                
                    
                screen.blit(cursor_img, mouse_pos)
                pygame.display.flip()
                clock.tick(64)

            case "win":
                pygame.mixer.music.pause()
                win_sound.play()
                mouse_pos = pygame.mouse.get_pos()
                reset_game = Button.reset.rect.collidepoint(mouse_pos)
                menu = Button.menu.rect.collidepoint(mouse_pos)


                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        win_sound.stop()
                        button_sound.play()
                        if reset_game:
                            pygame.mixer.music.play(-1)
                            start_ticks = pygame.time.get_ticks()
                            Player.hp = 400
                            state = "init"
                            projectiles = []
                            enemies = []
                            
                        if menu:
                            pygame.mixer.music.play(-1)
                            state = 'menu'

                bg_Win = pygame.image.load("sprites/backgroud_glass.png")
                
                Win = pygame.image.load("sprites/win.png")
                
                screen.blit(bg_Win,(-4,0))
                screen.blit(Win,(400,150))
                
                if menu:
                    screen.blit(Button.menu.img_hover,Button.menu.rect)
                else:
                    screen.blit(Button.menu.img,Button.menu.rect)
                    
                if reset_game:
                    screen.blit(Button.reset.img_hover,Button.reset.rect)
                else:
                    screen.blit(Button.reset.img,Button.reset.rect)

                screen.blit(cursor_img, mouse_pos)
                pygame.display.flip()
                clock.tick(64)

            case "options":
                mouse_pos = pygame.mouse.get_pos()
                button_VER = Button.effect_VR.rect.collidepoint(mouse_pos)
                button_VEL = Button.effect_VL.rect.collidepoint(mouse_pos)
                
                button_VMR = Button.music_VR.rect.collidepoint(mouse_pos)
                button_VML = Button.music_VL.rect.collidepoint(mouse_pos)
                
                difficultyR = Button.difR.rect.collidepoint(mouse_pos)
                difficultyL = Button.difL.rect.collidepoint(mouse_pos)
                
                exitoptions = Button.exitop.rect.collidepoint(mouse_pos)
                
                atk_sound.set_volume(volume_E/10.0)
                button_sound.set_volume(volume_E/10.0)
                damage_sound.set_volume(volume_E/10.0)
                win_sound.set_volume(volume_M/10.0)
                lose_sound.set_volume(volume_M/10.0)
                pygame.mixer.music.set_volume(volume_M/10.0)
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if exitoptions:
                                button_sound.play()
                                state = "menu"
                                
                            if volume_E < 10:
                                if button_VER:
                                    button_sound.play()
                                    volume_E += 1
                            if volume_E > 0:
                                if button_VEL:
                                    button_sound.play()
                                    volume_E -= 1
                                    
                            if volume_M < 10:
                                if button_VMR:
                                    button_sound.play()
                                    volume_M += 1
                            if volume_M > 0:
                                if button_VML:
                                    button_sound.play()
                                    volume_M -= 1
                                    
                            if dif_cursor < 2:
                                if difficultyR:
                                    button_sound.play()
                                    dif_cursor += 1
                            if dif_cursor > 0:
                                if difficultyL:
                                    button_sound.play()
                                    dif_cursor -= 1
                                

                                

                        
                screen.blit(bg_menu,(0,0))
                screen.blit(option,(190,70))

                screen.blit(Button.effect_VL.img,Button.effect_VL.rect)
                screen.blit(Button.effect_VR.img,Button.effect_VR.rect)
                
                screen.blit(Button.music_VL.img,Button.music_VL.rect)
                screen.blit(Button.music_VR.img,Button.music_VR.rect)
                
                screen.blit(Button.difL.img,Button.difL.rect)
                screen.blit(Button.difR.img,Button.difR.rect)
                
                screen.blit(Button.exitop.img,Button.exitop.rect)
                
                volume = fontOP.render(f"{volume_E}", True, (255, 255, 255)) 
                screen.blit(volume, (750 + 140, 300))
                
                volumeM = fontOP.render(f"{volume_M}", True, (255, 255, 255)) 
                screen.blit(volumeM, (750 + 140, 300 + 140)) 
                
                diftext = fontOP.render(f"{difficulty}", True, (255, 255, 255)) 
                screen.blit(diftext, (700 + 130, 610) )
                
                screen.blit(cursor_img, mouse_pos)
                pygame.display.flip()
                clock.tick(64)
except:
    error = pygame.image.load("sprites/error.png")
    clock = pygame.time.Clock()
    print(Exception)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
        
        screen.blit(error,(190,70))                             
        pygame.display.flip()
        clock.tick(64)
            
pygame.quit()
