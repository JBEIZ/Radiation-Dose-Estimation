📟 AI Radiation Dose Estimator – X-ray, CT, Mammogram
A Streamlit-based AI tool that estimates radiation dose for X-ray, CT, and Mammogram procedures using trained machine learning models. This project combines medical physics knowledge with AI to support smarter, faster dose estimation in diagnostic imaging.

🖥️ Live Demo
(Optional) Deployed at: [https://radiation-dose-estimation.streamlit.app/]

📂 Project Structure
bash
Copy
Edit
radiation-dose-estimator/
├── streamlit_app.py               # Main Streamlit app
├── radiation_dose_model.pkl       # AI model for X-ray (DAP)
├── ct_dose_model.pkl              # AI model for CT (DLP)
├── mammo_dose_model.pkl           # AI model for Mammogram (AGD)
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation

🚀 Features
✅ Supports 3 exam types: X-ray, CT, and Mammogram

📊 Real-time dose prediction using trained ML models:

X-ray: Predicts DAP (Dose Area Product)

CT: Predicts DLP (Dose Length Product)

Mammogram: Predicts AGD (Average Glandular Dose)

🧠 Physics-informed synthetic data and dose logic

🎛️ User-friendly Streamlit UI with sliders & dropdowns

🧪 Inputs by Modality
Modality	Input Parameters	Output
X-ray	kVp, mAs, exposure time, patient thickness, projection (AP/PA/LAT)	DAP (mGy·cm²)
CT	CTDIvol (mGy), scan length (cm), number of phases	DLP (mGy·cm)
Mammogram	kVp, mAs, breast thickness, view (CC/MLO)	AGD (mGy)

🔧 Installation
bash
Copy
Edit
pip install -r requirements.txt
streamlit run streamlit_app.py

🌐 Deployment
Push your files to a public GitHub repo

Go to streamlit.io/cloud

Connect your GitHub and select streamlit_app.py as the entry point

Upload your .pkl models under “Files” in app settings

📘 Use Case Scenarios
🏥 Radiographers estimating patient dose on the spot

👩‍🔬 Medical physics students learning dose optimization

📊 Research teams prototyping dose monitoring systems

🤝 Acknowledgements
This project was developed as a mini AI-medical physics integration initiative to showcase the potential of AI-assisted dose estimation in diagnostic imaging workflows.
