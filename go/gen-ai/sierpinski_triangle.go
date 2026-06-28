package main

import (
    "fmt"
    "image"
    "image/color"
    "image/png"
    "os"
    "path/filepath"
    "time"
)

func main() {
    start := time.Now()

    const (
        width  = 800
        height = 800
        depth  = 8
    )

    img := image.NewNRGBA(image.Rect(0, 0, width, height))

    for y := 0; y < height; y++ {
        for x := 0; x < width; x++ {
            img.Set(x, y, color.White)
        }
    }

    drawSierpinski(img, width, height, depth)

    outputDir := filepath.Join("c:\\", "tmp")
    if err := os.MkdirAll(outputDir, 0o755); err != nil {
        panic(err)
    }

    outputPath := filepath.Join(outputDir, "sierpinski_triangle.png")
    outFile, err := os.Create(outputPath)
    if err != nil {
        panic(err)
    }
    defer outFile.Close()

    if err := png.Encode(outFile, img); err != nil {
        panic(err)
    }

    fmt.Printf("Saved Sierpiński triangle to %s\n", outputPath)
    fmt.Printf("Total time: %s\n", time.Since(start))
}

func drawSierpinski(img *image.NRGBA, width, height, depth int) {
    const scale = 2.0

    var draw func(x1, y1, x2, y2, x3, y3 float64, level int)
    draw = func(x1, y1, x2, y2, x3, y3 float64, level int) {
        if level == 0 {
            drawTriangle(img, width, height, x1, y1, x2, y2, x3, y3)
            return
        }

        mid12x := (x1 + x2) / 2
        mid12y := (y1 + y2) / 2
        mid23x := (x2 + x3) / 2
        mid23y := (y2 + y3) / 2
        mid31x := (x3 + x1) / 2
        mid31y := (y3 + y1) / 2

        draw(x1, y1, mid12x, mid12y, mid31x, mid31y, level-1)
        draw(mid12x, mid12y, x2, y2, mid23x, mid23y, level-1)
        draw(mid31x, mid31y, mid23x, mid23y, x3, y3, level-1)
    }

    topX := float64(width) / 2
    topY := 20.0
    leftX := 20.0
    rightX := float64(width) - 20.0
    bottomY := float64(height) - 20.0

    draw(topX, topY, leftX, bottomY, rightX, bottomY, depth)
}

func drawTriangle(img *image.NRGBA, width, height int, x1, y1, x2, y2, x3, y3 float64) {
    minX := int(x1)
    maxX := int(x1)
    minY := int(y1)
    maxY := int(y1)

    for _, p := range []struct{ x, y float64 }{{x2, y2}, {x3, y3}} {
        if int(p.x) < minX {
            minX = int(p.x)
        }
        if int(p.x) > maxX {
            maxX = int(p.x)
        }
        if int(p.y) < minY {
            minY = int(p.y)
        }
        if int(p.y) > maxY {
            maxY = int(p.y)
        }
    }

    for y := minY; y <= maxY; y++ {
        for x := minX; x <= maxX; x++ {
            if x >= 0 && x < width && y >= 0 && y < height {
                img.Set(x, y, color.Black)
            }
        }
    }
}
