import face_recognition

image = face_recognition.load_image_file(r'C:\Users\matma\CodeBoxx\Rocket_Elevators_Django_API\Rocket_Elevators_Django_API\quickstart\employee\bob_ross.jpg')

encoded_face = face_recognition.face_encodings(image)[0]

array = [i for i in encoded_face]

print(array)


