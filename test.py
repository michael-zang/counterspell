import pygame
import sys
from time import *
import time
from random import *

# Importing images
pygame.display.set_caption('image')


# Sprites:
man = pygame.image.load("newhagrid.png")
newbackground = pygame.image.load("bg.webp")
hands = pygame.image.load("hands.png")
handstogether = pygame.image.load("handstogether.png")
background = pygame.image.load("brick.jpeg")
star = pygame.image.load("star.png")

# Jumpscare
darkbackground = pygame.image.load("darkbackground.webp")
facescary = pygame.image.load("facescary.webp")
JS1 = pygame.image.load("JS1.webp")
JS2 = pygame.image.load("JS2.webp")
facescaryBLACK = pygame.image.load("facescaryBLACK.jpeg")

# Initialize Pygame
pygame.init()

# Sound
pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(1.0)
sfx2 = pygame.mixer.Sound("yay.mp3")
sfx2.set_volume(1.0)
sfx1 = pygame.mixer.Sound("lightning.mp3")
sfx1.set_volume(1.0)  # 100% volume
sfx3 = pygame.mixer.Sound("scream.mp3")
sfx3.set_volume(1.5)  # 150% volume
sfx4 = pygame.mixer.Sound("screech.mp3")
sfx4.set_volume(1.0)  # 100% volume
sfx5 = pygame.mixer.Sound("water.mp3")
sfx5.set_volume(1.5)  # 150% volume
sfx6 = pygame.mixer.Sound("warning.mp3")  # The warning sound
sfx6.set_volume(3.0)  # 100% volume


# Set up the display
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Bathroom Mirror and Sink")


# Changing the scale of the images
darkbackground = pygame.transform.scale(darkbackground, (WINDOW_WIDTH, WINDOW_HEIGHT))
background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))
newbackground = pygame.transform.scale(newbackground, (WINDOW_WIDTH, WINDOW_HEIGHT))
man = pygame.transform.scale(man, (280, 250))
star = pygame.transform.scale(star, (75, 75))

handstogether = pygame.transform.scale(handstogether, (200,225))
handstogether_closer = pygame.transform.scale(handstogether, (900, 900))
facescary = pygame.transform.scale(facescary, (280, 250))
JS1 = pygame.transform.scale(JS1, (WINDOW_WIDTH, WINDOW_HEIGHT))
JS2 = pygame.transform.scale(JS2, (WINDOW_WIDTH, WINDOW_HEIGHT))
facescaryBLACK = pygame.transform.scale(facescaryBLACK, (WINDOW_WIDTH, WINDOW_HEIGHT))



# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (6, 15, 28)
MIRRORBLUE = (151, 217, 243)
WATER = (0, 191, 255)
RED = (179, 11, 11)
water_y_pos = 380

# Font setup
font = pygame.font.Font(None, 50)  # Default font, size 50

# Timer and game state variables
epoch = time.time()
total_hands_up_time = 0
last_hands_up_time = 0  
scary_face_shown = False
hands_closer = False
hands_closer_start_time = None
jumpscare_time = 0  # Time when the jumpscare starts
jumpscare_active = False  # Flag for jumpscare state
image_toggle = True  # Toggle between JS1 and JS2
random_jumpscare_time = randint(17, 20)  # Randomize the jumpscare time within 15-17 seconds
jumpscare_triggered = False  # Flag to check if jumpscare time has passed

# Death timer variables
death_time = randint(3, 6)  # Random time between 3 and 6 seconds for the death time
print(death_time)
warning_time = death_time - 1  # 1 second before death
print(warning_time)
death_timer_started = False
warning_triggered = False


