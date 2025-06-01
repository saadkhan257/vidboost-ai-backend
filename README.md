# ⚡ VidBoost AI Backend

VidBoost AI is a next-generation video and image enhancement engine built for mobile. This is the official Python-based backend powered by **Real-ESRGAN**, designed to upscale and enhance images with ultra-clarity — up to 4x resolution improvement.

---

## 🚀 Project Highlights

- ✅ Built with Flask and Flask-CORS  
- ✅ Powered by Real-ESRGAN AI model  
- ✅ Accepts image uploads over API  
- ✅ Auto-renames enhanced outputs with branding  
- ✅ Returns downloadable enhanced image  
- ✅ Deployment-ready on Render or Railway  

---

## 🧠 AI Model Used

- **Model**: [`RealESRGAN_x4plus.pth`](https://github.com/xinntao/Real-ESRGAN)  
- **Purpose**: Upscales low-res images by 4x using deep neural networks  
- **Precision**: Forced `--fp32` for CPU safety  
- **Directory**: Place model file in `/models/` or linked into the Real-ESRGAN `weights` folder  

---

## 📂 Folder Structure

```
vidboost-ai-backend/
├── app.py                  # Main Flask app
├── enhancer/
│   └── upscaler.py         # Core AI enhancement logic
├── models/                 # Holds Real-ESRGAN model .pth file
├── inputs/                 # Temp upload folder
├── outputs/                # Enhanced image results
├── third_party/
│   └── Real-ESRGAN/        # Cloned official AI repo
├── requirements.txt
├── runtime.txt
├── README.md
└── .gitignore
```

---

## 🔧 Local Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/your-username/vidboost-ai-backend.git
cd vidboost-ai-backend
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Download the model
Place `RealESRGAN_x4plus.pth` into:
```
models/RealESRGAN_x4plus.pth
```

### 4. Run the Flask API
```bash
python app.py
```

---

## 🔁 API Usage

### 🔸 POST `/enhance`

Uploads an image and returns the enhanced result.

#### ✅ Request:
```http
POST /enhance
Content-Type: multipart/form-data
Body: file = <image file>
```

#### ✅ Example using `curl`:
```bash
curl -X POST http://127.0.0.1:5000/enhance \
  -F "file=@inputs/test.jpg" \
  --output result.png
```

#### ✅ Response:
- Returns a `.png` file (branded as `*_vidboost-ai.png`)
- If enhancement fails, returns:
```json
{ "error": "Enhancement failed" }
```

---

## 🌐 Deployment (Render.com)

### 🔸 Required Files:
- `requirements.txt`
- `runtime.txt`
- `app.py`

### 🔸 Render Settings:
| Option         | Value                        |
|----------------|------------------------------|
| Build Command  | `pip install -r requirements.txt` |
| Start Command  | `python app.py`              |
| Runtime        | `python-3.11.11` (via runtime.txt) |
| Service Type   | Web Service                  |

> ⚠️ On free tier (CPU-only), use `--fp32` mode only. For GPU, use Railway or AWS Lambda GPU layer.

---

## ✅ To Do Next

- [ ] Add video enhancement logic (Real-ESRGAN + FFmpeg)
- [ ] Add `/status` route with enhancement time
- [ ] Enable token system for user usage limits
- [ ] Connect with Flutter app via HTTP package

---

## 📩 Contact

For support or collaboration, reach out via [technicalforest.com](https://technicalforest.com)  
Maintained by **Saad Khan** — Founder of VidBoost AI & Technical Forest.

---

> "VidBoost AI — Enhance videos like never before."
