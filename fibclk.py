import datetime
import pygame
import time
import sys
white=(255,255,255)
black=(0,0,0)
red=(255,0,0,125)
blue=(0,0,255)
green=(0,100,0)

color_of_5=0
color_of_3=0
color_of_2=0
color_of_1=0

gamedisplay=pygame.display.set_mode((415,265))
gamedisplay.fill(white)
pygame.display.set_caption('Fibonacci Clock') 

num_list=[5,3,2,1,1]

def hour_factors(d1):
    
    j=0
    while(d1!=0):
        if(d1>=num_list[j]):
            d1=d1-num_list[j]
            hr_factors.append(num_list[j])
        j+=1

def minute_factors(d2):
         
         j=0
         while(d2!=0):
            if(d2>=num_list[j]):
                d2=d2-num_list[j]
                min_factors.append(num_list[j])
            j+=1         
        
def assign_colors():
 if (5 in hr_factors) and (5 in min_factors):
  color_of_5=blue
 elif (5 in hr_factors):
  color_of_5=red
 elif (5 in min_factors):
  color_of_5=green
 else:    
  color_of_5=white
 if (3 in hr_factors) and (3 in min_factors):
  color_of_3=blue
 elif (3 in hr_factors):
  color_of_3=red
 elif (3 in min_factors):
  color_of_3=green
 else:    
  color_of_3=white
 if (2 in hr_factors) and (2 in min_factors):
  color_of_2=blue
 elif (2 in hr_factors):
  color_of_2=red
 elif (2 in min_factors):
  color_of_2=green
 else:    
  color_of_2=white    
 if (1 in hr_factors) and (1 in min_factors):
  color_of_1=blue
 elif (1 in hr_factors):
  color_of_1=red
 elif (1 in min_factors):
  color_of_1=green
 else:    
  color_of_1=white 
 return color_of_1,color_of_11,color_of_2,color_of_3,color_of_5    

     

while 1:
 t=datetime.datetime.now()
 hr=t.hour
 mn=t.minute
 
 if (hr==00)or (hr==12):
     color_of_11=red
     hr=12
 else:
     color_of_11=white
 
 mn5=mn%5
 if (mn5==0):
    mn=mn/5
 else:
    mn=mn-mn5
    mn=mn/5
 if(hr>12):
    hr=hr-12



 d1=hr
 d2=mn
 hr_factors=[]
 min_factors=[]

 hour_factors(d1)
 minute_factors(d2)
 
 color_of_1,color_of_11,color_of_2,color_of_3,color_of_5 =assign_colors()


 
 
     
 pygame.draw.rect(gamedisplay,black,[0,0,5,265])
 pygame.draw.rect(gamedisplay,black,[5,0,415,5])
 r2=pygame.draw.rect(gamedisplay,color_of_2,[5,5,100,105])
 pygame.draw.rect(gamedisplay,black,[105,5,5,105])
 r1=pygame.draw.rect(gamedisplay,color_of_1,[110,5,50,50])
 pygame.draw.rect(gamedisplay,black,[110,55,50,5])
 r11=pygame.draw.rect(gamedisplay,color_of_11,[110,60,50,50])
 pygame.draw.rect(gamedisplay,black,[160,5,5,265])
 pygame.draw.rect(gamedisplay,black,[5,110,160,5])
 r3=pygame.draw.rect(gamedisplay,color_of_3,[5,115,155,150])
 pygame.draw.rect(gamedisplay,black,[5,260,415,5])
 pygame.draw.rect(gamedisplay,black,[160,5,5,400])
 r4=pygame.draw.rect(gamedisplay,color_of_5,[165,5,250,255])
 pygame.draw.rect(gamedisplay,black,[410,5,5,405])

 pygame.display.update()  
 

 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   
   pygame.display.quit()
   sys.exit()
