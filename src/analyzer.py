import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

class EmotionAnalyzer:
    def __init__(self, data_manager):
        self.data_manager = data_manager
        
    def generate_daily_report(self, target_date=None):
        df = self.data_manager.get_daily_emotions(target_date)
        
        if df.empty:
            return "Nenhuma emoção detectada hoje."
        
        # Análise das emoções do dia
        emotion_counts = df['emotion'].value_counts()
        dominant_emotion = emotion_counts.index[0]
        total_detections = len(df)
        
        # Calcular percentuais
        emotion_percentages = (emotion_counts / total_detections * 100).round(2)
        
        report = f"""
        📊 RELATÓRIO DIÁRIO DE EMOÇÕES - {target_date or datetime.now().date()}
        
        🎯 Emoção Dominante: {dominant_emotion} ({emotion_percentages[dominant_emotion]:.1f}%)
        📈 Total de Detecções: {total_detections}
        
        📋 Distribuição das Emoções:
        """
        
        for emotion, percentage in emotion_percentages.items():
            emoji = self._get_emotion_emoji(emotion)
            report += f"\n{emoji} {emotion}: {percentage:.1f}%"
        
        # Análise de tendências
        report += self._analyze_emotional_patterns(df)
        
        return report
    
    def _get_emotion_emoji(self, emotion):
        emoji_map = {
            'Feliz': '😊', 'Triste': '😢', 'Raiva': '😠',
            'Surpresa': '😲', 'Medo': '😨', 'Nojo': '🤢',
            'Neutro': '😐'
        }
        return emoji_map.get(emotion, '🤔')
    
    def _analyze_emotional_patterns(self, df):
        analysis = "\n\n🔍 ANÁLISE COMPORTAMENTAL:\n"
        
        # Análise por período do dia
        df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
        morning = df[df['hour'].between(6, 12)]
        afternoon = df[df['hour'].between(12, 18)]
        evening = df[df['hour'].between(18, 24)]
        
        periods = {
            'Manhã (6h-12h)': morning,
            'Tarde (12h-18h)': afternoon,
            'Noite (18h-24h)': evening
        }
        
        for period_name, period_df in periods.items():
            if not period_df.empty:
                dominant = period_df['emotion'].mode().iloc[0]
                analysis += f"\n• {period_name}: Predominantemente {dominant}"
        
        return analysis
    
    def create_emotion_chart(self, days=7):
        df = self.data_manager.get_emotion_summary(days)
        
        if df.empty:
            return None
        
        # Gráfico de pizza das emoções
        emotion_totals = df.groupby('emotion')['count'].sum()
        
        fig = px.pie(
            values=emotion_totals.values,
            names=emotion_totals.index,
            title=f'Distribuição de Emoções - Últimos {days} dias'
        )
        
        return fig