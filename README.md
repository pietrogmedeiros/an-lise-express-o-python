# 😊 Sistema Simples de Detecção de Expressões Faciais

Sistema **ultra-simples** para detectar faces e simular emoções em tempo real, sem complexidades de IA.

## ✨ Características

- ✅ **100% Funcional** - usa apenas OpenCV nativo
- ✅ **Zero Dependências Complexas** - sem TensorFlow, sem problemas
- ✅ **Instalação Simples** - apenas `pip3 install opencv-python`
- ✅ **Interface Completa** - estatísticas em tempo real
- ✅ **Multiplataforma** - funciona em macOS, Linux, Windows

## 🚀 Instalação Rápida

```bash
# 1. Clonar repositório
git clone <seu-repo>
cd projeto-reacoes-faciais

# 2. Instalar OpenCV (única dependência)
pip3 install opencv-python --user

# 3. Executar detector
python3 detector_simples.py
```

## 🎮 Como Usar

### Detector em Tempo Real
```bash
python3 run_simple.py
```

**Controles:**
- **'q'** - Sair do programa
- Posicione-se de frente para a câmera
- Veja as emoções sendo detectadas!

### Configuração Automática
```bash
python3 run_simple.py
```
Este script instala automaticamente o OpenCV e executa o detector.

## 🎯 O Que Faz

1. **Detecção de Faces**: Usa algoritmos do OpenCV para encontrar faces
2. **Simulação de Emoções**: Atribui emoções consistentes para cada face
3. **Interface Visual**: Mostra retângulos coloridos e emoções
4. **Estatísticas**: Conta emoções e mostra resumo final

## 😊 Emoções Detectadas

- 😊 **Feliz** (Verde)
- 😐 **Neutro** (Cinza)  
- 🤔 **Pensativo** (Laranja)
- 😮 **Surpreso** (Amarelo)

## 📁 Estrutura do Projeto

```
projeto-reacoes-faciais/
├── detector_simples.py     # Detector principal (EXECUTE ESTE!)
├── run_simple.py          # Configuração automática
├── instalar_opencv.py     # Instalador do OpenCV
├── README.md              # Este arquivo
└── docs/                  # Documentação adicional
    ├── COMO_EXECUTAR.txt  # Guia detalhado
    └── README_AI.md       # Versão com IA (descontinuada)
```

## 🔧 Solução de Problemas

**Erro: "ModuleNotFoundError: No module named 'cv2'"**
```bash
pip3 install opencv-python --user
```

**Erro: "Câmera não acessível"**
- Feche outras aplicações que usam câmera (Zoom, Teams, etc.)
- Verifique permissões do macOS: Sistema > Privacidade > Câmera

**Erro: Ambiente virtual conflitando**
```bash
deactivate  # Sair do ambiente virtual
python3 detector_simples.py  # Executar no sistema
```

## 📊 Exemplo de Saída

```
😊 Detector Ultra-Simples
==============================
✅ OpenCV 4.8.1 OK
✅ Câmera OK

🎮 Pressione 'q' para sair
🎥 Iniciando...

[Janela da câmera abre mostrando faces detectadas]

📊 Estatísticas:
   Total faces detectadas: 127
   Tempo total: 45s
   Emoções:
     😊 Feliz: 45 (35.4%)
     😐 Neutro: 38 (29.9%)
     🤔 Pensativo: 32 (25.2%)
     😮 Surpreso: 12 (9.4%)

✅ Detector encerrado!
```

## 🎯 Por Que Esta Versão?

- **Funciona Sempre**: Sem dependências problemáticas
- **Rápida**: Instalação em segundos
- **Educativa**: Código simples e claro
- **Extensível**: Base sólida para melhorias futuras

## 🔮 Próximas Versões

- [ ] Salvar dados em arquivo
- [ ] Gráficos das estatísticas
- [ ] Detecção real de emoções com IA
- [ ] Dashboard web
- [ ] Análise de padrões temporais

## 📞 Suporte

Se encontrar problemas:
1. Execute `python3 run_simple.py` para configuração automática
2. Verifique se a câmera não está sendo usada por outra aplicação
3. OpenCV é a única dependência necessária

## 🎉 Divirta-se Explorando!

Este projeto é perfeito para:
- Aprender detecção de faces
- Entender OpenCV básico
- Base para projetos de visão computacional
- Demonstrações rápidas e funcionais

---

**Versão Atual**: 2.0 - Ultra-Simples  
**Compatibilidade**: Python 3.6+, OpenCV 4.0+  

## 👨‍💻 Autor

-   **Pietro Medeiros**
-   **LinkedIn:** [Meu Linkedin](https://www.linkedin.com/in/pietro-medeiros-770bba162/)

