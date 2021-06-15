import cv2
import os
import sys


#Funcion para el reconocimiento facial
def face(imagePath, sF, mN):
	#Valores constantes para ambos modos 
	cascPath = "haarcascade_frontalface_default.xml"
	faceCascade = cv2.CascadeClassifier(cascPath)
	

	if ".jpg" in imagePath :
		#Opcion para imagenes
		image = cv2.imread(imagePath)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		faces = faceCascade.detectMultiScale(
			gray,
			scaleFactor=sF,
			minNeighbors=mN,
			minSize=(30, 30),
		)
		print("\nEncontrados {0} rostros!".format(len(faces)))
		for (x, y, w, h) in faces:
			cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

		cv2.imshow("Rostros encontrados", image)
		print("\ncierre la imagen para continuar...")
		cv2.waitKey(0)
	else:
		if imagePath !="webcam":
			#Opcion para video
			video_capture = cv2.VideoCapture(imagePath)
		else:
			#Opcion para webcam
			video_capture = cv2.VideoCapture(0)

		#opciones constantes de video
		print("\nMostrando video, presione la tecla Q en la ventana del video para terminar...")
		while True:
			ret, frame = video_capture.read()
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			faces = faceCascade.detectMultiScale(
				gray,
				scaleFactor=sF,
				minNeighbors=mN,
				minSize=(30, 30),
			)
			for (x, y, w, h) in faces:
				cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
			
			cv2.imshow('Video', frame)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
		video_capture.release()
		cv2.destroyAllWindows()


while True:
	os.system("cls") if(os.name=="nt") else os.system("clear")
	print("Selecciona una opcion")
	print("\t1 - Reconocimiento facial utilizando imagenes")
	print("\t2 - Reconocimeinto facial utilizando video")
	print("\t3 - Reconocimiento facial utilizando webcam")
	print("\t9 - Salir")
	opcionMenu=input("\n Ingrese opcion: ")
	if opcionMenu == "1":
		while True:
			os.system("cls") if(os.name=="nt") else os.system("clear")
			print("Selecciona una opcion")
			print("\t1 - Utilizar imagen con 1 rostro")
			print("\t2 - Utilizar imagen con 15 rostros")
			print("\t3 - Utilizar imagen con 25 rostros")
			print("\t9 - Volver al menu principal")
			opcionMenu1=input("\n Ingrese opcion: ")
			if opcionMenu1 == "1":
				face('1-1.jpg',1.1,5)
				continue
			elif opcionMenu1 == "2":
				face("1-2.jpg",1.2,5)
				continue
			if opcionMenu1 == "3":
				face("1-3.jpg",1.2,5)
				continue
			if opcionMenu1 == "9":
				break
			else:
				input("\nOpcion ingresada no valida...\nPulse una tecla para continuar")
	elif opcionMenu == "2":
		face("2.mp4",1.3,5)
		continue

	elif opcionMenu == "3":
		face("webcam",1.2,5)
		continue
	elif opcionMenu == "9":
		break
	else:
		input("\nOpcion ingresada no valida...\nPulse una tecla para continuar")