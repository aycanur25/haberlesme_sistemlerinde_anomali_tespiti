# WiFi Intrusion Detection System

WiFi ağlarında saldırı tespiti için makine öğrenimi tabanlı sistem. AWID2 veri seti kullanılarak çeşitli sınıflandırma algoritmalarının performanslarını K-Fold cross validation, undersampling ve SMOTE teknikleri ile karşılaştırır.

## Proje Açıklaması

Bu proje, WiFi ağ trafiğini analiz ederek aşağıdaki saldırı türlerini tespit etmeyi amaçlar:
- **Normal**: Yasal WiFi trafiği
- **Flooding**: Ağ kaynaklarını tüketen saldırılar
- **Impersonation**: Kimlik sahtekarlığı saldırıları

Proje, veri dengesizliği problemini çözmek için undersampling ve SMOTE tekniklerini kullanır ve model performansını K-Fold cross validation ile değerlendirir.

## Gereksinimler

```bash
pip install pandas numpy matplotlib scikit-learn seaborn lightgbm imbalanced-learn
```

### Gerekli Kütüphaneler:
- `pandas` - Veri manipülasyonu
- `numpy` - Sayısal hesaplamalar
- `matplotlib` - Görselleştirme
- `scikit-learn` - Makine öğrenimi algoritmaları
- `seaborn` - İstatistiksel görselleştirme
- `lightgbm` - Gradient boosting algoritması
- `imbalanced-learn` - Veri dengeleme teknikleri (SMOTE)

## Veri Seti

**AWID2 (Aegean WiFi Intrusion Dataset)** kullanılmaktadır:
- **Eğitim Seti**: `AWID-CLS-R-Trn/1`
- **Test Seti**: `AWID-CLS-R-Tst/1`
- **Özellik Sayısı**: 154 (16 seçili özellik kullanılıyor)
- **Veri Dengesizliği**: Normal sınıf diğer sınıflardan çok daha fazla örnek içerir

### Seçili Özellikler:
- Frame özellikleri: `frame.len`
- Radiotap özellikleri: `radiotap.length`, `radiotap.channel.freq`, `radiotap.dbm_antsignal`
- WLAN özellikleri: `wlan.duration`, `wlan.fc.type`, `wlan.fc.subtype`, vb.

## Kullanılan Algoritmalar

1. **Decision Tree** - Karar ağacı algoritması
2. **LightGBM** - Gradient boosting algoritması
3. **Logistic Regression** - Lojistik regresyon
4. **SGD Classifier** - Stokastik gradyan iniş
5. **Linear SVC** - Destek vektör makinesi
6. **Random Forest** - Rastgele orman
7. **Extra Trees** - Ekstra ağaçlar

## Veri Dengeleme Teknikleri

### 1. K-Fold Cross Validation
- **Stratified K-Fold** (k=10) kullanılır
- Sınıf dağılımını koruyarak veriyi böler
- Her fold'da eğitim ve test setlerinin sınıf oranları korunur
- Model performansının daha güvenilir değerlendirilmesini sağlar

### 2. Undersampling
- Çoğunluk sınıfından (Normal) rastgele örnekler çıkarır
- Hızlı işlem süresi sağlar
- Veri kaybına neden olabilir ancak dengeyi sağlar

### 3. SMOTE (Synthetic Minority Oversampling Technique)
- Azınlık sınıfları için sentetik örnekler üretir
- K-nearest neighbors algoritması kullanır
- Veri kaybı olmadan sınıf dengesini sağlar
- Overfitting riskini azaltır

## Kullanım

### 1. Veri Hazırlama
```python
# Veri setini yükle
awid2trn_data = pd.read_csv("path/to/train/data", header=None, names=features)
awid2tst_data = pd.read_csv("path/to/test/data", header=None, names=features)

# Seçili özellikleri filtrele
awid2trn_data = awid2trn_data.loc[:, selected_features + ['class']]
```

### 2. Veri Ön İşleme
```python
# NaN değerleri temizle
data = data.replace(r'^\s*$', pd.NA, regex=True)
data = data.replace('?', pd.NA)
data = data.dropna()

# Injection sınıfını kaldır
filter_data = data['class'] != 'injection'
data = data[filter_data]
```

### 3. Özellik Mühendisliği
```python
# Sinyal gücü dönüşümü
X['radiotap.dbm_antsignal'] = X['radiotap.dbm_antsignal'].apply(convert_to_integer)

# Min-Max ölçeklendirme
scaler = MinMaxScaler()
X[columns_to_scale] = scaler.fit_transform(X[columns_to_scale])

# One-hot encoding
X = pd.get_dummies(X, columns=columns_to_one_hot_encode)
```


### 4. Model Eğitimi ve Değerlendirme
```python
# 10-Fold Cross Validation fonksiyonu
def train_and_evaluate_model(model, X, y, kfold, model_name=""):
    accumulated_metrics = {
        'accuracy': [], 'f1_macro': [], 'f1_micro': [], 'f1_weighted': [],
        'precision_macro': [], 'precision_micro': [], 'precision_weighted': [],
        'recall_macro': [], 'recall_micro': [], 'recall_weighted': [], 'auc': []
    }
    
    for train_index, test_index in kfold.split(X, y):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]
        
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        metrics = calculate_metrics(y_test, y_pred, model, X_test)
        for key in accumulated_metrics.keys():
            accumulated_metrics[key].append(metrics.get(key, np.nan))
    
    return accumulated_metrics
```

