# import pygame
# import sys
#
# pygame.init()
#
# FPS = 60
# SCREEN_WIDTH = 1000
# SCREEN_HIGHT = 800
#
# screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HIGHT))
#
# background_img = pygame.image.load("background.jpg")
# screen.blit(background_img,(0,0))
# clock = pygame.time.Clock()
# running = True
# dt = 0
#
# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
#
# while True:
#     screen.blit(background_img, (0,0))
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#     pygame.draw.circle(screen,"red",player_pos,40)
#     dt = clock.tick(FPS) / 1000
#     pygame.display.flip()
#
#
#     key = pygame.key.get_pressed()
#
#     if key[pygame.K_w]:
#         if player_pos.y >= 300 * dt: player_pos.y -= 300 * dt
#     if key[pygame.K_s]:
#         if player_pos.y <= screen.get_height() - 300 * dt: player_pos.y += 300 * dt
#     if key[pygame.K_a]:
#         if player_pos.x >= 300 * dt: player_pos.x -= 300 * dt
#     if key[pygame.K_d]:
#         if player_pos.x <= screen.get_width() - 300 * dt: player_pos.x += 300 * dt
#
#     screen.fill ('black')

# start_position=pygame.Vector2(3,4)
# destination=pygame.Vector2(8,7)
# way_length=starts_pos.dictance.Vector2(6,9)
#
# import pygame
#
# pygame.init()
#
# v1 = pygame.Vector2(150,100)
# v1 = pygame.Vector2(500,700)
#
# FPS = 60
# SCREEN_WIDTH = 1000
# SCREEN_HIGHT = 800
#
# screen = pygame.display.set_mode(5)
#
# obj_pos += dt * SPEED * (v2-v1).normalize()

# import pygame
#
# pygame.init()
#
# screen = pygame.display.set_mode((800, 600))
# clock = pygame.time.Clock()
#
# player = pygame.Vector2(400, 500)
# enemy = pygame.Vector2(400, 100)
#
# running = True
# while running:
#     dt = clock.tick(60) / 1000
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     # Движение игрока (стрелки)
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]: player.x -= 300 * dt
#     if keys[pygame.K_UP]: player.y -= 300 * dt
#     if keys[pygame.K_RIGHT]: player.x += 300 * dt
#     if keys[pygame.K_DOWN]: player.y += 300 * dt
#
#     screen.fill((0, 0, 0))
#     pygame.draw.circle(screen, (0, 255, 0), player, 20)
#     pygame.draw.circle(screen, (255, 0, 0), enemy, 20)
#     pygame.display.flip()

# import pygame
#
# pygame.init()
#
# screen = pygame.display.set_mode((800, 600))
# clock = pygame.time.Clock()
#
#
# player_pos = pygame.Vector2(400, 500)
# enemy_pos = pygame.Vector2(400, 100)
# radius = 20
#
# running = True
# while running:
#     dt = clock.tick(60) / 1000
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:  player_pos.x -= 300 * dt
#     if keys[pygame.K_RIGHT]: player_pos.x += 300 * dt
#     if keys[pygame.K_UP]:    player_pos.y -= 300 * dt
#     if keys[pygame.K_DOWN]:  player_pos.y += 300 * dt
#
#
#     distance = player_pos.distance_to(enemy_pos)
#
#     (20 + 20 == 40)
#     if distance < (radius * 2):
#         color_player = (255, 255, 255)
#     else:
#         color_player = (0, 255, 0)
#
#     screen.fill((0, 0, 0))
#
#
#     pygame.draw.circle(screen, color_player, player_pos, radius)
#     pygame.draw.circle(screen, (255, 0, 0), enemy_pos, radius)
#
#     pygame.display.flip()
#
# pygame.quit()
#
# import pygame as pg
#
# pg.init()
# sc = pg.display.set_mode((800, 600))
# x, y = 400, 500  # Игрок
# ex, ey = 400, 100  # Враг
#
# while pg.event.get(pg.QUIT) == []:
#     k = pg.key.get_pressed()
#     # Запоминаем старые координаты
#     old_x, old_y = x, y
#
#     # Движение
#     if k[pg.K_LEFT]:  x -= 5
#     if k[pg.K_RIGHT]: x += 5
#     if k[pg.K_UP]:    y -= 5
#     if k[pg.K_DOWN]:  y += 5
#
#     # ПРОВЕРКА: Если после шага расстояние < 40, возвращаем игрока назад
#     if (x - ex) ** 2 + (y - ey) ** 2 < 1600:
#         x, y = old_x, old_y
#
#     sc.fill(0)
#     pg.draw.circle(sc, (0, 255, 0), (int(x), int(y)), 20)
#     pg.draw.circle(sc, (255, 0, 0), (ex, ey), 20)
#     pg.display.flip()
#     pg.time.delay(10)
#
# import pygame as pg, random as r
#
# pg.init()
# sc = pg.display.set_mode((800, 600))
# f = pg.font.SysFont(None, 40)
# x, y, ex, ey, cx, cy, score = 400, 500, 400, 100, 200, 200, 0
# pl = pg.Rect(100, 300, 200, 20)
# ps = 3
#
# while not pg.event.get(pg.QUIT):
#     k = pg.key.get_pressed()
#     ox, oy = x, y
#     x += (k[pg.K_RIGHT] - k[pg.K_LEFT]) * 5
#     y += (k[pg.K_DOWN] - k[pg.K_UP]) * 5
#
#     # Враг и монета
#     ex += 1 if ex < x else -1
#     ey += 1 if ey < y else -1
#     if (x - ex) ** 2 + (y - ey) ** 2 < 1600: x, y = ox, oy
#     if (x - cx) ** 2 + (y - cy) ** 2 < 900:
#         score += 1
#         cx, cy = r.randint(50, 750), r.randint(50, 550)
#
#     # Платформа
#     pl.x += ps
#     if pl.right > 800 or pl.left < 0: ps *= -1
#     hit = pl.collidepoint(x, y)  # Упрощенная проверка (центр игрока в платформе)
#
#     sc.fill(0)
#     for c, p, r_ in [("gold", (cx, cy), 10), ("red", (ex, ey), 20), ("green", (x, y), 20)]:
#         pg.draw.circle(sc, c, p, r_)
#     pg.draw.rect(sc, "blue", pl)
#
#     txt = f"S: {score}" + (" | HIT!" if hit else "")
#     sc.blit(f.render(txt, 1, "white"), (10, 10))
#     pg.display.flip()
#     pg.time.wait(10)


