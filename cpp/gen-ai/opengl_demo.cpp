// https://claude.ai/chat/0b9b8563-77e2-4a6a-b846-85f078112d23

/* 
zig c++ gl_demo.cpp -o gl_demo.exe -lopengl32 -lgdi32 -luser32

zig c++ gl_demo.cpp -o gl_demo.exe -target x86_64-windows-gnu -lopengl32 -lgdi32 -luser32
*/

// gl_demo.cpp - Minimal Win32 + OpenGL animation demo
// Compiles with just MinGW (no GLFW/GLEW needed) or MSVC.
//
// Build (MinGW):
//   g++ gl_demo.cpp -o gl_demo.exe -lopengl32 -lgdi32 -luser32
// Build (MSVC, Developer Command Prompt):
//   cl gl_demo.cpp opengl32.lib gdi32.lib user32.lib

#include <windows.h>
#include <gl/gl.h>
#include <math.h>

HDC hDC;
HGLRC hRC;
HWND hWnd;
float angle = 0.0f;

void InitGL(int width, int height) {
    glViewport(0, 0, width, height);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(-1, 1, -1, 1, -1, 1);
    glMatrixMode(GL_MODELVIEW);
    glClearColor(0.08f, 0.08f, 0.1f, 1.0f);
}

void DrawFrame() {
    glClear(GL_COLOR_BUFFER_BIT);
    glLoadIdentity();
    glRotatef(angle, 0.0f, 0.0f, 1.0f);

    glBegin(GL_TRIANGLES);
        glColor3f(1.0f, (sinf(angle * 0.03f) + 1.0f) * 0.5f, 0.2f);
        glVertex2f(0.0f, 0.6f);

        glColor3f(0.2f, 1.0f, (cosf(angle * 0.02f) + 1.0f) * 0.5f);
        glVertex2f(-0.6f, -0.4f);

        glColor3f((sinf(angle * 0.04f) + 1.0f) * 0.5f, 0.2f, 1.0f);
        glVertex2f(0.6f, -0.4f);
    glEnd();

    SwapBuffers(hDC);
    angle += 1.0f;
}

LRESULT CALLBACK WndProc(HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam) {
    switch (msg) {
        case WM_DESTROY:
            PostQuitMessage(0);
            return 0;
        case WM_SIZE:
            InitGL(LOWORD(lParam), HIWORD(lParam));
            return 0;
        case WM_KEYDOWN:
            if (wParam == VK_ESCAPE) PostQuitMessage(0);
            return 0;
    }
    return DefWindowProc(hwnd, msg, wParam, lParam);
}

void CreateGLWindow(const char* title, int width, int height) {
    WNDCLASS wc = {0};
    wc.style = CS_OWNDC | CS_HREDRAW | CS_VREDRAW;
    wc.lpfnWndProc = WndProc;
    wc.hInstance = GetModuleHandle(NULL);
    wc.lpszClassName = "GLDemoWindow";
    RegisterClass(&wc);

    hWnd = CreateWindow("GLDemoWindow", title,
        WS_OVERLAPPEDWINDOW | WS_VISIBLE,
        CW_USEDEFAULT, CW_USEDEFAULT, width, height,
        NULL, NULL, wc.hInstance, NULL);

    hDC = GetDC(hWnd);

    PIXELFORMATDESCRIPTOR pfd = {0};
    pfd.nSize = sizeof(pfd);
    pfd.nVersion = 1;
    pfd.dwFlags = PFD_DRAW_TO_WINDOW | PFD_SUPPORT_OPENGL | PFD_DOUBLEBUFFER;
    pfd.iPixelType = PFD_TYPE_RGBA;
    pfd.cColorBits = 32;
    pfd.cDepthBits = 24;

    int pf = ChoosePixelFormat(hDC, &pfd);
    SetPixelFormat(hDC, pf, &pfd);

    hRC = wglCreateContext(hDC);
    wglMakeCurrent(hDC, hRC);

    InitGL(width, height);
}

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow) {
    CreateGLWindow("OpenGL Animation Demo", 800, 600);

    MSG msg;
    bool running = true;
    while (running) {
        while (PeekMessage(&msg, NULL, 0, 0, PM_REMOVE)) {
            if (msg.message == WM_QUIT) running = false;
            TranslateMessage(&msg);
            DispatchMessage(&msg);
        }
        DrawFrame();
        Sleep(16); // ~60 FPS
    }

    wglMakeCurrent(NULL, NULL);
    wglDeleteContext(hRC);
    ReleaseDC(hWnd, hDC);
    return 0;
}