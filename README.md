

# Crop Yield Prediction 🍵🌱🫖

A machine learning-powered web app for predicting crop yields, built with Python and Streamlit. Instantly estimate the yield of your crops based on input features like rainfall, temperature, soil type, and more! 🚜✨

<p align="center">
  <a href="https://cropyieldprediction-nmsn2nzjjjqgagbxwt95br.streamlit.app/">
    <img src="https://img.shields.io/badge/Open%20Live%20Dashboard-Streamlit%20🚀-brightgreen?style=for-the-badge&logo=streamlit" alt="Open in Streamlit"/>
  </a>
  <img src="https://img.shields.io/github/stars/nadee2k/crop_yield_prediction?style=for-the-badge" alt="GitHub stars"/>
  <img src="https://img.shields.io/github/forks/nadee2k/crop_yield_prediction?style=for-the-badge" alt="GitHub forks"/>
</p>

---

## 🚀 Features

- ✨ **User-Friendly Streamlit Interface**: Clean, interactive UI for data input and instant results.
- 🤖 **Accurate Predictions**: Uses advanced ML models for reliable crop yield forecasts.
- 📊 **Visualizations**: See charts and graphs for your predictions and input data.
- ⚡ **Easy to Deploy**: Run locally or deploy on Streamlit Cloud!

---

<details>
<summary><strong>📦 Quick Start</strong></summary>

```bash
git clone https://github.com/nadee2k/crop_yield_prediction.git
cd crop_yield_prediction
pip install -r requirements.txt
streamlit run app.py
```

</details>

---

## 🧑‍🌾 How to Use

1. **Input Features:**
   - Select crop type, soil type, region, etc.
   - Enter values for rainfall, temperature, fertilizer used, etc.
2. **Get Prediction:**
   - Click "Predict Yield".
   - View the estimated yield and visualizations.
3. **Export Results:**
   - Download results as CSV (if implemented).

---

## 🛠️ Tech Stack

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white"/>
</p>

---

## 🌟 Example

### App Screenshot

![App Screenshot](demo/Screenshot_1.jpeg)

![App Screenshot](demo/Screenshot_2.jpeg)
*Above: Example of the crop yield prediction interface and results.*

---

<details>
<summary><strong>📂 Project Structure</strong></summary>

```
crop_yield_prediction/
│
├── model/           # Trained ML models
├── data/            # Sample data files
├── .venv/           # Virtual environment (optional)
├── notebooks/       # Jupyter notebooks for experiments
├── app.py           # Streamlit application
├── requirements.txt # Python dependencies
├── README.md        # Project documentation
└── demo/            # Demo screenshots
```

</details>

---

## 🤝 Contributing

Pull requests and stars are welcome! For major changes, open an issue first to discuss your ideas.

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## ❓ FAQ

- **Q: Can I use my own data?**
  - A: Yes! Replace the sample data in the `data/` folder with your own, and retrain the model as needed.
- **Q: How do I deploy this app?**
  - A: You can deploy on [Streamlit Cloud](https://streamlit.io/cloud) or any platform supporting Streamlit.

---

## ✨ Acknowledgments

- [Streamlit](https://streamlit.io/)
- [Scikit-learn](https://scikit-learn.org/)
- Unsplash for images

---

> Built with ❤️ by [nadee2k](https://github.com/nadee2k)
