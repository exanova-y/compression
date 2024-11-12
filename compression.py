from PIL import Image
image = Image.open(r'C:\Users\DELL\Documents\Minerva\year 2\cs113\parrot.png')
#image.show()
pixels = list(image.getdata())

v = [27, 149, 8, 161, 230, 54, 202, 5]
e1 = 10
e2 = 50
e3 = 100


# thres for parrot
e4 = 32

c1 = [n if n > e1 else 0 for n in v]
c2 = [n if n > e2 else 0 for n in v]
c3 = [n if n > e4 else 0 for n in v]
c4 = [n if n > e4 else 0 for n in pixels]

# show parrot 
filtered_image = Image.new("L", image.size)
filtered_image.putdata(c4)
filtered_image.show()
