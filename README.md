# 求職網站

這是一個使用 Vue 3 和 Django 構建的求職網站。

## 後端技術棧

- Python 3.11
- Django
- Django REST framework
- drf-yasg (Swagger/OpenAPI 文檔)

## 前端技術棧

- Vue 3
- Naive UI
- Vue Router
- Pinia (狀態管理)
- Axios (HTTP 客戶端)

## 安裝和運行

1. 克隆項目：
```bash
git clone <repository-url>
cd job-search-website
```

2. 創建並激活虛擬環境：
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
.\venv\Scripts\activate  # Windows
```

3. 安裝依賴：
```bash
pip install -r requirements.txt
```

4. 運行數據庫遷移：
```bash
cd backend
python manage.py migrate
```

5. 運行開發服務器：
```bash
python manage.py runserver
```

## API 文檔

本項目使用 Swagger/OpenAPI 提供 API 文檔。

### 訪問 Swagger UI

1. 啟動開發服務器後，訪問：
   http://127.0.0.1:8000/swagger/

2. Swagger UI 提供以下功能：
   - 所有 API 端點的詳細文檔
   - API 請求和響應的模式
   - 在線 API 測試工具

### API 端點

主要的 API 端點包括：

- 用戶相關：`/api/users/`
  - 用戶註冊、登錄、個人資料管理

- 職位相關：`/api/jobs/`
  - 職位列表、詳情、創建、更新、刪除

- 公司相關：`/api/companies/`
  - 公司信息、職位發布管理

### 開發模式下的 API 測試

1. 訪問 Swagger UI：http://127.0.0.1:8000/swagger/
2. 在右上角找到 "Authorize" 按鈕（如果需要認證）
3. 展開任意 API 端點查看詳細信息
4. 使用 "Try it out" 按鈕測試 API

## 項目結構

```
.
├── frontend/                # Vue 3 前端專案
│   ├── src/
│   │   ├── components/     # 組件目錄
│   │   │   ├── layout/     # 布局組件
│   │   │   │   ├── BaseLayout.vue    # 基礎布局組件
│   │   │   │   ├── Navbar.vue        # 導航欄組件
│   │   │   │   ├── LeftSidebar.vue   # 左側邊欄組件
│   │   │   │   └── RightSidebar.vue  # 右側邊欄組件
│   │   │   └── main-panel/ # 主要內容面板組件
│   │   │       ├── Home.vue          # 首頁面板
│   │   │       ├── Profile.vue       # 個人資料面板
│   │   │       └── Company.vue       # 公司面板
│   │   ├── views/         # 視圖組件
│   │   │   ├── HomeView.vue
│   │   │   ├── ProfileView.vue
│   │   │   └── CompanyView.vue
│   │   ├── router/        # 路由配置
│   │   ├── stores/        # Pinia 狀態管理
│   │   └── assets/        # 靜態資源
└── backend/               # Django 後端專案
    ├── apps/             # Django 應用程式
    │   ├── jobs/        # 職位相關功能
    │   ├── companies/   # 公司相關功能
    │   └── users/       # 用戶相關功能
    ├── config/          # 專案配置
    ├── media/           # 媒體文件目錄
    │   └── company_logos/  # 公司標誌存儲目錄
    └── manage.py        # Django 管理腳本
```

## 技術棧

- 前端：
  - Vue 3 + JavaScript + Pinia + Vue Router
  - UI 框架：Naive UI
  - HTTP 客戶端：Axios
    - 基礎 URL: `http://localhost:8000`
    - 請求攔截器：添加認證 token
    - 響應攔截器：處理錯誤響應
- 後端：Django + Django REST framework
  - 圖片處理：Pillow
  - API 過濾：django-filter
  - API 文檔：drf-yasg
- 資料庫：SQLite（開發環境）

## 圖片處理說明

### 後端圖片存儲
- 圖片存儲位置：`backend/media/company_logos/`
- 支持的圖片格式：JPG、JPEG、PNG、GIF
- 最大圖片大小：5MB
- 圖片訪問 URL：`http://localhost:8000/media/company_logos/圖片名稱`

### API 響應中的圖片信息
- `logo` 欄位：圖片的相對路徑
- `logo_url` 欄位：圖片的完整 URL

## 前端組件結構說明

