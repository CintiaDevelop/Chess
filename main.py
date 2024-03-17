# Chess Game
import pygame

pygame.init()

width = 1000
height = 1000

screen = pygame.display.set_mode([width,height])
timer = pygame.time.Clock()
fps = 60

# variables and positioning

matrix = [
    ["BRook", "BKnight", "BBishop", "BKing ", "BQueen", "BBishop", "BKnight", "BRook"],
    ["BPawn", " BPawn ", " BPawn ", "BPawn ", "BPawn ", " BPawn ", " BPawn ", "BPawn"],
    ["     ", "       ", "       ", "      ", "      ", "       ", "       ", "     "],
    ["     ", "       ", "       ", "      ", "      ", "       ", "       ", "     "],
    ["     ", "       ", "       ", "      ", "      ", "       ", "       ", "     "],
    ["     ", "       ", "       ", "      ", "      ", "       ", "       ", "     "],
    ["WPawn", " WPawn ", " WPawn ", "WPawn ", "WPawn ", " WPawn ", " WPawn ", "WPawn"],
    ["WRook", "WKnight", "WBishop", "WQueen", "WKing ", "WBishop", "WKnight", "WRook"]
]

captured_pieces_white = []
captured_pieces_black = []

for fila in matrix:
    for elemento in fila:
        print(elemento, end=" ")
    print()

#load pieces images
BRook = pygame.image.load('images/BRook.png')    
BRook = pygame.transform.scale(BRook, (80, 80))
BRook_small = pygame.transform.scale(BRook, (45, 45))
BKinght = pygame.image.load('images/BKnight.png')    
BKnight = pygame.transform.scale(BKinght, (80, 80))
BKnight_small = pygame.transform.scale(BKnight, (45, 45))
BBishop = pygame.image.load('images/BBishop.png')    
BBishop = pygame.transform.scale(BBishop, (80, 80))
BBishop_small = pygame.transform.scale(BBishop, (45, 45))
BQueen = pygame.image.load('images/BQueen.png')    
BQueen = pygame.transform.scale(BQueen, (80, 80))
BQueen_small = pygame.transform.scale(BQueen, (45, 45))
BKing = pygame.image.load('images/BKing.png')    
BKing = pygame.transform.scale(BKing, (80, 80))
BKing_small = pygame.transform.scale(BKing, (45, 45))
BPawn = pygame.image.load('images/BPawn.png')    
BPawn = pygame.transform.scale(BPawn, (65, 65))
BPawn_small = pygame.transform.scale(BPawn, (45, 45))

WRook = pygame.image.load('images/WRook.png')    
WRook = pygame.transform.scale(WRook, (80, 80))
WRook_small = pygame.transform.scale(WRook, (45, 45))
WKinght = pygame.image.load('images/WKnight.png')    
WKnight = pygame.transform.scale(WKinght, (80, 80))
WKnight_small = pygame.transform.scale(WKnight, (45, 45))
WBishop = pygame.image.load('images/WBishop.png')    
WBishop = pygame.transform.scale(WBishop, (80, 80))
WBishop_small = pygame.transform.scale(WBishop, (45, 45))
WQueen = pygame.image.load('images/WQueen.png')    
WQueen = pygame.transform.scale(WQueen, (80, 80))
WQueen_small = pygame.transform.scale(WQueen, (45, 45))
WKing = pygame.image.load('images/WKing.png')    
WKing = pygame.transform.scale(WKing, (80, 80))
WKing_small = pygame.transform.scale(WKing, (45, 45))
WPawn = pygame.image.load('images/BPawn.png')    
WPawn = pygame.transform.scale(WPawn, (65, 65))
WPawn_small = pygame.transform.scaleW(WPawn, (45, 45))

# draw game board
def draw_board():
    for i in range (64):
        column = i % 8
        row = i // 8
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray', [600 - (column * 200), row * 100, 100, 100])
        else:
            pygame.draw.rect(screen, 'light gray', [700 - (column * 200), row * 100, 100, 100])
        pygame.draw.rect(screen, 'gray', [0, 800, width, 100])
        pygame.draw.rect(screen, 'gold', [0, 800, width, 100], 5)
        pygame.draw.rect(screen, 'gold', [800, 0, 200, height], 5)


#game loop
run = True
while run:
    timer.tick(fps)
    screen.fill('dark gray')        
    draw_board()
