import face_recognition
from PIL import Image, ImageDraw
import base64
import os
from io import BytesIO



path = 'img/faces'
# for filename in os.listdir(path):
#     f = os.path.join(path, filename)
#     if os.path.isfile(f):
#         print(filename.replace('.jpg', ''))


known_face_encodings = []    
known_face_names = []

# take JSON data
def recognition():
    attendance = {}
    # for every face:
    for filename in os.listdir(path):
        f = os.path.join(path, filename)
        if os.path.isfile(f):
            student_img = face_recognition.load_image_file(f)
            student_face_encoding = face_recognition.face_encodings(student_img)[0]
            known_face_encodings.append(student_face_encoding)
            known_face_names.append(filename.replace('.jpg', ''))

    class_image = face_recognition.load_image_file("img/class/test_image_6.jpg")

    # Find faces in test image
    face_locations = face_recognition.face_locations(class_image)
    face_encodings = face_recognition.face_encodings(class_image, face_locations)

    # Convert to PIL format
    pil_image = Image.fromarray(class_image)

    i = 0
    # Loop through faces in test image
    for face_location, face_encoding in zip(face_locations, face_encodings):
        top, right, bottom, left = face_location
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)

        name = "Unknwon Person"

        # If match
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
        face_image = class_image[top:bottom, left:right]
        # print(face_image)
        pil_image = Image.fromarray(face_image)
        buffered = BytesIO()
        pil_image.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue())
        attendance[f"{name}{i}"] = f"{img_str}"
        i += 1
    return attendance




#   load_image_file
#   face_encoding
#   push into known_face_encodings
#   push name into known face_names


# load class image
# class_image = face_recognition.load_image_file("img/class/test_image_6.jpg")