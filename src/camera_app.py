import cv2
import threading
import time
from datetime import datetime
from emotion_detector import EmotionDetector
from data_manager import DataManager

class CameraApp:
    def __init__(self):
        self.detector = EmotionDetector()
        self.data_manager = DataManager()
        self.is_running = False
        self.last_save_time = time.time()
        self.save_interval = 5  # Salvar a cada 5 segundos
        
    def start_detection(self):
        self.is_running = True
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("Erro: Não foi possível acessar a câmera")
            return
        
        print("Pressione 'q' para sair, 's' para salvar manualmente")
        
        while self.is_running:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Detectar emoções
            processed_frame, emotions = self.detector.detect_emotion(frame)
            
            # Salvar emoções automaticamente
            current_time = time.time()
            if emotions and (current_time - self.last_save_time) > self.save_interval:
                # Pegar a emoção com maior confiança
                best_emotion = max(emotions, key=lambda x: x['confidence'])
                self.data_manager.save_emotion(
                    best_emotion['emotion'], 
                    best_emotion['confidence']
                )
                self.last_save_time = current_time
                print(f"Emoção salva: {best_emotion['emotion']} ({best_emotion['confidence']:.2f})")
            
            # Mostrar informações na tela
            cv2.putText(processed_frame, f"Deteccoes: {len(emotions)}", 
                       (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(processed_frame, datetime.now().strftime("%H:%M:%S"), 
                       (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            cv2.imshow('Detector de Emocoes', processed_frame)
            
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('s') and emotions:
                # Salvar manualmente
                best_emotion = max(emotions, key=lambda x: x['confidence'])
                self.data_manager.save_emotion(
                    best_emotion['emotion'], 
                    best_emotion['confidence']
                )
                print(f"Emoção salva manualmente: {best_emotion['emotion']}")
        
        cap.release()
        cv2.destroyAllWindows()
        self.is_running = False
    
    def stop_detection(self):
        self.is_running = False