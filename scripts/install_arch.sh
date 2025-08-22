#!/bin/bash
# سكريبت تثبيت Bilingual Book Formatter على Arch Linux
# يحل مشاكل GUI وإعداد البيئة

set -euo pipefail

echo "=== تثبيت Bilingual Book Formatter على Arch Linux ==="

# التحقق من النظام
if ! command -v pacman >/dev/null 2>&1; then
    echo "هذا السكريبت مخصص لـ Arch Linux/Manjaro"
    exit 1
fi

# تثبيت المتطلبات الأساسية
echo "تثبيت المتطلبات الأساسية..."
sudo pacman -S --needed --noconfirm \
    python python-pip python-virtualenv \
    python-pyqt6 python-pyqt6-sip \
    python-pypdf2 python-pillow python-beautifulsoup4 \
    poppler-utils \
    qt6-wayland qt6-base \
    nodejs npm

# إنشاء البيئة الافتراضية
echo "إنشاء البيئة الافتراضية..."
if [ ! -d ".venv" ]; then
    python -m venv .venv
fi

# تفعيل البيئة الافتراضية
source .venv/bin/activate

# تثبيت المتطلبات من requirements.txt
echo "تثبيت متطلبات Python..."
if [ -f "requirements.txt" ]; then
    pip install --upgrade pip
    pip install -r requirements.txt
else
    echo "ملف requirements.txt غير موجود، تثبيت المتطلبات الأساسية..."
    pip install PyQt6 python-docx pdfplumber ebooklib Pillow beautifulsoup4 deepl googletrans fastapi uvicorn
fi

# إعداد متغيرات البيئة لـ Qt
echo "إعداد متغيرات البيئة لـ Qt..."
cat > .env << 'EOF'
# Qt Environment Variables
export QT_QPA_PLATFORM=xcb
export QT_AUTO_SCREEN_SCALE_FACTOR=1
export QT_SCALE_FACTOR=1
export DISPLAY=${DISPLAY:-:0}

# Wayland support (if needed)
if [ "$XDG_SESSION_TYPE" = "wayland" ]; then
    export QT_QPA_PLATFORM=wayland
    export QT_WAYLAND_DISABLE_WINDOWDECORATION=1
fi
EOF

# إنشاء سكريبت تشغيل GUI
echo "إنشاء سكريبت تشغيل GUI..."
cat > run_gui.sh << 'EOF'
#!/bin/bash
# تشغيل الواجهة الرسومية لـ Bilingual Book Formatter

cd "$(dirname "$0")"

# تحميل متغيرات البيئة
if [ -f ".env" ]; then
    source .env
fi

# تفعيل البيئة الافتراضية
if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
fi

# تشغيل التطبيق
echo "تشغيل الواجهة الرسومية..."
python bilingual_book_formatter.py --gui

EOF

chmod +x run_gui.sh

# إنشاء سكريبت تشغيل الواجهة الويب
echo "إنشاء سكريبت تشغيل الواجهة الويب..."
cat > run_web.sh << 'EOF'
#!/bin/bash
# تشغيل الواجهة الويب لـ Bilingual Book Formatter

cd "$(dirname "$0")"

# الانتقال إلى مجلد الواجهة الويب
if [ -d "bilingual-formatter-web" ]; then
    cd bilingual-formatter-web
    
    # تثبيت المتطلبات إذا لم تكن مثبتة
    if [ ! -d "node_modules" ]; then
        echo "تثبيت متطلبات الواجهة الويب..."
        npm install
    fi
    
    # تشغيل الخادم
    echo "تشغيل الواجهة الويب على http://localhost:5173"
    npm run dev
else
    echo "مجلد الواجهة الويب غير موجود"
    exit 1
fi
EOF

chmod +x run_web.sh

# إنشاء ملف desktop للانشر
echo "إنشاء ملف desktop..."
cat > BilingualBookFormatter.desktop << 'EOF'
[Desktop Entry]
Version=1.0
Type=Application
Name=Bilingual Book Formatter
Name[ar]=معالج الكتب ثنائية اللغة
Comment=Format bilingual books and documents
Comment[ar]=تنسيق الكتب والوثائق ثنائية اللغة
Exec=/home/$USER/Bilingual-Book-Formatter/run_gui.sh
Icon=text-editor
Terminal=false
Categories=Office;Publishing;
StartupWMClass=BilingualBookFormatter
EOF

# نسخ ملف desktop إلى مجلد التطبيقات
if [ -d "$HOME/.local/share/applications" ]; then
    cp BilingualBookFormatter.desktop "$HOME/.local/share/applications/"
    echo "تم إضافة التطبيق إلى قائمة التطبيقات"
fi

echo ""
echo "=== تم التثبيت بنجاح! ==="
echo ""
echo "طرق التشغيل:"
echo "1. الواجهة الرسومية: ./run_gui.sh"
echo "2. الواجهة الويب: ./run_web.sh"
echo "3. سطر الأوامر: source .venv/bin/activate && python bilingual_book_formatter.py"
echo ""
echo "إذا واجهت مشاكل في الواجهة الرسومية، شغّل:"
echo "python scripts/diagnose_qt.py"
echo ""
echo "ملاحظة: تأكد من تشغيل السكريبت من داخل مجلد المشروع"

