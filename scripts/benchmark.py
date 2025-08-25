import cv2
import time

def benchmark_camera(camera_index=0, num_frames=300):
    cap = cv2.VideoCapture(camera_index)
    
    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    
    start_time = time.time()
    
    for _ in range(num_frames):
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    fps = num_frames / elapsed_time
    
    print(f"Captured {num_frames} frames in {elapsed_time:.2f} seconds.")
    print(f"Estimated FPS: {fps:.2f}")
    
    cap.release()

if __name__ == "__main__":
    benchmark_camera()