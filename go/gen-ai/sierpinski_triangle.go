package main

import (
    "fmt"
    "image"
    "image/color"
    "image/png"
    "math"
    "math/rand"
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
            img.SetNRGBA(x, y, color.NRGBA{0, 0, 0, 0})
        }
    }

    rng := rand.New(rand.NewSource(time.Now().UnixNano()))
    drawSierpinski(img, width, height, depth, rng)

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

func drawSierpinski(img *image.NRGBA, width, height, depth int, rng *rand.Rand) {
    var draw func(x1, y1, x2, y2, x3, y3 float64, level int)
    draw = func(x1, y1, x2, y2, x3, y3 float64, level int) {
        if level == 0 {
            drawTriangle(img, width, height, x1, y1, x2, y2, x3, y3, depth-level, rng)
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

func drawTriangle(img *image.NRGBA, width, height int, x1, y1, x2, y2, x3, y3 float64, level int, rng *rand.Rand) {
    minX := int(math.Min(math.Min(x1, x2), x3))
    maxX := int(math.Max(math.Max(x1, x2), x3))
    minY := int(math.Min(math.Min(y1, y2), y3))
    maxY := int(math.Max(math.Max(y1, y2), y3))

    hue := rng.Float64() * 360
    saturation := 0.55 + rng.Float64()*0.35
    value := 0.65 + rng.Float64()*0.3

    for y := minY; y <= maxY; y++ {
        for x := minX; x <= maxX; x++ {
            if x < 0 || x >= width || y < 0 || y >= height {
                continue
            }
            if pointInTriangle(float64(x), float64(y), x1, y1, x2, y2, x3, y3) {
                shimmer := (rng.Float64()-0.5) * 20
                c := hsvToRGB(hue+shimmer+float64(level)*8, saturation, value)
                img.SetNRGBA(x, y, c)
            }
        }
    }
}

func pointInTriangle(px, py, x1, y1, x2, y2, x3, y3 float64) bool {
    d1 := sign(px, py, x2, y2, x3, y3)
    d2 := sign(px, py, x3, y3, x1, y1)
    d3 := sign(px, py, x1, y1, x2, y2)

    hasNeg := (d1 < 0) || (d2 < 0) || (d3 < 0)
    hasPos := (d1 > 0) || (d2 > 0) || (d3 > 0)
    return !(hasNeg && hasPos)
}

func sign(px, py, x1, y1, x2, y2 float64) float64 {
    return (px-x1)*(y2-y1) - (x2-x1)*(py-y1)
}

func hsvToRGB(h, s, v float64) color.NRGBA {
    h = math.Mod(h, 360)
    if h < 0 {
        h += 360
    }

    c := v * s
    x := c * (1 - math.Abs(math.Mod(h/60, 2)-1))
    m := v - c

    var r, g, b float64
    switch {
    case h < 60:
        r, g, b = c, x, 0
    case h < 120:
        r, g, b = x, c, 0
    case h < 180:
        r, g, b = 0, c, x
    case h < 240:
        r, g, b = 0, x, c
    case h < 300:
        r, g, b = x, 0, c
    default:
        r, g, b = c, 0, x
    }

    return color.NRGBA{
        R: uint8((r + m) * 255),
        G: uint8((g + m) * 255),
        B: uint8((b + m) * 255),
        A: 255,
    }
}
