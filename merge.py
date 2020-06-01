import pygame
import random
pygame.font.init()
#window
screen = pygame.display.set_mode((900,650))
#Title and Icon
pygame.display.set_caption("MERGE SORT VISUALISATION")
img = pygame.image.load("symbol.png")
pygame.display.set_icon(img)

width = 900
length = 600
arr = [0]*151
arr_color = [(0,204,102)]*151
color_index = 0
color = [(0, 204, 102), (255, 0, 0), (0, 0, 153), (255, 102, 0)]  #green,red,darkblue,orange
fnt = pygame.font.SysFont("comicsans",30)
fnt1 = pygame.font.SysFont("comicsans",20)


#Generating new array
def generate_arr():
    for i in range(1,151):
        arr_color[i] = color[0]  #making all array elements to green
        arr[i] = random.randrange(1,100)  #putting randon no.s to array

generate_arr()


def draw():
    txt = fnt.render("PRESS 'ENTER' TO PERFORM SORTING",1,(0,0,0))  # 1 is for antialiasing
    screen.blit(txt,(20,20))  #position where text is placed

    txt1 = fnt.render("PRESS 'N' FOR NEW ARRAY",1,(0,0,0))
    screen.blit(txt1,(20,40))

    txt2 = fnt1.render("ALGORITHM USED:MERGE SORT", 1, (0, 0, 0))
    screen.blit(txt2, (600, 60))
    element_width = (width-150)//150
    boundary_arr = 900/150
    boundary_grp = 550/100
    pygame.draw.line(screen,(0,0,0),(0,95),(900,95),6)  #surface,color,strt_pos,end_pos,width

    for i in range(1,100):
        pygame.draw.line(screen,(224,224,224),(0,boundary_grp * i +100),(900,boundary_grp * i +100),1)   #color-grey/cement

    #drawing arr values as lines
    for i in range(1,151):
        pygame.draw.line(screen,arr_color[i],(boundary_arr * i-3,100),(boundary_arr * i-3,arr[i]*boundary_grp + 100),element_width)


def refill():
    screen.fill((255,255,255))  #screen color is white
    draw()
    pygame.display.update()
    pygame.time.delay(20)


def merge(arr,low,mid,high):
    i = low
    j = mid + 1
    temp = []
    pygame.event.pump()   #internally process pygame event handlers
    while(i <= mid and j <= high):
        arr_color[i] = color[1]   #color of changes to red
        arr_color[j] = color[1]
        refill()
        arr_color[i] = color[0]  #color changed back to green
        arr_color[j] = color[0]

        if(arr[i] < arr[j]):
            temp.append(arr[i])
            i+=1

        else:
            temp.append(arr[j])
            j+=1

    while(i<=mid):
        arr_color[i] = color[1]  #red
        refill()
        arr_color[i] = color[0]
        temp.append(arr[i])
        i+=1

    while(j <= high):
        arr_color[j] = color[1]
        refill()
        arr_color[j] = color[0]
        temp.append(arr[j])
        j+=1
    j = 0
    for i in range(low,high+1):
        pygame.event.pump()
        arr[i] = temp[j]
        j+=1
        arr_color[i] = color[2]   #dark blue
        refill()
        if(high-low == len(arr)-2):
            arr_color[i] = color[3]  #orange
        else:
            arr_color[i] = color[0]  #green


def mergesort(arr,low,high):
    mid = (low + high)//2
    if(low < high):
        mergesort(arr,low,mid)
        mergesort(arr,mid+1,high)
        merge(arr,low,mid,high)


#main loop
run = True
while(run):
    screen.fill((255,255,255))
    for event in pygame.event.get():   #to access all events in pygame
        if(event.type == pygame.QUIT):    #when user clicks on close button
            run = False
        if(event.type == pygame.KEYDOWN):  #if user presses the key
            if(event.key == pygame.K_n):
                generate_arr()

            if(event.key == pygame.K_RETURN):
                mergesort(arr,1,len(arr)-1)
    draw()   #does drawing of sort
    pygame.display.update()

pygame.quit()

