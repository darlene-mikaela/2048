from ctypes import Array
import random, math, copy
from tabulate import tabulate
def main():
  board = [['X','X','X','X'],
           ['X','X','X','X'],
           ['X','X','X','X'],
           ['X','X','X','X']]
  # RANDOM START POSITION
  for i in range(3):
    board = add_random(board)

  while boardIsFull(board) == False:
    print(tabulate(board, tablefmt="simple_grid"))
    dir = get_dir(board)
    board = change_dir(dir, board)
    board = add_random(board)

  # IF LOOP ENDED THEN GAME OVER
  print("GAME OVER")
  highScore = 0
  for i in board:
    if 'X' not in i and max(i) > highScore:
      highScore = max(i)
  print(f"Your highest number was {highScore}")

def add_random(board: list, dir: int=2) -> list:
  # FIND MAX MULTIPLE
  maxNum = 2
  for i in board:
    if 'X' not in i and math.log(max(i),2) > maxNum:
      maxNum = math.log(max(i),2)

  while True:
    i = random.randint(0,3)
    j = random.randint(0,3)
    if board[i][j] == 'X':
      board[i][j] = 2**random.randint(1,maxNum)
      break

  return board

# TODO: SEARCH NO MORE MOVES
def boardIsFull(board: list) -> bool:
  for i in range(4):
    if 0 in board[i]:
      return False

  # CHECK UP DOWN
  for i in range(0,4):
    for j in range(0,4):
      if i <= 2 and board[i][j] == board[i+1][j]:
        return False
      if j <= 2 and board[i][j] == board[i][j+1]:
        return False

  return True

# KALO TIDAK ADA YANG BERUBAH ULANGI MEMILIH ARAH
def change_dir(dir: int, arr: list) -> list:
  # LEFT
  if dir == 1: #left
    for i in range(0,4):
      for j in range(1,4): # geser kiri kalo kosong
        # angka ini dan sebelumya sama DAN (sebelumnya tidak sama ATAU sudah paling ujung)
        if arr[i][j] == arr[i][j-1] and arr[i][j] != 'X' and (j-1==0 or (arr[i][j-2] != arr[i][j] and arr[i][0] != 'X')): # tambahin kalo sama
          arr[i][j-1] = arr[i][j-1]*2
          arr[i][j] = 'X'
        if arr[i][j-1] == 'X':
          arr[i].pop(j-1)
          arr[i].append('X')
          break

  # RIGHT #GANTI JADI MULAI KANAN
  elif dir == 2: #right
    for i in range(0,4):
      for j in range(2,-1,-1): 
        if arr[i][j] == arr[i][j+1] and arr[i][j] != 'X' and (j+1==3 or (arr[i][j+2] != arr[i][j] and arr[i][3] != 'X')): # tambahin kalo sama
          arr[i][j+1] = arr[i][j+1]*2
          arr[i].pop(j)
          arr[i].insert(0,'X')
          break
        if arr[i][j+1] == 'X': # geser kanan kalo kosong
          arr[i].pop(j+1)
          arr[i].insert(0,'X')
          break

  # UP
  elif dir == 3: #up
    for i in range(1,4):
      for j in range(0,4):
        if arr[i][j] == arr[i-1][j] and arr[i][j] != 'X' and (i-1==0 or (arr[i-2][j] != arr[i][j] and arr[0][j] != 'X')): # tambahin kalo sama dan mentok
          arr[i-1][j] = arr[i-1][j]*2
          arr[i][j] = 'X'
        if arr[i-1][j] == 'X': # geser atas kalo kosong
          arr[i-1][j] = arr[i][j]
          arr[i][j] = 'X'

  # DOWN
  elif dir==4: #down
    for i in range(2,-1,-1):
      for j in range(0,4):
        if arr[i][j] == arr[i+1][j] and arr[i][j] != 'X' and (i+1==3 or (arr[i+2][j] != arr[i][j] and arr[3][j] != 'X')): # tambahin kalo sama dan mentok
          arr[i+1][j] = arr[i+1][j]*2
          arr[i][j] = 'X'
        if arr[i+1][j] == 'X' and arr[i][j] != 'X': # geser ke bawah kalo kosong
          arr[i+1][j] = arr[i][j]
          arr[i][j] = 'X'

  return arr

def get_dir(board: list) -> int:
  while True:
    try:
      dir = int(input("""Pick a direction
1. Left
2. Right
3. Up
4. Down\n"""))
      changed = copy.deepcopy(board)
      if dir and 1 <= dir and 4 >= dir and change_dir(dir,changed) != board:
        break
    except ValueError:
      continue
  return dir


main()
