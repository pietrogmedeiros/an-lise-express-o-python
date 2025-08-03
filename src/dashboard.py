import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import date, timedelta
from data_manager import DataManager
from analyzer import EmotionAnalyzer

def main():
    st.set_page_config(
        page_title="Análise de Emoções",
        page_icon="😊",
        layout="wide"
    )
    
    st.title("🎭 Dashboard de Análise Emocional")
    st.sidebar.title("Configurações")
    
    # Inicializar componentes
    data_manager = DataManager()
    analyzer = EmotionAnalyzer(data_manager)
    
    # Sidebar para seleção de período
    days_to_analyze = st.sidebar.slider("Dias para análise", 1, 30, 7)
    selected_date = st.sidebar.date_input("Data específica", date.today())
    
    # Métricas principais
    col1, col2, col3 = st.columns(3)
    
    # Dados do dia selecionado
    daily_data = data_manager.get_daily_emotions(selected_date)
    
    with col1:
        total_detections = len(daily_data)
        st.metric("Detecções Hoje", total_detections)
    
    with col2:
        if not daily_data.empty:
            dominant_emotion = daily_data['emotion'].mode().iloc[0]
            st.metric("Emoção Dominante", dominant_emotion)
        else:
            st.metric("Emoção Dominante", "N/A")
    
    with col3:
        if not daily_data.empty:
            avg_confidence = daily_data['confidence'].mean()
            st.metric("Confiança Média", f"{avg_confidence:.2f}")
        else:
            st.metric("Confiança Média", "N/A")
    
    # Relatório diário
    st.header("📊 Relatório Diário")
    daily_report = analyzer.generate_daily_report(selected_date)
    st.text(daily_report)
    
    # Gráficos
    st.header("📈 Visualizações")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico de pizza das emoções
        chart = analyzer.create_emotion_chart(days_to_analyze)
        if chart:
            st.plotly_chart(chart, use_container_width=True)
        else:
            st.info("Sem dados suficientes para gráfico")
    
    with col2:
        # Gráfico de linha temporal
        if not daily_data.empty:
            daily_data['timestamp'] = pd.to_datetime(daily_data['timestamp'])
            daily_data['hour'] = daily_data['timestamp'].dt.hour
            
            hourly_emotions = daily_data.groupby(['hour', 'emotion']).size().reset_index(name='count')
            
            fig = px.line(hourly_emotions, x='hour', y='count', color='emotion',
                         title='Emoções ao Longo do Dia')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Sem dados para o dia selecionado")
    
    # Tabela de dados brutos
    if st.checkbox("Mostrar dados brutos"):
        st.subheader("Dados Brutos")
        summary_data = data_manager.get_emotion_summary(days_to_analyze)
        st.dataframe(summary_data)

if __name__ == "__main__":
    main()