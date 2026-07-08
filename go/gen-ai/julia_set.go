// Package main generates a Julia set fractal image.
// A Julia set is a fractal produced by iterating a simple complex number function.
package main

import (
    "fmt"
    "image"
    "image/color"
    "image/png"
    "math/cmplx"
    "os"
    "path/filepath"
    "time"
)

func main() {
    // Track execution time for performance measurement
    start := time.Now()

    const (
        // Canvas dimensions in pixels
        width    = 800
        height   = 800
        // Maximum number of iterations per pixel (higher = more detail but slower)
        maxIter  = 200
        // Zoom level (1.0 = no zoom, >1 = zoomed in)
        zoom     = 1.0
        // Offset to pan the view horizontally (real axis)
        offsetX  = 0.0
        // Offset to pan the view vertically (imaginary axis)
        offsetY  = 0.0
    )

    // Julia set parameter c: determines the shape of the fractal.
    // Different values of c produce different Julia set patterns.
    // This particular value produces an aesthetically pleasing pattern.
    c := complex(-0.7, 0.27015)

    // Create an RGBA image buffer to render the Julia set onto
    img := image.NewNRGBA(image.Rect(0, 0, width, height))

    // Iterate over each pixel in the image
    for y := 0; y < height; y++ {
        for x := 0; x < width; x++ {
            // Convert pixel coordinates to complex plane coordinates.
            // Map pixel position to the complex number domain with appropriate scaling.
            zx := (float64(x-width/2) / (float64(width) / 4)) * zoom + offsetX
            zy := (float64(y-height/2) / (float64(height) / 4)) * zoom + offsetY

            // Initial complex number for this pixel
            z := complex(zx, zy)
            // Iteration counter (used for coloring)
            iter := 0

            // Escape time algorithm: iterate z = z*z + c until magnitude exceeds 2
            // (or until max iterations reached). Points that escape quickly are colored
            // based on iteration count; points that never escape are part of the set.
            for iter < maxIter && cmplx.Abs(z) <= 2 {
                z = z*z + c
                iter++
            }

            // Color the pixel based on iteration count
            if iter == maxIter {
                // Points in the Julia set (didn't escape) are colored black
                img.Set(x, y, color.Black)
            } else {
                // Points outside the set are colored based on escape speed.
                // Use iteration count to create a hue-based gradient coloring.
                hue := uint8(10 * iter % 256)
                img.Set(x, y, color.NRGBA{
                    R: hue,
                    G: uint8(int(hue) * 2 % 256),
                    B: uint8(int(hue) * 3 % 256),
                    A: 255,
                })
            }
        }
    }

    // Create output directory if it doesn't exist
    outputDir := filepath.Join("c:\\", "tmp")
    if err := os.MkdirAll(outputDir, 0o755); err != nil {
        panic(err)
    }

    // Construct the output file path
    outputPath := filepath.Join(outputDir, "julia_set.png")
    outFile, err := os.Create(outputPath)
    if err != nil {
        panic(err)
    }
    defer outFile.Close()

    // Encode the image buffer as PNG and write to file
    if err := png.Encode(outFile, img); err != nil {
        panic(err)
    }

    // Print completion message and execution time
    fmt.Printf("Saved Julia set image to %s\n", outputPath)
    fmt.Printf("Total time: %s\n", time.Since(start))
}