# import pygame as pg
# import random
#
# pg.init()
# sc = pg.display.set_mode((800, 600))
# f = pg.font.SysFont("Arial", 40)
#
# # Координаты и переменные
# px, py = 400, 300  # Игрок
# ex, ey = 50, 50  # Враг
# cx, cy = 600, 400  # Монета
# score = 0
# run = True
# msg = ""  # Сообщение в конце игры
#
# while run:
#     for ev in pg.event.get():
#         if ev.type == pg.QUIT: run = False
#
#     # 1. Управление
#     k = pg.key.get_pressed()
#     if k[pg.K_LEFT]:  px -= 5
#     if k[pg.K_RIGHT]: px += 5
#     if k[pg.K_UP]:    py -= 5
#     if k[pg.K_DOWN]:  py += 5
#
#     # 2. Враг преследует игрока
#     if ex < px: ex += 2
#     if ex > px: ex -= 2
#     if ey < py: ey += 2
#     if ey > py: ey -= 2
#
#     # 3. УСЛОВИЕ ПРОИГРЫША (Враг поймал)
#     if (px - ex) ** 2 + (py - ey) ** 2 < 1600:
#         msg = "ВРАГ ПОЙМАЛ! ПРОИГРЫШ"
#         run = False
#
#     # 4. Сбор монет
#     if (px - cx) ** 2 + (py - cy) ** 2 < 900:
#         score += 1
#         cx, cy = random.randint(50, 750), random.randint(50, 550)
#
#         # 5. УСЛОВИЕ ПОБЕДЫ (20 очков)
#         if score >= 20:
#             msg = "ПОБЕДА! 20 ОЧКОВ!"
#             run = False
#
#     # Рисование
#     sc.fill((0, 0, 0))
#     pg.draw.circle(sc, "gold", (cx, cy), 10)
#     pg.draw.circle(sc, "red", (ex, ey), 20)
#     pg.draw.circle(sc, "green", (px, py), 20)
#
#     txt = f.render(f"Счет: {score} / 20", True, "white")
#     sc.blit(txt, (20, 20))
#
#     pg.display.flip()
#     pg.time.delay(20)
#
# # ЭКРАН ЗАВЕРШЕНИЯ
# if msg:
#     sc.fill("black")
#     end_txt = f.render(msg, True, "yellow")
#     # Рисуем текст по центру
#     sc.blit(end_txt, (400 - end_txt.get_width() // 2, 300))
#     pg.display.flip()
#     pg.time.wait(3000)  # Ждем 3 секунды перед закрытием
#
# pg.quit()
#
# image_loaded = pygama/image.load('img/player.png')
# image = pygame.transform.scale(self.image_loaded, (40, 40))
# screen.blit(image, blit_pos)
# pygame.display.flip()

