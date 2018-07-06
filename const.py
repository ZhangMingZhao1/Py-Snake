#存储常量
import pygame
from pygame.locals import *
class Const:
	pass
#创建类的对象 并写入常量
const = Const()
const.BOX = 20 #一个格子的长和宽是20px
const.BOARD_WIDTH = 20 #屏幕的宽
const.BOARD_HEIGHT = 20 #屏幕的高
#颜色的常量
const.BLACK_COLOR=pygame.Color(0,0,0)
const.RED_COLOR=pygame.Color(255,0,0)
const.GREEN_COLOR=pygame.Color(0,255,0)
const.BLUE_COLOR=pygame.Color(0,0,255)
const.YELLOW_COLOR=pygame.Color(255,255,0)
const.CYAN_COLOR=pygame.Color(0,255,255)
const.PUPPLE_COLOR=pygame.Color(255,255,0)
const.WHITE_COLOR=pygame.Color(255,255,255)
const.STATE_GAMEOVER = 0
const.STATE_MOVE = 1
const.STATE_EAT_FOOD = 2 