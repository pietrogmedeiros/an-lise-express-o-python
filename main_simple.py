#!/usr/bin/env python3
"""
Sistema de Análise de Expressões Faciais - Versão Simplificada
"""

import argparse
import sys
import os
import cv2

# Adicionar src ao path
sys.path.append('src')

from emotion_detector_minimal import MinimalEmotionDetector
from data_manager import DataManager
from analyzer_simple import SimpleEmotionAnalyzer

def main():
    parser = argparse.ArgumentParser(description='Sistema de Análise de Expressões Faciais')
    parser.add_argument('--mode', choices=['camera', 'report'], 
                       default='camera', help='Modo de execução')
    parser.add_argument('--days', type=int, default=7, 
                       help='Número de dias para análise')
    
    args = parser.parse_args()
    
    if args.mode == 'camera':
        print("🎥 Iniciando detecção de emoções...")
        print("Pressione 'q' para sair, 's' para salvar emoção")
        
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("❌ Câmera não acessível")
            return
        
        detector = MinimalEmotionDetector()
        data_manager = DataManager()
        
        emotion_counter = {}

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
                
                # Salvar emoção se detectada
                if emotions:
                    best_emotion = max(emotions, key=lambda x: x['confidence'])
                    data_manager.save_emotion(
                        best_emotion['emotion'], 
                        best_emotion['confidence']
                    )
                
                # Mostrar estatísticas
                cv2.putText(processed_frame, f"Faces detectadas: {len(emotions)}", 
                           (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                
                # Mostrar emoção mais comum
                if emotion_counter:
                    most_common = max(emotion_counter, key=emotion_counter.get)
                    cv2.putText(processed_frame, f"Mais comum: {most_common}", 
                               (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                
                cv2.putText(processed_frame, "Pressione 'q' para sair", 
                           (10, processed_frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                
                cv2.imshow('Detector de Emocoes', processed_frame)
                
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    break
                elif key == ord('s') and emotions:
                    print(f"💾 Emoção salva: {best_emotion['emotion']}")
            
        except KeyboardInterrupt:
            print("\n👋 Encerrando...")
        finally:
            cap.release()
            cv2.destroyAllWindows()
    
    elif args.mode == 'report':
        print(f"📊 Gerando relatório dos últimos {args.days} dias...")
        data_manager = DataManager()
        analyzer = SimpleEmotionAnalyzer(data_manager)
        
        report = analyzer.generate_daily_report()
        print(report)

if __name__ == "__main__":
    main()
