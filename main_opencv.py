#!/usr/bin/env python3
"""
Sistema de detecção usando apenas OpenCV - 100% funcional
"""

import argparse
import sys
import os
import cv2
import time
from datetime import datetime

# Adicionar src ao path
sys.path.append('src')

from emotion_detector_opencv import OpenCVEmotionDetector
from data_manager import DataManager

def main():
    parser = argparse.ArgumentParser(description='Detector OpenCV de Emoções')
    parser.add_argument('--mode', choices=['camera', 'report'], 
                       default='camera', help='Modo de execução')
    
    args = parser.parse_args()
    
    if args.mode == 'camera':
        print("🎯 Iniciando detector OpenCV...")
        
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("❌ Câmera não acessível")
            return
        
        detector = OpenCVEmotionDetector()
        data_manager = DataManager()
        
        emotion_counter = {}
        last_save_time = time.time()
        save_interval = 3

        print("🎮 Controles: 'q'=sair, 's'=salvar, 'i'=info, 'r'=reset")

        try:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                
                processed_frame, emotions = detector.detect_emotion(frame)
                
                # Contar emoções
                for emotion_data in emotions:
                    emotion = emotion_data['emotion']
                    emotion_counter[emotion] = emotion_counter.get(emotion, 0) + 1
                
                # Salvar automaticamente
                current_time = time.time()
                if emotions and (current_time - last_save_time) > save_interval:
                    best_emotion = max(emotions, key=lambda x: x['confidence'])
                    data_manager.save_emotion(
                        best_emotion['emotion'], 
                        best_emotion['confidence']
                    )
                    last_save_time = current_time
                    print(f"💾 {best_emotion['emotion']} ({best_emotion['confidence']:.2f})")
                
                # Interface
                cv2.putText(processed_frame, "🎯 OpenCV Detector", 
                           (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                cv2.putText(processed_frame, f"Faces: {len(emotions)}", 
                           (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                cv2.putText(processed_frame, datetime.now().strftime("%H:%M:%S"), 
                           (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                
                if emotion_counter:
                    most_common = max(emotion_counter, key=emotion_counter.get)
                    cv2.putText(processed_frame, f"Dominante: {most_common}", 
                               (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                
                cv2.imshow('🎯 Detector OpenCV', processed_frame)
                
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    break
                elif key == ord('s') and emotions:
                    best_emotion = max(emotions, key=lambda x: x['confidence'])
                    data_manager.save_emotion(best_emotion['emotion'], best_emotion['confidence'])
                    print(f"💾 Salvo: {best_emotion['emotion']}")
                elif key == ord('i'):
                    print(f"\n📊 Estatísticas:")
                    for emotion, count in emotion_counter.items():
                        print(f"   {emotion}: {count}")
                elif key == ord('r'):
                    emotion_counter.clear()
                    detector.face_tracker.clear()
                    print("🔄 Estatísticas resetadas")
        
        except KeyboardInterrupt:
            print("\n👋 Encerrando...")
        finally:
            cap.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    main()