# import pygame as pg
# import random
#
# import pygame.transform
#
# player_img = pg.image.load('213.png')
# player_img = pg.transform.scale(player_img, (100, 100))
#
# enemy_img = pg.image.load('321.png')
# enemy_img = pg.transform.scale(player_img, (100, 100))
#
# coin_img = pg.image.load('312.png')
# coin_img = pg.transform.scale(player_img, (100, 100))
#
# pg.init()
# sc = pg.display.set_mode((1600, 1000))
# f = pg.font.SysFont("Arial", 100)
#
# try:
#     img_player_raw = pg.image.load('213.png')
#     img_enemy_raw = pg.image.load('321.png')
#     img_coin_raw = pg.image.load('312.png')
# except:
#     # Если картинок нет, создаем цветные квадраты, чтобы код не вылетал
#
#     img_enemy_raw = pg.Surface((100, 100)); img_enemy_raw.fill((255, 0, 0))
#     img_coin_raw = pg.Surface((100, 100)); img_coin_raw.fill((255, 215, 0))
#
#
# img_player = pg.transform.scale(img_player_raw, (100, 100))
# img_enemy = pg.transform.scale(img_enemy_raw, (100, 100))
# img_coin = pg.transform.scale(img_coin_raw, (100, 100))
#
#
# px, py = 400, 300
# ex, ey = 50, 50
# cx, cy = 600, 400
# score = 0
# run = True
# msg = ""
#
# while run:
#     for ev in pg.event.get():
#         if ev.type == pg.QUIT: run = False
#
#
#     k = pg.key.get_pressed()
#     if k[pg.K_LEFT]:  px -= 5
#     if k[pg.K_RIGHT]: px += 5
#     if k[pg.K_UP]:    py -= 5
#     if k[pg.K_DOWN]:  py += 5
#
#
#     if ex < px: ex += 2
#     if ex > px: ex -= 2
#     if ey < py: ey += 2
#     if ey > py: ey -= 2
#
#
#     if (px - ex) ** 2 + (py - ey) ** 2 < 1600:
#         msg = "КАЛАШИСТ ВАС ПОЙМАЛ. ВАС ЗАРЕЙДИЛИ"
#         run = False
#
#
#     if (px - cx) ** 2 + (py - cy) ** 2 < 900:
#         score += 1
#         cx, cy = random.randint(100, 1500), random.randint(100, 900)
#         if score >= 20:
#             msg = "ВЫ ДОБЫЛИ 20 СЕРЫ. ВЫ ЗАРЕЙДИЛИ КАЛАШИСТА"
#             run = False
#
#
#
#     # --- РИСОВАНИЕ ---
#     sc.fill((0, 0, 0))
#
#     # --- ЭТАП 3: Blit на экран (вместо pg.draw.circle) ---
#     # Мы вычитаем половину размера картинки, чтобы px/py оставались центром объекта
#     sc.blit(img_coin, (cx - 15, cy - 15))
#     sc.blit(img_enemy, (ex - 20, ey - 20))
#     sc.blit(img_player, (px - 20, py - 20))
#
#     txt = f.render(f"Счет: {score} / 20", True, "white")
#     sc.blit(txt, (20, 20))
#
#     # --- ЭТАП 4: Вывод всех слоев на экран ---
#     pg.display.flip()
#     pg.time.delay(20)
#
# # ЭКРАН ЗАВЕРШЕНИЯ
# if msg:
#     sc.fill("black")
#     end_txt = f.render(msg, True, "yellow")
#     sc.blit(end_txt, (400 - end_txt.get_width() // 2, 300))
#     pg.display.flip()
#     pg.time.wait(3000)
#
# pg.quit()
#
# class Player:
#     def __init__(self):
#         self.pos = pygame.Vector2 ()
#
#     class Mob:
#
#         alive = True
#         SPEED_PER_SEC = 200
#         frame = 0
#
#         def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
#             self.pos = pygame.Vector2(
#                 random.randint(0, SCREEN_WIDTH),
#                 random.randint(0, SCREEN_HEIGHT)
#             )
#             self.speed = int(self.SPEED_PER_SEC)
#             a = pygame.image.load("assets\\prepared_img\\pipo-enemy047a.png")
#             b = pygame.image.load("assets\\prepared_img\\pipo-enemy047a2.png")
#             self.anim = [a, b]
#
#             self.animation_timer = 0
#             self.anim_frame_speed = 0.5
#
#
#
# #Для анимаций
#     def draw_me(self, screen, dt):
#         frame = self.get_animation_frame(dt)
#         #Для того, чтобы был посередине, если лень делать rect
#         blit_pos = (self.pos.x - frame.get_width() // 2,
#                     self.pos.y - frame.get_height() // 2)
#         screen.blit(frame, blit_pos)
#
#
#     def get_animation_frame(self, dt):
#         self.animation_timer += dt
#         if self.animation_timer >= self.anim_frame_speed:
#             self.frame += 1
#             if self.frame == len(self.anim):
#                 self.frame = 0
#             self.animation_timer = 0
#         return self.anim[self.frame]
#
# import pygame
# import random
#
# class Player:
#     def __init__(self, x, y):
#         self.pos = pygame.Vector2(x, y)
#         self.score = 0
#
#         a = pygame.image.load("pipo-enemy047a.png")
#         b = pygame.image.load("pipo-enemy047a2.png")
#         self.anim = [a, b]
#         self.frame = 0
#         self.animation_timer = 0
#         self.anim_frame_speed = 0.2
#
#     def draw_me(self, screen, dt):
#
#         self.animation_timer += dt
#         if self.animation_timer >= self.anim_frame_speed:
#             self.frame = (self.frame + 1) % len(self.anim)
#             self.animation_timer = 0
#
#         current_frame = self.anim[self.frame]
#
#         blit_pos = (self.pos.x - current_frame.get_width() // 2,
#                     self.pos.y - current_frame.get_height() // 2)
#         screen.blit(current_frame, blit_pos)
#
# class Mob:
#     def __init__(self, sw, sh):
#         self.pos = pygame.Vector2(random.randint(0, sw), random.randint(0, sh))
#         self.speed = 150
#
#     def update(self, target_pos, dt):
#
#         dir = (target_pos - self.pos)
#         if dir.length() > 0:
#             self.pos += dir.normalize() * self.speed * dt
#
#     def draw(self, screen):
#         pygame.draw.circle(screen, "red", self.pos, 20)
#
# pygame.init()
# SW, SH = 800, 600
# screen = pygame.display.set_mode((SW, SH))
# clock = pygame.time.Clock()
# font = pygame.font.SysFont("Arial", 32)
#
# player = Player(400, 300)
# enemy = Mob(SW, SH)
# coin_pos = pygame.Vector2(random.randint(50, 750), random.randint(50, 550))
#
# running = True
# msg = ""
#
# while running:
#     dt = clock.tick(60) / 1000.0
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: running = False
#
#     if not msg:
#
#         keys = pygame.key.get_pressed()
#         move = pygame.Vector2(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT],
#                               keys[pygame.K_DOWN] - keys[pygame.K_UP])
#         if move.length() > 0:
#             player.pos += move.normalize() * 300 * dt
#
#         enemy.update(player.pos, dt)
#
#         if player.pos.distance_to(enemy.pos) < 45:
#             msg = "ПРОИГРЫШ! ВРАГ ПОЙМАЛ"
#
#         if player.pos.distance_to(coin_pos) < 35:
#             player.score += 1
#             coin_pos = pygame.Vector2(random.randint(50, 750), random.randint(50, 550))
#             if player.score >= 20:
#                 msg = "ПОБЕДА! 20 МОНЕТ!"
#
#     screen.fill((30, 30, 30))
#
#     pygame.draw.circle(screen, "gold", coin_pos, 10)  #
#     enemy.draw(screen)
#     player.draw_me(screen, dt)
#
#     score_txt = font.render(f"Счет: {player.score}/20", True, "white")
#     screen.blit(score_txt, (10, 10))
#
#     if msg:
#          res_txt = font.render(msg, True, "yellow")
#          screen.blit(res_txt, (SW // 2 - res_txt.get_width() // 2, SH // 2))
#          pygame.display.flip()
#          pygame.time.wait(3000)
#          running = False
#
#     pygame.display.flip()
#
# pygame.quit()

