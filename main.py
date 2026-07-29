import pygame
import asyncio

pygame.init()

screen = pygame.display.set_mode((800, 600))

async def main():
    while True:
        screen.fill((255, 0, 255))
        pygame.display.flip()
        print("tick")
        await asyncio.sleep(0)

asyncio.run(main())