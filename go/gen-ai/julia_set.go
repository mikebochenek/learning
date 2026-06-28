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
        width    = 800
        height   = 800
        maxIter  = 200
        zoom     = 1.0
        offsetX  = 0.0
        offsetY  = 0.0
    )

    // A classic Julia set parameter.
    c := complex(-0.7, 0.27015)

    img := image.NewNRGBA(image.Rect(0, 0, width, height))

    for y := 0; y < height; y++ {
        for x := 0; x < width; x++ {
            zx := (float64(x-width/2) / (float64(width) / 4)) * zoom + offsetX
            zy := (float64(y-height/2) / (float64(height) / 4)) * zoom + offsetY

            z := complex(zx, zy)
            iter := 0

            for iter < maxIter && cmplx.Abs(z) <= 2 {
                z = z*z + c
                iter++
            }

            if iter == maxIter {
                img.Set(x, y, color.Black)
            } else {
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

    outputDir := filepath.Join("c:\\", "tmp")
    if err := os.MkdirAll(outputDir, 0o755); err != nil {
        panic(err)
    }

    outputPath := filepath.Join(outputDir, "julia_set.png")
    outFile, err := os.Create(outputPath)
    if err != nil {
        panic(err)
    }
    defer outFile.Close()

    if err := png.Encode(outFile, img); err != nil {
        panic(err)
    }

    fmt.Printf("Saved Julia set image to %s\n", outputPath)
    fmt.Printf("Total time: %s\n", time.Since(start))
}
