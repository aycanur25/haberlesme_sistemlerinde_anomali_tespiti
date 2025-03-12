import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
import os

def data_upload(file_path):
    """
    datayi CSV dosyasından yükler.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dosya bulunamadı: {file_path}")
    
    try:
        data = pd.read_csv(file_path)
        print(f"data başarıyla yüklendi. Toplam {data.shape[0]} örnek ve {data.shape[1]} özellik.")
        return data
    except Exception as e:
        raise Exception(f"data yükleme hatası: {str(e)}")


def data_preprocessing(data):
    """
    dataleri temizler, eksik değerleri doldurur ve ölçeklendirir.
    """
    # Eksik değerleri kaldır
    data = data.dropna()
    
    # Kategorik dataleri sayısal değerlere dönüştür
    label_encoder = LabelEncoder()
    for sutun in data.select_dtypes(include=['object']).columns:
        data[sutun] = label_encoder.fit_transform(data[sutun])

    # dataleri normalleştir
    scaler = StandardScaler()
    features = data.iloc[:, :-1]  # Son sütunun label olduğunu varsayıyoruz
    labels = data.iloc[:, -1]

    features = scaler.fit_transform(features)
    
    print("data ön işleme tamamlandı.")
    return features, labels


def save_process_data(features, labels, output_file="data_process.csv"):
    """
    İşlenmiş datayi CSV dosyasına kaydeder.
    """
    data_process = np.column_stack((features, labels))
    kolon_isimleri = [f"ozellik_{i}" for i in range(features.shape[1])] + ["label"]
    df = pd.DataFrame(data_process, columns=kolon_isimleri)
    df.to_csv(output_file, index=False)
    print(f"İşlenmiş data {output_file} dosyasına kaydedildi.")


if __name__ == "__main__":
    file_path = "dataset/awid.csv"  # Kendi data seti yolunu buraya gir
    data = data_upload(file_path)
    features, labels = data_preprocessing(data)
    save_process_data(features, labels)
