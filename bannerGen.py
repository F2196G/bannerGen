from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import urllib.request

def generateBanner(title, version, uptime, system, plugins):
    
    scriptDir = Path(__file__).resolve().parent
    fontPath = scriptDir / 'RobotoMono-Regular.ttf'
    outputPath = scriptDir / 'output.jpg'
    imgPathUrl = scriptDir / 'misatobg.jpg'
        
    if not imgPathUrl.exists():
        urllib.request.urlretrieve('https://cdn.r0rt1z2.com/misatobg.jpg', imgPathUrl)

    with Image.open(imgPathUrl) as img:

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(str(fontPath), 15)
        
        textBody = f"• Version: {version} \n\n• Uptime: {uptime} \n\n• System: {system} \n\n• Plugins: {plugins} plugin(s) active"

        draw.text((19,40), title, font=font, fill=(0,0,0))
        draw.text((19,110), textBody, font=font, fill=(0,0,0))

        img.save(outputPath, quality = 95)

    return str(outputPath)    
