# https://claude.ai/chat/efb9ee93-223a-4855-9c4b-dbf67c6c439a
# can you show me some python code which takes four .jpg files, and merges them into 
# an animated gif using any existing open source python librarires

from PIL import Image

# List of input JPEG files
image_files = ['03-17.png','04-13.png','05-17.png','06-23.png','07-31.png','08-31.png'] #,'12-01.png']
image_folder = 'C:\\Users\\User\\ownCloud\\Documents\\fitness\\'
prefix_2024= 'fitness_2024-'
prefix_2025= 'fitness_2025_'
output_fn = image_folder+'output_2024.gif'
#['04-12.png','05_01.png','06_08.png','04-12.png']

# Load all images
images = [Image.open(image_folder+prefix_2024+img) for img in image_files]

# Save as animated GIF
images[0].save(
    output_fn,
    save_all=True,
    append_images=images[1:],
    duration=500,  # Duration per frame in milliseconds
    loop=0  # 0 means loop forever
)

print("Animated GIF created successfully as " + output_fn)

'''
alternative
import imageio

images = [imageio.imread(f'image{i}.jpg') for i in range(1, 5)]
imageio.mimsave('output.gif', images, duration=0.5)
'''