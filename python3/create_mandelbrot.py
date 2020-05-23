# I can't believe I'm rewriting this the first time since 1998...
# https://en.wikipedia.org/wiki/Mandelbrot_set

import matplotlib.image
from datetime import datetime

def generate(w, h, max_iterations):
    startTime = datetime.now()

    matrix = [[0 for x in range(w)] for y in range(h)] 

    for j in range(h):
        for i in range(w):
            x0 = (1.0 * i / w) * 3 - 2.3
            y0 = (1.0 * j / h) * 2 - 1.0 
            x = 0.0
            y = 0.0
            iteration = 0;
            while ((x**2 + y**2 <= 4) and iteration < max_iterations):
                xtemp = x**2 - y**2 + x0
                y = 2*x*y + y0
                x = xtemp
                iteration = iteration + 1
                
            matrix[j][i] = iteration  
    
    print(datetime.now() - startTime, 'time taken to generate', w, h, 'max:', max_iterations) 

    return matrix

array = generate(800, 600, 40)
outputfile = '/tmp/mandelbrot.png'
matplotlib.image.imsave(outputfile, array)
print (outputfile)


'''        
for each pixel (Px, Py) on the screen do
    x0 = scaled x coordinate of pixel (scaled to lie in the Mandelbrot X scale (-2.5, 1))
    y0 = scaled y coordinate of pixel (scaled to lie in the Mandelbrot Y scale (-1, 1))
    x := 0.0
    y := 0.0
    iteration := 0
    max_iteration := 1000
    while (x×x + y×y ≤ 2×2 AND iteration < max_iteration) do
        xtemp := x×x - y×y + x0
        y := 2×x×y + y0
        x := xtemp
        iteration := iteration + 1
 
    color := palette[iteration]
    plot(Px, Py, color)
'''
