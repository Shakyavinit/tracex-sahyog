# 🪟 Windows Setup & Installation Guide
## **TraceX — Blockchain Intelligence & VASP Attribution Engine**
**Theme**: Ministry of Home Affairs (MHA) // Indian Cyber Crime Coordination Centre (I4C)  
**Problem Statement ID**: 26182  
**Target Operating System**: Windows 10 / Windows 11 (64-bit)  

---

## ⚡ Method 1: 1-Click Automated Setup (Recommended)

Follow these 3 simple steps:

### **Step 1: Install Python (If Not Already Installed)**
If Python is not yet installed on your system:
1. Download Python from the official portal: 👉 **[Python Official Website](https://www.python.org/downloads/)** (Python 3.10, 3.11, or 3.12 recommended).
2. While running the installer, **ensure you enable this checkbox** at the bottom:
   ```
   ☑ Add python.exe to PATH   <--- (CRITICAL: MUST BE CHECKED)
   ```
3. Click **"Install Now"**.

---

### **Step 2: Extract the Project Archive**
1. Right-click the **`TraceX_v2_Pro_System.zip`** (or folder bundle).
2. Select **"Extract All..."** and choose your preferred destination directory (e.g., `Desktop` or `Downloads`).

---

### **Step 3: Double-Click `start.bat`**
1. Open the extracted folder and double-click **`start.bat`**.
2. The automated launcher will:
   - Detect your Python installation.
   - Automatically install all required dependencies (`fastapi`, `uvicorn`, `networkx`, `pydantic`, etc.).
   - Launch your default browser directly to: **`http://localhost:8765`**.
3. The **TraceX Forensic Dashboard** is now live and ready for investigation! 🎉

---

## 💻 Method 2: Manual Setup (Command Prompt / PowerShell)

To start the engine manually via command line:

### 1. Open Terminal in Project Directory:
- In the project folder, hold `Shift + Right Click` on an empty area and select **"Open in Terminal"** or **"Open PowerShell window here"**.
- Alternatively, type `cmd` in the folder address bar and press `Enter`.

### 2. Install Dependencies:
```cmd
pip install -r requirements.txt
```

### 3. Start Forensic Backend:
```cmd
python -m uvicorn app:app --host 0.0.0.0 --port 8765 --reload
```

### 4. Access the Dashboard:
Open your browser and navigate to:
👉 **`http://localhost:8765`**

---

## 🛠️ Troubleshooting & Frequently Asked Questions

### 1. Error: `'python' is not recognized as an internal or external command`
* **Root Cause:** The "Add python.exe to PATH" option was omitted during Python installation.
* **Resolution:**
  1. Re-run the Python installer.
  2. Select **"Modify"** or perform a clean re-installation.
  3. On the first installation screen, check **`☑ Add python.exe to PATH`**.

### 2. Windows Opens the Microsoft Store Instead of Running Python
* **Root Cause:** Windows 10/11 default "App Execution Aliases" are enabled.
* **Resolution:**
  1. Open Windows Search and type: `Manage app execution aliases`.
  2. Toggle **OFF** (Disable) both `App Installer (python.exe)` and `App Installer (python3.exe)`.

### 3. Windows Firewall Prompt
- Upon the initial launch, Windows Defender Firewall may prompt: *"Windows Defender Firewall has blocked some features of this app"*.
- Select **"Private networks"** and click **"Allow access"**.

### 4. Port 8765 Already in Use
If port 8765 is occupied by an earlier process:
Run Command Prompt as Administrator:
```cmd
netstat -ano | findstr :8765
```
Identify the PID at the end of the line (e.g., `12345`) and terminate it:
```cmd
taskkill /PID 12345 /F
```
Then launch `start.bat` again.

---

## 🎯 Verification Checklist
1. **System Health Check:** Check the top bar indicators (**"ENGINE OPERATIONAL"** and **"FASTAPI v2.0"**).
2. **Pre-Loaded Benchmark Cases:** Click any case in the left sidebar (e.g., *TRON Multi-Hop* or *Bitcoin Peel Chain*) to observe live graph traversal.
3. **AI Investigator Copilot:** Click **"Court Report"** or **"Refresh Summary"** in the AI panel to generate real-time intelligence briefings.
4. **Live API Connectivity:** Click the **`7/7 APIS LIVE`** telemetry pill to verify all external intelligence gateways.
