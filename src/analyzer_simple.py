import pandas as pd
from datetime import datetime

class SimpleEmotionAnalyzer:
    def __init__(self, data_manager):
        self.data_manager = data_manager
        
    def generate_daily_report(self, target_date=None):
        df = self.data_manager.get_daily_emotions(target_date)
        
        if df.empty:
            return "📊 Nenhuma emoção detectada hoje."
        
        emotion_counts = df['emotion'].value_counts()
        dominant_emotion = emotion_counts.index[0]
        total_detections = len(df)
        
        emotion_percentages = (emotion_counts / total_detections * 100).round(2)
        
        report = f"""
📊 RELATÓRIO DIÁRIO - {target_date or datetime.now().date()}

🎯 Emoção Dominante: {dominant_emotion} ({emotion_percentages[dominant_emotion]:.1f}%)
📈 Total de Detecções: {total_detections}

📋 Distribuição das Emoções:
"""
        
        for emotion, percentage in emotion_percentages.items():
            emoji = self._get_emotion_emoji(emotion)
            report += f"\n{emoji} {emotion}: {percentage:.1f}%"
        
        return report
    
    def _get_emotion_emoji(self, emotion):
        emoji_map = {
            'Feliz': '😊', 'Triste': '😢', 'Raiva': '😠',
            'Surpresa': '😲', 'Medo': '😨', 'Nojo': '🤢',
            'Neutro': '😐'
        }
        return emoji_map.get(emotion, '🤔')