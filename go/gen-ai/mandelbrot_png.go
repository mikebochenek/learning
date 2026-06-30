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
    start := time.Now()

    const (
        width       = 1600
        height      = 1200
        maxIter     = 200
        scale       = 1.5
        centerX     = -0.5
        centerY     = 0.0
    )

    img := image.NewNRGBA(image.Rect(0, 0, width, height))

    for y := 0; y < height; y++ {
        for x := 0; x < width; x++ {
            zx := (float64(x-width/2) / float64(width/2)) * scale
            zy := (float64(y-height/2) / float64(height/2)) * scale

            c := complex(centerX+zx, centerY+zy)
            z := complex(0, 0)
            iter := 0

            for iter < maxIter && cmplx.Abs(z) <= 2 {
                z = z*z + c
                iter++
            }

            if iter == maxIter {
                img.Set(x, y, color.Black)
            } else {
                col := color.NRGBA{R: uint8(10 * iter % 256), G: uint8(20 * iter % 256), B: uint8(30 * iter % 256), A: 255}
                img.Set(x, y, col)
            }
        }
    }

    outputDir := filepath.Join("c:\\", "tmp")
    if err := os.MkdirAll(outputDir, 0o755); err != nil {
        panic(err)
    }

    outputPath := filepath.Join(outputDir, "mandelbrot.png")
    outFile, err := os.Create(outputPath)
    if err != nil {
        panic(err)
    }
    defer outFile.Close()

    if err := png.Encode(outFile, img); err != nil {
        panic(err)
    }

    fmt.Printf("Saved Mandelbrot image to %s (%d x %d))\n", outputPath, width, height)
    fmt.Printf("Total time: %s\n", time.Since(start))
}
