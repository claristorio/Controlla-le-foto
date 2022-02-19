import random, cv2, os

path = os.getcwd() + '\\'
filesInData = os.listdir(path)

for k in filesInData:
    if k.isalpha():
        dirPath = path + k + '\\'
        filesInDir = os.listdir(dirPath)
        imgPaths = [dirPath + e for e in filesInDir if not (e.endswith('.ini')) and not (e.endswith('.py')) and not (e.endswith('.xml'))]

        cascPath = path + "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascPath)

        for (i, el)  in enumerate(imgPaths):
            image = cv2.imread(el)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(30, 30),
                flags = cv2.CASCADE_SCALE_IMAGE
            )

            print(f'Ho trovato {len(faces)} facce!')
            ext = '.' + el.split('.')[1]
            if len(faces) == 1:
                new = dirPath + 'tieni_' + str(hex(random.randrange(0, 32768))) + ext
            else:
                new = dirPath + 'butta_' + str(hex(random.randrange(0, 32768))) + ext
            os.rename(el, new)
            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.imshow("Faces found", image)
            cv2.waitKey(0)