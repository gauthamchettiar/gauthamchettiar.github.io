from PIL import Image, ImageDraw, ImageFont

# Create a new image with a white background
image = Image.new('RGB', (400, 400), 'white')

# Create a drawing context
draw = ImageDraw.Draw(image)

# Draw Santa's face
draw.ellipse((100, 50, 300, 250), fill='red')

# Draw Santa's beard
draw.polygon([(200, 250), (250, 350), (150, 350)], fill='white')

# Draw Santa's eyes
draw.ellipse((120, 70, 140, 90), fill='white')
draw.ellipse((260, 70, 280, 90), fill='white')

# Draw Santa's pupils
draw.ellipse((125, 75, 135, 85), fill='black')
draw.ellipse((265, 75, 275, 85), fill='black')

# Draw Santa's nose
draw.polygon([(200, 120), (210, 160), (190, 160)], fill='orange')

# Draw Santa's mouth
draw.arc((170, 130, 230, 170), 0, 180, fill='black')

# Add some text
# font = ImageFont.truetype('arial.ttf', 24)
# draw.text((150, 300), 'Ho Ho Ho!', font=font, fill='white')

# Save the image
image.save('santa.png')