def setup():
    size(1200, 1200)
    background(255)
    global loadedImage
    loadedImage = loadImage("loadTheImage.jpg")
    strokeWeight(10)
    textSize(25)
 
def draw():
    try:
        image(loadedImage, 300, 300, 450, 450)
    except:
        fill(0)
        text("blad - obraz", 25, 25)
        stroke("#FF0000")
    else:
        stroke("#0000FF")
    finally:
        noFill()
        rect(300, 300, 450, 450)
