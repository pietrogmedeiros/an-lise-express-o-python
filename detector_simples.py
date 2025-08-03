#!/usr/bin/env python3
"""
Detector ultra-simples - SEM dependências complexas
"""

def main():
    print("😊 Detector Ultra-Simples")
    print("=" * 30)
    
    # Testar OpenCV
    try:
        import cv2
        print(f"✅ OpenCV {cv2.__version__} OK")
    except ImportError:
        print("❌ OpenCV não encontrado")
        print("💡 Execute: pip3 install opencv-python --user")
        return
    
    import random
    import time
    
    # Testar câmera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Câmera não acessível")
        return
    
    print("✅ Câmera OK")
    
    # Detector de faces
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )
    
    # Emoções e cores
    emotions = ['😊 Feliz', '😐 Neutro', '🤔 Pensativo', '😮 Surpreso']
    colors = [(0, 255, 0), (128, 128, 128), (255, 128, 0), (0, 255, 255)]
    
    # Contadores
    emotion_count = {}
    total_faces = 0
    start_time = time.time()
    
    print("\n🎮 Pressione 'q' para sair")
    print("🎥 Iniciando...")
    
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Detectar faces
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            
            # Processar faces
            for (x, y, w, h) in faces:
                # Emoção aleatória mas consistente
                emotion_idx = (x + y) % len(emotions)
                emotion = emotions[emotion_idx]
                color = colors[emotion_idx]
                
                # Contar
                emotion_count[emotion] = emotion_count.get(emotion, 0) + 1
                total_faces += 1
                
                # Desenhar
                cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
                cv2.putText(frame, emotion, (x, y-10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
            
            # Info na tela
            runtime = int(time.time() - start_time)
            cv2.putText(frame, f"Faces: {len(faces)}", 
                       (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(frame, f"Total: {total_faces}", 
                       (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(frame, f"Tempo: {runtime}s", 
                       (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            
            # Mostrar
            cv2.imshow('😊 Detector Simples - Pressione Q para sair', frame)
            
            # Sair com 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    
    except KeyboardInterrupt:
        print("\n👋 Interrompido")
    
    finally:
        cap.release()
        cv2.destroyAllWindows()
        
        # Estatísticas finais
        if total_faces > 0:
            print(f"\n📊 Estatísticas:")
            print(f"   Total faces detectadas: {total_faces}")
            print(f"   Tempo total: {int(time.time() - start_time)}s")
            print(f"   Emoções:")
            for emotion, count in emotion_count.items():
                pct = count / total_faces * 100
                print(f"     {emotion}: {count} ({pct:.1f}%)")
        
        print("\n✅ Detector encerrado!")

if __name__ == "__main__":
    main()
