# FAQ : cv2.putText()

The syntax is

```python
cv.putText(img, text, org, fontFace, fontScale, color, thickness, lineType, bottomLeftOrigin)
```

**img** = Image to display

**text** = Text to display on the image

**org** = Origin co-ordinates => **(x, y)**

**fontFace** = Type of Hershey Font Face to use

> **Available Hershey Font Faces :**

- FONT_HERSHEY_SIMPLEX = 0
- FONT_HERSHEY_PLAIN = 1
- FONT_HERSHEY_DUPLEX = 2
- FONT_HERSHEY_COMPLEX = 3
- FONT_HERSHEY_TRIPLEX = 4
- FONT_HERSHEY_COMPLEX_SMALL = 5
- FONT_HERSHEY_SCRIPT_SIMPLEX = 6
- FONT_HERSHEY_SCRIPT_COMPLEX = 7
- FONT_ITALIC = 16

**fontScale** = Size of the text

**color** = Color of the text in RGB values

**thicknes** = Text/Font Thickness

**lineType** = Which line type to use

> **Available Line Types :**

- FILLED = -1 (Filled)
- LINE_4 = 4 (4 Connected Line)
- LINE_8 = 8 (8 Connected Line)
- LINE_AA = 16 (Anti-Aliased Line)

**bottomLeftOrigin** = Origin of the text is set to the bottom left, if set to **True**. Default is **False**