while True:
    # Start screen
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                start = False  # Exit start screen

        # Fill the screen and draw start screen elements
        screen.blit(background, (0, 0))

        # Draw text
        text = font.render("Press SPACE to start", True, BLACK)
        text2 = font.render("Toggle space to wash your face", True, BLACK)
        text3 = font.render("45 seconds. Good Luck", True, BLACK)
        screen.blit(text, (200, 500))
        screen.blit(text2, (150, 100))
        screen.blit(text3, (185, 300))

        # Update the display
        pygame.display.flip()

    #timer
    epoch = time.time()

    #total hand up time
    totalhtime = 0
    handup = 0
    handdown = 0
    handuptime = 0

    # Add these variables at the start of your game (where you declare other variables)
    total_hands_up_time = 0
    last_hands_up_time = 0
    scary_face_shown = False

    # Main game loop
    running = True
    hands_closer = False
    hands_closer_start_time = None  # Add this variable to track when hands_closer becomes True

    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                hands_closer = not hands_closer
                if hands_closer:
                    sfx5.play()
                    hands_closer_start_time = time.time()  # Start timing when hands go up
                    death_time = randint(3, 6)
                    warning_time = death_time - 1  # Set warning time to 1 second before death
                    death_timer_started = True
                    warning_triggered = False
                else:
                    sfx5.stop()
                    hands_closer_start_time = None  # Reset timer when hands go down

        # Draw mirror
        pygame.draw.circle(screen, BLACK, (400, 170), 168)
        pygame.draw.circle(screen, MIRRORBLUE, (400, 170), 160)


        # Draw Hagrid
        screen.blit(man, (250, 80))

        screen.blit(newbackground,(0,0))

        # Draw sink
        pygame.draw.rect(screen, GRAY, (250, 400, 300, 200))  # Sink base
        pygame.draw.ellipse(screen, WHITE, (275, 410, 250, 100))  # Sink bowl

        # Draw faucet
        pygame.draw.rect(screen, GRAY, (375, 380, 50, 30))  # Faucet base
        pygame.draw.rect(screen, GRAY, (390, 350, 20, 30))  # Faucet neck

        

        # Update water flow
        water_y_pos += 10
        if water_y_pos > 500:
            water_y_pos = 380
        hand_closer_count = 0

        if hands_closer: # Hands go up
            if handup == 0:
                epoch2 = time.time()
                handup += 1
                handdown += 1
            
            handuptime += 1
            current_time = time.time()
            htime = round(total_hands_up_time + (current_time - epoch2))
            print(f"Current htime: {htime}")

            # Always start with dark background
            screen.blit(darkbackground, (0,0))
            
            # Hagrid progression based on htime
            if htime <= 4:
                screen.blit(man, (250,80))  # Very dirty (initial state)
            elif htime > 4 and htime <= 8:
                screen.blit(man, (250,80))   # Less dirty
            elif htime > 8:
                screen.blit(man, (250,80))  # Cleanest state

            # Always draw hands last
            screen.blit(handstogether_closer, (-50,-20))
        
            
            if htime >= 15:
                # win screen
                pygame.draw.circle(screen, BLACK, (400, 170), 168)
                pygame.draw.circle(screen, MIRRORBLUE, (400, 170), 160)

                screen.blit(man, (250, 80))

                screen.blit(newbackground,(0,0))
                # Draw sink
                pygame.draw.rect(screen, GRAY, (250, 400, 300, 200))  # Sink base
                pygame.draw.ellipse(screen, WHITE, (275, 410, 250, 100))  # Sink bowl

                # Draw faucet
                pygame.draw.rect(screen, GRAY, (375, 380, 50, 30))  # Faucet base
                pygame.draw.rect(screen, GRAY, (390, 350, 20, 30))  # Faucet neck
                
                screen.blit(handstogether, (300, 380))

                screen.blit(star, (400, 100))
                screen.blit(star, (320, 200))
        
                text = font.render("Congratulations, Hagrid cleaned his face", True, BLACK)
                screen.blit(text, (50, 500))
                
                pygame.display.flip()
                sfx2.play()
                hands_closer = False

                sleep(3)
                
                running = False
                start = True
            
            pygame.draw.rect(screen, WHITE, (10, 50, 790, 80), width= 5)
            pygame.draw.rect(screen, WATER, (10, 50, 50+54*htime, 80))
        
        else: # Hands go down

            if handup > 0:
                total_hands_up_time += time.time() - epoch2
                handup = 0
            screen.blit(handstogether, (300,400))
            pygame.draw.line(screen, WATER, (400, 380), (400, water_y_pos), 10)  # Then water

            handuptime = 0
            # Trigger jumpscare if not yet triggered and within random time window
            if not jumpscare_triggered and time.time() - epoch >= random_jumpscare_time:
                jumpscare_triggered = True
                sfx4.play()
                screen.blit(facescaryBLACK, (0, 0))  # Show the facescaryBLACK image for 0.5 seconds
                pygame.display.flip()
                sleep(0.1)  # Delay to show the scary face for 0.5 seconds
            

        #timer counting up all seconds
        if start == False:
            seconds = time.time() - epoch
            if seconds <= 45:
                seconds = str(round(seconds))
                text = font.render(seconds, True, BLACK)
                screen.blit(text, (200, 500))
                seconds = int(seconds)
                
                # Showing the scary face after 10 seconds
                if seconds > 8 and not scary_face_shown:
                    if hands_closer == False:
                        sfx1.play()
                        screen.blit(facescary, (260, 80))
                        pygame.display.flip()
                        sleep(0.25)
                        scary_face_shown = True
                        screen.blit(newbackground,(0,0))
                        screen.blit(man, (250, 80))
                        screen.blit(handstogether, (300, 400))  # Always draw hands last
                        pygame.mixer.music.play(-1)  # -1 makes the music loop indefinitely


            else:
                pygame.mixer.music.stop()
                hands_closer = False

                pygame.draw.circle(screen, BLACK, (400, 170), 168)
                pygame.draw.circle(screen, MIRRORBLUE, (400, 170), 160)

                screen.blit(man, (250, 80))

                screen.blit(newbackground,(0,0))
        
                text = font.render("Hagrid failed to clean his face", True, BLACK)
                screen.blit(text, (50, 500))
                
                pygame.display.flip()
                sleep(3)
                
                running = False
                start = True
        
        # Update the display
        pygame.display.flip()
        sleep(0.0005)

        if hands_closer:
            if time.time() - hands_closer_start_time >= death_time-1.5 and not warning_triggered:
                sfx6.play()
                warning_triggered = True
            # Check if random seconds have passed since hands went up
            elif time.time() - hands_closer_start_time >= death_time:
                print(time.time() - hands_closer_start_time)
                # Jumpscare effect: Alternate images quickly
                start_jumpscare_time = time.time()  # Start the jumpscare timer
                while time.time() - start_jumpscare_time < 2:  # Run for 2 seconds
                    # Alternate between JS1 and JS2 every 0.1 second
                    current_time = time.time()
                    sfx3.play()
                    if current_time % 0.02 < 0.01:  # Show JS1 for 0.1 seconds
                        screen.blit(JS1, (0, 0))
                    else:  # Show JS2 for the next 0.1 seconds
                        screen.blit(JS2, (0, 0))
                    pygame.display.flip()

                    sleep(0.00001)
            # After jumpscare ends, reset the game instead of exiting
                screen.blit(background, (0, 0))  # Dark background
                text = font.render("Game Over! You lost!", True, BLACK)
                text2 = font.render("Try not toggle space for so long", True, BLACK)
                screen.blit(text2, (150, 500))
                screen.blit(text, (200, 300))
                pygame.display.flip()

                pygame.mixer.music.stop()  # Stop the background music
                sleep(2)  # Wait for 2 seconds before closing
                # Reset game state
                scary_face_shown = False
                hands_closer = False

                total_hands_up_time = 0
                last_hands_up_time = 0
                epoch = time.time()  # Reset the timer
                start = True  # Go back to the start screen
                break  # Exit the current game loop to go back to the start screen
            

# Quit Pygame
pygame.quit()
sys.exit()      