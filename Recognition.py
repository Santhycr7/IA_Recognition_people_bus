#OpenCV module
import cv2
#modulo para leer directorios y rutas de archivos
import os
#OpenCV trabaja con arreglos de numpy
import numpy
#se importa la lista de personas permitidas
from listaPermitidos import flabianos
flabs=flabianos()

#Parte 1: Creando el entrenamiento del modelo
print ('Formando...'

#Directorio donde se encuentra las carpetas con las caras de entrenamiento
dir_faces = 'att_faces/orl_faces'

#Crear una lista de imagenes y  una lista de nombres correspondientes
(images, lables, names, id) = ([], [], {}, 0)
for (subdirs, dirs, files) in os.walk(dir_faces):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(dir_faces, subdir)
        for filename in os.listdir(subjectpath):
            path = subjectpath + '/' + filename
            lable = id
            images.append(cv2.imread(path, 0))
            lables.append(int(lable))
        id += 1
(im_width, im_height) = (112, 92)

# Crear una matriz Numpy de las dos listas anteriores
(images, lables) = [numpy.array(lis) for lis in [images, lables]]
# OpenCV entrena un modelo a partir de las imagenes
model = cv2.face.LBPHFaceRecognizer_create()
model.train(images, lables)

#Parte 2: Utilizar el modelo entrenado en funcionamiento de la camara
face cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while True:
    #leemos un frame y lo gardamos
    rval, frame = cap.read()
    frame=cv2.flip(frame,1,0)

    #convertimos la imagen a blanco y negro
    gray = cv2.cvtColor(frame,  cv2.COLOR_BGR2GRAY)

    #redimensional la imagen
    mini = cv2.resize(gray, (int(gray.shape[1]/size), int(gray.shape[0]/size)))

    #buscamos las coordenadas de los rostros y guardamos su posicion
    faces = face_cascade.detectMultiScale(mini)

    for i in range(len(faces)):
        face_i = faces[i]
        (x, y, w, h) = [v*size for v in face_i]
        face = gray [y:y + h, x:x + w]
        face_resize = cv2. resize(face, (im_width, im_height))

        #intentanto reconocer la cara
        prediction = model.predict(face_resize)

        #Dibujamos en las coordenadas del rostro
        cv2.rectangle(frame, (x, y), (x = w, y = h),(0, 255, 0), 3)

        #Escribiendo el numero en la cara reconocida
        #La variable cara tendra numeros de 0 hasta la cantidad de personas que suban al autobus.
        cara = '%s' %(number[prediction[0]])

        #Reconoce a una persona y se toma la prediccion valida
        if prediction[1]<25 :
        	#ponemos el numero a la persona que se reconoce
        	cv2.putText(frame, '%s - %.0f' % (cara,predictio[1]),(x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))

        	#Del numero de personas disponibles
        	#Busca si el numero de personas reconocidas esta dentro de los que tienen acceso
        	flabs.TuSiTuNo(cara)
        	
        #Si la prediccion es mayor al numero permitido 25 no permite ingresar mas personas
        elif prediction[1]>26:
        	cv2.putText(frame, 'no permitido',(x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))

        #Mostrar la imagen
        cv2.imshow('OpenCV Reconocimiento facial', frame)
    
