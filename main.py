import playsound
import asyncio

def nextround():
    playsound.playsound('nextround.mp3', False)

def oneminleft():
    playsound.playsound('oneminleft.mp3', False)

def timeout():
    playsound.playsound('timeout.mp3', False)

MINUTES = 5
SECINMINUTE = 60

async def runround():
    nextround()
    await asyncio.sleep((MINUTES-1)*SECINMINUTE)
    oneminleft()
    await asyncio.sleep(SECINMINUTE)
    timeout()

async def countdown():
    for i in range(MINUTES*SECINMINUTE,0,-1):
        print(f'{i//SECINMINUTE}:{i%SECINMINUTE:02}',end='\r')
        await asyncio.sleep(1)

async def mainround():
    await asyncio.gather(runround(),countdown())

while True:
    print('Type "next" and hit ENTER to continue')
    print('Type "exit" and hit ENTER to exit program')
    cmd = input('Your command: ')
    if(cmd.lower() == 'exit'):
        break
    elif(cmd.lower() != 'next'):
        print('Invalid command:',cmd)
        continue

    asyncio.run(mainround())
    print()