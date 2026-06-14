// https://claude.ai/chat/66ee8fd7-e11c-45f1-8020-2ace5a66412f

// mandelbrot.cpp — C++17 Mandelbrot set renderer → PNG
// Compile: g++ -std=c++17 -O2  mandelbrot.cpp -lpng
// Output:  mandelbrot.png  (1920×1080, smooth HSV coloring)

// (base) PS C:\dev\code\learning\cpp\gen-ai> zig c++ .\mandelbrot.cpp
// 'png.h' file not foundt.cpp
// .h>12 | #include <pngmandelbrot.cpp

#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <memory>
#include <vector>
#include <png.h>

// ── Image / fractal parameters ──────────────────────────────────
constexpr int    WIDTH      = 8000;
constexpr int    HEIGHT     = 6000;
constexpr int    MAX_ITER   = 512;
constexpr double CENTER_X   = -0.75;
constexpr double CENTER_Y   =  0.0;
constexpr double ZOOM       =  2.5;   // half-width in complex-plane units

// ── Smooth iteration count (avoids banding) ─────────────────────
static double mandelbrot(double cx, double cy)
{
    double zx = 0.0, zy = 0.0;
    int i = 0;
    while (zx*zx + zy*zy <= 4.0 && i < MAX_ITER) {
        double tmp = zx*zx - zy*zy + cx;
        zy = 2.0*zx*zy + cy;
        zx = tmp;
        ++i;
    }
    if (i == MAX_ITER) return static_cast<double>(MAX_ITER);
    // Smooth colouring: add fractional part based on escape magnitude
    double log_zn = std::log(zx*zx + zy*zy) / 2.0;
    double nu     = std::log(log_zn / std::log(2.0)) / std::log(2.0);
    return static_cast<double>(i) + 1.0 - nu;
}

// ── HSV → RGB (h in [0,360), s,v in [0,1]) ──────────────────────────────────
struct RGB { uint8_t r, g, b; };

static RGB hsv_to_rgb(double h, double s, double v)
{
    h = std::fmod(h, 360.0);
    int    hi = static_cast<int>(h / 60.0) % 6;
    double f  = h / 60.0 - std::floor(h / 60.0);
    double p  = v * (1.0 - s);
    double q  = v * (1.0 - f * s);
    double t  = v * (1.0 - (1.0 - f) * s);
    double r = 0, g = 0, b = 0;
    switch (hi) {
        case 0: r=v; g=t; b=p; break;
        case 1: r=q; g=v; b=p; break;
        case 2: r=p; g=v; b=t; break;
        case 3: r=p; g=q; b=v; break;
        case 4: r=t; g=p; b=v; break;
        case 5: r=v; g=p; b=q; break;
    }
    return { static_cast<uint8_t>(r*255), static_cast<uint8_t>(g*255), static_cast<uint8_t>(b*255) };
}

// ── Map smooth iteration value → colour ──────────────────────────────────────
static RGB iteration_to_color(double t)
{
    if (t >= static_cast<double>(MAX_ITER)) return {0, 0, 0};   // inside = black
    double hue        = std::fmod(t * 8.5, 360.0);              // cycle hues
    double value      = 1.0 - std::pow(t / MAX_ITER, 0.45);     // darken near set
    return hsv_to_rgb(hue, 0.85, value);
}

// ── Write raw pixel buffer to PNG via libpng ─────────────────────────────────
static bool write_png(const char* path,
                      const std::vector<uint8_t>& pixels,
                      int width, int height)
{
    FILE* fp = std::fopen(path, "wb");
    if (!fp) { std::perror("fopen"); return false; }

    png_structp png  = png_create_write_struct(PNG_LIBPNG_VER_STRING,
                                               nullptr, nullptr, nullptr);
    png_infop   info = png ? png_create_info_struct(png) : nullptr;
    if (!png || !info) {
        std::fclose(fp);
        return false;
    }

    if (setjmp(png_jmpbuf(png))) {
        png_destroy_write_struct(&png, &info);
        std::fclose(fp);
        return false;
    }

    png_init_io(png, fp);
    png_set_IHDR(png, info, static_cast<uint32_t>(width),
                 static_cast<uint32_t>(height),
                 8, PNG_COLOR_TYPE_RGB,
                 PNG_INTERLACE_NONE,
                 PNG_COMPRESSION_TYPE_DEFAULT,
                 PNG_FILTER_TYPE_DEFAULT);
    png_write_info(png, info);

    // Write row-by-row (no extra allocation — point into existing buffer)
    for (int y = 0; y < height; ++y) {
        const uint8_t* row = pixels.data() + y * width * 3;
        png_write_row(png, const_cast<uint8_t*>(row));
    }

    png_write_end(png, nullptr);
    png_destroy_write_struct(&png, &info);
    std::fclose(fp);
    return true;
}

// ── Main ─────────────────────────────────────────────────────────────────────
int main()
{
    const double aspect = static_cast<double>(WIDTH) / HEIGHT;
    const double x_min  = CENTER_X - ZOOM * aspect / 2.0;
    const double x_max  = CENTER_X + ZOOM * aspect / 2.0;
    const double y_min  = CENTER_Y - ZOOM / 2.0;
    const double y_max  = CENTER_Y + ZOOM / 2.0;

    std::vector<uint8_t> pixels(static_cast<std::size_t>(WIDTH * HEIGHT * 3));

    std::printf("Rendering %dx%d Mandelbrot set...\n", WIDTH, HEIGHT);

    for (int py = 0; py < HEIGHT; ++py) {
        double cy = y_max - (y_max - y_min) * py / (HEIGHT - 1);
        for (int px = 0; px < WIDTH; ++px) {
            double cx   = x_min + (x_max - x_min) * px / (WIDTH - 1);
            double iter = mandelbrot(cx, cy);
            RGB    col  = iteration_to_color(iter);
            std::size_t idx = static_cast<std::size_t>((py * WIDTH + px) * 3);
            pixels[idx]     = col.r;
            pixels[idx + 1] = col.g;
            pixels[idx + 2] = col.b;
        }
        if (py % 100 == 0)
            std::printf("  row %4d / %d\n", py, HEIGHT);
    }

    const char* outfile = "mandelbrot.png";
    if (write_png(outfile, pixels, WIDTH, HEIGHT)) {
        std::printf("Saved → %s\n", outfile);
        return 0;
    } else {
        std::fprintf(stderr, "Failed to write PNG.\n");
        return 1;
    }
}