# from random import randint
# import pygame as pg
# import sys
#
# W = 400
# H = 400
# WHITE = (255, 255, 255)
#
#
# class Car(pg.sprite.Sprite):
#     def __init__(self, x, filename):
#         pg.sprite.Sprite.__init__(self)
#         self.raw_image=pg.image.load(filename).convert_alpha()
#         self.image=pg.transform.scale(self.raw_image,(35,60))
#         self.rect=self.image.get_rect(center=(x, 0))
#
#     def update(self):
#
#         if self.rect.y < H:
#            self.rect.y += 2
#         else:
#            self.rect.y = 0
#
#
# sc = pg.display.set_mode((W, H))
#
#
# car1 = Car(randint(1, W), 'Screenshot_1.png')
# car2 = Car(randint(1, W), 'Screenshot_2.png')
# car3 = Car(randint(1, W), 'Screenshot_3.png')
#
# while 1:
#     for i in pg.event.get():
#         if i.type == pg.QUIT:
#             sys.exit()
#
#     sc.fill(WHITE)
#
#
#     sc.blit(car1.image, car1.rect)
#     sc.blit(car2.image, car2.rect)
#     sc.blit(car3.image, car3.rect)
#
#     pg.display.update()
#     pg.time.delay(20)
#
#
#     car1.update()
#     car2.update()
#     car3.update()
#
# from random import randint
# import pygame as pg
# import sys
#
#
# pg.init()
#
#
# pg.time.set_timer(pg.USEREVENT, 3000)
#
#
# W = 400
# H = 400
# WHITE = (255, 255, 255)
#
#
# CARS = ('Screenshot_1.png', 'Screenshot_2.png', 'Screenshot_2.png')
#
# CARS_SURF = []
#
#
# sc = pg.display.set_mode((W, H))
#
#
# for i in range(len(CARS)):
#     CARS_SURF.append(pg.image.load(CARS[i]).convert_alpha())
#
# class Car(pg.sprite.Sprite):
#     def __init__(self, x, surf, group):
#         pg.sprite.Sprite.__init__(self)
#         self.image = surf
#
#         self.rect = self.image.get_rect(center=(x, 0))
#
#         self.add(group)
#
#         self.speed = randint(1, 3)
#
#     def update(self):
#         if self.rect.y < H:
#             self.rect.y += self.speed
#         else:
#
#             self.kill()
#
#
# cars = pg.sprite.Group()
#
#
# Car(randint(1, W), CARS_SURF[randint(0, 2)], cars)
#
#
# clock = pg.time.Clock()
# while True:
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()
#             sys.exit()
#         if event.type == pg.USEREVENT:
#
#             Car(randint(1, W), CARS_SURF[randint(0, 2)], cars)
#
#     sc.fill(WHITE)
#     cars.update()
#     cars.draw(sc)
#     pg.display.update()
#     clock.tick(60)
#
#     while 1:
#         for i in pg.event.get():
#             if i.type == pg.QUIT:
#                 sys.exit()
#             elif i.type == pg.USEREVENT:
#                 Car(randint(1, W), CARS_SURF[randint(0, 2)], cars)
#
#         sc.fill(WHITE)
#
#         cars.draw(sc)
#
#         pg.display.update()
#         pg.time.delay(20)
#
#         cars.update()

