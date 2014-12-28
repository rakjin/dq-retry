width = 1
height = 1

matrix = [0]*(width*height)

deltas = [1, width, -1, -width]
direction = 0

go_x = width
go_y = height-1

count, index = 0, -1

while go_x >= 0 and go_y >= 0:
  delta = deltas[direction]
  print('delta: %d' % delta)
  if direction%2 == 0:
    go = go_x
    go_x -= 1
  else:
    go = go_y
    go_y -= 1
  print('go: %d, go_x: %d, go_y: %d' % (go, go_x, go_y))
  if go > 0:
    for i in range(0, go):
      index += delta
      matrix[index] = count
      print('matrix[%d] = %d' % (index, count))
      count += 1
  direction = (direction + 1) % 4

maxnum = width*height-1
digits = len(str(maxnum))

for y in range(0, height):
  padded = [str(x).rjust(digits) for x in matrix[y*width:(y+1)*width]]
  print(' '.join(padded))
