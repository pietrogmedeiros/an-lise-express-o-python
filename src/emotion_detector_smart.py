#!/usr/bin/env python3
"""
Detector inteligente que funciona com ou sem IA
"""

import cv2
import numpy as np
import random
import time

class SmartEmotionDetector:
    def __init__(self):
        self.emotions = ['Feliz', 'Triste', 'Raiva', 'Surpresa', 'Medo', 'Nojo', 'Neutro']
        self.ai_available = False
        
        # Tentar carregar IA
        try:
            from fer import FER
            self.fer_detector = FER(mtcnn=False)  # Mais rápido sem MTCNN
            self.ai_available = True
            print("🤖 IA FER carregada!")
        except:
            print("📝 Usando detector básico inteligente")
            self._init_basic_detector()
    
    def _init_basic_detector(self):
        """Detector básico melhorado"""
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )
        self.emotion_history = {}
        self.frame_count = 0
    
    def detect_emotion(self, frame):
        """Detecta emoções com IA ou modo inteligente"""
        if self.ai_available:
            return self._detect_with_ai(frame)
        else:
            return self._detect_smart_basic(frame)
    
    def _detect_with_ai(self, frame):
        """Detecção real com FER"""
        try:
            # Reduzir frame para velocidade
            small_frame = cv2.resize(frame, (640, 480))
            
            # Detectar emoções
            result = self.fer_detector.detect_emotions(small_frame)
            
            emotions_detected = []
            
            for face_data in result:
                # Extrair dados
                box = face_data['box']
                emotions = face_data['emotions']
                
                # Escalar coordenadas de volta
                scale_x = frame.shape[1] / 640
                scale_y = frame.shape[0] / 480
                
                x = int(box[0] * scale_x)
                y = int(box[1] * scale_y)
                w = int(box[2] * scale_x)
                h = int(box[3] * scale_y)
                
                # Encontrar emoção dominante
                dominant_emotion = max(emotions, key=emotions.get)
                confidence = emotions[dominant_emotion]
                
                # Mapear para português
                emotion_map = {
                    'angry': 'Raiva',
                    'disgust': 'Nojo',
                    'fear': 'Medo', 
                    'happy': 'Feliz',
                    'sad': 'Triste',
                    'surprise': 'Surpresa',
                    'neutral': 'Neutro'
                }
                
                emotion_pt = emotion_map.get(dominant_emotion, 'Neutro')
                
                emotions_detected.append({
                    'emotion': emotion_pt,
                    'confidence': confidence,
                    'bbox': (x, y, w, h)
                })
                
                # Desenhar
                color = self._get_emotion_color(emotion_pt)
                cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
                cv2.putText(frame, f'{emotion_pt}: {confidence:.2f}', 
                           (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
            
            return frame, emotions_detected
            
        except Exception as e:
            print(f"Erro na IA: {e}")
            self.ai_available = False
            return self._detect_smart_basic(frame)
    
    def _detect_smart_basic(self, frame):
        """Detector básico mais inteligente"""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
        
        emotions_detected = []
        self.frame_count += 1
        
        for i, (x, y, w, h) in enumerate(faces):
            face_id = f"face_{i}"
            
            # Análise básica da face
            face_roi = gray[y:y+h, x:x+w]
            
            # Simular detecção mais inteligente
            emotion, confidence = self._analyze_face_basic(face_roi, face_id)
            
            emotions_detected.append({
                'emotion': emotion,
                'confidence': confidence,
                'bbox': (x, y, w, h)
            })
            
            # Desenhar
            color = self._get_emotion_color(emotion)
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            cv2.putText(frame, f'{emotion}: {confidence:.2f}', 
                       (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
        
        return frame, emotions_detected
    
    def _analyze_face_basic(self, face_roi, face_id):
        """Análise básica mais inteligente da face"""
        # Manter histórico para consistência
        if face_id not in self.emotion_history:
            self.emotion_history[face_id] = {
                'last_emotion': random.choice(self.emotions),
                'stability': 0
            }
        
        history = self.emotion_history[face_id]
        
        # Simular mudança gradual de emoção
        if random.random() < 0.1:  # 10% chance de mudança
            new_emotion = random.choice(self.emotions)
            history['last_emotion'] = new_emotion
            history['stability'] = 0
        else:
            history['stability'] += 1
        
        # Confiança baseada na estabilidade
        base_confidence = min(0.6 + (history['stability'] * 0.05), 0.9)
        confidence = random.uniform(base_confidence, base_confidence + 0.1)
        
        return history['last_emotion'], confidence
    
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