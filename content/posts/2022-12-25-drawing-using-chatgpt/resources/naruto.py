from PIL import Image, ImageDraw

# Create a new image with a white background
image = Image.new('RGB', (400, 400), 'white')

# Create a drawing context
draw = ImageDraw.Draw(image)

# Draw Naruto's face
draw.ellipse((100, 100, 300, 300), fill='orange')

# Draw Naruto's eyes
draw.ellipse((150, 150, 200, 200), fill='white')
draw.ellipse((250, 150, 300, 200), fill='white')
draw.ellipse((155, 155, 195, 195), fill='black')
draw.ellipse((255, 155, 295, 195), fill='black')

# Draw Naruto's eyebrows
draw.line((150, 150, 200, 150), fill='black', width=3)
draw.line((250, 150, 300, 150), fill='black', width=3)

# Draw Naruto's nose
draw.polygon([(225, 175), (235, 190), (215, 190)], fill='orange')

# Draw Naruto's mouth
draw.arc((175, 200, 275, 220), 0, 180, fill='red')

# Draw Naruto's whiskers
draw.line((100, 200, 150, 250), fill='black', width=3)
draw.line((100, 200, 150, 150), fill='black', width=3)
draw.line((300, 200, 250, 250), fill='black', width=3)
draw.line((300, 200, 250, 150), fill='black', width=3)

# Draw Naruto's headband
points = [(100, 100), (200, 50), (300, 100)]
draw.polygon(points, fill='black')

# Save the image
image.save('naruto.png')
