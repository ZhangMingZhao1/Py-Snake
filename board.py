#棋盘类
import random
import math
import copy
from const import *
class Board:
	def __init__(self):
		pass
	#属性
	food = [4,5]
	head = [0,0]
	tailArr = []
	direct = 1
 
	def set_food(self,food):
		self.food = food
	def set_head(self,head):
		self.head = head
	def set_tailArr(self,tailArr):
		self.tailArr = tailArr
	def set_direct(self,direct):
		self.direct = direct
	def initFoodPos(self):
		while True:
			x=math.floor(random.random() * const.BOARD_WIDTH)
			y=math.floor(random.random() * const.BOARD_HEIGHT)
			if [x,y] == self.head:
				continue
			if [x,y] in self.tailArr:
				continue
			return [x,y]
	#参数pos点用列表表示 列表里面有两个值 分别表示x和y
	#参数direction方向 值为left right up down
	def move(self,pos,direction):
		nextPos = copy.deepcopy(pos);
		if direction == "left":
			nextPos[0] -= self.direct
		elif direction == "right":
			nextPos[0] += self.direct
		elif direction == "up":
			nextPos[1] -= self.direct
		elif direction == "down":
			nextPos[1] += self.direct
		return nextPos
	def move_with_tail(self,direction):
		if not self.is_move_possible(self.head,direction):
			return const.STATE_GAMEOVER
		food_eated=False
		self.tailArr.insert(0,self.head)
		self.head = self.move(self.head,direction)
		if self.food == self.head:
			self.food = self.initFoodPos()
			food_eated = True
		else:
			self.tailArr.pop()
		if food_eated:
			return const.STATE_EAT_FOOD
		else:
			return const.STATE_MOVE
	def is_in_board(self,pos,direction):
		nextPos=self.move(pos,direction)
		if nextPos[0]<0 or nextPos[0] >= const.BOARD_WIDTH or nextPos[1]<0 or nextPos[1] >= const.BOARD_HEIGHT:
			return False
		return True
	def is_move_possible(self,pos,direction):
		if not self.is_in_board(pos,direction):
			return False
		nextPos = self.move(pos,direction)
		if nextPos in self.tailArr:
			return False
		return True 