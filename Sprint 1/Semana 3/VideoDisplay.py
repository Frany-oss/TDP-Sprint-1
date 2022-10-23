import cv2
import DetectPoseFunction as dp

def PoseEstimator(path = None, verbose = False):

    '''
    Args:
        Path: si no se pasa un path se asume que sera WebCam, de lo contrario se tomara el video que se le pase en path
        Verbose: Si se requiere mostart los landmarks se pone en verdadero, de lo contrario se deja en false  
    '''
    
    # Configurar la funcion Pose para el video.
    pose_video = dp.mp_pose.Pose(static_image_mode = False, min_detection_confidence = 0.5, model_complexity = 1)

    # Inicializa el objeto VideoCapture para leer de un video o reconocer camara.
    if path != None:
        video = cv2.VideoCapture(path)
    else:
        video = cv2.VideoCapture(0)

    # Crear una ventana con nombre para cambiar el tamano
    # cv2.namedWindow('Pose Detection in 3D', cv2.WINDOW_NORMAL)
    
    # Seteando las dimensiones de la camara
    video.set(3,1280)
    video.set(4,960)

    while video.isOpened():

        # Leer un frame
        ok, frame = video.read()

        # Si el frame no esta Ok
        if not ok:
            break
        
        # Voltea el marco horizontalmente para una visualizacion natural (selfie-view).
        frame = cv2.flip(frame, 1)

        # Obtener la anchura y la altura del frame
        frame_height, frame_width, _ =  frame.shape

        # Cambia el tamano del cuadro manteniendo la relacion de aspecto.
        frame = cv2.resize(frame, (int(frame_width * (640 / frame_height)), 640))

        # Realice la deteccion de puntos de referencia de la pose.
        frame, _ = dp.detectPose(frame, pose_video, verbose, display = False)

        # Mostrar el frame
        cv2.imshow('Pose Detection in 3D', frame)

        # capturar que tecla se presiona
        k = cv2.waitKey(1) & 0xFF

        # si pulsa 'ESC' cerrar ventana
        if(k == 27):
            break

    # Liberar el objeto VideoCapture.
    video.release()

    # Cerrar la ventana
    cv2.destroyAllWindows()

PoseEstimator(None, True)

