from PIL import Image, ImageDraw

# Create a new image with a white background
image = Image.new('RGB', (400, 400), 'white')

# Create a drawing context
draw = ImageDraw.Draw(image)

# Draw a red circle
draw.ellipse((100, 100, 300, 300), fill='red')

# Save the image
image.save('circle.png')