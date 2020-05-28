import pygame # Loading pygame

# Setting up window
pygame.init()
window = pygame.display.set_mode((1000,500))
pygame.display.set_caption("GreenCubic")
icon = pygame.image.load('data/icon.ico')
pygame.display.set_icon(icon)

# Making loading screen
window.fill((255,255,255))

arial100 = pygame.font.Font('data/fonts/arial.ttf',100)
arial80 = pygame.font.Font('data/fonts/arial.ttf',80)
arial40 = pygame.font.Font('data/fonts/arial.ttf',40)

GreenCubicText = arial100.render("GreenCubic",1,(0,0,0))
loadingText = arial80.render("Loading...",1,(0,0,0))

window.blit(GreenCubicText,(175,100))
window.blit(loadingText,(300,250))

pygame.draw.rect(window,(0,255,0),(725,120,75,75))
pygame.display.update()

loadingModulesText = arial40.render("Loading modules...",1,(0,0,0))
loadingSettingsText = arial40.render("Loading settings...",1,(0,0,0))
settingUpDiscordRPCText = arial40.render("Setting up discord RPC...",1,(0,0,0))
loadingVariablesText = arial40.render("Loading variables...",1,(0,0,0))
loadingFontsText = arial40.render("Loading fonts...",1,(0,0,0))
prerenderingTextsText = arial40.render("Prerendering texts...",1,(0,0,0))
loadingTexturesText = arial40.render("Loading textures...",1,(0,0,0))
loadingClassesText = arial40.render("Loading classes...",1,(0,0,0))

# Loading other modules
window.blit(loadingModulesText,(300,400))
pygame.display.update()
from time import time
from pypresence import Presence
from configparser import ConfigParser
from json import load as JSONload

# Loading settings
pygame.draw.rect(window,(255,255,255),(100,350,700,100))
window.blit(loadingSettingsText,(300,400))
pygame.display.update()

settings = ConfigParser()
settings.read('settings.ini')

# Setting up Rich Presence
pygame.draw.rect(window,(255,255,255),(100,350,700,100))
window.blit(settingUpDiscordRPCText,(300,400))
pygame.display.update()

discordConnect = settings.getboolean('DEFAULT','discordrpc')
startTime = int(time())
clientID = '603692122704707594'
RPC = Presence(clientID)

if discordConnect:
    try:
        RPC.connect()
        print("Discord Rich Presence activated.")
    except:
        discordConnect = False
        print("Discord not found. Rich Presence is not activated.")
	
# Some variables
pygame.draw.rect(window,(255,255,255),(100,350,700,100))
window.blit(loadingVariablesText,(300,400))
pygame.display.update()

x = settings.getint('EXPERIMENTAL','startx')
y = settings.getint('EXPERIMENTAL','starty')

width = settings.getint('EXPERIMENTAL','cubewidth')
height = settings.getint('EXPERIMENTAL','cubeheight')

speed = settings.getint('EXPERIMENTAL','cubespeed')
speedY = 0

facing = 1

Jump = False
canRun = True

health = 100
food = 100
water = 100
energy = 100

inMenu = True

# Load fonts
pygame.draw.rect(window,(255,255,255),(100,350,700,100))
window.blit(loadingFontsText,(300,400))
pygame.display.update()

verdana40 = pygame.font.Font('data/fonts/verdana.ttf',40)
verdana30 = pygame.font.Font('data/fonts/verdana.ttf',30)
verdana100 = pygame.font.Font('data/fonts/verdana.ttf',100)

with open('data/locales.json', 'r', encoding='utf-8') as f: # Loading languages
    locale = JSONload(f)
language = settings.get('DEFAULT','language') # Getting language

# Prerender text
pygame.draw.rect(window,(255,255,255),(100,350,700,100))
window.blit(prerenderingTextsText,(300,400))
pygame.display.update()

playText = verdana40.render(locale[language]['menuText']['play'],1,(0,0,0))
settingsText = verdana40.render(locale[language]['menuText']['settings'],1,(0,0,0))
exitText = verdana40.render(locale[language]['menuText']['exit'],1,(0,0,0))
pauseText = verdana100.render(locale[language]['menuText']['pause'],1,(0,0,0))
exitToMenuText = verdana30.render(locale[language]['menuText']['exitToMenu'],1,(0,0,0))
resumeText = verdana40.render(locale[language]['menuText']['resume'],1,(0,0,0))
restartText = verdana40.render(locale[language]['menuText']['restart'],1,(0,0,0))
youDiedText = verdana100.render(locale[language]['menuText']['youDied'],1,(255,0,0))
settingsText2 = verdana100.render(locale[language]['menuText']['settings'],1,(0,0,0))
discordRPCtext = verdana40.render("Discord RPC",1,(0,0,0))
dayNightCycleText = verdana30.render(locale[language]['menuText']['dayNightCycle'],1,(0,0,0))
dayNightText = verdana40.render(locale[language]['menuText']['dayNight'],1,(0,0,0))
languageText = verdana40.render(locale[language]['menuText']['language'],1,(0,0,0))
languageText2 = verdana100.render(locale[language]['menuText']['language'],1,(0,0,0))
englishText = verdana40.render("English",1,(0,0,0))
russianText = verdana40.render("Русский",1,(0,0,0))
ukrainianText = verdana40.render("Українська",1,(0,0,0))
polishText = verdana40.render("Polski",1,(0,0,0))
deutchText = verdana40.render("Deutsch",1,(0,0,0))

