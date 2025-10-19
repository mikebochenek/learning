# https://claude.ai/chat/efb9ee93-223a-4855-9c4b-dbf67c6c439a
# can you show me some python code which takes four .jpg files, and merges them into 
# an animated gif using any existing open source python librarires

from PIL import Image

# List of input JPEG files
image_files = ['image1.jpg', 'image2.jpg', 'image3.jpg', 'image4.jpg']

# Load all images
images = [Image.open(img) for img in image_files]

# Save as animated GIF
images[0].save(
    'output.gif',
    save_all=True,
    append_images=images[1:],
    duration=500,  # Duration per frame in milliseconds
    loop=0  # 0 means loop forever
)

print("Animated GIF created successfully as 'output.gif'")

'''
alternative
import imageio

images = [imageio.imread(f'image{i}.jpg') for i in range(1, 5)]
imageio.mimsave('output.gif', images, duration=0.5)
'''