from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
INK = (11, 26, 20)
INK2 = (17, 42, 32)
PITCH = (32, 208, 112)
CHALK = (245, 242, 234)
MUTE = (159, 181, 169)

img = Image.new("RGB", (W, H), INK)
draw = ImageDraw.Draw(img)

# subtle diagonal gradient band (top-right glow, approximated with translucent circles)
for i in range(6):
    r = 260 + i * 70
    alpha_col = tuple(int(INK[c] + (PITCH[c] - INK[c]) * (0.06 - i * 0.008)) for c in range(3))
    draw.ellipse(
        [W - 300 - r, -300 - r, W - 300 + r, -300 + r],
        fill=alpha_col,
    )

# bottom pitch-line motif (concentric rings, bottom-right)
for i, rad in enumerate([420, 460, 500]):
    draw.ellipse(
        [W - 140 - rad, H - 140 - rad, W - 140 + rad, H - 140 + rad],
        outline=(32, 208, 112, 40),
        width=2,
    )

FONT_DIR = "/usr/share/fonts/truetype/liberation/"
bold_big = ImageFont.truetype(FONT_DIR + "LiberationSans-Bold.ttf", 92)
bold_mid = ImageFont.truetype(FONT_DIR + "LiberationSans-Bold.ttf", 40)
eyebrow_font = ImageFont.truetype(FONT_DIR + "LiberationSans-Bold.ttf", 28)

# Eyebrow
draw.text((80, 110), "GAA STRENGTH AND CONDITIONING", font=eyebrow_font, fill=PITCH)

# Headline (three lines, last word green)
draw.text((78, 160), "BE FASTER.", font=bold_big, fill=CHALK)
draw.text((78, 260), "HIT HARDER.", font=bold_big, fill=CHALK)
draw.text((78, 360), "STAY ON THE PITCH.", font=bold_big, fill=PITCH)

# Sub line
sub_font = ImageFont.truetype(FONT_DIR + "LiberationSans-Bold.ttf", 32)
draw.text((80, 480), "STRENGTH · SPEED · POWER · INJURY PREVENTION", font=sub_font, fill=MUTE)

# Small logo mark bottom-left
draw.rounded_rectangle([78, 540, 118, 580], radius=9, fill=PITCH)
draw.polygon([(88, 572), (98, 550), (104, 562), (108, 554), (112, 572)], fill=INK)
logo_font = ImageFont.truetype(FONT_DIR + "LiberationSans-Bold.ttf", 30)
draw.text((130, 549), "GAA", font=logo_font, fill=CHALK)
w = draw.textlength("GAA ", font=logo_font)
draw.text((130 + w, 549), "PERFORMANCE", font=logo_font, fill=PITCH)

img.save("/home/claude/gaaperformance/og-image.png", "PNG", optimize=True)
print("saved", img.size)