# Texts for discord status
pauseStatus = locale[language]['menuText']['pause']
settingsStatus = locale[language]['menuText']['settings']
diedStatus = locale[language]['discordStatus']['died']
mainMenuStatus = locale[language]['discordStatus']['mainMenu']
languageSettingsStatus = locale[language]['discordStatus']['languageSettings']
locationStatus = locale[language]['discordStatus']['location']
foodStatus = locale[language]['discordStatus']['food']
healthStatus = locale[language]['discordStatus']['health']
waterStatus = locale[language]['discordStatus']['water']
energyStatus = locale[language]['discordStatus']['energy']

pygame.draw.rect(window,(255,255,255),(100,350,700,100))
window.blit(loadingTexturesText,(300,400))
pygame.display.update()

# Loading bar icons
print("Loading bar icons")
baricon = (
    pygame.image.load('data/baricons/health.png'),
    pygame.image.load('data/baricons/food.png'),
    pygame.image.load('data/baricons/water.png'),
    pygame.image.load('data/baricons/energy.png')
)
# Loading scenes
print("Loading scenes")
scene = (
    pygame.image.load('data/backgrounds/basement.png'),
    pygame.image.load('data/backgrounds/home.png'),
    pygame.image.load('data/backgrounds/yard.png'),
    pygame.image.load('data/backgrounds/village.png'),
    pygame.image.load('data/backgrounds/garden.png'),
#    pygame.image.load('data/backgrounds/farm.png'),
    pygame.image.load('data/backgrounds/field.png'),
    pygame.image.load('data/backgrounds/forest.png'),
    pygame.image.load('data/backgrounds/city.png'),
    pygame.image.load('data/backgrounds/beach.png')
)
stars = pygame.image.load('data/backgrounds/stars.png') # Star sky

# Menu icons
settingsIcon = pygame.image.load('data/menuIcons/settings.png')
exitIcon = pygame.image.load('data/menuIcons/exit.png')
mainMenuIcon = pygame.image.load('data/menuIcons/mainMenu.png')
restartIcon = pygame.image.load('data/menuIcons/restart.png')
languageIcon = pygame.image.load('data/menuIcons/language.png')

# Cubic faces in menu
sleepingMenuFace = pygame.image.load('data/menuFaces/sleeping.png')
diedMenuFace = pygame.image.load('data/menuFaces/died.png')

# Countries flags
UKflag = pygame.image.load('data/flags/UK.png')
russiaFlag = pygame.image.load('data/flags/russia.png')
ukraineFlag = pygame.image.load('data/flags/ukraine.png')
polandFlag = pygame.image.load('data/flags/poland.png')
germanyFlag = pygame.image.load('data/flags/germany.png')

# Other sprites
wrenchMenuIcon = pygame.image.load('data/menuIcons/wrenchIcon.png')
zzz = pygame.image.load('data/zzz.png')

# Scenes names for Rich Presence.
scenename = (
    locale[language]['discordStatus']['locations']['basement'],
    locale[language]['discordStatus']['locations']['home'],
    locale[language]['discordStatus']['locations']['yard'],
    locale[language]['discordStatus']['locations']['village'],
    locale[language]['discordStatus']['locations']['garden'],
#    "Farm",
    locale[language]['discordStatus']['locations']['field'],
    locale[language]['discordStatus']['locations']['forest'],
    locale[language]['discordStatus']['locations']['city'],
    locale[language]['discordStatus']['locations']['beach']
)
scenenum = settings.getint('EXPERIMENTAL','startscene') # Number of current scene
scenecount = len(scene) - 1 # Scenes count
run = True

pygame.draw.rect(window,(255,255,255),(100,350,700,100))
window.blit(loadingClassesText,(300,400))
pygame.display.update()

