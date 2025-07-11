from ultralytics import YOLO
import cv2

# ────────────────────────────────────────────────────────────────
# Configuration
# ────────────────────────────────────────────────────────────────
MODEL_PATH     = "yolov8m.pt"  # or "yolov8n.pt", "best.pt"
CONF_THRES     = 0.25          # Minimum confidence
TARGET_CLASSES = ["person", "laptop", "bottle", "cell phone", "keyboard", "mouse", "book", "chair", "remote"]

# ────────────────────────────────────────────────────────────────
# Load model
# ────────────────────────────────────────────────────────────────
model = YOLO(MODEL_PATH)
print(f"[EVA] YOLOv8 model loaded: {MODEL_PATH}")

# ────────────────────────────────────────────────────────────────
# Object Detection Function
# ────────────────────────────────────────────────────────────────
def detect_objects():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return {"status": "error", "message": "Webcam not accessible"}

    success, frame = cap.read()
    if not success:
        cap.release()
        return {"status": "error", "message": "Failed to capture frame"}

    # Run YOLO detection
    results = model(frame, stream=False, verbose=False)[0]
    detections = []

    if results.boxes is not None and len(results.boxes) > 0:
        for box in results.boxes:
            cls_id  = int(box.cls[0])
            conf    = float(box.conf[0])
            label   = model.names[cls_id]

            if conf < CONF_THRES:
                continue
            if label not in TARGET_CLASSES:
                continue

            detections.append({
                "object": label,
                "confidence": round(conf, 2)
            })

    cap.release()

    # Sort by confidence
    detections.sort(key=lambda x: x["confidence"], reverse=True)

    return {
        "status": "success",
        "frame_shape": frame.shape,
        "detections": detections,
        "detected_count": len(detections)
    }

# ────────────────────────────────────────────────────────────────
# Camera Test Function
# ────────────────────────────────────────────────────────────────
def test_camera():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return {"status": "error", "message": "Webcam not accessible"}

    success, frame = cap.read()
    cap.release()

    if not success:
        return {"status": "error", "message": "Failed to capture frame"}

    return {
        "status": "success",
        "message": "Camera is working ✅",
        "frame_shape": frame.shape
    }
