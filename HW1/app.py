
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pandas as pd

# 2. 從頭開始實作線性迴歸模型
class LinearRegression:
    def __init__(self, learning_rate=0.01, n_iters=1000):
        self.lr = learning_rate
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    # 2-1. 初始化權重和偏差
    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        # 2-4. 實施梯度下降進行最佳化
        for _ in range(self.n_iters):
            # 2-2. 定義假設函數（h（x）= wx + b）
            y_predicted = self.predict(X)
            
            # 計算梯度
            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)
            
            # 更新權重和偏差
            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias

# 2-3. 定義成本函數（均方誤差）
def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# 1. 幫我生成一組用來做線性回歸的資料集
def generate_data(n_samples, a, noise_var):
    X = np.random.rand(n_samples, 1) * 10  # Feature is between 0 and 10
    noise = np.random.randn(n_samples, 1) * np.sqrt(noise_var)
    # y = ax + b, let's assume b is a constant, e.g., 5
    b = 5 
    y = a * X + b + noise
    return X, y.ravel() # flatten y

# --- Streamlit App ---

st.set_page_config(layout="wide")

st.title("互動式線性迴歸模型")

# 7. 建立操作介面
st.sidebar.header("參數調整")
n_points = st.sidebar.slider("Number of data points (n)", 100, 1000, 100)
a_coeff = st.sidebar.slider("Coefficient 'a' (y = ax + b + noise)", -10.0, 10.0, 2.5, 0.1)
noise_var = st.sidebar.slider("Noise Variance (var)", 0.0, 1000.0, 0.5, 0.1)

# 生成資料
X, y = generate_data(n_points, a_coeff, noise_var)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. 使用訓練資料訓練模型
regressor = LinearRegression(learning_rate=0.01, n_iters=1000)
regressor.fit(X_train, y_train)

# --- 新增功能：計算離群值 ---
# 使用整個資料集來找出離群值
all_predictions = regressor.predict(X)
residuals = np.abs(y - all_predictions)
outlier_indices = np.argsort(residuals)[-5:] # 找出5個最大殘差的索引

# 8. 呈現線性回歸的圖表
st.header("線性回歸結果")
fig, ax = plt.subplots(figsize=(10, 6))

# 5. 將預測值與實際值進行視覺化
ax.scatter(X, y, color='blue', label='Actual Data')
ax.plot(X, all_predictions, color='red', linewidth=2, label='Regression Line')
ax.scatter(X[outlier_indices], y[outlier_indices], color='purple', s=100, label='Top 5 Outliers', zorder=5)

# 在圖表中標示出離群值的原始索引
for idx in outlier_indices:
    ax.text(X[idx], y[idx], f" Outlier {idx}", fontsize=9, verticalalignment='bottom')

ax.set_xlabel("X")
ax.set_ylabel("y")
ax.set_title("Linear Regression Visualization")
ax.legend()
st.pyplot(fig)

# --- 新增功能：Model Coefficients ---
st.header("Model Coefficients")
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Coefficient 'a' (斜率)", value=f"{regressor.weights[0]:.4f}")
with col2:
    st.metric(label="Coefficient 'b' (截距)", value=f"{regressor.bias:.4f}")

# --- 新增功能：Top 5 Outliers ---
st.header("Top 5 Outliers")
# 為了顯示，將離群值從最大到最小排序
sorted_outlier_indices = outlier_indices[::-1]
outlier_data = {
    'Outlier Index': sorted_outlier_indices,
    'X': X[sorted_outlier_indices].ravel(),
    'y': y[sorted_outlier_indices],
    'residuals': all_predictions[sorted_outlier_indices]
}
outlier_df = pd.DataFrame(outlier_data)
outlier_df.set_index('Outlier Index', inplace=True)
st.dataframe(outlier_df.style.format({'X': '{:.4f}', 'y (Actual)': '{:.4f}', 'y (Predicted)': '{:.4f}'}))


# 4. 對測試集做出預測，並計算評估指標
predictions_test = regressor.predict(X_test)
mse = mean_squared_error(y_test, predictions_test)
r2 = r2_score(y_test, predictions_test)

# 9. 輸出均方誤差（MSE）以及 R 平方
st.header("模型評估指標")
col3, col4 = st.columns(2)
with col3:
    st.metric(label="均方誤差 (Mean Squared Error)", value=f"{mse:.4f}")
with col4:
    st.metric(label="R 平方 (R-squared)", value=f"{r2:.4f}")