# Classes
class Bar: 
    '''Class for bars'''

    def __init__(self, x,y, red,green,blue, height, value, multiplier, iconnum):
        self.x = 25
        self.y = y
        self.red = red
        self.green = green
        self.blue = blue
        self.height = height
        self.value = value
        self.multiplier = multiplier
        self.iconnum = iconnum
	
    def draw(self):
        if self.value > 0:
            pygame.draw.rect(window,(self.red,self.green,self.blue),(self.x,self.y, self.value * self.multiplier, self.height))
        window.blit(baricon[self.iconnum], (self.x - 22, self.y))
	
    def update(self, value):
        self.value = value
	
class DayNight:
    '''Class for day and night'''

    def __init__(self):
        self.cycle = settings.getboolean('TIME','cycle')
        self.cp = settings.getint('TIME','time')
        self.raising = False
	
    def tick(self):
        '''One time tick'''
        if self.cycle:
            if self.raising:
                if self.cp < 255:
                    self.cp += 0.06
                else:
                    self.raising = False
            else:
                if self.cp > 0:
                  self.cp -= 0.06
                else:
                    self.raising = True
		
    def draw(self):
        '''Drawing sky'''
        window.fill((0,self.cp / 1.5,self.cp))
        if self.cp < 50:
            window.blit(stars,(0,0))
	
