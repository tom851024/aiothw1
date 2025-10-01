# 開發日誌 (Development Log)

## 1.0-2.0：初始設置
- **User:** 要求建立一個 `Todo.md` 檔案來追蹤所有專案步驟。
- **Gemini:** 建立 `D:\Users\User\Desktop\碩士\作業\物聯網\Todo.md`。

## 3.0-5.0：開發日誌的建立與刪除
- **User:** 要求建立 `0_devLog.md`。
- **Gemini:** 建立 `D:\Users\User\Desktop\碩士\作業\物聯網\0_devLog.md`。
- **User:** 改變主意，要求刪除 `0_devLog.md`。
- **Gemini:** 刪除 `0_devLog.md` 並在 `Todo.md` 中記錄此操作。

## 6.0-11.0 onwards：重新定義開發日誌
- **User:** 要求重新建立 `0_devLog.md`，並將整個對話歷史記錄在其中，使用指定的標題格式。
- **Gemini:** 正在執行此操作。

## 12.0-13.0：運行 Streamlit 應用程式
- **Gemini:** 提供 `streamlit run HW1/app.py` 指令來啟動應用程式。
- **User:** (在本機端成功執行指令)

## 14.0-End: Streamlit 應用程式開發與迭代 (詳細對話紀錄)
- **User:** 根據 prompt.txt 中的prompt進行網站製作。
- **Gemini:** 讀取 `prompt.txt`，分析需求後提議使用 Streamlit 建立一個互動式線性迴歸網站，並規劃了 `app.py` 和 `requirements.txt` 檔案結構。
- **User:** 同意計畫。
- **Gemini:** 建立 `app.py` 和 `requirements.txt` 檔案。在安裝 `requirements.txt` 時，`sklearn` 套件安裝失敗。
- **Gemini:** 發現 `sklearn` 是已棄用的套件名稱，將其更正為 `scikit-learn` 後成功安裝。
- **User:** 要求將圖表中的文字改成英文。
- **Gemini:** 修改 `app.py`，將圖表的標題和圖例改為英文。
- **User:** 要求調整三個滑桿的數值範圍。
- **Gemini:** 修改 `app.py` 中的 `st.sidebar.slider` 參數。
- **User:** 要求在圖表中標出5個最大的離群值，並新增 Model Coefficients 和 Top 5 Outliers 區塊。
- **Gemini:** 修改 `app.py`，加入離群值計算、在圖表中繪製離群點，並新增對應的 UI 區塊。
- **User:** 要求移除「對新資料進行預測」區塊。
- **Gemini:** 從 `app.py` 中移除相關程式碼。
- **User:** 要求離群值標示為 #1, #2...
- **Gemini:** 修改 `app.py`，在圖表和表格中加入離群值排名。
- **User:** 要求離群值標示為其在資料集中的原始索引，如 "Outlier 30"。
- **Gemini:** 再次修改 `app.py`，將排名標示改為原始索引標示。
- **User:** 要求撰寫 README.md 報告。
- **Gemini:** 根據開發過程和結果，生成 `README.md` 檔案。
- **User:** 要求將 `HW1` 資料夾的內容上傳到 GitHub。
- **Gemini:** 執行 `git init`, `git remote add`, `git add`, `git commit`, `git push` 等指令，成功將專案上傳。
- **User:** 要求移除 `HW1` 資料夾，將所有檔案移至根目錄。
- **Gemini:** 移動檔案，並透過 `git commit` 和 `git push` 更新 GitHub 儲存庫的檔案結構。
- **User:** 詢問 Python 版本。
- **Gemini:** 執行 `python --version` 並回報版本為 `3.12.2`。
- **User:** 要求更新 `requirements.txt`。
- **Gemini:** 執行 `pip freeze`，篩選出專案直接相依的套件，並將其鎖定版本後更新 `requirements.txt`，然後將變更推送到 GitHub。
- **User:** 要求將開發日誌的摘要部分改為對話格式。
- **Gemini:** 整理並更新了開發日誌為詳細的對話格式，並將其推送到 GitHub。