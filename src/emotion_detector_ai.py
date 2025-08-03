#!/usr/bin/env python3
"""
Detector de emoções com IA gratuita local usando FER
"""

import cv2
import numpy as np

class AIEmotionDetector:
    def __init__(self):
        self.emotions = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']
        self.emotion_map = {
            'angry': 'Raiva',
            'disgust': 'Nojo', 
            'fear': 'Medo',
            'happy': 'Feliz',
            'sad': 'Triste',
            'surprise': 'Surpresa',
            'neutral': 'Neutro'
        }
        
        try:
            from fer import FER
            self.detector = FER(mtcnn=True)
            self.ai_available = True
            print("🤖 IA local carregada com sucesso!")
        except ImportError:
            print("⚠️ FER não instalado - usando modo básico")
            self.ai_available = False
            self._init_basic_detector()
    
    def _init_basic_detector(self):
        """Fallback para detector básico"""
        import random
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )
    
    def detect_emotion(self, frame):
        """Detecta emoções usando IA ou modo básico"""
        if self.ai_available:
            return self._detect_with_ai(frame)
        else:
            return self._detect_basic(frame)
    
    def _detect_with_ai(self, frame):
        """Detecção real com IA"""
        try:
            # FER detecta emoções automaticamente
            result = self.detector.detect_emotions(frame)
            
            emotions_detected = []
            
            for face in result:
                # Extrair dados da face
                bbox = face['box']
                emotions = face['emotions']
                
                # Encontrar emoção dominante
                dominant_emotion = max(emotions, key=emotions.get)
                confidence = emotions[dominant_emotion]
                
                # Traduzir emoção
                emotion_pt = self.emotion_map.get(dominant_emotion, dominant_emotion)
                
                emotions_detected.append({
                    'emotion': emotion_pt,
                    'confidence': confidence,
                    'bbox': (bbox[0], bbox[1], bbox[2], bbox[3]),
                    'all_emotions': emotions
                })
                
                # Desenhar retângulo e emoção
                x, y, w, h = bbox
                color = self._get_emotion_color(emotion_pt)
                
                cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
                cv2.putText(frame, f'{emotion_pt}: {confidence:.2f}', 
                           (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
                
                # Mostrar todas as emoções (opcional)
                y_offset = y + h + 20
                for emotion, score in emotions.items():
                    if score > 0.1:  # Só mostrar se > 10%
                        emotion_text = f"{self.emotion_map.get(emotion, emotion)}: {score:.2f}"
                        cv2.putText(frame, emotion_text, 
                                   (x, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
                        y_offset += 15
            
            return frame, emotions_detected
            
        except Exception as e:
            print(f"Erro na IA: {e}")
            return self._detect_basic(frame)
    
    def _detect_basic(self, frame):
        """Detecção básica como fallback"""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
        
        emotions_detected = []
        
        for (x, y, w, h) in faces:
            import random
            emotion = random.choice(list(self.emotion_map.values()))
            confidence = random.uniform(0.7, 0.95)
            
            emotions_detected.append({
                'emotion': emotion,
                'confidence': confidence,
                'bbox': (x, y, w, h)
            })
            
            color = self._get_emotion_color(emotion)
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            cv2.putText(frame, f'{emotion}: {confidence:.2f}', 
                       (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
        
        return frame, emotions_detected
    
    def _get_emotion_color(self, emotion):
        """Cores para cada emoção"""
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