class Menu:
    '''Class for menus'''

    def __init__(self):
        self.menuType = "MAIN"
	
    def draw(self):
        '''Menu draw'''
        global mouseX,mouseY
	
        if self.menuType == "MAIN": # Drawing main menu
            window.fill((0,170,255))
            window.blit(scene[1],(0,0))
            pygame.draw.rect(window,(0,255,0),(730,360,50,50))
            if mouseX >= 250 and mouseX <= 750 and mouseY >= 150 and mouseY <= 200: # Play button
                pygame.draw.rect(window,(100,100,100),(250,150,500,50))
            else:
                pygame.draw.rect(window,(200,200,200),(250,150,500,50))
            if mouseX >= 250 and mouseX <= 750 and mouseY >= 250 and mouseY <= 300: # Settings button
                pygame.draw.rect(window,(100,100,100),(250,250,500,50))
            else:
                pygame.draw.rect(window,(200,200,200),(250,250,500,50))
            if mouseX >= 250 and mouseX <= 750 and mouseY >= 350 and mouseY <= 400: # Exit button
                pygame.draw.rect(window,(100,100,100),(250,350,500,50))
            else:
                pygame.draw.rect(window,(200,200,200),(250,350,500,50))
            window.blit(playText,(440,145))
            if language == "ukrainian":
                window.blit(settingsText,(350,245))
            else:
                window.blit(settingsText,(400,245))
            window.blit(exitText,(440,350))
            pygame.draw.rect(window,(0,255,0),(710,160,30,30))
            window.blit(settingsIcon,(710,260))
            window.blit(exitIcon,(710,360))
            window.blit(GreenCubicText,(175,20))
            pygame.draw.rect(window,(0,255,0),(720,40,70,70))
		
        elif self.menuType == "PAUSE": # Drawing pause menu
            DN.draw()
            window.blit(scene[scenenum],(0,0))
            pygame.draw.rect(window,(0,255,0),(x,y,50,50))
            window.blit(pauseText,(295,20))
            pygame.draw.rect(window,(0,255,0),(595,60,70,70))
            window.blit(sleepingMenuFace,(595,60))
            window.blit(zzz,(665,10))
            if mouseX >= 300 and mouseX <= 650 and mouseY >= 150 and mouseY <= 200: # Resume button
                pygame.draw.rect(window,(100,100,100),(300,150,350,50))
            else:
                pygame.draw.rect(window,(200,200,200),(300,150,350,50))
            if mouseX >= 300 and mouseX <= 650 and mouseY >= 225 and mouseY <= 275: # Restart button
                pygame.draw.rect(window,(100,100,100),(300,225,350,50))
            else:
                pygame.draw.rect(window,(200,200,200),(300,225,350,50))
            if mouseX >= 300 and mouseX <= 650 and mouseY >= 300 and mouseY <= 350: # Exit to menu button
                pygame.draw.rect(window,(100,100,100),(300,300,350,50))
            else:
                pygame.draw.rect(window,(200,200,200),(300,300,350,50))
            if mouseX >= 300 and mouseX <= 650 and mouseY >= 375 and mouseY <= 425: # Exit button
                pygame.draw.rect(window,(100,100,100),(300,375,350,50))
            else:
                pygame.draw.rect(window,(200,200,200),(300,375,350,50))
            if language != "english" and language != "polish" and language != "deutch":
                window.blit(resumeText,(330,150))
                window.blit(restartText,(300,225))
            else:
                window.blit(resumeText,(380,150))
                window.blit(restartText,(380,225))
            window.blit(exitToMenuText,(360,305))
            window.blit(exitText,(420,375))
            pygame.draw.rect(window,(0,255,0),(610,160,30,30))
            window.blit(restartIcon,(610,235))
            window.blit(mainMenuIcon,(610,310))
            window.blit(exitIcon,(610,385))
		
        elif self.menuType == "DIED": # "You died!" Menu
            DN.draw()
            window.blit(scene[scenenum],(0,0))
            pygame.draw.rect(window,(0,0,0),(x,y,50,50))
            if language == "deutch":
                window.blit(youDiedText,(150,20))
                pygame.draw.rect(window,(0,255,0),(730,50,70,70))
                window.blit(diedMenuFace,(730,50))
            else:
                window.blit(youDiedText,(210,20))
                pygame.draw.rect(window,(0,255,0),(680,50,70,70))
                window.blit(diedMenuFace,(680,50))
            if mouseX >= 250 and mouseX <= 750 and mouseY >= 150 and mouseY <= 200: # Restart button
                pygame.draw.rect(window,(100,100,100),(250,150,500,50))
            else:
                pygame.draw.rect(window,(200,200,200),(250,150,500,50))
            if mouseX >= 250 and mouseX <= 750 and mouseY >= 250 and mouseY <= 300: # Exit to menu button
                pygame.draw.rect(window,(100,100,100),(250,250,500,50))
            else:
                pygame.draw.rect(window,(200,200,200),(250,250,500,50))
            window.blit(restartText,(380,150))
            window.blit(exitToMenuText,(360,255))
            pygame.draw.rect(window,(0,255,0),(710,160,30,30))
            window.blit(mainMenuIcon,(710,260))
		
        elif self.menuType == "SETTINGS": # Settings menu
            window.fill((0,170,255))
            window.blit(scene[1],(0,0))
            pygame.draw.rect(window,(0,255,0),(700,360,50,50))
            if language == "ukrainian":
                window.blit(settingsText2,(85,20))
                pygame.draw.rect(window,(0,255,0),(850,60,70,70))
                window.blit(wrenchMenuIcon,(905,60))
            elif language == "russian" or language == "polish":
                window.blit(settingsText2,(200,20))
                pygame.draw.rect(window,(0,255,0),(750,60,70,70))
                window.blit(wrenchMenuIcon,(805,60))
            elif language == "deutch":
                window.blit(settingsText2,(110,20))
                pygame.draw.rect(window,(0,255,0),(780,60,70,70))
                window.blit(wrenchMenuIcon,(835,60))
            else:
                window.blit(settingsText2,(250,20))
                pygame.draw.rect(window,(0,255,0),(670,60,70,70))
                window.blit(wrenchMenuIcon,(725,60))
            if discordConnect:
                pygame.draw.rect(window,(0,255,0),(30,150,40,40))
            else:
                pygame.draw.rect(window,(255,0,0),(30,150,40,40))
            if DN.cycle:
                pygame.draw.rect(window,(0,255,0),(30,200,40,40))
            else:
                pygame.draw.rect(window,(255,0,0),(30,200,40,40))
            if DN.cp == 255:
                pygame.draw.rect(window,(0,255 / 1.5,255),(30,250,40,40))
            else:
                pygame.draw.rect(window,(0,0,10),(30,250,40,40))
            window.blit(discordRPCtext,(75,145))
            window.blit(dayNightCycleText,(75,200))
            window.blit(dayNightText,(75,245))
            if mouseX >= 30 and mouseX <= 330 and mouseY >= 420 and mouseY <= 470: # Exit to menu button
                pygame.draw.rect(window,(100,100,100),(30,420,300,50))
            else:
                pygame.draw.rect(window,(200,200,200),(30,420,300,50))
            if mouseX >= 670 and mouseX <= 970 and mouseY >= 420 and mouseY <= 470: # Language button
                pygame.draw.rect(window,(100,100,100),(670,420,300,50))
            else:
                pygame.draw.rect(window,(200,200,200),(670,420,300,50))
            if language != "english" and language != "deutch":
                window.blit(languageText,(750,415))
            else:
                window.blit(languageText,(720,415))
            window.blit(exitToMenuText,(40,425))
            window.blit(mainMenuIcon,(290,430))
            window.blit(languageIcon,(930,430))
	
        elif self.menuType == "LANGUAGE": # Language choose menu
            window.fill((0,170,255))
            window.blit(scene[1],(0,0))
            pygame.draw.rect(window,(0,255,0),(700,360,50,50))
            if language != "english":
                window.blit(languageText2,(300,10))
            else:
                window.blit(languageText2,(200,10))
            if mouseX >= 30 and mouseX <= 385 and mouseY >= 420 and mouseY <= 470: # Exit to settings button
                pygame.draw.rect(window,(100,100,100),(30,420,355,50))
            else:
                pygame.draw.rect(window,(200,200,200),(30,420,355,50))
            if language != "english":
                window.blit(settingsText,(40,420))
            else:
                window.blit(settingsText,(100,420))
            window.blit(settingsIcon,(345,430))
            if language == "english":
                pygame.draw.rect(window,(0,255,0),(30,150,40,40))
            elif language == "russian":
                pygame.draw.rect(window,(0,255,0),(30,200,40,40))
            elif language == "ukrainian":
                pygame.draw.rect(window,(0,255,0),(30,250,40,40))
            elif language == "polish":
                pygame.draw.rect(window,(0,255,0),(30,300,40,40))
            elif language == "deutch":
                pygame.draw.rect(window,(0,255,0),(30,350,40,40))
            window.blit(UKflag,(35,157))
            window.blit(russiaFlag,(35,207))
            window.blit(ukraineFlag,(35,257))
            window.blit(polandFlag,(35,307))
            window.blit(germanyFlag,(35,357))
            window.blit(englishText,(80,140))
            window.blit(russianText,(80,190))
            window.blit(ukrainianText,(80,240))
            window.blit(polishText,(80,290))
            window.blit(deutchText,(80,340))
        else:
            print("Unknown menu type! Returning to main.")
            self.menuType = "MAIN"
        pygame.display.update()
