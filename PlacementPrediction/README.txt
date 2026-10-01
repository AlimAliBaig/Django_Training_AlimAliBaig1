STUDENT PLACEMENT PREDICTION - DJANGO + ML

1. Open PowerShell in this folder.
2. Create/activate your virtual environment.
3. Install packages:
   pip install -r requirements.txt
4. Run migrations:
   python manage.py migrate
5. Start server:
   python manage.py runserver
6. Open:
   http://127.0.0.1:8000/

FLOW:
Signup -> Login -> Student Profile (optional) -> Placement Prediction -> Result

MODEL INPUTS:
cgpa, iq, profile_score

FILES:
placement_model/placement_model.pkl   = uploaded SVC model
placement_model/placement_scaler.pkl  = uploaded StandardScaler
placement_model/placement_dataset.csv = uploaded placement dataset

NOTE:
The uploaded scikit-learn model/scaler were serialized with scikit-learn 1.6.1. If your environment uses a different version, you may see an InconsistentVersionWarning. For best compatibility, use the same scikit-learn version used to create the PKL files.
