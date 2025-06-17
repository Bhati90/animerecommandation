
# 🎬 Anime Recommendation System

A complete end-to-end Machine Learning pipeline for anime prediction — built with modular components, data versioning using DVC, containerized with Docker, and automated CI/CD via Jenkins.

---

## 📌 Features

- 🔁 End-to-end ML pipeline (training & inference)
- 📦 Data & model version control using **DVC**
- 🐳 Containerized with **Docker**
- 🔧 Automated CI/CD with **Jenkins**
- 🌐 Deployed via **Flask** web app
- 📊 Interactive notebook for EDA
- 🧠 Pretrained weights included

---

## 🧠 Tech Stack

| Category      | Tools |
|---------------|---------------------------|
| Programming   | Python |
| ML/EDA        | scikit-learn, pandas, numpy |
| Deployment    | Flask, Docker |
| MLOps         | DVC, Jenkins |
| Others        | Jupyter, Git, HTML/CSS |

---

## 📁 Project Structure

```

.
├── config/                   # Config files
├── custom\_jenkins/           # Jenkins scripts
├── notebook/anime.ipynb      # EDA Notebook
├── pipeline/                 # Training & prediction logic
├── src/                      # Core ML code
├── utils/                    # Utilities
├── static/, templates/       # Web UI (Flask)
├── weights/                  # Pretrained model
├── application.py            # Flask app entry point
├── Dockerfile                # Docker image setup
├── Jenkinsfile               # Jenkins CI/CD pipeline
├── requirements.txt          # Python dependencies
└── README.md                 # You are here

````

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/anime-recommendation.git
cd anime-recommendation
````

### 2. Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Pull Data and Model Files via DVC

```bash
dvc pull
```

### 4. Train the Model

```bash
python pipeline/training_pipeline.py
```

### 5. Launch the Web App

```bash
python application.py
```

Visit 👉 [http://localhost:5000](http://localhost:5000)

---

## 🐳 Run with Docker

```bash
docker build -t anime-recommender .
docker run -p 5000:5000 anime-recommender
```

---

## 🔁 Jenkins Integration

* CI/CD pipeline defined in `Jenkinsfile`
* Supports build/test/deploy on push
* Docker-based automation

---

## 📷 Screenshot

> *(Add a UI image here if you have one)*

---

## 🙋‍♂️ Author

**Kishan Bhati**
🔗 [GitHub](https://github.com/Bhati90) | 🌐 [LinkedIn](https://linkedin.com/in/kishan-bhati-565b66236/)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---


