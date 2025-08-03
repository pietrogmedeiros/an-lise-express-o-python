#!/usr/bin/env python3
"""
Sistema de Análise de Expressões Faciais com IA Local
"""

import argparse
import sys
import os
import cv2
import time
from datetime import datetime

# Adicionar src ao path
sys.path.append('src')

from emotion_detector_ai import AIEmotionDetector
from data_manager import DataManager
from analyzer_simple import SimpleEmotionAnalyzer

def main():
    parser = argparse.ArgumentParser(description='Sistema de IA para Análise de Expressões Faciais')
    parser.add_argument('--mode', choices=['camera', 'report'], 
                       default='camera', help='Modo de execução')
    parser.add_argument('--days', type=int, default=7, 
                       help='Número de dias para análise')
    
    args = parser.parse_args()
    
    if args.mode == 'camera':
        print("🤖 Iniciando detecção com IA local...")
        print("Pressione 'q' para sair, 's' para salvar, 'i' para info")
        
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("❌ Câmera não acessível")
            return
        
        detector = AIEmotionDetector()
        data_manager = DataManager()
        
        emotion_counter = {}
        last_save_time = time.time()
        save_interval = 3  # Salvar a cada 3 segundos

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
                
                # Salvar emoção automaticamente
                current_time = time.time()
                if emotions and (current_time - last_save_time) > save_interval:
                    best_emotion = max(emotions, key=lambda x: x['confidence'])
                    data_manager.save_emotion(
                        best_emotion['emotion'], 
                        best_emotion['confidence']
                    )
                    last_save_time = current_time
                    print(f"💾 Salvo: {best_emotion['emotion']} ({best_emotion['confidence']:.2f})")
                
                # Mostrar estatísticas na tela
                cv2.putText(processed_frame, f"🤖 IA: {'ON' if detector.ai_available else 'OFF'}", 
                           (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                cv2.putText(processed_frame, f"Faces: {len(emotions)}", 
                           (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                cv2.putText(processed_frame, datetime.now().strftime("%H:%M:%S"), 
                           (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                
                # Mostrar emoção mais comum
                if emotion_counter:
                    most_common = max(emotion_counter, key=emotion_counter.get)
                    cv2.putText(processed_frame, f"Mais comum: {most_common}", 
                               (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                
                cv2.imshow('🤖 Detector de Emocoes com IA', processed_frame)
                
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    break
                elif key == ord('s') and emotions:
                    # Salvar manualmente
                    best_emotion = max(emotions, key=lambda x: x['confidence'])
                    data_manager.save_emotion(
                        best_emotion['emotion'], 
                        best_emotion['confidence']
                    )
                    print(f"💾 Salvo manualmente: {best_emotion['emotion']}")
                elif key == ord('i'):
                    # Mostrar informações
                    print(f"\n📊 Estatísticas atuais:")
                    for emotion, count in emotion_counter.items():
                        print(f"   {emotion}: {count}")
                    print(f"🤖 IA ativa: {detector.ai_available}")
        
        except KeyboardInterrupt:
            print("\n👋 Encerrando...")
        finally:
            cap.release()
            cv2.destroyAllWindows()
    
    elif args.mode == 'report':
        print("📊 Gerando relatório...")
        analyzer = SimpleEmotionAnalyzer()
        analyzer.generate_report(args.days)

if __name__ == "__main__":
    main()