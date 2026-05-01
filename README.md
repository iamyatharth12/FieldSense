# 🌱 FieldSense

**AI-powered crop diagnosis tool that turns plant images into actionable farming decisions.**

---

## 🚀 What It Does

FieldSense helps farmers quickly identify crop issues using a simple photo.

Upload an image → get:

* **Disease detection** (e.g., fungal infection, nutrient deficiency)
* **Actionable treatment steps**
* **Risk warnings**
* **Weather-based advice**

All in seconds.

---

## 🧠 Why It Matters

Farmers often rely on guesswork or delayed expert advice.

FieldSense reduces:

* crop loss
* decision delay
* uncertainty

by providing **instant, easy-to-understand guidance**.

---

## ⚙️ How It Works

* Image is uploaded through a simple web interface
* Backend processes the image
* System maps it to predefined agricultural scenarios
* Returns:

  * Disease
  * Action
  * Warning
* Weather API adds contextual advice

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS (mobile-first UI)
* **Backend:** FastAPI (Python)
* **Logic:** Rule-based + scenario mapping
* **Weather:** OpenWeather API

---

## 🖥️ How to Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/iamyatharth12/FieldSense.git
cd FieldSense/backend
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r ../requirements.txt
```

### 4. Run the server

```bash
uvicorn main:app --reload
```

### 5. Open in browser

```
http://127.0.0.1:8000
```

---

## 📱 Features

* 📸 Image-based crop analysis
* ⚡ Instant results
* 🌦️ Weather-aware recommendations
* 📱 Mobile-friendly interface
* 🧠 Clean, structured outputs

---

## ⚠️ Limitations

* Uses predefined scenarios (not full ML model)
* Accuracy depends on input image quality
* Not a replacement for expert agronomy advice

---

## 🔮 Future Improvements

* Real ML-based disease detection
* Offline support for rural areas
* Expanded crop and disease database
* Regional language support

---

## 👨‍💻 Built For

Grizzly Hacks III — solving real-world problems for farmers with simple, effective tech.

---

## 📌 Demo

[https://youtu.be/M3nYjSsp7EU](https://youtube.com/shorts/DuuiufAGqNs?feature=share)
---

## 🧬 Final Note

FieldSense focuses on **clarity over complexity** — helping farmers act faster, with confidence.
