from PIL import Image, ImageDraw, ImageFont
import os
import urllib.request

def generateBanner(version, uptime, system, plugins):
    
    scriptDir = os.path.dirname(os.path.abspath(__file__))
    fontPath = os.path.join(scriptDir, 'RobotoMono-Regular.ttf')
    outputPath = os.path.join(scriptDir, 'output.jpg')
    imgPathUrl = os.path.join(scriptDir, 'misatobg.jpg')
        
    if not os.path.exists(imgPathUrl):
        urllib.request.urlretrieve('http://custompng.altervista.org/Server/misatobg.jpg', imgPathUrl)
        print("my ass")

    with Image.open(imgPathUrl) as img:

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(fontPath, 15)

        textTitle = "GSMC Auth Plugin Status"
        textBody = f"• Version: {version} \n\n• Uptime: {uptime} \n\n• System: {system} \n\n• Plugins: {plugins} plugin(s) active"

        draw.text((19,40), textTitle, font=font, fill=(0,0,0))
        draw.text((19,110), textBody, font=font, fill=(0,0,0))

        img.save(outputPath, quality = 95)

    return outputPath    
