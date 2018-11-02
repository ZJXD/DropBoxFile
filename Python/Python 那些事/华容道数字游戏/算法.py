import random

# 用来存放位置信息的二维数组
blocks = []

# 产生随机数组,0 代表空的位置
arr = range(16)
numbers = random.sample(arr, 16)

for row in range(4):
	blocks.append([])
	for column in range(4):
		blocks[row].append(numbers[row*4 + column])

# 打印结果
for i in range(4):
	print(blocks[i])


# 移动
# zero_row 代表数字0 所在二维数组的行下标，zero_column代表数字0 所在二维数组的列下标
def move(direction):
    if(direction == 'UP'): # 上
        if zero_row != 3:
            blocks[zero_row][zero_column] = blocks[zero_row + 1][zero_column]
            blocks[zero_row + 1][zero_column] = 0
            zero_row += 1
    if(direction == 'DOWN'): # 下
        if zero_row != 0:
            blocks[zero_row][zero_column] = blocks[zero_row - 1][zero_column]
            blocks[zero_row - 1][zero_column] = 0
            zero_row -= 1
    if(direction == 'LEFT'): # 左
        if zero_column != 3:
            blocks[zero_row][zero_column] = blocks[zero_row][zero_column + 1]
            blocks[zero_row][zero_column + 1] = 0
            zero_column += 1
    if(direction == 'RIGHT'): # 右
        if zero_column != 0:
            blocks[zero_row][zero_column] = blocks[zero_row][zero_column - 1]
            blocks[zero_row][zero_column - 1] = 0
            zero_column -= 1

# 检测是否完成
def checkResult():
        # 先检测最右下角是否为0
        if blocks[3][3] != 0:
            return False

        for row in range(4):
            for column in range(4):
            	# 运行到此处说名最右下角已经为0，pass即可
                if row == 3 and column == 3:
                    pass
                # 值是否对应
                elif blocks[row][column] != row * 4 + column + 1:
                    return False

        return True