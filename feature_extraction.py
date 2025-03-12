import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.decomposition import PCA

def feature_selection(features, labels, method="SelectKBest", number_of_feature=10):
    """
    Özellik seçim yöntemini uygular ve en iyi özellikleri döndürür.
    """
    if method == "SelectKBest":
        selective = SelectKBest(score_func=f_classif, k=number_of_feature)
        feature_new = selective.fit_transform(features, labels)
        print(f"SelectKBest yöntemiyle en iyi {number_of_feature} özellik seçildi.")
        
    elif method == "PCA":
        pca = PCA(n_components=number_of_feature)
        feature_new = pca.fit_transform(features)
        print(f"PCA yöntemiyle en iyi {number_of_feature} bileşen seçildi.")
        
    else:
        raise ValueError("Geçersiz yöntem seçildi. Yalnızca 'SelectKBest' veya 'PCA' kullanılabilir.")
        
    return feature_new


if __name__ == "__main__":
    # İşlenmiş datayi yükle
    file_path = "data_process.csv"
    data = pd.read_csv(file_path)
    
    features = data.iloc[:, :-1].values
    labels = data.iloc[:, -1].values
    
    # Özellik seçimini uygula
    feature_new = feature_selection(features, labels, method="SelectKBest", number_of_feature=10)
