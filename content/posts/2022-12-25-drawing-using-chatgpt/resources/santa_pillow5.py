from PIL import Image, ImageDraw

# Create a new image with a white background
image = Image.new('RGB', (400, 400), 'white')

# Create a drawing context
draw = ImageDraw.Draw(image)

# Draw Santa's face
draw.ellipse((100, 100, 300, 300), fill='red')
draw.ellipse((150, 150, 250, 250), fill='white')
draw.ellipse((165, 165, 235, 235), fill='black')
draw.line((210, 185, 210, 215), fill='black', width=5)

# Draw Santa's hat
points = [(100, 100), (200, 50), (300, 100)]
draw.polygon(points, fill='red')

# Draw Santa's beard
points = [(150, 300), (250, 300), (200, 350)]
draw.polygon(points, fill='white')

# Draw Santa's triangular beard
points = [(150, 300), (200, 250), (250, 300)]
draw.polygon(points, fill='white')

# Draw Santa's nose
draw.polygon([(200, 175), (210, 190), (190, 190)], fill='red')

# Draw Santa's eyes
draw.ellipse((170, 130, 220, 180), fill='white')
draw.ellipse((230, 130, 280, 180), fill='white')
draw.ellipse((175, 135, 215, 175), fill='black')
draw.ellipse((235, 135, 275, 175), fill='black')

# Draw Santa's eyebrows
draw.line((170, 130, 220, 130), fill='black', width=3)
draw.line((230, 130, 280, 130), fill='black', width=3)

# Draw Santa's smile
draw.arc((175, 200, 275, 220), 0, 180, fill='red')

# Save the image
image.save('santa.png')
