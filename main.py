import asyncio
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

async def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill((30, 30, 30)) # Dark gray background
        print("Tick")
        pygame.display.flip()
        
        await asyncio.sleep(0) 
        clock.tick(60)

await main()
