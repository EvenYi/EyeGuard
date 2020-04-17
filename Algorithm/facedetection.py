from scipy.spatial import distance as dist
from imutils.video import VideoStream
import numpy as np
from imutils import face_utils
import imutils
import time
import dlib
import cv2
import setting


# define two constants, one for the eye aspect ratio to indicate
# blink and then a second constant for the number of consecutive
# frames the eye must be below the threshold
EYE_AR_THRESH = 0.2
EYE_AR_CONSEC_FRAMES = 2
# initialize the frame counters and the total number of blinks
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]


def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])

    ear = (A + B) / (2.0 * C)
    return ear


def eye_blinks_count(rect, gray, predictor):
    shape = predictor(gray, rect)
    shape = face_utils.shape_to_np(shape)
    # extract the left and right eye coordinates, then use the
    # coordinates to compute the eye aspect ratio for both eyes
    leftEye = shape[lStart:lEnd]
    rightEye = shape[rStart:rEnd]
    leftEAR = eye_aspect_ratio(leftEye)
    rightEAR = eye_aspect_ratio(rightEye)
    # average the eye aspect ratio together for both eyes
    ear = (leftEAR + rightEAR) / 2.0
    # compute the convex hull for the left and right eye, then
    # visualize each of the eyes
    leftEyeHull = cv2.convexHull(leftEye)
    rightEyeHull = cv2.convexHull(rightEye)
    cv2.drawContours(setting.frame, [leftEyeHull], -1, (0, 255, 0), 1)
    cv2.drawContours(setting.frame, [rightEyeHull], -1, (0, 255, 0), 1)
    # check to see if the eye aspect ratio is below the blink
    # threshold, and if so, increment the blink frame counter
    if ear < EYE_AR_THRESH:
        setting.COUNTER += 1
    # otherwise, the eye aspect ratio is not below the blink
    # threshold
    else:
        # if the eyes were closed for a sufficient number of
        # then increment the total number of blinks
        if setting.COUNTER >= EYE_AR_CONSEC_FRAMES:
            setting.TOTAL += 1
        # reset the eye frame counter
        setting.COUNTER = 0
        # draw the total number of blinks on the frame along with
        # the computed eye aspect ratio for the frame
    cv2.putText(setting.frame, "Blinks: {}".format(setting.TOTAL), (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.putText(setting.frame, "EAR: {:.2f}".format(ear), (300, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)


def head_posture(rect, gray, predictor, size):
    shape0 = predictor(gray, rect)
    shape0 = np.array(face_utils.shape_to_np(shape0))
    # 2D image points. If you change the image, you need to change vector
    image_points = np.array([
        (shape0[33, :]),  # Nose tip
        (shape0[8, :]),  # Chin
        (shape0[36, :]),  # Left eye left corner
        (shape0[45, :]),  # Right eye right corne
        (shape0[48, :]),  # Left Mouth corner
        (shape0[54, :])  # Right mouth corner
    ], dtype="double")
    # 3D model points.
    model_points = np.array([
        (0.0, 0.0, 0.0),  # Nose tip
        (0.0, -330.0, -65.0),  # Chin
        (-225.0, 170.0, -135.0),  # Left eye left corner
        (225.0, 170.0, -135.0),  # Right eye right corne
        (-150.0, -150.0, -125.0),  # Left Mouth corner
        (150.0, -150.0, -125.0)  # Right mouth corner

    ])
    # Camera internals
    focal_length = size[1]
    center = (size[1] / 2, size[0] / 2)
    camera_matrix = np.array(
        [[focal_length, 0, center[0]],
         [0, focal_length, center[1]],
         [0, 0, 1]], dtype="double"
    )
    # print("Camera Matrix :\n {0}".format(camera_matrix))

    dist_coeffs = np.zeros((4, 1))  # Assuming no lens distortion
    (success, setting.rotation_vector, setting.translation_vector) = cv2.solvePnP(model_points, image_points, camera_matrix,
                                                                  dist_coeffs, flags=cv2.SOLVEPNP_ITERATIVE)

    # print("Rotation Vector:\n {0}".format(setting.rotation_vector))
    # print("Translation Vector:\n {0}".format(setting.translation_vector))
    # Project a 3D point (0, 0, 1000.0) onto the image plane.
    # We use this to draw a line sticking out of the nose

    (nose_end_point2D, jacobian) = cv2.projectPoints(np.array([(0.0, 0.0, 1000.0)]), setting.rotation_vector,
                                                     setting.translation_vector, camera_matrix, dist_coeffs)

    for p in image_points:
        cv2.circle(setting.frame, (int(p[0]), int(p[1])), 3, (0, 0, 255), -1)

    p1 = (int(image_points[0][0]), int(image_points[0][1]))
    p2 = (int(nose_end_point2D[0][0][0]), int(nose_end_point2D[0][0][1]))

    cv2.putText(setting.frame, "rotation: {}".format(setting.rotation_vector), (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.putText(setting.frame, "translation: {}".format(setting.translation_vector), (10, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.line(setting.frame, p1, p2, (255, 0, 0), 2)


def facedetection_background():
    # initialize dlib's face detector (HOG-based) and then create
    # the facial landmark predictor
    print("[INFO] loading facial landmark predictor...")
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    # grab the indexes of the facial landmarks

    print("[INFO] starting video stream thread...")
    setting.vs=VideoStream(src=1).start()
    time.sleep(1.0)

    while True:
        print(setting.TOTAL)
        setting.frame = setting.vs.read()
        setting.frame = imutils.resize(setting.frame, width=450)
        gray = cv2.cvtColor(setting.frame, cv2.COLOR_BGR2GRAY)
        # detect faces in the grayscale frame
        rects = detector(gray, 0)
        size = setting.frame.shape
        for rect in rects:
            eye_blinks_count(rect, gray, predictor)
            head_posture(rect, gray, predictor, size)


