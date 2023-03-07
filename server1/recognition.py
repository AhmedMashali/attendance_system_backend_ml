import face_recognition
from PIL import Image
import os
from utils import encode_npImage_to_base64

path = 'img/faces'

# getting attendance
def recognition():

    known_face_encodings = []    
    known_face_names = []
    attendance = {}

    # prepare refernce faces for recognition
    create_faceEncodings_with_names(known_face_encodings, known_face_names, path)
    # prepare the taken image for recognition
    taken_image = face_recognition.load_image_file("img/taken img/image.jpg")

    # Find faces in taken image
    face_locations = face_recognition.face_locations(taken_image)
    face_encodings = face_recognition.face_encodings(taken_image, face_locations)

    # Compare refernce faces with faces from the taken image and get the attendance faces and names
    get_attendance(face_locations, face_encodings, known_face_encodings, known_face_names, taken_image, attendance)
    
    return attendance

# prepare refernce faces for recognition
def create_faceEncodings_with_names(known_face_encodings, known_face_names, path):
    # iterate over the files in the folder to get images paths
    for filename in os.listdir(path):
            f = os.path.join(path, filename)
            if os.path.isfile(f):
                # prepare refernce face
                reference_face = face_recognition.load_image_file(f)
                student_face_encoding = face_recognition.face_encodings(reference_face)[0]
                known_face_encodings.append(student_face_encoding)
                # getting the name from the filename then appending it to known_face_names
                known_face_names.append(filename.replace('.jpg', ''))

# Compare refernce faces with faces from the taken image and get the attendance faces and names
def get_attendance(face_locations, face_encodings, known_face_encodings, known_face_names, class_image, attendance):
    i = 0
    for face_location, face_encoding in zip(face_locations, face_encodings):
        # getting face location
        top, right, bottom, left = face_location
        # checking for the mathed faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)

        name = "Unknwon Person"

        # If match
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
        # pull face
        face_image = class_image[top:bottom, left:right]
        # incode face to base64
        face_b64 = encode_npImage_to_base64(face_image)
        # appending face with name to the attendance data
        attendance[f"{name}{i}"] = f"{face_b64}"
        i += 1


"""
attendace = {
    'known' : {
        'name': 'face b46',
        'name': 'face b46',
            .
            .
            .
    },
    'unknown': {
        'face b64', 'face b64', 'face b64', 
    }

}

attendance = {
    'name': 'face b46',
    'name': 'face b46',
        .
        .
        .

"""