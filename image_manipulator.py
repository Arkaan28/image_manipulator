from PIL import Image
from PIL import ImageEnhance
from IPython.display import display

image=Image.open("sample.jpg")
#display(image)
#image=image.convert("RGB")
enhanced_image=ImageEnhance.Brightness(image)
images=[]

for i in range(0,10):
    images.append(enhanced_image.enhance(i/10))

#print(images)

test_image=images[0]
cont_sheet=Image.new(test_image.mode,(test_image.width,10*test_image.height))

y=0
for img in images:
    cont_sheet.paste(img,(0,y))
    y+=3024  #Depending on the image size

cont_sheet=cont_sheet.resize((403,3024)) #depends on the image size
#display(cont_sheet)

cont_sheet_two=Image.new(test_image.mode,(3*test_image.width,3*test_image.height))
a=0
b=0
for img in images[1:]:
    cont_sheet_two.paste(img,(a,b))
    if a+test_image.width==cont_sheet_two.width:
        a=0
        b+=test_image.height
    else:
        a+=test_image.width
#cont_sheet_two=contact_sheet_two.resize()
display(cont_sheet_two)