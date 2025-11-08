from PIL import Image, ImageDraw, ImageFont
import os
import urllib.request

def generateBanner(title, version, uptime, system, plugins):
    
    scriptDir = os.path.dirname(os.path.abspath(__file__))
    fontPath = os.path.join(scriptDir, 'RobotoMono-Regular.ttf')
    outputPath = os.path.join(scriptDir, 'output.jpg')
    imgPathUrl = os.path.join(scriptDir, 'misatobg.jpg')
        
    if not os.path.exists(imgPathUrl):
        urllib.request.urlretrieve('https://cdn.r0rt1z2.com/misatobg.jpg', imgPathUrl)

    with Image.open(imgPathUrl) as img:

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(fontPath, 15)
        
        textBody = f"• Version: {version} \n\n• Uptime: {uptime} \n\n• System: {system} \n\n• Plugins: {plugins} plugin(s) active"

        draw.text((19,40), title, font=font, fill=(0,0,0))
        draw.text((19,110), textBody, font=font, fill=(0,0,0))

        img.save(outputPath, quality = 95)

    return outputPath    