# def __init__(self, x, y):
#     self.pos = pygame.Vector2(x, y)
#     self.score = 0
#
#     a = pygame.image.load("pipo-enemy047a.png")
#     b = pygame.image.load("pipo-enemy047a2.png")
#     self.anim = [a, b]
#     self.frame = 0
#     self.animation_timer = 0
#     self.anim_frame_speed = 0.2
#
#
# class Player:
#     def __init__(self):
#         self.pos = pygame.Vector2 ()
#
#     class Mob:
#
#         alive = True
#         SPEED_PER_SEC = 200
#         frame = 0
#
#         def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT):
#             self.pos = pygame.Vector2(
#                 random.randint(0, SCREEN_WIDTH),
#                 random.randint(0, SCREEN_HEIGHT)
#             )
#             self.speed = int(self.SPEED_PER_SEC)
#             a = pygame.image.load("assets\\prepared_img\\pipo-enemy047a.png")
#             b = pygame.image.load("assets\\prepared_img\\pipo-enemy047a2.png")
#             self.anim = [a, b]
#
#             self.animation_timer = 0
#             self.anim_frame_speed = 0.5
#
#
#
# #Для анимаций
#     def draw_me(self, screen, dt):
#         frame = self.get_animation_frame(dt)
#         #Для того, чтобы был посередине, если лень делать rect
#         blit_pos = (self.pos.x - frame.get_width() // 2,
#                     self.pos.y - frame.get_height() // 2)
#         screen.blit(frame, blit_pos)
#
#
#     def get_animation_frame(self, dt):
#         self.animation_timer += dt
#         if self.animation_timer >= self.anim_frame_speed:
#             self.frame += 1
#             if self.frame == len(self.anim):
#                 self.frame = 0
#             self.animation_timer = 0
#         return self.anim[self.frame]
#
# import pygame
# import random
#
# class Player:
#
#
#     flame = list = pygame.image.load()
#     tl_weiglt = 800
#     tl_height = 600
#     self.frame
#
#     flamec_in_row = 5
#     rows = 3
#     flame_rect = pygame.Rect(0, 0)
#
#     sprite - sheet = pygame.image.ioad('adventure_tilesheet.png').convert_alpha()
#     flame_rect = pygame.Rect(0, 0, )
#
#
#     def draw_me(self, screen, dt):
#
#         self.animation_timer += dt
#         if self.animation_timer >= self.anim_frame_speed:
#             self.frame = (self.frame + 1) % len(self.anim)
#             self.animation_timer = 0
#
#         current_frame = self.anim[self.frame]
#
#         blit_pos = (self.pos.x - current_frame.get_width() // 2,
#                     self.pos.y - current_frame.get_height() // 2)
#         screen.blit(current_frame, blit_pos)
#
# class Mob:
#     def __init__(self, sw, sh):
#         self.pos = pygame.Vector2(random.randint(0, sw), random.randint(0, sh))
#         self.speed = 150
#
#     def update(self, target_pos, dt):
#
#         dir = (target_pos - self.pos)
#         if dir.length() > 0:
#             self.pos += dir.normalize() * self.speed * dt
#
#     def draw(self, screen):
#         pygame.draw.circle(screen, "red", self.pos, 20)
#
# pygame.init()
# SW, SH = 800, 600
# screen = pygame.display.set_mode((SW, SH))
# clock = pygame.time.Clock()
# font = pygame.font.SysFont("Arial", 32)
#
# player = Player(400, 300)
# enemy = Mob(SW, SH)
# coin_pos = pygame.Vector2(random.randint(50, 750), random.randint(50, 550))
#
# running = True
# msg = ""
#
# while running:
#     dt = clock.tick(60) / 1000.0
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: running = False
#
#     if not msg:
#
#         keys = pygame.key.get_pressed()
#         move = pygame.Vector2(keys[pygame.K_RIGHT] - keys[pygame.K_LEFT],
#                               keys[pygame.K_DOWN] - keys[pygame.K_UP])
#         if move.length() > 0:
#             player.pos += move.normalize() * 300 * dt
#
#         enemy.update(player.pos, dt)
#
#         if player.pos.distance_to(enemy.pos) < 45:
#             msg = "ПРОИГРЫШ! ВРАГ ПОЙМАЛ"
#
#         if player.pos.distance_to(coin_pos) < 35:
#             player.score += 1
#             coin_pos = pygame.Vector2(random.randint(50, 750), random.randint(50, 550))
#             if player.score >= 20:
#                 msg = "ПОБЕДА! 20 МОНЕТ!"
#
#     screen.fill((30, 30, 30))
#
#     pygame.draw.circle(screen, "gold", coin_pos, 10)  #
#     enemy.draw(screen)
#     player.draw_me(screen, dt)
#
#     score_txt = font.render(f"Счет: {player.score}/20", True, "white")
#     screen.blit(score_txt, (10, 10))
#
#     if msg:
#          res_txt = font.render(msg, True, "yellow")
#          screen.blit(res_txt, (SW // 2 - res_txt.get_width() // 2, SH // 2))
#          pygame.display.flip()
#          pygame.time.wait(3000)
#          running = False
#
#     pygame.display.flip()
#
# pygame.quit()
#
# import pygame
# import random
#
# pygame.init()
#
# screen = pygame.display.set_mode((800, 600))
# clock = pygame.time.Clock()
# FPS=60
#
#
# class Player:
#     def __init__(self):
#         self.pos = pygame.Vector2(400, 500)
#         self.speed = 300
#         self.sprite
#         self.tl_weiglt = 800
#         self.tl_height = 600
#         self.
#         self
#         self
#         self
#         self
#
# player = Player()
#
# running = True
# while running:
#     dt = clock.tick(FPS) / 1000
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     screen.fill((30, 30, 30))
#     player.draw(screen, dt)
#
#     pygame.display.flip()
#
# pygame.quit()

