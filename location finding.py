import webbrowser

if "where is" in text:
    text = text.replace("where is", "")
    location = text
    talk(f"opening {location} on google maps just a second")
    webbrowser.open("https://www.google.co.in/maps/place/ " + location)