### 布局組件 (layout/)
- `BaseLayout.vue`: 基礎布局組件，包含整體頁面結構
  - 整合了 Navbar、LeftSidebar、RightSidebar
  - 提供插槽用於放置主要內容
- `Navbar.vue`: 頂部導航欄
- `LeftSidebar.vue`: 左側邊欄
- `RightSidebar.vue`: 右側邊欄

### 主要內容面板 (main-panel/)
- `Home.vue`: 首頁主要內容
- `Profile.vue`: 個人資料頁面內容
- `Company.vue`: 公司頁面內容

### 視圖組件 (views/)
- 每個視圖組件都使用 BaseLayout 作為基礎布局
- 通過插槽將對應的 main-panel 組件放入布局中

## 開發環境設置

### 前端設置

1. 進入前端目錄：
```bash
cd frontend
```

2. 安裝依賴：
```bash
npm install
```

3. 啟動開發伺服器：
```bash
npm run dev
```

4. 在瀏覽器中開啟：http://localhost:5173

### 後端設置

1. 確保你在專案根目錄下，然後創建並激活虛擬環境：
```bash
# 創建虛擬環境
python -m venv venv

# 激活虛擬環境
# Mac/Linux:
source venv/bin/activate
# Windows:
.\venv\Scripts\activate
```

2. 安裝所有必要的依賴：
```bash
pip install -r requirements.txt
```

3. 運行資料庫遷移：
```bash
python manage.py migrate
```

4. 啟動Django開發伺服器：
```bash
先回到整個資料夾的路徑
cd ..
python manage.py runserver
```

## 日後開啟專案

1. 在Vscode中開啟終端機
```bash
Ctrl + j 
```

2. 進入frontend資料夾
```bash
cd frontend
```

3. 運行前端項目
```bash
npm run dev
```

4. 新增終端機（在原終端機視窗右上角的加號）

5. 執行後端
```bash
python manage.py runserver
```

## 後端應用程式說明

### 1. jobs 應用程式
- 職位管理功能
- API 端點：`/api/jobs/`
- 功能：
  - 職位列表查詢
  - 職位搜尋和過濾
  - 職位詳情查看
  - 職位發布和管理

### 2. companies 應用程式
- 公司管理功能
- API 端點：`/api/companies/`
- 功能：
  - 公司列表查詢
  - 公司資訊管理
  - 公司職位關聯
  - 公司搜尋和過濾

### 3. users 應用程式
- 用戶管理功能
- API 端點：`/api/users/`
- 功能：
  - 用戶註冊和登入
  - 個人資料管理
  - 權限控制
  - 用戶認證

## 功能特性

- 用戶認證系統
  - 註冊和登入
  - 個人資料管理
  - 權限控制
- 職位管理
  - 職位發布和編輯
  - 職位搜尋和篩選
  - 職位詳情查看
- 公司管理
  - 公司資訊維護
  - 公司職位關聯
  - 公司搜尋和篩選
- 履歷管理
  - 履歷上傳
  - 履歷編輯
  - 履歷投遞

## 注意事項

- 確保你的Python版本是3.8或更高版本
- 如果遇到端口被佔用的問題，可以使用 `python manage.py runserver 8001` 來指定不同的端口
- 要停止伺服器，按 Ctrl+C
- 開發時請確保同時運行前端和後端服務

## 貢獻指南

1. Fork 專案
2. 創建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 開啟 Pull Request

## 前端技術說明

### Naive UI 組件使用
- 使用 Naive UI 作為主要 UI 框架
- 主要使用的組件：
  - 布局組件：`n-layout`, `n-grid`
  - 導航組件：`n-menu`, `n-breadcrumb`
  - 表單組件：`n-form`, `n-input`, `n-select`
  - 數據展示：`n-table`, `n-card`, `n-list`
  - 反饋組件：`n-modal`, `n-message`, `n-notification`

### 主題配置
- 支持亮色/暗色主題切換
- 自定義主題變量
- 響應式設計

## 開發說明

- API 文檔自動生成：項目使用 drf-yasg 自動生成 Swagger 文檔
- RESTful API：遵循 REST 設計原則
- 權限控制：基於 Django REST framework 的權限系統

## 待開發功能

- [ ] 用戶認證和授權
- [ ] 職位搜索和過濾
- [ ] 簡歷上傳和管理
- [ ] 公司認證
- [ ] 前端界面開發
