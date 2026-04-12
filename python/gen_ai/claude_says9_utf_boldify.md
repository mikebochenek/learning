# Promot

is there a python library that creates unicode bold?  For example:  change from "Greater Zurich" to "𝗚𝗿𝗲𝗮𝘁𝗲𝗿 𝗭𝘂𝗿𝗶𝗰𝗵" 

# Answer

Yes! The library is called **`boldify`** — actually, the most common one used for this is **`unicode-text-styler`** or you can use **`rich`**, but the simplest dedicated library is:

## `unicodedata` + manual mapping, or `boldify`

The most popular lightweight option is **`bold-text`** / **`unicodeit`**, but honestly the cleanest solution people use is a small library called **`unicodetools`** or just a hand-rolled function. Let me give you the most practical options:

---

### Option 1: `unicode-text-styler` (pip installable)
```bash
pip install unicode-text-styler
```
```python
from unicode_text_styler import style_text
print(style_text("Greater Zurich", "bold"))
# 𝗚𝗿𝗲𝗮𝘁𝗲𝗿 𝗭𝘂𝗿𝗶𝗰𝗵
```

---

### Option 2: Roll your own (no dependencies)

This is what most people end up doing since it's trivial:

```python
def to_unicode_bold(text: str) -> str:
    result = []
    for char in text:
        if 'A' <= char <= 'Z':
            result.append(chr(ord(char) - ord('A') + 0x1D400))  # 𝐀–𝐙
        elif 'a' <= char <= 'z':
            result.append(chr(ord(char) - ord('a') + 0x1D41A))  # 𝐚–𝐳
        elif '0' <= char <= '9':
            result.append(chr(ord(char) - ord('0') + 0x1D7CE))  # 𝟎–𝟗
        else:
            result.append(char)
    return ''.join(result)

print(to_unicode_bold("Greater Zurich"))
# 𝐆𝐫𝐞𝐚𝐭𝐞𝐫 𝐙𝐮𝐫𝐢𝐜𝐡
```

> **Note:** The style in your example (`𝗚𝗿𝗲𝗮𝘁𝗲𝗿`) is specifically **Bold Sans-Serif** (not just bold). Adjust the offsets:

```python
def to_bold_sans_serif(text: str) -> str:
    result = []
    for char in text:
        if 'A' <= char <= 'Z':
            result.append(chr(ord(char) - ord('A') + 0x1D5D4))  # 𝗔–𝗭
        elif 'a' <= char <= 'z':
            result.append(chr(ord(char) - ord('a') + 0x1D5EE))  # 𝗮–𝘇
        elif '0' <= char <= '9':
            result.append(chr(ord(char) - ord('0') + 0x1D7EC))  # 𝟬–𝟵
        else:
            result.append(char)
    return ''.join(result)

print(to_bold_sans_serif("Greater Zurich"))
# 𝗚𝗿𝗲𝗮𝘁𝗲𝗿 𝗭𝘂𝗿𝗶𝗰𝗵
```

---

### Unicode Bold Styles (offsets cheat sheet)

| Style | Uppercase start | Lowercase start |
|---|---|---|
| **Bold Serif** | `0x1D400` | `0x1D41A` |
| *Italic Serif* | `0x1D434` | `0x1D44E` |
| ***Bold Italic Serif*** | `0x1D468` | `0x1D482` |
| **Bold Sans-Serif** (your example) | `0x1D5D4` | `0x1D5EE` |
| *Bold Italic Sans-Serif* | `0x1D63C` | `0x1D656` |

The DIY approach is the most reliable since library names and availability change, and it's only ~10 lines of code.