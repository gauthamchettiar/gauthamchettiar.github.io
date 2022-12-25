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

# Save the image
image.save('santa.png')