# SHA256:FsbRkxlF1Kk9l8vH3uqZ5Crxwe1W4CtlkBQhUK2UCxQ artembodic138@gmail.com
# git config --global user.email "artembodic138@gmail.com"
# git config --global user.name "Artem"
# ssh-keygen -t ed25519 -C "artembodic138@gmail.com"

# import pygame
# import sys
#
# pygame.init()
# WIDTH, HEIGHT = 800, 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# clock = pygame.time.Clock()
#
# # Цвета
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# YELLOW = (255, 255, 0)
# all_sprites = pygame.sprite.Group()
# bullets_group = pygame.sprite.Group()
#
# class Bullet(pygame.sprite.Sprite):
#     def __init__(self, start_pos, target_pos):
#         super().__init__()
#
#         pygame.draw.circle(self.image, YELLOW, (5, 5), 5)
#         self.image.set_colorkey((0, 0, 0))
#         self.rect = self.image.get_rect(center=start_pos)
#
#
#         direction = pygame.Vector2(target_pos) - start_pos
#         if direction.length() > 0:
#             self.velocity = direction.normalize() * 7
#         else:
#             self.velocity = pygame.Vector2(0, -7)
#
#     def update(self):
#         self.rect.centerx += self.velocity.x
#         self.rect.centery += self.velocity.y
#
#         if not screen.get_rect().colliderect(self.rect):
#             self.kill()
#
#
# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.Surface((50, 50))
#         self.image.fill(RED)
#         self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
#         self.speed = 5
#
#     def update(self):
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_w]: self.rect.y -= self.speed
#         if keys[pygame.K_s]: self.rect.y += self.speed
#         if keys[pygame.K_a]: self.rect.x -= self.speed
#         if keys[pygame.K_d]: self.rect.x += self.speed
#
#
# class TargetObject(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.Surface((40, 40))
#         self.image.fill(BLUE)
#         self.rect = self.image.get_rect(center=(100, 100))
#
#     def move_to(self, pos):
#         self.rect.center = pos
#
#
# class DraggableObject(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.Surface((60, 60))
#         self.image.fill(GREEN)
#         self.rect = self.image.get_rect(center=(200, 400))
#         self.dragging = False
#         self.offset_x = 0
#         self.offset_y = 0
#
#     def handle_event(self, event):
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if event.button == 1 and self.rect.collidepoint(event.pos):
#                 self.dragging = True
#                 self.offset_x = self.rect.x - event.pos[0]
#                 self.offset_y = self.rect.y - event.pos[1]
#         elif event.type == pygame.MOUSEBUTTONUP:
#             if event.button == 1:
#                 self.dragging = False
#
#     def update(self):
#         if self.dragging:
#             mouse_x, mouse_y = pygame.mouse.get_pos()
#             self.rect.x = mouse_x + self.offset_x
#             self.rect.y = mouse_y + self.offset_y
#
#
# player = Player()
# target_obj = TargetObject()
# drag_obj = DraggableObject()
#
# all_sprites.add(player, target_obj, drag_obj)
#
# running = True
# while running:
#     screen.fill(WHITE)
#     events = pygame.event.get()
#     for event in events:
#         if event.type == pygame.QUIT:
#             running = False
#
#         if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
#             target_obj.move_to(event.pos)
#
#         drag_obj.handle_event(event)
#
#         if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
#             new_bullet = Bullet(player.rect.center, event.pos)
#             bullets_group.add(new_bullet)
#             all_sprites.add(new_bullet)
#
#     all_sprites.update()
#
#     all_sprites.draw(screen)
#     pygame.display.flip()
#     clock.tick(60)
#
# pygame.quit()
# sys.exit()

