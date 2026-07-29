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
        pygame.display.flip()
        
        # CRITICAL: This allows the browser to render frames without crashing
        await asyncio.sleep(0) 
        clock.tick(60)

# Yes this normally would be an error however since pyscript runs the python file in an async top level awaits are permitted. ik its weird
await main()
