import pygame
import asyncio  # Required for web compatibility

# Initialize game elements
pygame.init()
screen = pygame.display.set_size((800, 600))

async def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.fill((0, 0, 0))
        pygame.display.flip()
        
        # CRITICAL: Gives control back to the browser thread
        await asyncio.sleep(0) 

# Start the event loop execution
asyncio.run(main())
