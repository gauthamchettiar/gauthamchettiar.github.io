from PIL import Image, ImageDraw

# Create a new image with a white background
image = Image.new('RGB', (400, 400), 'white')

# Create a drawing context
draw = ImageDraw.Draw(image)

# Draw my body
points = [(200, 200), (250, 100), (300, 200)]
draw.polygon(points, fill='cyan')

# Draw my arms and legs
draw.line((225, 200, 175, 250), fill='cyan', width=5)
draw.line((275, 200, 325, 250), fill='cyan', width=5)
draw.line((200, 200, 150, 300), fill='cyan', width=5)
draw.line((300, 200, 350, 300), fill='cyan', width=5)

# Draw my head
draw.ellipse((150, 50, 350, 250), fill='cyan')

# Draw my eyes
draw.ellipse((180, 80, 220, 120), fill='white')
draw.ellipse((280, 80, 320, 120), fill='white')

# Draw my pupils
draw.ellipse((185, 85, 215, 115), fill='black')
draw.ellipse((285, 85, 315, 115), fill='black')

# Draw my mouth
draw.arc((210, 130, 290, 170), 0, 180, fill='black')

# Save the image
image.save('ai.png')