## Değerlendirme Metrikleri

### Temel Metrikler
- **Accuracy** - Doğruluk oranı
- **F1-Score** (Macro, Micro, Weighted)
  - **Macro**: Her sınıfın eşit ağırlıkta değerlendirilmesi
  - **Micro**: Tüm örneklerin eşit ağırlıkta değerlendirilmesi
  - **Weighted**: Sınıf boyutlarına göre ağırlıklandırılmış değerlendirme
- **Precision** (Macro, Micro, Weighted)
- **Recall** (Macro, Micro, Weighted)
- **AUC-ROC** - ROC eğrisi altındaki alan

### Görselleştirme
- **Confusion Matrix** - Karışıklık matrisi (3x3 matrix: Normal, Flooding, Impersonation)
- **Performance Comparison Charts** - Farklı dengeleme yöntemlerinin karşılaştırması

## Önemli Fonksiyonlar

### `convert_to_integer(value)`
Birden fazla sinyal gücü değerini ortalama değere dönüştürür.

### `calculate_metrics(y_test, y_pred, model, X_test)`
Model performans metriklerini hesaplar (accuracy, F1-score, precision, recall, AUC).

### `train_and_evaluate_model(model, X, y, kfold, model_name)`
- K-Fold cross validation gerçekleştirir
- Her fold için model eğitir ve test eder
- Ortalama performans metriklerini hesaplar
- Karışıklık matrisini oluşturur

### `plot_confusion_matrix(cm, model_name)`
Karışıklık matrisini heatmap olarak görselleştirir.

## Model Hiperparametreleri

### Decision Tree
```python
DecisionTreeClassifier(
    max_depth=20,
    ccp_alpha=0.001,
    max_leaf_nodes=100,
    min_samples_leaf=2,
    random_state=42
)
```

### LightGBM
```python
LGBMClassifier(
    objective='multiclass',
    num_leaves=20,
    learning_rate=0.01,
    max_depth=10,
    n_estimators=80,
    reg_alpha=0.01,
    reg_lambda=0.01
)
```

### Random Forest
```python
RandomForestClassifier(
    max_depth=20,
    ccp_alpha=0.001,
    max_leaf_nodes=100,
    min_samples_leaf=2,
    random_state=42
)
```

### Extra Trees
```python
ExtraTreesClassifier(
    max_depth=200,
    n_estimators=200,
    ccp_alpha=0.0001,
    max_leaf_nodes=500,
    min_samples_leaf=2,
    min_samples_split=10,
    random_state=42
)
```

## Dengeleme Yöntemleri Karşılaştırması

| Yöntem | Avantajlar | Dezavantajlar | Kullanım Durumu |
|--------|------------|---------------|-----------------|
| **Original** | Gerçek veri dağılımı | Sınıf dengesizliği | Baseline karşılaştırma |
| **Undersampling** | Hızlı işlem, basit | Veri kaybı | Büyük veri setleri |
| **SMOTE** | Veri kaybı yok, sentetik çeşitlilik | Hesaplama maliyeti, overfitting riski | Küçük-orta veri setleri |

## Beklenen Performans Sonuçları

### Dengesiz Veri Seti
- Normal sınıf için yüksek precision/recall
- Azınlık sınıfları için düşük recall
- Genel accuracy yüksek ama yanıltıcı

### Undersampling Sonrası
- Dengeli precision/recall değerleri
- Azınlık sınıfları için iyileştirilmiş performans
- Düşük genel accuracy ancak daha adil değerlendirme

### SMOTE Sonrası
- En dengeli performans metrikleri
- Tüm sınıflar için optimize edilmiş F1-score
- Gerçekçi ve güvenilir model performansı

## K-Fold Cross Validation Avantajları

1. **Güvenilir Değerlendirme**: 10 farklı train/test bölünmesi ile robust sonuçlar
2. **Overfitting Kontrolü**: Model genelleme yeteneğinin test edilmesi
3. **Stratified Sampling**: Sınıf dağılımının her fold'da korunması
4. **İstatistiksel Anlamlılık**: Ortalama ve standart sapma ile güven aralıkları


## Önemli Notlar

- **Veri Yolu**: Google Colab kullanıyorsanız Drive yollarını güncelleyin
- **Bellek Kullanımı**: SMOTE büyük veri setlerinde yüksek bellek kullanabilir
- **İşlem Süresi**: K-Fold CV ile işlem süreleri uzayabilir
- **Sınıf Dengeleme**: Gerçek dünya uygulamalarında uygun yöntemi seçin
- **Hiperparametre Optimizasyonu**: Grid Search ile daha iyi sonuçlar alınabilir

## Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/BalancingMethod`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add SMOTE implementation'`)
4. Branch'inizi push edin (`git push origin feature/BalancingMethod`)
5. Pull Request oluşturun


## 📧 İletişim

Sorularınız için lütfen issue açın.

---

**Not**: Bu proje akademik amaçlı geliştirilmiştir. Gerçek üretim ortamında kullanmadan önce ek güvenlik testleri ve model validasyonu yapılmalıdır.