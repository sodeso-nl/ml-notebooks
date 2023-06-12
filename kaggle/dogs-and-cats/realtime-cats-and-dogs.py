import cv2
import sys

sys.path.append("../../ext")

import ext.ml_layer as mll
import ext.ml_data as mld
import ext.ml_internal as mlint
import numpy as np

BASE_MODEL_NAME = "efficientnetv2b3"
model = mll.load_model_alt(directory=f"./models/{BASE_MODEL_NAME}", name="cats_dogs_2nd_pass_categorical", format="h5")

class_names = ["cat", "dog"]

# noinspection PyUnresolvedReferences
cam = cv2.VideoCapture(0)

# noinspection PyUnresolvedReferences
cv2.namedWindow("test")

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break

    # noinspection PyUnresolvedReferences
    img = cv2.resize(frame, dsize=(224, 224), interpolation = cv2.INTER_CUBIC)

    # noinspection PyUnresolvedReferences
    cv2.imshow("test", img)

    # noinspection PyUnresolvedReferences
    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    else:
        # SPACE pressed
        img_data = np.asarray(img)
        y = model.predict(x=mld.add_batch_to_tensor(img), verbose=0)
        if y[0] > 0.95:
            sparse_y = mlint.sparse_labels(y)
            print(f"Pred {y[0]}: {class_names[sparse_y[0]]}")

cam.release()

# noinspection PyUnresolvedReferences
cv2.destroyAllWindows()