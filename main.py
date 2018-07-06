import pygame
from pygame.locals import *
import sys
from const import *
from board import *
def main():
    #初始化pygame
    pygame.init()
    #窗口大小
    SCREEN_SIZE = (const.BOARD_WIDTH*const.BOX,const.BOARD_HEIGHT*const.BOX)
    #初始化board
    board = Board()
    food = board.initFoodPos()
    board.set_food(food) #食物初始化
    board.set_head([0,0]) #蛇头初始化
    board.set_tailArr([]) #蛇尾初始化
    fps = 5
    #三个参数 参数1 分辨率（元组） 参数2 标志位 参数3 颜色深度
    playSurface=pygame.display.set_mode(SCREEN_SIZE,0,32)
	#修改窗口标题
    pygame.display.set_caption("贪吃蛇")
    direction = "right"
    fpsClock = pygame.time.Clock()
    flag=1
    #游戏主循环
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            board.set_direct(1)
            if event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == ord('a')) and (not len(board.tailArr) or direction!="right"):
                    direction = "left"
                elif (event.key == K_RIGHT or event.key == ord('d')) and (not len(board.tailArr) or direction!="left"):
                    direction = "right"
                elif (event.key == K_UP or event.key == ord('w')) and (not len(board.tailArr) or direction!="down"):
                    direction = "up"
                elif (event.key == K_DOWN or event.key == ord('s')) and (not len(board.tailArr) or direction!="up"):
                    direction = "down"
                elif event.key == ord('1'):
                    if flag == 1:
                        fps += 5
                        flag=0
                    elif flag == 0:
                        fps -=5
                        flag=1
                elif event.key == ord('2'):
                   board.set_direct(2)
                elif event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
        cur_state=board.move_with_tail(direction)
        #背景颜色
        playSurface.fill(const.BLACK_COLOR)
        #绘制食物
        #参数1 surface对象 参数2 Color对象 参数3 rect
        pygame.draw.rect(playSurface,const.RED_COLOR,Rect(board.food[0]*const.BOX,board.food[1]*const.BOX,20,20))
        #绘制蛇头
        pygame.draw.rect(playSurface,const.CYAN_COLOR,Rect(board.head[0]*const.BOX,board.head[1]*const.BOX,20,20))
        #绘制蛇尾
        for position in board.tailArr:
            pygame.draw.rect(playSurface,const.BLUE_COLOR,Rect(position[0]*const.BOX,position[1]*const.BOX,20,20))
        #刷新界面
        pygame.display.flip()
        if cur_state == const.STATE_GAMEOVER:
            pygame.event.post(pygame.event.Event(QUIT))
        fpsClock.tick(fps)
 
 
if __name__ == "__main__":
	main()