# https://github.com/artembodic138/good-repository/pull/new/feature-object-2
# https://github.com/artembodic138/good-repository/pull/new/feature-drag-and-drop
#

# import pygame
# import random
# import math
#
# # Инициализация
# pygame.init()
#
# # Константы
# WIDTH, HEIGHT = 800, 600
# WHITE = (255, 255, 255)
# GOLD = (255, 215, 0)
# RED = (220, 20, 60)
# BLUE = (30, 144, 255)
# GREEN = (50, 205, 50)
# BLACK = (0, 0, 0)
#
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Coin Collector & Shooter")
# clock = pygame.time.Clock()
#
#
# # Класс Игрока
# class Player:
#     def __init__(self):
#         self.rect = pygame.Rect(400, 300, 40, 40)
#         self.speed = 5
#         self.score = 0
#
#     def move(self, keys):
#         if keys[pygame.K_LEFT] and self.rect.left > 0: self.rect.x -= self.speed
#         if keys[pygame.K_RIGHT] and self.rect.right < WIDTH: self.rect.x += self.speed
#         if keys[pygame.K_UP] and self.rect.top > 0: self.rect.y -= self.speed
#         if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT: self.rect.y += self.speed
#
#     def draw(self):
#         pygame.draw.rect(screen, BLUE, self.rect)
#
#
# # Класс Врага
# class Enemy:
#     def __init__(self):
#         self.rect = pygame.Rect(100, 100, 40, 40)
#         self.vx = random.choice([-3, 3])
#         self.vy = random.choice([-3, 3])
#
#     def move(self):
#         self.rect.x += self.vx
#         self.rect.y += self.vy
#         # Отскок от стен
#         if self.rect.left <= 0 or self.rect.right >= WIDTH: self.vx *= -1
#         if self.rect.top <= 0 or self.rect.bottom >= HEIGHT: self.vy *= -1
#
#         if random.random() < 0.02:
#             self.vx = random.randint(-4, 4)
#             self.vy = random.randint(-4, 4)
#
#     def draw(self):
#         pygame.draw.rect(screen, RED, self.rect)
#
# class Coin:
#     def __init__(self):
#         self.spawn()
#
#     def spawn(self):
#         self.rect = pygame.Rect(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50), 20, 20)
#
#     def draw(self):
#         pygame.draw.ellipse(screen, GOLD, self.rect)
#
# class Projectile:
#     def __init__(self, start_pos, target_pos):
#         self.pos = list(start_pos)
#         angle = math.atan2(target_pos[1] - start_pos[1], target_pos[0] - start_pos[0])
#         self.vx = math.cos(angle) * 7
#         self.vy = math.sin(angle) * 7
#
#     def move(self):
#         self.pos[0] += self.vx
#         self.pos[1] += self.vy
#
#     def draw(self):
#         pygame.draw.circle(screen, BLACK, (int(self.pos[0]), int(self.pos[1])), 5)
#
#
#
# platform = pygame.Rect(300, 250, 200, 20)
# platform_health = 3
#
# player = Player()
# enemy = Enemy()
# coins = [Coin() for _ in range(5)]
# projectiles = []
#
# font = pygame.font.SysFont("Arial", 24)
#
# running = True
# while running:
#     screen.fill(WHITE)
#     keys = pygame.key.get_pressed()
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         # Стрельба на клик мыши
#         if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#             projectiles.append(Projectile(player.rect.center, event.pos))
#
#     player.move(keys)
#     enemy.move()
#
#     for coin in coins:
#         if player.rect.colliderect(coin.rect):
#             player.score += 1
#             coin.spawn()
#
#     for p in projectiles[:]:
#         p.move()
#         p_rect = pygame.Rect(p.pos[0], p.pos[1], 5, 5)
#
#         if platform_health > 0 and p_rect.colliderect(platform):
#             platform_health -= 1
#             projectiles.remove(p)
#             continue
#
#         if not (0 < p.pos[0] < WIDTH and 0 < p.pos[1] < HEIGHT):
#             projectiles.remove(p)
#
#     if player.rect.colliderect(enemy.rect):
#         print(f"Игра окончена! Счёт: {player.score}")
#         running = False
#
#     player.draw()
#     enemy.draw()
#     for coin in coins: coin.draw()
#     for p in projectiles: p.draw()
#
#     if platform_health > 0:
#         pygame.draw.rect(screen, GREEN, platform)
#         hp_text = font.render(f"HP: {platform_health}", True, BLACK)
#         screen.blit(hp_text, (platform.x + 70, platform.y - 25))
#
#     score_surface = font.render(f"Счёт: {player.score}", True, BLACK)
#     screen.blit(score_surface, (10, 10))
#
#     pygame.display.flip()
#     clock.tick(60)
#
# pygame.quit()

import pygame
import random
import math

# Настройки
WIDTH, HEIGHT = 800, 600
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def load_res(name, size):
    try:
        img = pygame.image.load(name).convert_alpha()
        return pygame.transform.scale(img, size)
    except:
        surf = pygame.Surface(size)
        surf.fill((200, 50, 50))
        return surf


