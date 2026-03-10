from google.cloud import vision

def analyze_image(image_path):
    client = vision.ImageAnnotatorClient()

    with open(image_path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    face_response = client.face_detection(image=image)
    label_response = client.label_detection(image=image)
    object_response = client.object_localization(image=image)

    faces = face_response.face_annotations
    labels = label_response.label_annotations
    objects = object_response.localized_object_annotations

    return {
        "faces": faces,
        "labels": labels,
        "objects": objects
    }