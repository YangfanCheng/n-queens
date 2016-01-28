from func import *


pygame.init()
clock = pygame.time.Clock()


#intro screen
def intro():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quitGame()
		frame.fill(white)
		myFont = pygame.font.SysFont("monospace",36)
		
		Banner = myFont.render("N queens", True, black)
		frame.blit(Banner, (display_size / 3, display_size / 3))
	
		button("start", display_size/3.0, display_size/(golden_ratio), display_size/3.0, 50, green, bright_green, main)
		button("info", display_size/3.0, display_size/(golden_ratio)+50, display_size/3.0, 50, blue, bright_blue, info)
		button("quit", display_size/3.0, display_size/(golden_ratio)+100, display_size/3.0, 50, red, bright_red, quitGame)

		pygame.display.update()
		clock.tick(60)

def main():

	x = 0
	y = 0
	#we start with the first queen at q = 0
	q = 0
	count = 0
	queen = pygame.image.load("queen.png")
	running = True
	queensproblem(q)
	print (len(solutions))
	while running:
		x = 0
		y = 0
		click = pygame.mouse.get_pressed()
		print(click)
		if click[0] == 1:
			count += 1
		if count == len(solutions):
			count = 0
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			


		frame.fill(white)
		square_size = display_size / n
		queen = pygame.transform.scale(queen, (square_size, square_size))
		row = 0
		for j in range(0, display_size, square_size):
			if row % 2 == 0:
				for i in range(0, display_size, square_size * 2):
					frame.fill(black, (x + i, y + j, square_size, square_size))
			else:
				for i in range(square_size, display_size, square_size * 2):
					frame.fill(black, (x + i, y + j, square_size, square_size))
			row += 1
		for item in solutions[count]:
			x = 0
			x = item * square_size
			frame.blit(queen,(x,y))
			y = y + square_size
		#pygame.time.wait(3000)
		pygame.display.update()
		#count += 1
		#if count == len(solutions):
		#	count = 0
		clock.tick(10)
	
	pygame.quit()
	

## n-queens logic
def is_safe(q , r):
	for i in range(q):
		tmp_q = position[i]
		if (tmp_q == r) or (tmp_q == r - (q - i)) or (tmp_q == r + (q - i)):
			return False
	return True

def queensproblem(q):
	# q equals n, we have finished placed all the queens on each row
	if(q == n):
		solution = []
		for i in range(n):
			solution.append(position[i])
		solutions.append(solution)
	else:
		#look for all possibility in each row, 0...n
		for i in range(n):
			if(is_safe(q, i)):
				position[q] = i
				queensproblem(q + 1)


#for solution in queensproblem(n,n):
#   print(solution)
while True:
	n = raw_input("hi, please input n for N queens solutions(n > 3)\nkeep in mind the number of solutions ge generated grows at the expoential rate as n gets bigger.\nn should ideally be less than 10 \ninput: ")
	n = int(n)
	if n > 3:
		break
	else:
		print("n should be greater than 3")

q = 0
solutions = []
position = [None]*n
intro()
main()




