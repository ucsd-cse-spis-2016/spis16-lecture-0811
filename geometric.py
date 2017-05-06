from PIL import Image

def somefunc():

    pic = Image.open("butterfly.jpg")
    for x in range(pic.size[0]):
       for y in range(pic.size[1]):
            (red,green,blue) = pic.getpixel((x,y))
            pic.putpixel((x,y),(red,0,0))

    pic.show()


#somefunc()













def darken():
    pic = Image.open("butterfly.jpg")
    for x in range( pic.size[0]):
       for y in range( pic.size[1] ):
          (red,green,blue) = pic.getpixel( (x,y) )
          newRed = red/2
          newGreen = green/2
          newBlue = blue/2
          pic.putpixel((x, y),(newRed,newGreen,newBlue))

    pic.show()



def mystery(N):
    pic = Image.open("butterfly.jpg")
   
    for x in range(pic.size[0]):
        for y in range(pic.size[1]-N):
            fromX = x
            fromY = y+N
            (newRed,newGreen,newBlue) = pic.getpixel((fromX,fromY))
            pic.putpixel((x, y),(newRed,newGreen,newBlue))

        
    pic.show()


def mystery2(N):
  pic = Image.open("butterfly.jpg")
  for x in range(pic.size[0]):
    for y in range(pic.size[1]-1, N+1, -1):
      fromX = x
      fromY = y-N
      (newRed,newGreen,newBlue) = pic.getpixel((fromX,fromY))
      pic.putpixel((x, y),(newRed,newGreen,newBlue))

  pic.show()

# darken()
mystery2(100)



