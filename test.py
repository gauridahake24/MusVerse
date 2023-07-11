import magic

extension = magic.from_file('static/Abhi Mujh Me Kahi.mp3', mime=True).split("/")[1]
print(extension)
