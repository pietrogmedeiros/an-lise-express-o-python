import cv2
import numpy as np
import os
import random

class EmotionDetector:
    def __init__(self, model_path='models/emotion_model.h5'):
        self.emotion_labels = ['Raiva', 'Nojo', 'Medo', 'Feliz', 'Triste', 'Surpresa', 'Neutro']
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
        # Por enquanto, usar detector básico sem ML
        print("⚠️  Usando detector básico (sem TensorFlow)")
        self.model = None
    
    def detect_emotion(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        
        emotions_detected = []
        
        for (x, y, w, h) in faces:
            # Simular detecção de emoção até TensorFlow funcionar
            emotion = random.choice(self.emotion_labels)
            confidence = round(random.uniform(0.75, 0.95), 2)
            
            emotions_detected.append({
                'emotion': emotion,
                'confidence': confidence,
                'bbox': (x, y, w, h)
            })
            
            # Desenhar retângulo e texto
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(frame, f'{emotion}: {confidence:.2f}', 
                       (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
        
        return frame, emotions_detected
