from PIL import Image
import playsound
img = Image.open('heresy.jpg')
img.show()
playsound.playsound('heresy_sound.mp3')