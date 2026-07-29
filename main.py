import pygame
import asyncio

print("HELLO FROM PYTHON")

pygame.init()

screen = pygame.display.set_mode((800, 600))
screen.fill((255, 0, 255))
pygame.display.flip()

async def main():
    while True:
        print("tick")
        await asyncio.sleep(1)

asyncio.run(main())