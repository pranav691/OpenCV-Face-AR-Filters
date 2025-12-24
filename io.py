import cv2
import numpy as np
import mediapipe as mp
import os

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)
cap = cv2.VideoCapture(0)

MODE_HAT = "hat"
MODE_GLASSES = "glasses"
MODE_MOUSTACHE = "moustache"
current_mode = MODE_HAT

def load_folder_images(path):
    images = []
    for file in sorted(os.listdir(path)):
        if file.lower().endswith(".png"):
            img = cv2.imread(os.path.join(path, file), cv2.IMREAD_UNCHANGED)
            images.append(img)
    return images

hats = load_folder_images("Resources/hats")
glasses = load_folder_images("Resources/glasses")
moustaches = load_folder_images("Resources/moustache")

hat_index = 0
glasses_index = 0
moustache_index = 0
prev_points = {}

def smooth_point(name, new, alpha=0.7):
    if name not in prev_points:
        prev_points[name] = new
        return new
    old = prev_points[name]
    smoothed = (int(alpha * old[0] + (1 - alpha) * new[0]), int(alpha * old[1] + (1 - alpha) * new[1]))
    prev_points[name] = smoothed
    return smoothed

def overlay_png(frame, png, x, y, w, h, angle=0):
    png = cv2.resize(png, (w, h), interpolation=cv2.INTER_AREA)
    if angle != 0:
        center = (w // 2, h // 2)
        mat = cv2.getRotationMatrix2D(center, angle, 1.0)
        png = cv2.warpAffine(png, mat, (w, h), flags=cv2.INTER_AREA)
    if png.shape[2] == 4:
        alpha = png[:, :, 3] / 255.0
        rgb = png[:, :, :3]
    else:
        alpha = np.ones((h, w))
        rgb = png
    if y < 0 or x < 0 or y + h > frame.shape[0] or x + w > frame.shape[1]:
        return frame
    roi = frame[y:y + h, x:x + w]
    for c in range(3):
        roi[:, :, c] = roi[:, :, c] * (1 - alpha) + rgb[:, :, c] * alpha
    frame[y:y + h, x:x + w] = roi
    return frame

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    hframe, wframe = frame.shape[:2]
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        for face in results.multi_face_landmarks:
            lm = face.landmark
            f = smooth_point("f", (int(lm[10].x * wframe), int(lm[10].y * hframe)))
            c = smooth_point("c", (int(lm[152].x * wframe), int(lm[152].y * hframe)))
            l = smooth_point("l", (int(lm[234].x * wframe), int(lm[234].y * hframe)))
            r = smooth_point("r", (int(lm[454].x * wframe), int(lm[454].y * hframe)))
            face_height = abs(c[1] - f[1])
            face_width = abs(r[0] - l[0])
            angle = np.degrees(np.arctan2(r[1] - l[1], r[0] - l[0]))

            if current_mode == MODE_HAT:
                img = hats[hat_index]
                w = int(face_width * 1.3)
                h = int(face_height * 1.2)
                x = int(f[0] - w // 2)
                y = int(f[1] - h * 0.7)
                frame = overlay_png(frame, img, x, y, w, h, angle)

            elif current_mode == MODE_GLASSES:
                img = glasses[glasses_index]
                w = int(face_width * 1.3)
                h = int(face_height * 0.4)
                ey = int((f[1] + c[1]) / 2)
                x = int((l[0] + r[0]) / 2 - w // 2)
                y = int(ey - h // 2)
                frame = overlay_png(frame, img, x, y, w, h, angle)

            elif current_mode == MODE_MOUSTACHE:
                img = moustaches[moustache_index]
                w = int(face_width * 0.9)
                h = int(face_height * 0.25)
                my = int(c[1] - face_height * 0.55)
                x = int((l[0] + r[0]) / 2 - w // 2)
                y = int(my)
                frame = overlay_png(frame, img, x, y, w, h, angle)

    cv2.imshow("Advanced AR Filter", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == 27:
        break
    if key == ord('1'):
        current_mode = MODE_HAT
    if key == ord('2'):
        current_mode = MODE_GLASSES
    if key == ord('3'):
        current_mode = MODE_MOUSTACHE
    if key == ord('h'):
        hat_index = (hat_index + 1) % len(hats)
    if key == ord('g'):
        glasses_index = (glasses_index + 1) % len(glasses)
    if key == ord('m'):
        moustache_index = (moustache_index + 1) % len(moustaches)

cap.release()
cv2.destroyAllWindows()
