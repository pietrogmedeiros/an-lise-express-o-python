import cv2
import numpy as np

class MinimalEmotionDetector:
    def __init__(self):
        # Usar detector de faces do OpenCV
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
        # Emoções básicas (simuladas por enquanto)
        self.emotions = ['Neutro', 'Feliz', 'Triste', 'Surpresa', 'Raiva', 'Medo', 'Nojo']
    
    def detect_emotion(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
        
        emotions_detected = []
        
        for (x, y, w, h) in faces:
            # Melhorar a detecção baseada no tamanho da face
            face_area = w * h
            
            # Faces maiores = mais confiança
            base_confidence = 0.7 if face_area > 10000 else 0.6
            
            # Simular emoção com base na posição (temporário)
            import random
            emotion = random.choice(self.emotions)
            confidence = random.uniform(base_confidence, 0.95)
            
            # Cores diferentes para cada emoção
            color = self._get_emotion_color(emotion)
            
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            cv2.putText(frame, f"{emotion} ({confidence:.2f})", 
                       (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
            
            emotions_detected.append({
                'emotion': emotion,
                'confidence': confidence,
                'bbox': (x, y, w, h)
            })
        
        return frame, emotions_detected

    def _get_emotion_color(self, emotion):
        colors = {
            'Feliz': (0, 255, 0),      # Verde
            'Triste': (255, 0, 0),     # Azul
            'Raiva': (0, 0, 255),      # Vermelho
            'Surpresa': (0, 255, 255), # Amarelo
            'Medo': (128, 0, 128),     # Roxo
            'Nojo': (0, 128, 128),     # Marrom
            'Neutro': (128, 128, 128)  # Cinza
        }
        return colors.get(emotion, (255, 255, 255))