"""
class Clouds:
    def __init__(self,cloudCount,maxCircles,minCircles,circleRadius):
        self.cloudCount = cloudCount
        self.maxCircles = maxCircles
        self.minCircles = minCircles
        self.circleRadius = circleRadius
        self.clouds = [[{x:5,y:17},{y:6,y:20}],[{x:20,y:8},{x:26,y:12}]]
    def tick(self):
        pass
    def draw(self):
        for cloud in self.clouds:
            for circle in cloud:
                pygame.draw.circle(window,(255,255,255),(circle[x],circle[y]),self.circleRadius)
class Cubic():
    '''Класс, отвечающий за другие кубики'''
    def __init__(self, x,y,scene, red,green,blue):
        self.x = x
        self.y = y
        self.scene = scene
        self.red = red
        self.green = green
        self.blue = blue
        self.speedY = 0
        self.friend = False
        self.health = 100
    def draw(self):
        if self.scene == scenenum:
            pygame.draw.rect(window, (self.red,self.green,self.blue), (self.x,self.y,50,50))
    def jump(self):
        speedY = -15
    def physicsRender(self):
        pass
    def AIrender(self):
        pass
"""

# Objects
healthBar = Bar(25,10, 255,0,0, 20, health, 3, 0)
foodBar = Bar(25,40, 255,127,0, 20, food, 3, 1)
waterBar = Bar(25, 70, 0,150,220, 20, water, 3, 2)
energyBar = Bar(25, 100, 255,255,0, 20, energy, 3, 3)
DN = DayNight()
menu = Menu()

# Functions
def restartGame():
    '''Function for game restarting'''
    # Variables for cubic 
    global x,y,width,height,speed,speedY,facing,Jump,canRun,health,food,water,energy,scenenum
    x = settings.getint('EXPERIMENTAL','startx')
    y = settings.getint('EXPERIMENTAL','starty')
    width = settings.getint('EXPERIMENTAL','cubewidth')
    height = settings.getint('EXPERIMENTAL','cubeheight')
    speed = settings.getint('EXPERIMENTAL','cubespeed')
    speedY = 0
    facing = 1
    Jump = False
    canRun = True
    health = 100
    food = 100
    water = 100
    energy = 100
    # Other variables
    inMenu = True
    scenenum = settings.getint('EXPERIMENTAL','startscene')
    # Some functions
    DN.__init__()
    print("Game reloaded!")
	
