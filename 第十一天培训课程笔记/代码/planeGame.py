#coding:utf-8
import os,sys 
import random
from pygame.locals import *
from gameObj import *
#初始化游戏
pygame.init()
#创建一个屏幕，设置宽高
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
#设置标题
pygame.display.set_caption('打飞机游戏')
#载入背景图片(生成一个图片对象)
background_img = pygame.image.load('data\\img\\background.png')
#得到矩形的相关参数
background_img_rect = background_img.get_rect()
#载入游戏结束的图片
game_over_img = pygame.image.load('data\\img\\gameover.png')
game_over_img_rect = game_over_img.get_rect()
#载入大图片  shoot
shoot_img = pygame.image.load('data\\img\\shoot.png')
#载入音效
#整个项目的音乐效果
bullet_sound=pygame.mixer.Sound('data\\audio\\bullet.wav')
enemy1_down_sound=pygame.mixer.Sound('data\\audio\\enemy1_down.wav')
#pygame.mixer.music.load载入文件用于播放
game_music_sound=pygame.mixer.music.load('data\\audio\\game_music.wav')
game_over_sound=pygame.mixer.Sound('data\\audio\\game_over.wav')
#1的声音最大
bullet_sound.set_volume(0.3)
#play(loops=0 -1表示一直重复, start=0.0开始位置 秒数)
pygame.mixer.music.play(-1,0.0)
#设置音量
pygame.mixer.music.set_volume(0.3)
#玩家飞机在shoot图片中的位置列表
hero_rects = []
'''
pygame.Rect(left,top,width,height)  
img.subsurface(pygame.Rect(left,top,width,height))
从大图中得到小图
'''
#正常状态下我方飞机
hero_rects.append(pygame.Rect(0,100,100,125))  
#死亡状态下我方飞机
hero_rects.append(pygame.Rect(163,235,100,125)) 
#我方飞机的初始位置
hero_pos = [0,500]
#生成hero对象
hero = Hero(shoot_img,hero_rects,hero_pos)
#得到子弹图片的位置
bullet_rect = pygame.Rect(1004,987,15,25)
#得到子弹图片，但是还没画
bullet_img = shoot_img.subsurface(bullet_rect)
#敌机图片
enemy1_rect = pygame.Rect(535,615,52,40)
enemy1_img =  shoot_img.subsurface(enemy1_rect)
#敌机被击中时的图片
enemy1_down_rect = pygame.Rect(265,350,52,40)
enemy1_down_img =  shoot_img.subsurface(enemy1_down_rect)
#敌机的精灵组  实现碰撞问题
enemies1 = pygame.sprite.Group()
#敌机死亡的精灵组 实现算积分
enemies1_down = pygame.sprite.Group()
#发射子弹的频率
shot_fre = 0
#是否发射子弹
isShot = True
#生成敌机的频率
enemy_fre = 0
#是否正常运行的变量
isRunning = True
#切换形态的变量
change = 0
#得分
score = 0
#所有的操作都放在一个死循环中，循环不停止，画面就一直更新
while isRunning:
    '''
        帧速率是指程序每秒钟在屏幕中绘制图像的数量，用FPS表示
        一般都能达到每秒60帧，越小越卡
    '''
    pygame.time.Clock().tick(60) 
    
    #绘制背景
    screen.fill(0) #fill(颜色) 设置屏幕的颜色
    #blit(image,rect)与设置背景相关
    screen.blit(background_img,background_img_rect)
    
    #判断用户是否点击了关闭按钮
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    #生成敌机
    if enemy_fre %50 ==0:
        #生成的敌机的坐标范围 (页面宽度之内,0)
        enemy1_pos = [random.randint(0,SCREEN_WIDTH-enemy1_rect.width),0]
        #实例化敌机
        enemy1 = Enemy(enemy1_img,enemy1_down_img,enemy1_pos)
        #敌机加入精灵组
        enemies1.add(enemy1)
    enemy_fre += 1
    if enemy_fre>=50:
        enemy_fre=0

    #绘制我方飞机
    if not hero.is_hit:
        screen.blit(hero.image[change],hero.rect)
    else:
        screen.blit(hero.image[1],hero.rect)
        #画完了爆炸的我方飞机游戏才结束
        isRunning=False
    
    #判断我方飞机与敌方飞机是否相遇
    #pygame.sprite.collide_circle()判断相遇
    for enemy in enemies1:
        #移动敌机
        enemy.move()
        if pygame.sprite.collide_circle(enemy,hero):
            #加入敌机死亡组
            enemies1_down.add(enemy)
            #从敌机组移除
            enemies1.remove(enemy)
            #如果有无敌功能，在此处判断
            hero.is_hit = True 
            break
    #如果敌机移动超过屏幕，移除
        if enemy.rect.top>SCREEN_HEIGHT:
            enemies1.remove(enemy)
            
    #发射子弹,自动发射。如何手动发射?
    if not hero.is_hit:
        if shot_fre %5==0:
            isShot = True
        else:
            isShot = False
        shot_fre+=1
        if shot_fre>=20:
            shot_fre=0
    #移动子弹
        for bullet in hero.bullets:
            bullet.moveUp()
            if bullet.rect.top<0:
                 hero.bullets.remove(bullet)       
    #判断子弹与敌机的相遇问题
#groupcollide(精灵组1,精灵组2,是否移除精灵组1,是否移除精灵组2,回调函数)
#groupcollide(精灵,精灵组,是否移除精灵组,回调函数)
    #collisions是被精灵组1移除的精灵组
    collisions =  pygame.sprite.groupcollide(enemies1, hero.bullets, 1, 1, None)   
    for enemy_down in collisions:
        #把相遇的敌机加入敌机死亡组
        enemies1_down.add(enemy_down)
    
    
    #绘制死亡的敌机,遍历死亡敌机精灵组
    for enemy_down in enemies1_down:
        print('a')
        screen.blit(enemy1_down_img,enemy_down.rect)
        enemies1_down.remove(enemy_down)
        #算分
        score +=10
        
    
    #绘制敌机
    enemies1.draw(screen)
    #绘制子弹
    hero.bullets.draw(screen)
    
    #绘制得分
    #pygame.font.Font(文件名,size)
    score_font = pygame.font.Font('data\\font\\CHILLER.TTF',36)
    #得到文本对象reder(文本,字体是否平滑True,字体颜色,背景颜色 可以为空,位置)
    score_text = score_font.render(str(score),True,(240,0,87))
    score_text_rect = score_text.get_rect()
    screen.blit(score_text,score_text_rect)
    
    #键盘监听
    key_pressed = pygame.key.get_pressed()
    if not hero.is_hit:
        if key_pressed[K_UP] or key_pressed[K_w]:
            hero.moveUp()
        if key_pressed[K_DOWN] or key_pressed[K_s]:
            hero.moveDown()
        if key_pressed[K_LEFT] or key_pressed[K_a]:
            hero.moveLeft()
        if key_pressed[K_RIGHT] or key_pressed[K_d]:
            hero.moveRight()
        if key_pressed[K_c]:
            change = 1
        if key_pressed[K_v]:
            change = 0
        if key_pressed[K_k]:
            #清屏
            for i in enemies1:
                enemies1.remove(i)
                enemies1_down.add(i)
        if key_pressed[K_SPACE] and isShot:
            hero.shoot(bullet_img)
    #屏幕中有任何的改变，都要更新屏幕
    pygame.display.update()
screen.blit(game_over_img,game_over_img_rect)
pygame.display.update()
    #判断用户是否点击了关闭按钮
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()