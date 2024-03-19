import face_recognition as fr

def reconhece_face(url_foto):
    foto = fr.load_image_file(url_foto)
    rostos = fr.face_encodings(foto)
    if(len(rostos) > 0):
        return True, rostos
    
    return False, []

def get_rostos():
    rostos_conhecidos = []
    nomes_dos_rostos = []

    arthur1 = reconhece_face("./fotos/arthur1.jpeg")
    if(arthur1[0]):
        rostos_conhecidos.append(arthur1[1][0])
        nomes_dos_rostos.append("Arthur")

    bernardo = reconhece_face("./fotos/bernardoface.jpg")
    if(bernardo[0]):
        rostos_conhecidos.append(bernardo[1][0])
        nomes_dos_rostos.append("Bernardo")
    
    return rostos_conhecidos, nomes_dos_rostos