def reloadLocale():
    "Function for reloading language"
    global playText,settingsText,exitText,pauseText,exitToMenuText,resumeText,restartText,youDiedText,settingsText,settingsText2,dayNightCycleText,dayNightText,languageText,languageText2,pauseStatus,settingsStatus,diedStatus,mainMenuStatus,languageSettingsStatus,locationStatus,foodStatus,waterStatus,healthStatus,energyStatus,scenename
    language = settings.get('DEFAULT','language') # Getting language
    # Rendering texts
    playText = verdana40.render(locale[language]['menuText']['play'],1,(0,0,0))
    settingsText = verdana40.render(locale[language]['menuText']['settings'],1,(0,0,0))
    exitText = verdana40.render(locale[language]['menuText']['exit'],1,(0,0,0))
    pauseText = verdana100.render(locale[language]['menuText']['pause'],1,(0,0,0))
    exitToMenuText = verdana30.render(locale[language]['menuText']['exitToMenu'],1,(0,0,0))
    resumeText = verdana40.render(locale[language]['menuText']['resume'],1,(0,0,0))
    restartText = verdana40.render(locale[language]['menuText']['restart'],1,(0,0,0))
    youDiedText = verdana100.render(locale[language]['menuText']['youDied'],1,(255,0,0))
    settingsText2 = verdana100.render(locale[language]['menuText']['settings'],1,(0,0,0))
    dayNightCycleText = verdana30.render(locale[language]['menuText']['dayNightCycle'],1,(0,0,0))
    dayNightText = verdana40.render(locale[language]['menuText']['dayNight'],1,(0,0,0))
    languageText = verdana40.render(locale[language]['menuText']['language'],1,(0,0,0))
    languageText2 = verdana100.render(locale[language]['menuText']['language'],1,(0,0,0))
    # Texts for discord status
    pauseStatus = locale[language]['menuText']['pause']
    settingsStatus = locale[language]['menuText']['settings']
    diedStatus = locale[language]['discordStatus']['died']
    mainMenuStatus = locale[language]['discordStatus']['mainMenu']
    languageSettingsStatus = locale[language]['discordStatus']['languageSettings']
    locationStatus = locale[language]['discordStatus']['location']
    foodStatus = locale[language]['discordStatus']['food']
    healthStatus = locale[language]['discordStatus']['health']
    waterStatus = locale[language]['discordStatus']['water']
    energyStatus = locale[language]['discordStatus']['energy']
    # Scenes names
    scenename = (
        locale[language]['discordStatus']['locations']['basement'],
        locale[language]['discordStatus']['locations']['home'],
        locale[language]['discordStatus']['locations']['yard'],
        locale[language]['discordStatus']['locations']['village'],
        locale[language]['discordStatus']['locations']['garden'],
        #    "Farm",
        locale[language]['discordStatus']['locations']['field'],
        locale[language]['discordStatus']['locations']['forest'],
        locale[language]['discordStatus']['locations']['city'],
        locale[language]['discordStatus']['locations']['beach']
    )
	
def onLadder():
    '''Is player on ladder?'''
    if scenenum == 0 and x > 835 and x < 935 and y < 450: # Ladder in basement
        return True
    else:
        return False

def drawWindow():
    '''Function for drawing everything in window'''
    if (scenenum <= scenecount and scenenum >= 0):
        DN.draw()
        window.blit(scene[scenenum], (0,0))
    else:
        window.fill((0,0,0))
    healthBar.draw()
    foodBar.draw()
    waterBar.draw()
    energyBar.draw()
    pygame.draw.rect(window, (0,255,0), (x, y, width, height)) 
    pygame.display.update()

# Removing unused texts
del loadingModulesText
del loadingSettingsText
del settingUpDiscordRPCText
del loadingVariablesText
del loadingFontsText
del prerenderingTextsText
del loadingTexturesText
del loadingClassesText

