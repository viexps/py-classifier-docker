import pandas as pd
from pydantic import BaseModel


class FeatureData(BaseModel):
    age: int
    sex: str
    dataset: str
    cp: str
    trestbps: float
    chol: float
    fbs: bool
    restecg: str
    thalch: float
    exang: bool
    oldpeak: float
    slope: str
    ca: float
    thal: str


example = FeatureData.parse_obj({
    'age': 63,
    'sex': 'Male',
    'dataset': 'Cleveland',
    'cp': 'typical angina',
    'trestbps': 145.0,
    'chol': 233.0,
    'fbs': True,
    'restecg': 'lv hypertrophy',
    'thalch': 150.0,
    'exang': False,
    'oldpeak': 2.3,
    'slope': 'downsloping',
    'ca': 0.0,
    'thal': 'fixed defect'
})


def make_df_from_single(e) -> pd.DataFrame:
    processed = {k: [v] for k, v in e.items()}
    return pd.DataFrame(processed)
