import imprev
import cv2
import os

SHOW_VID = False

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)

    while(cv2.waitKey(1) & 0xFF != ord('q')):
        # Get screensize for reduction
        size = os.get_terminal_size()

        # Get image data
        ret, frame = cap.read()

        out_string = imprev.prev(frame, size)
        print(out_string)

        if SHOW_VID:
                    cv2.imshow('frame', frame)

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()