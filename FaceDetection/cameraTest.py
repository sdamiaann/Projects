import cv2

cap = cv2.VideoCapture(0)  # or change index if needed

if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    print("Camera opened successfully!")

    while True:
        ret, frame = cap.read()  # Capture frame-by-frame
        if not ret:
            print("Error: Failed to capture frame.")
            break

        cv2.imshow('Camera Feed', frame)  # Display the frame

        # Press 'q' to exit the camera window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()  # Release the camera
    cv2.destroyAllWindows()  # Close all OpenCV windows