# Ресурсы
coin_imgs = [load_res(f"537313244285364442{i}.jpg", (30, 30)) for i in range(2, 7)]
enemy_imgs = [load_res("pipo-enemy047a.png", (50, 50)), load_res("pipo-enemy047a2.png", (50, 50))]
bullet_img = load_res("Снимок.PNG", (15, 25))
player_img_orig = load_res("чел.png", (50, 50))
wall_tex_v = load_res("стена.png", (20, 80))  # Вертикальная
wall_tex_h = load_res("стена.png", (120, 20))  # Горизонтальная


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img_orig
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 50))
        self.angle = 0
        self.score = 0

    def update(self, keys):
        old_pos = self.rect.topleft
        if keys[pygame.K_LEFT]:  self.rect.x -= 5; self.angle = 90
        if keys[pygame.K_RIGHT]: self.rect.x += 5; self.angle = -90
        if keys[pygame.K_UP]:    self.rect.y -= 5; self.angle = 0
        if keys[pygame.K_DOWN]:  self.rect.y += 5; self.angle = 180

        self.image = pygame.transform.rotate(player_img_orig, self.angle)
        new_rect = self.image.get_rect(center=self.rect.center)

        # Коллизия игрока со стенами
        self.rect = new_rect
        if pygame.sprite.spritecollideany(self, walls_group):
            self.rect.topleft = old_pos


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = enemy_imgs[0]
        self.rect = self.image.get_rect(center=pos)
        self.vx, self.vy = 3, 3
        self.frame = 0

    def update(self, *args):
        # Движение по X с отскоком от стен
        self.rect.x += self.vx
        if self.rect.left < 0 or self.rect.right > WIDTH or pygame.sprite.spritecollideany(self, walls_group):
            self.vx *= -1
            self.rect.x += self.vx

        # Движение по Y с отскоком
        self.rect.y += self.vy
        if self.rect.top < 0 or self.rect.bottom > HEIGHT or pygame.sprite.spritecollideany(self, walls_group):
            self.vy *= -1
            self.rect.y += self.vy

        self.frame = (self.frame + 0.1) % 2
        self.image = enemy_imgs[int(self.frame)]


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, is_vertical=True):
        super().__init__()
        self.image = wall_tex_v if is_vertical else wall_tex_h
        self.rect = self.image.get_rect(center=(x, y))
        self.hp = 3


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, target):
        super().__init__()
        angle = math.atan2(target[1] - pos[1], target[0] - pos[0])
        self.image = pygame.transform.rotate(bullet_img, -math.degrees(angle) - 90)
        self.rect = self.image.get_rect(center=pos)
        self.vx, self.vy = math.cos(angle) * 10, math.sin(angle) * 10

    def update(self, *args):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if not screen.get_rect().colliderect(self.rect): self.kill()


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_imgs[0]
        self.rect = self.image.get_rect(center=(random.randint(50, 750), random.randint(50, 550)))
        self.frame = 0

    def update(self, *args):
        self.frame = (self.frame + 0.2) % 5
        self.image = coin_imgs[int(self.frame)]


# Инициализация
all_sprites = pygame.sprite.Group()
walls_group = pygame.sprite.Group()
coins_group = pygame.sprite.Group()
bullets_group = pygame.sprite.Group()

player = Player();
all_sprites.add(player)
enemy = Enemy((100, 100));
all_sprites.add(enemy)

# Создание стен
all_walls = [
    Wall(WIDTH // 2, HEIGHT // 2, False),  # Центральная
    Wall(200, 150), Wall(600, 150),  # Верхние вертикальные
    Wall(200, 450), Wall(600, 450)  # Нижние вертикальные
]
for w in all_walls:
    walls_group.add(w);
    all_sprites.add(w)

for _ in range(5):
    c = Coin();
    coins_group.add(c);
    all_sprites.add(c)

# Главный цикл
run = True
print("Собери 20 монет для победы!")
while run:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            b = Bullet(player.rect.center, event.pos)
            all_sprites.add(b);
            bullets_group.add(b)

    all_sprites.update(keys)

    # Коллизии пуль со стенами (3 попадания)
    hits = pygame.sprite.groupcollide(bullets_group, walls_group, True, False)
    for wall_list in hits.values():
        for w in wall_list:
            w.hp -= 1
            if w.hp <= 0: w.kill()

    # Сбор монет и СЧЕТ
    if pygame.sprite.spritecollide(player, coins_group, True):
        player.score += 1
        print(f"Счет: {player.score}")  # Вывод счета
        if player.score >= 20:
            print("ПОБЕДА!")  # Условие победы
            run = False
        else:
            c = Coin();
            coins_group.add(c);
            all_sprites.add(c)

    # Проигрыш
    if player.rect.colliderect(enemy.rect):
        print("ИГРА ОКОНЧЕНА! Враг тебя поймал.")
        run = False

    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

git checkout main

git checkout -b feature-Dz-9-april

git add .

git commit -m "Dz 9 April: Coins, Player, Enemy, Wall"

git push -u origin feature-Dz-9-april














