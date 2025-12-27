# Deployment Guide

## 1. Vercel Project Configuration
The project is located in a subdirectory `Antigravity youtube/web` within the repository. You must configure Vercel to look in the correct place.

### **CRITICAL STEP**: Set Root Directory
1. Go to your Vercel Project Dashboard.
2. Click on **Settings**.
3. On the left sidebar, click **Build and Deployment**.
4. Find the **"Root Directory"** section.
5. Click **Edit**.
6. Enter: `Antigravity youtube/web`
7. Click **Save**.

## 2. Environment Variables
Ensure the following variables are set in Vercel (**Settings** -> **Environment Variables**):
- `OPENAI_API_KEY`: (If using OpenAI)
- `GOOGLE_API_KEY`: (If using Gemini)
- `GEMINI_API_KEY`: (Same as above, depending on code usage)

## 3. Redeploy
After changing the Root Directory:
1. Go to the **Deployments** tab.
2. Click the three dots (`...`) next to the latest deployment (or the failed one).
3. Select **Redeploy**.
4. Make sure "Use existing Build Cache" is **unchecked** just to be safe (optional).
5. Click **Redeploy**.

The site should now build the Next.js application instead of the static HTML file.
