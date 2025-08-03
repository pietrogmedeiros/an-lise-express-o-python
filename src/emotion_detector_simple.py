import cv2
import numpy as np

class SimpleEmotionDetector:
    def __init__(self):
        self.emotion_labels = ['Neutro', 'Feliz', 'Triste', 'Surpresa', 'Raiva']
        try:
            self.face_cascade = cv2.CascadeClassifier(
                cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
            )
            print("✅ Detector facial carregado com sucesso")
        except Exception as e:
            print(f"❌ Erro ao carregar detector: {e}")
    
    def detect_faces_only(self, frame):
        """Versão simplificada que apenas detecta rostos"""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        
        emotions_detected = []
        
        for (x, y, w, h) in faces:
            # Por enquanto, retorna emoção aleatória para teste
            emotion = np.random.choice(self.emotion_labels)
            confidence = np.random.uniform(0.7, 0.95)
            
            emotions_detected.append({
                'emotion': emotion,
                'confidence': confidence,
                'bbox': (x, y, w, h)
            })
            
            # Desenhar retângulo e texto
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, f'{emotion}: {confidence:.2f}', 
                       (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        return frame, emotions_detected