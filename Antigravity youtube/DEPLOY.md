# 部署指南 (Deployment Guide)

这个网站是基于 **Next.js** 构建的，最推荐的部署方式是使用 **Vercel**（Next.js 的母公司，完全免费且速度极快）。

以下是让您的网站上线的详细步骤：

## 第一步：准备代码 (Push to GitHub)

如果您还没有将代码上传到 GitHub，请先创建一个仓库并上传：

1. 登录 [GitHub](https://github.com/) 创建一个新的 Repository（例如命为 `noise-reduction-web`）。
2. 在您的项目文件夹 (`web` 目录) 打开终端，运行：
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/noise-reduction-web.git
   git push -u origin main
   ```

## 第二步：在 Vercel 上导入项目

1. 访问 [Vercel Dashboard](https://vercel.com/dashboard) 并注册/登录 (推荐使用 GitHub 账号登录)。
2. 点击 **"Add New..."** -> **"Project"**。
3. 在 "Import Git Repository" 列表中找到刚才创建的 `noise-reduction-web`，点击 **"Import"**。

## 第三步：配置环境变量 (关键！)

在 Vercel 的部署配置页面 (Configure Project)：

1. 找到 **Environment Variables** 区域。
2. 即使我们代码里有“备用”的 Key，为了安全和灵活性，**强烈建议**您在这里填入飞书的配置信息：
    *   **key**: `FEISHU_APP_ID`  | **value**: `cli_a9c6a1bb56f89cd4`
    *   **key**: `FEISHU_APP_SECRET` | **value**: `Ox6v51RIbon1bbxaHmvUGhqRNnW3CiUs`
    *   **key**: `FEISHU_APP_TOKEN` | **value**: `FCnWb734NawZW6spPVvcMjtonjf`
    *   **key**: `FEISHU_TABLE_ID` | **value**: `tblZh4KDjOUZnpod`

3. 确保 **Framework Preset** 选的是 `Next.js`。
4. **Root Directory** (根目录)：点击 Edit，选择 `web` 文件夹作为根目录（因为您的 Next.js 项目是在 `web` 子文件夹里）。

## 第四步：点击 Deploy

点击蓝色的 **"Deploy"** 按钮。

Vercel 会自动开始构建：
1. 下载代码
2. 安装依赖 (`npm install`)
3. 构建项目 (`npm run build`)

大约 1 分钟后，您满屏幕的五彩纸屑 🎉，由于您已经配置了环境变量，网站将会立即上线，并且您可以获得一个类似 `https://noise-reduction-web.vercel.app` 的永久免费域名。

## 分享给朋友

您可以直接把这个链接发给任何人，他们都能看到这个精美的、“果味十足”的 AI 资讯站了！