# General game cycle
print("Game Started!")
while run:
    while inMenu:
        pygame.time.delay(20)
        mousePos = pygame.mouse.get_pos() # Getting mouse position
        mouseX = mousePos[0]
        mouseY = mousePos[1]
        # Getting event
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                inMenu = False
                run = False
            # Pressing buttons in menu
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Main menu
                if menu.menuType == "MAIN":
                    if mouseX >= 250 and mouseX <= 750 and mouseY >= 150 and mouseY <= 200: # Play
                        restartGame()
                        inMenu = False
                    if mouseX >= 250 and mouseX <= 750 and mouseY >= 250 and mouseY <= 300: # Settings
                        menu.menuType = "SETTINGS"
                    if mouseX >= 250 and mouseX <= 750 and mouseY >= 350 and mouseY <= 400: # Exit
                        inMenu = False
                        run = False
                # Pause
                if menu.menuType == "PAUSE":
                    if mouseX >= 300 and mouseX <= 650 and mouseY >= 150 and mouseY <= 200: # Resume
                        inMenu = False
                    if mouseX >= 300 and mouseX <= 650 and mouseY >= 300 and mouseY <= 350: # Exit to main menu
                        menu.menuType = "MAIN"
                        restartGame()
                    if mouseX >= 300 and mouseX <= 650 and mouseY >= 225 and mouseY <= 275: # Restart
                        restartGame()
                        inMenu = False
                    if mouseX >= 300 and mouseX <= 650 and mouseY >= 375 and mouseY <= 425: # Exit
                        inMenu = False
                        run = False
                # "You died!"
                if menu.menuType == "DIED":
                    if mouseX >= 250 and mouseX <= 750 and mouseY >= 150 and mouseY <= 200: # Restart
                        restartGame()
                        inMenu = False
                    if mouseX >= 250 and mouseX <= 750 and mouseY >= 250 and mouseY <= 300: # Exit to menu
                        menu.menuType = "MAIN"
                # Settings
                if menu.menuType == "SETTINGS":
                    if mouseX >= 30 and mouseX <= 70 and mouseY >= 150 and mouseY <= 190: # Discord status
                        if discordConnect:
                            discordConnect = False
                            RPC.close()
                            del RPC
                            settings.set('DEFAULT','discordRPC','off')
                        else:
                            discordConnect = True
                            RPC = Presence(clientID)
                            try:
                                RPC.connect()
                            except:
                                discordConnect = False
                                del RPC
                            settings.set('DEFAULT','discordRPC','on')
                    if mouseX >= 30 and mouseX <= 70 and mouseY >= 200 and mouseY <= 240: # Day/Night cycle
                        if DN.cycle:
                            DN.cycle = False
                            settings.set('TIME','cycle','off')
                        else:
                            DN.cycle = True
                            settings.set('TIME','cycle','on')
                    if mouseX >= 30 and mouseX <= 70 and mouseY >= 250 and mouseY <= 290: # Day or night
                        if DN.cp == 255:
                            DN.cp = 0
                            settings.set('TIME','time','0')
                        else:
                            DN.cp = 255
                            settings.set('TIME','time','255')
                    if mouseX >= 30 and mouseX <= 330 and mouseY >= 420 and mouseY <= 470: # Exit to menu
                        with open('settings.ini','w') as f: # Saving settings
                            settings.write(f)
                        menu.menuType = "MAIN"
                    if mouseX >= 670 and mouseX <= 970 and mouseY >= 420 and mouseY <= 470: # Language choose menu
                        menu.menuType = "LANGUAGE"
                # Language choose menu
                if menu.menuType == "LANGUAGE":
                    if mouseX >= 30 and mouseX <= 385 and mouseY >= 420 and mouseY <= 470: # Exit to settings
                        menu.menuType = "SETTINGS"
                        with open('settings.ini','w') as f: # Saving settings
                            settings.write(f)
                    # Languages
                    if mouseX >= 30 and mouseX <= 300 and mouseY >= 150 and mouseY <= 190: # English
                        language = "english"
                    if mouseX >= 30 and mouseX <= 300 and mouseY >= 200 and mouseY <= 240: # Russian
                        language = "russian"
                    if mouseX >= 30 and mouseX <= 300 and mouseY >= 250 and mouseY <= 290: # Ukrainian
                        language = "ukrainian"
                    if mouseX >= 30 and mouseX <= 300 and mouseY >= 300 and mouseY <= 340: # Polish
                        language = "polish"
                    if mouseX >= 30 and mouseX <= 300 and mouseY >= 350 and mouseY <= 390: # Deutch
                        language = "deutch" 
                    settings.set('DEFAULT','language',language)
                    reloadLocale()
        menu.draw()
        # Rich Presence
        if discordConnect:
            if menu.menuType == "MAIN":
                RPC.update(
                start=startTime,
                large_image="greencubic",
                large_text="GreenCubic",
                state=mainMenuStatus,
                )
            if menu.menuType == "PAUSE":
                RPC.update(
                start=startTime,
                large_image="greencubic",
                large_text="GreenCubic",
                state=pauseStatus,
                )
            if menu.menuType == "DIED":
                RPC.update(
                start=startTime,
                large_image="greencubic",
                large_text="GreenCubic",
                state=diedStatus,
                )
            if menu.menuType == "SETTINGS":
                RPC.update(
                start=startTime,
                large_image="greencubic",
                large_text="GreenCubic",
                state=settingsStatus,
                )
            if menu.menuType == "LANGUAGE":
                RPC.update(
                start=startTime,
                large_image="greencubic",
                large_text="GreenCubic",
                state=languageSettingsStatus,
                )
    pygame.time.delay(20)
    # Getting events
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            run = False
    # Updating bars.
    healthBar.update(health)
    foodBar.update(food)
    waterBar.update(water)
    energyBar.update(energy)
    # Control.
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
        facing = -1
    if keys[pygame.K_RIGHT]:
        facing = 1
        if (scenenum != 8 and x < 1000 - width): # Physics that makes you can't go to water
            x += speed
        elif (scenenum == 8 and x < 450 - width):
            x += speed
    if not(Jump) and keys[pygame.K_UP]: # Jump or climbing on ladder
        if onLadder(): # Ladder
            y -= speed
        elif energy > 10:
            speedY = -20
            Jump = True
            energy -= 10
    if not(Jump) and keys[pygame.K_DOWN]: # Jump down or climbing down on ladder
        if onLadder() and y < 500 - height: # Ladder
            y += speed
        elif y < 500 - height:
            speedY += 15
            Jump = True
    if keys[pygame.K_LSHIFT] and (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]): # Sprint    
        if energy > 0 and canRun:
            energy -= 0.25
            if speed < 10:
                speed += 1
        elif energy < 1:
            speed = settings.getint('EXPERIMENTAL','cubespeed')
            canRun = False
    else:
        speed = settings.getint('EXPERIMENTAL','cubespeed')
    if keys[pygame.K_ESCAPE]: # Pause
        inMenu = True
        menu.menuType = "PAUSE"
    if keys[pygame.K_d]: # Drink (from nothing yet)
        if water < 100:
            water += 1
    if keys[pygame.K_e]: # Eat (from nothing yet)
        if food < 100:
            food += 1
	
    # Player options
    if food > 0 and water > 0: # Wasting water and food in idling
        food -= 0.002
        water -= 0.005
    elif energy > 0: # Active energy waste if food or water is 0
        energy -= 0.5
    else: # Damage if energy, food and water is 0
        health -= 0.05
    if food < 1 or water < 1: # Slowing if water or food is 0
        speed = 2
    if health < 1: # If health is 0, you're dying
        inMenu = True
        menu.menuType = "DIED"
    if health < 100 and food > 0 and water > 0: # Regenerating health
        health += 0.05
        food -= 0.025
        water -= 0.01
    if energy < 100 and not(keys[pygame.K_LSHIFT]) and food > 0 and water > 0: # Regenerating energy
        energy += 0.5
        food -= 0.05
        water -= 0.025
    
    if energy > 0: # You can sprint, if you have energy
        canRun = True
	
    # Physics
    y += speedY
    if scenenum == 0 or scenenum == 1: # Ceiling
        if y < 1 and not(onLadder()):
            if speedY < -10: # Damage from hitting ceiling
                health -= 10 - speedY
            speedY = 0
            y = 1
    if scenenum == 1 and x >= 590 - width and x <= 835 and y >= 395 - height and y <= 420 - height: # Bed
        if speedY > 0: # Bounce!
            if keys[pygame.K_UP] and energy > 10:
                speedY = speedY * -1.1
                energy -= 5
            elif keys[pygame.K_DOWN]:
                speedY = 0
            else:
                speedY = speedY * -0.9
        else:
            Jump = False
            speedY = 0
            y = 410 - height
    elif scenenum == 1 and x >= 407 - width and x <= 561 and y >= 190 - height and y <= 210 - height: # Cupboard
        speedY = 0
        Jump = False
        y = 196 - height
    elif scenenum == 1 and x >= 147 - width and x <= 355 and y >= 235 - height and y <= 255 - height: # TV
        speedY = 0
        Jump = False
        y = 243 - height
    elif scenenum == 1 and x >= 160 - width and x <= 340 and y >= 350 - height and y < 370 - height: # Bedside table
        speedY = 0
        Jump = False
        y = 362 - height
    elif scenenum == 0 and x >= 55 - width and x <= 170 and y >= 390 - height and y <= 410 - height: # Box
        speedY = 0
        Jump = False
        y = 398 - height
    elif y < 500 - height and not(onLadder()): # Falling
        speedY += 1
        Jump = True
    else: # Fell on the ground.
        if not(onLadder()): # Ladder
            if speedY > 20: # Damage for falling
                health -= speedY - 20
            y = 500 - height
        speedY = 0
        Jump = False
	
    # Changing normal location
    if scenenum >= 2 and scenenum < scenecount and x > 999 - width:
        x = 1
        scenenum += 1
    if scenenum > 2 and scenenum <= scenecount and x < 1:
        x = 999 - width
        scenenum -= 1
	
    # Changing special location
    if scenenum == 1 and x > 999 - width and y > 200: # Go out
        x = 1
        scenenum = 2
    if scenenum == 2 and x < 1 and y > 200: # Enter the house
        x = 999 - width
        scenenum = 1
    if scenenum == 1 and x < 90 and y > 490 - height and keys[pygame.K_DOWN]: # Go down to the basement
        x = 890
        y = 0
        scenenum = 0
    if scenenum == 0 and x > 835 and x < 935 and y <= height * -1: # Get out of the basement
        y = 450
        x = 50
        scenenum = 1
	
    # Rich Presence
    if discordConnect:
	    RPC.update(
        start=startTime,
        large_image="greencubic",
        large_text="GreenCubic",
        state=healthStatus + str(int(health)) + foodStatus + str(int(food)) + waterStatus + str(int(water)) + energyStatus + str(int(energy)),
        details=locationStatus + scenename[scenenum]
	    )
	
    drawWindow()
    DN.tick()
	
# Bye.
print("Game Stopped!")
RPC.close()
pygame.quit()
