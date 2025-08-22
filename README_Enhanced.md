# Bilingual Book Formatter v2.4 - Enhanced Edition

<div align="center">

![Bilingual Book Formatter](https://img.shields.io/badge/Version-2.4-blue.svg)
![Python](https://img.shields.io/badge/Python-3.11+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey.svg)

**معالج الكتب ثنائية اللغة - الإصدار المحسن**

أداة شاملة لتنسيق ومعالجة الكتب والوثائق ثنائية اللغة مع دعم متقدم للعربية والإنجليزية

</div>

## ✨ الميزات الجديدة في v2.4

- 🖥️ **واجهة رسومية محسنة** مع PyQt6 ودعم كامل لـ Linux
- 🌐 **واجهة ويب تفاعلية** مبنية بـ React
- 🔧 **أدوات تشخيص وإصلاح** للمشاكل الشائعة
- 📦 **مثبت تلقائي لويندوز** مع تحميل المتطلبات
- 🐧 **دعم محسن لـ Arch Linux** مع سكريپتات تثبيت
- 🚀 **بناء تلقائي** عبر GitHub Actions
- 🎨 **دعم أفضل للـ RTL** والخطوط العربية

## 🚀 التثبيت السريع

### Windows
```bash
# تحميل وتشغيل المثبت التلقائي
curl -O https://github.com/DrAbdulmalek/Bilingual-Book-Formatter/releases/latest/download/BilingualBookFormatter_Windows.zip
# استخراج الملفات وتشغيل BilingualBookFormatter.exe
```

### Linux (Arch/Manjaro)
```bash
git clone https://github.com/DrAbdulmalek/Bilingual-Book-Formatter.git
cd Bilingual-Book-Formatter
chmod +x scripts/install_arch.sh
./scripts/install_arch.sh
./run_gui.sh
```

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3-pyqt6 python3-pip python3-venv
git clone https://github.com/DrAbdulmalek/Bilingual-Book-Formatter.git
cd Bilingual-Book-Formatter
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python bilingual_book_formatter.py --gui
```

## 🎯 طرق الاستخدام

### 1. الواجهة الرسومية (GUI)
```bash
# Linux
./run_gui.sh

# Windows
run_gui.bat

# أو مباشرة
python bilingual_book_formatter.py --gui
```

### 2. الواجهة الويب
```bash
# Linux
./run_web.sh

# Windows
run_web.bat

# أو يدوياً
cd bilingual-formatter-web
npm install
npm run dev
```

### 3. سطر الأوامر (CLI)
```bash
python bilingual_book_formatter.py \
  --lang1 english_book.docx \
  --lang2 arabic_translation.docx \
  --output bilingual_result.docx \
  --format two-column
```

## 🛠️ حل المشاكل

### مشكلة عدم ظهور الواجهة الرسومية على Linux
```bash
# تشغيل أداة التشخيص
python scripts/diagnose_qt.py

# إصلاح مشاكل Qt الشائعة
export QT_QPA_PLATFORM=xcb
# أو للـ Wayland
export QT_QPA_PLATFORM=wayland

# تثبيت المتطلبات المفقودة (Arch)
sudo pacman -S qt6-wayland python-pyqt6

# تثبيت المتطلبات المفقودة (Ubuntu)
sudo apt install python3-pyqt6 libxcb-cursor0
```

### مشاكل الواجهة الويب
```bash
# التأكد من تثبيت Node.js
node --version
npm --version

# إعادة تثبيت المتطلبات
cd bilingual-formatter-web
rm -rf node_modules package-lock.json
npm install
npm run dev
```

## 📁 هيكل المشروع

```
Bilingual-Book-Formatter/
├── bilingual_book_formatter.py    # الملف الرئيسي
├── app.py                         # خادم FastAPI
├── enhanced_windows_installer.py  # مثبت ويندوز محسن
├── build_windows_executable.py    # بناء ملف تنفيذي
├── config.json                    # ملف الإعدادات
├── requirements.txt               # متطلبات Python
├── scripts/                       # سكريپتات مساعدة
│   ├── install_arch.sh           # مثبت Arch Linux
│   ├── diagnose_qt.py            # أداة تشخيص Qt
│   └── publish_to_github.sh      # نشر على GitHub
├── bilingual-formatter-web/       # الواجهة الويب
│   ├── src/
│   ├── package.json
│   └── vite.config.js
├── .github/workflows/             # GitHub Actions
│   └── build-and-release.yml
├── tests/                         # الاختبارات
└── docs/                          # التوثيق
```

## 🔧 التطوير

### إعداد بيئة التطوير
```bash
# استنساخ المشروع
git clone https://github.com/DrAbdulmalek/Bilingual-Book-Formatter.git
cd Bilingual-Book-Formatter

# إنشاء بيئة افتراضية
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# أو
.venv\Scripts\activate     # Windows

# تثبيت المتطلبات
pip install -r requirements.txt

# تثبيت متطلبات التطوير
pip install pytest black flake8 mypy

# تشغيل الاختبارات
python -m pytest tests/
```

### بناء الإصدارات
```bash
# بناء الواجهة الويب
cd bilingual-formatter-web
npm run build

# بناء ملف تنفيذي لويندوز
python build_windows_executable.py

# إنشاء إصدار جديد
git tag v2.4.1
git push origin v2.4.1
# سيتم البناء التلقائي عبر GitHub Actions
```

## 📚 الصيغ المدعومة

### المدخلات
- **DOCX** - مستندات Microsoft Word
- **DOC** - مستندات Word القديمة  
- **PDF** - ملفات PDF (استخراج النص)
- **EPUB** - كتب إلكترونية
- **HTML** - صفحات ويب
- **TXT** - ملفات نصية

### المخرجات
- **DOCX** - مستند Word منسق
- **HTML** - صفحة ويب تفاعلية
- **PDF** - ملف PDF منسق (قريباً)

## 🎨 خيارات التنسيق

- **عمودين جنباً إلى جنب** - اللغة الأولى يساراً والثانية يميناً
- **فقرات متناوبة** - فقرة بالإنجليزية تليها فقرة بالعربية
- **جداول مقارنة** - جدول بعمودين للمقارنة
- **تنسيق مخصص** - تحكم كامل في التخطيط

## 🌍 الدعم اللغوي

- **العربية** - دعم كامل للـ RTL وتشكيل النصوص
- **الإنجليزية** - تنسيق LTR متقدم
- **خطوط محسنة** - Amiri، Noto Naskh Arabic، Times New Roman
- **محاذاة ذكية** - محاذاة تلقائية حسب اتجاه النص

## 🔌 التكامل مع الخدمات

- **Google Translate API** - ترجمة تلقائية
- **DeepL API** - ترجمة عالية الجودة
- **Google Drive** - حفظ واسترجاع الملفات
- **Dropbox** - تخزين سحابي
- **GitHub** - إدارة الإصدارات

## 📊 الإحصائيات والتحليل

- **عدد الكلمات** - إحصائيات مفصلة لكل لغة
- **تحليل المحتوى** - كشف نوع المحتوى والتنسيق
- **تقرير الجودة** - تحليل جودة الترجمة والتنسيق
- **معاينة مباشرة** - عرض النتيجة قبل الحفظ

## 🤝 المساهمة

نرحب بمساهماتكم! يرجى اتباع الخطوات التالية:

1. **Fork** المشروع
2. إنشاء فرع للميزة الجديدة (`git checkout -b feature/amazing-feature`)
3. **Commit** التغييرات (`git commit -m 'Add amazing feature'`)
4. **Push** إلى الفرع (`git push origin feature/amazing-feature`)
5. فتح **Pull Request**

### إرشادات المساهمة
- اتبع معايير **PEP 8** للكود
- أضف **اختبارات** للميزات الجديدة
- حدث **التوثيق** عند الحاجة
- استخدم **رسائل commit** واضحة

## 🐛 الإبلاغ عن المشاكل

إذا واجهت أي مشكلة، يرجى:

1. التحقق من [المشاكل المعروفة](https://github.com/DrAbdulmalek/Bilingual-Book-Formatter/issues)
2. تشغيل أداة التشخيص: `python scripts/diagnose_qt.py`
3. إنشاء [issue جديد](https://github.com/DrAbdulmalek/Bilingual-Book-Formatter/issues/new) مع:
   - وصف المشكلة
   - خطوات إعادة الإنتاج
   - نتائج أداة التشخيص
   - نظام التشغيل والإصدار

## 📄 الترخيص

هذا المشروع مرخص تحت رخصة MIT - راجع ملف [LICENSE](LICENSE) للتفاصيل.

## 👨‍💻 المطور

**د. عبدالمالك تامر الحسيني**
- GitHub: [@DrAbdulmalek](https://github.com/DrAbdulmalek)
- البريد الإلكتروني: [البريد الإلكتروني]

## 🙏 شكر وتقدير

- **Manus AI** - للمساعدة في التطوير والتحسين
- **PyQt6** - للواجهة الرسومية الممتازة
- **React** - لواجهة الويب التفاعلية
- **جميع المساهمين** - لجهودهم في تحسين المشروع

## 📈 خارطة الطريق

### الإصدار القادم (v2.5)
- [ ] دعم المزيد من الصيغ (ODT، RTF)
- [ ] تصدير PDF محسن
- [ ] واجهة جوال (PWA)
- [ ] دعم المزيد من اللغات
- [ ] تحسينات الأداء

### المستقبل البعيد
- [ ] ذكاء اصطناعي لتحسين الترجمة
- [ ] تكامل مع المزيد من الخدمات السحابية
- [ ] إصدار macOS
- [ ] واجهة سطر أوامر محسنة

---

<div align="center">

**إذا أعجبك المشروع، لا تنس إعطاؤه ⭐ على GitHub!**

[🏠 الصفحة الرئيسية](https://github.com/DrAbdulmalek/Bilingual-Book-Formatter) | 
[📖 التوثيق](https://github.com/DrAbdulmalek/Bilingual-Book-Formatter/wiki) | 
[🐛 المشاكل](https://github.com/DrAbdulmalek/Bilingual-Book-Formatter/issues) | 
[💬 المناقشات](https://github.com/DrAbdulmalek/Bilingual-Book-Formatter/discussions)

</div>

