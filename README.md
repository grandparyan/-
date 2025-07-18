# Vitepress 部落格範本

![Vitepress](https://img.shields.io/badge/Vitepress-v1.6.3-646CFF?logo=vite&logoColor=fff&labelColor=8A2BE2)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=github-actions&logoColor=white)
![GitHub Pages](https://img.shields.io/badge/Template_v1.0.0-9fa?logo=github&logoColor=white&label=Github%20Pages&labelColor=121013)

> [!NOTE]
> Author: @CXPhoenix
>
> version: v1.0.0

這是一個使用 [VitePress](https://vitepress.dev/) 建立的說明文件網站範本。您可以直接使用此範本來建立您的專案文件。

## ✨ 功能特色

*   **VitePress 驅動**：享受 VitePress 帶來的極速開發體驗與強大功能。
*   **GitHub Pages 自動部署**：已設定好 GitHub Actions，當您推送（push）到 `main` branch 時，會自動將您的網站部署到 GitHub Pages。
*   **MIT License**：採用寬鬆的 MIT License，您可以自由地使用、修改與散佈。

## 🚀 快速開始

### 環境要求

請確認您的開發環境已安裝 [Node.js](https://nodejs.org/) (建議版本為 22 或以上)。

### 安裝

首先，複製此 repository 到您的本機，並安裝相關依賴套件：

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
npm install
```

### Localhost 開發

執行以下指令，即可在您的 Localhost 啟動開發伺服器：

```bash
npm run docs:dev
```

VitePress 將會在 `http://localhost:5173` 啟動一個熱重載（Hot-Reloading）的開發環境。

### 建置

當您準備好部署網站時，請執行以下指令來建置靜態網站檔案：

```bash
npm run docs:build
```

建置完成的檔案將會被輸出到 `docs/.vitepress/dist` 目錄下。

## 部署

本專案已設定好透過 GitHub Actions 自動部署到 GitHub Pages。您只需要將您的變更推送到 `main` branch，GitHub Actions 就會自動幫您完成建置與部署。

您可以在 `.github/workflows/deploy.yaml` 中查看詳細的部署設定。

## GitHub Pages 設定

為了讓 GitHub Actions 能夠順利部署，您需要先在您的 GitHub repository 中進行以下設定：

1.  前往您的 repository 的 **Settings** 頁面。
2.  在左側選單中，點選 **Pages**。
3.  在 **Build and deployment** -> **Source** 的下拉選單中，選擇 **GitHub Actions**。

完成以上設定後，當您推送到 `main` branch 時，GitHub Actions 就會自動將您的網站部署到 GitHub Pages。

## ⚙️ 客製化

您可以透過修改以下檔案，來客製化您的網站：

*   **網站設定**： `docs/.vitepress/config.mjs`
    *   修改網站標題 (`title`)、描述 (`description`)。
    *   設定導覽列 (`themeConfig.nav`)。
    *   設定側邊欄 (`themeConfig.sidebar`)。
    *   設定社群連結 (`themeConfig.socialLinks`)。
*   **網站內容**：
    *   在 `docs` 目錄下新增或修改 Markdown (`.md`) 檔案，即可新增或修改頁面內容。
    *   首頁內容位於 `docs/index.md`。

## 📄 授權

本專案採用 [MIT License](LICENSE)。