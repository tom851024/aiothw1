# 開發日誌 (Development Log)

## 1.0-2.0：初始設置
- **User:** 要求建立一個 `Todo.md` 檔案來追蹤所有專案步驟。
- **Gemini:** 建立 `D:\Users\User\Desktop\碩士\作業\物聯網\Todo.md`。

## 3.0-5.0：開發日誌的建立與刪除
- **User:** 要求建立 `0_devLog.md`。
- **Gemini:** 建立 `D:\Users\User\Desktop\碩士\作業\物聯網\0_devLog.md`。
- **User:** 改變主意，要求刪除 `0_devLog.md`。
- **Gemini:** 刪除 `0_devLog.md` 並在 `Todo.md` 中記錄此操作。

## 6.0 onwards：重新定義開發日誌
- **User:** 要求重新建立 `0_devLog.md`，並將整個對話歷史記錄在其中，使用指定的標題格式。
- **Gemini:** 正在執行此操作。

## 12.0-13.0：成功運行 Streamlit 應用程式

- **專案初始化**:
  - 根據 `prompt.txt` 的要求，使用 Streamlit 建立一個互動式線性迴歸網站。
  - 建立 `app.py` 和 `requirements.txt`。

- **核心功能開發**:
  - 從頭實作一個 `LinearRegression` 類別，包含 `fit` 和 `predict` 方法。
  - 實現梯度下降演算法來訓練模型。
  - 建立資料生成函數 `generate_data`。

- **使用者介面 (UI) 開發**:
  - 建立側邊欄，提供滑桿讓使用者調整資料點數量、係數 'a' 和雜訊變異數。
  - 實作 `matplotlib` 圖表以視覺化資料點和迴歸線。
  - 將圖表中的標籤和標題改為英文。
  - 調整滑桿的數值範圍以符合使用者需求。

- **進階功能與排版**:
  - 新增「Model Coefficients」區塊，顯示模型的斜率與截距。
  - 新增「Top 5 Outliers」區塊：
    - 計算並找出5個最大的離群值。
    - 在圖表上用紫色點和標籤 (`Outlier {index}`) 特別標示出離群值。
    - 建立一個表格，顯示離群值的原始索引、X/y 值和預測值。
  - 移除「對新資料進行預測」區塊。
  - 調整 UI 區塊順序，使其更符合參考網站的排版。