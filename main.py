import asyncio
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

async def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((255, 0, 255))
        print("Tick")
        pygame.display.flip()

        clock.tick(60)
        await asyncio.sleep(0)

await main()