# Desafio: Identificação de ZCTAs com Potencial para Novos Laboratórios

## 📌 Objetivo

Este projeto tem como objetivo identificar os **ZCTAs** (códigos postais dos EUA) com maior **potencial econômico** para a instalação de novos laboratórios clínicos, utilizando dados demográficos, transacionais e geográficos.

A análise considera:
- População total por ZCTA
- Proporção de gênero
- Custo dos exames
- Localização de laboratórios já existentes

Ao final, o algoritmo recomenda os **3 melhores ZCTAs** para expansão.

---

## 📁 Estrutura do Projeto

```
├── data/
│   └── data.zip           # Arquivo compactado com os datasets
├── Desafio.ipynb          # Versão em notebook interativo (Jupyter)
├── main.py                # Script executável em Python
├── README.md              # Este arquivo
```

---

## ⚙️ Pré-requisitos

Antes de executar qualquer código, você deve:
1. Ter o Python 3.8+ instalado.
2. Instalar as dependências:
```bash
pip install pandas numpy matplotlib seaborn
```
3. **Descompactar o arquivo `data.zip` dentro da pasta `data/`** para que os scripts possam acessar os arquivos `.csv`.

---

## ▶️ Como Executar

### Opção 1: Usando o script `main.py`

Ideal para rodar diretamente em terminal ou ambientes de produção.

```bash
python main.py
```

A saída exibirá os **3 ZCTAs recomendados** para abertura de novos laboratórios.

---

### Opção 2: Usando o notebook `Desafio.ipynb`

Ideal para quem deseja ver os gráficos, análises passo a passo e interagir com os dados.

Basta abrir o notebook em um ambiente Jupyter (como JupyterLab, VSCode ou Google Colab) e executar as células em ordem.

---

## 🧠 Lógica de Negócio

1. **Limpeza dos dados**:
   - Conversão de tipos numéricos
   - Remoção de valores ausentes e outliers

2. **Cálculo do lucro por exame**

3. **Criação do Índice de Potencial Econômico**:
   \[
   \text{Índice} = \left( \frac{\text{População Total}}{\text{SexRatio}} \right) \times \text{Fator de Gênero}
   \]

4. **Filtragem de ZCTAs com laboratórios existentes**

5. **Rankeamento e recomendação final**

---

## 📬 Contato

Posso esclarecer as demais dúvidas na entrevista técnica. :)