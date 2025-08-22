# أوامر البداية السريعة - Bilingual Book Formatter v2.4

## 🚨 تحذير أمان أولاً!
```bash
# ⚠️ ألغِ التوكين المكشوف فوراً من GitHub Settings!
# REMOVED_TOKEN
```

## 🚀 رفع المشروع على GitHub (الطريقة السريعة)

### الخطوة 1: إعداد SSH (مرة واحدة فقط)
```bash
# إنشاء مفتاح SSH
ssh-keygen -t ed25519 -C "your-email@example.com"

# إضافة المفتاح إلى ssh-agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# عرض المفتاح العام لنسخه إلى GitHub
cat ~/.ssh/id_ed25519.pub
```

**اذهب إلى GitHub → Settings → SSH and GPG keys → New SSH key والصق المفتاح**

### الخطوة 2: رفع المشروع
```bash
# الانتقال إلى مجلد المشروع
cd /path/to/Bilingual-Book-Formatter

# استخدام السكريپت الآمن (الأسهل)
chmod +x scripts/publish_to_github.sh
./scripts/publish_to_github.sh

# أو يدوياً:
git init
git branch -M main
git add .
git commit -m "Initial commit: Bilingual Book Formatter v2.4 Enhanced"
git remote add origin git@github.com:DrAbdulmalek/Bilingual-Book-Formatter.git
git push -u origin main

# إنشاء إصدار (سيبني EXE تلقائياً)
git tag v2.4.0
git push origin v2.4.0
```

## 🐧 تشغيل على Linux

### Arch/Manjaro
```bash
chmod +x scripts/install_arch.sh
./scripts/install_arch.sh
./run_gui.sh
```

### Ubuntu/Debian
```bash
sudo apt update
sudo apt install python3-pyqt6 python3-pip python3-venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python bilingual_book_formatter.py --gui
```

### إذا لم تظهر الواجهة الرسومية
```bash
python scripts/diagnose_qt.py
export QT_QPA_PLATFORM=xcb
python bilingual_book_formatter.py --gui
```

## 🪟 تشغيل على Windows

### الطريقة 1: استخدام المثبت التلقائي
```cmd
python enhanced_windows_installer.py
```

### الطريقة 2: يدوياً
```cmd
pip install -r requirements.txt
python bilingual_book_formatter.py --gui
```

## 🌐 تشغيل الواجهة الويب

```bash
cd bilingual-formatter-web
npm install
npm run dev
# افتح http://localhost:5173
```

## 🧪 تشغيل الاختبارات

```bash
python tests/test_basic_functionality.py
```

## 📦 بناء ملف تنفيذي لويندوز

```bash
pip install pyinstaller
python build_windows_executable.py
# الملف في dist/BilingualBookFormatter.exe
```

## 🔧 أوامر مفيدة

### تحديث المشروع
```bash
git pull origin main
pip install -r requirements.txt --upgrade
cd bilingual-formatter-web && npm update
```

### إنشاء إصدار جديد
```bash
git tag v2.4.1
git push origin v2.4.1
# سيبني GitHub Actions الملفات تلقائياً
```

### تنظيف الملفات المؤقتة
```bash
find . -name "__pycache__" -type d -exec rm -rf {} +
find . -name "*.pyc" -delete
rm -rf build/ dist/
cd bilingual-formatter-web && rm -rf node_modules/ dist/
```

## 🆘 حل المشاكل السريع

### مشكلة: Permission denied
```bash
chmod +x scripts/*.sh
```

### مشكلة: Module not found
```bash
pip install -r requirements.txt
```

### مشكلة: Qt platform plugin
```bash
sudo apt install libxcb-cursor0  # Ubuntu
sudo pacman -S qt6-wayland       # Arch
export QT_QPA_PLATFORM=xcb
```

### مشكلة: npm command not found
```bash
# Ubuntu/Debian
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs

# Arch
sudo pacman -S nodejs npm
```

## 📞 الحصول على المساعدة

1. **تشخيص تلقائي**: `python scripts/diagnose_qt.py`
2. **GitHub Issues**: https://github.com/DrAbdulmalek/Bilingual-Book-Formatter/issues
3. **التوثيق الكامل**: `README_Enhanced.md`

---

**نصيحة**: احفظ هذا الملف كمرجع سريع! 🔖

