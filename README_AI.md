# 🤖 Sistema de IA Local para Detecção de Emoções

## 🚀 Instalação da IA Gratuita

```bash
# 1. Instalar IA local
python3 install_ai.py

# 2. Testar sistema
python3 main_ai.py --mode camera
```

## 🎯 Funcionalidades da IA

- **FER (Facial Expression Recognition)** - IA gratuita e local
- **7 emoções detectadas**: Raiva, Nojo, Medo, Feliz, Triste, Surpresa, Neutro
- **Confiança real** baseada em análise facial
- **Fallback automático** para modo básico se IA falhar

## 🎮 Controles

- **'q'** - Sair
- **'s'** - Salvar emoção manualmente  
- **'i'** - Mostrar estatísticas

## 🔧 Vantagens da IA Local

- ✅ **Gratuita** - sem custos de API
- ✅ **Privacidade** - dados não saem do computador
- ✅ **Offline** - funciona sem internet
- ✅ **Rápida** - processamento local
- ✅ **Precisa** - detecção real de emoções

## 📊 Comparação

| Modo | Precisão | Velocidade | Privacidade |
|------|----------|------------|-------------|
| Básico | 🟡 Simulado | 🟢 Rápido | 🟢 Total |
| IA Local | 🟢 Real | 🟢 Rápido | 🟢 Total |
| IA Cloud | 🟢 Real | 🟡 Médio | 🔴 Limitada |

## 🛠️ Solução de Problemas

**Erro na instalação do FER:**
```bash
pip3 install --upgrade pip
pip3 install fer
```

**IA muito lenta:**
- Use `mtcnn=False` para velocidade
- Reduza resolução da câmera

**Detecção imprecisa:**
- Melhore iluminação
- Posicione-se de frente para câmera
- Evite óculos escuros