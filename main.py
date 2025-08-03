#!/usr/bin/env python3
"""
Sistema de Análise de Expressões Faciais
Detecta emoções através da câmera e gera relatórios de bem-estar
"""

import argparse
import sys
import os

# Adicionar src ao path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from camera_app import CameraApp
from data_manager import DataManager
from analyzer import EmotionAnalyzer

def main():
    parser = argparse.ArgumentParser(description='Sistema de Análise de Expressões Faciais')
    parser.add_argument('--mode', choices=['camera', 'dashboard', 'report'], 
                       default='camera', help='Modo de execução')
    parser.add_argument('--days', type=int, default=7, 
                       help='Número de dias para análise (modo report)')
    
    args = parser.parse_args()
    
    if args.mode == 'camera':
        print("🎥 Iniciando detecção de emoções...")
        print("Pressione 'q' para sair, 's' para salvar emoção manualmente")
        app = CameraApp()
        try:
            app.start_detection()
        except KeyboardInterrupt:
            print("\n👋 Encerrando aplicação...")
            app.stop_detection()
    
    elif args.mode == 'dashboard':
        print("🚀 Iniciando dashboard...")
        print("Acesse: http://localhost:8501")
        os.system("streamlit run src/dashboard.py")
    
    elif args.mode == 'report':
        print(f"📊 Gerando relatório dos últimos {args.days} dias...")
        data_manager = DataManager()
        analyzer = EmotionAnalyzer(data_manager)
        
        report = analyzer.generate_daily_report()
        print(report)
        
        # Salvar relatório em arquivo
        with open(f'relatorio_{args.days}dias.txt', 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"\n💾 Relatório salvo em: relatorio_{args.days}dias.txt")

if __name__ == "__main__":
    main()