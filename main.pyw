import mss, glitchart, pygame, ctypes, os

# Makes screenshot and glitch effect for it
def screenshot():
	mss.mss().shot()
	glitchart.png('monitor-1.png')

def main():
	screenshot()

	pygame.init()
	pygame.mouse.set_visible(False)
	white = (255, 255, 255)

	# Works only on Windows
	X = ctypes.windll.user32.GetSystemMetrics(0) # Get monitor width
	Y = ctypes.windll.user32.GetSystemMetrics(1) # Get monitor height

	display_surface = pygame.display.set_mode((X, Y))
	  
	image = pygame.image.load(f'{os.getcwd()}\\monitor-1_glitch.png')

	while True:
		display_surface.fill(white)
		display_surface.blit(image, (0, 0))
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					quit()

		screenshot()
		image = pygame.image.load(f'{os.getcwd()}\\monitor-1_glitch.png')
		pygame.display.update()

if __name__ == '__main__':
	main()
