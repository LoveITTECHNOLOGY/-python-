#coding:utf-8
import pygame
from pygame.locals import *
#设置屏幕大小
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 700
#子弹类,继承pygame中的精灵类,游戏会用到图片、速度、区域大小
class Bullet(pygame.sprite.Sprite):
    def __init__(self,bullet_img,init_pos):
        #子弹的构造函数，传入图片和初识位置
        #调用父类的构造函数，做一个初始化
        super(Bullet,self).__init__()
        self.image = bullet_img
        #得到图片的相关参数(得到精灵这个矩形的一些参数)
        self.rect = self.image.get_rect()
        #设置子弹的 下面中间 这个点的位置
        self.rect.midbottom = init_pos
        #设置速度,移动时的偏移量
        self.speed = 10
    def moveUp(self):
        #我方的子弹向上移动，距离上面的位置越来越小
        self.rect.top -= self.speed   
    def moveDown(self):
        #敌方机发射的子弹向下移动
        pass
#我方飞机
class Hero(pygame.sprite.Sprite):
    def __init__(self,shoot_png,hero_rects,init_pos):
        #hero_rects = [(left,top,width,height),(..),(..)]
        #我方机可能有很多状态，图片不一样，用列表存储
        super(Hero,self).__init__()
        self.image = []#存放我方飞机的图片的列表
        #得到飞机的初始属性
        for i in range(len(hero_rects)):
            #image.subsurface(rects) 从大图中得到小图
            #convert_alpha()填充 画图
            self.image.append(shoot_png.subsurface(hero_rects[i]).convert_alpha())
            self.rect = hero_rects[i]
            #初始化飞机的位置
            self.rect.topleft = init_pos
            self.speed = 8  #还可以通过道具加速
            #定义我方飞机发生的子弹对象
            #pygame.sprite.Group()用来管理大量的实体类
            #精灵组与精灵组直接的碰撞问题已经封装好了，可以直接用
            self.bullets = pygame.sprite.Group() 
            #我方飞机是否被击中   也可以是数值，即血量
            #self.bleed = 10   判断bleed是否为0，游戏是否结束
            self.is_hit = False
            #self.R = 5  #是否可以释放大招
            #self.wudi = False 是否是霸体状态
    #射击的方法
    def shoot(self,bullet_img):
        #实例化子弹
        #self.rect.midtop我方机的 上面中间
        bullet = Bullet(bullet_img,self.rect.midtop)
        #实例化出来的子弹添加至子弹精灵组
        self.bullets.add(bullet) 
    #移动的方法
    def moveUp(self):
        #向上移动，判断self.rect.top属性的值
        if self.rect.top<=0:
            self.rect.top=0
        else:
            self.rect.top -=self.speed
    #自己写完另外三个   self.rect.height 高度
    def moveDown(self):
        #向下移动，极限是top = SCREEN_HEIGHT-self.rect.height
        if self.rect.top>=SCREEN_HEIGHT-self.rect.height:
            self.rect.top=SCREEN_HEIGHT-self.rect.height
        else:
            self.rect.top +=self.speed 
    def moveLeft(self):
        if self.rect.left<=0:
            self.rect.left=0
        else:
            self.rect.left -=self.speed    
    def moveRight(self):
        if self.rect.left>=SCREEN_WIDTH-self.rect.width:
            self.rect.left=SCREEN_WIDTH-self.rect.width
        else:
            self.rect.left +=self.speed     
#敌机
class Enemy(pygame.sprite.Sprite):
    def __init__(self,enemy_img,enemy_down_img,init_pos):
        super(Enemy,self).__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.enemy_down_img = enemy_down_img
        self.speed = 2
    def move(self):
        self.rect.top +=self.speed
                
        
        
        
        