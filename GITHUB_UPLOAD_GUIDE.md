# دليل رفع مشروع Bilingual Book Formatter على GitHub

## 🚨 تحذير أمان مهم

**يجب إلغاء التوكين المكشوف فوراً!**

التوكين `REMOVED_TOKEN` الذي ذكرته مكشوف علناً ويشكل خطراً أمنياً. يرجى:

1. الدخول إلى GitHub → Settings → Developer settings → Personal access tokens
2. العثور على التوكين وإلغاؤه (Revoke)
3. إنشاء توكين جديد مع صلاحيات محدودة إذا لزم الأمر
4. **الأفضل: استخدام SSH بدلاً من التوكينات**

## 📋 الطرق المتاحة للرفع

### الطريقة الأولى: استخدام السكريپت الآمن (مُوصى بها)

```bash
# من داخل مجلد المشروع
./scripts/publish_to_github.sh
```

هذا السكريپت سيقوم بـ:
- إعداد SSH تلقائياً
- إنشاء مفتاح SSH إذا لم يكن موجوداً
- رفع المشروع بأمان
- إنشاء tags للإصدارات

### الطريقة الثانية: الرفع اليدوي

#### 1. إعداد SSH (مُوصى به)

```bash
# إنشاء مفتاح SSH
ssh-keygen -t ed25519 -C "your-email@example.com"

# إضافة المفتاح إلى ssh-agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# عرض المفتاح العام لنسخه
cat ~/.ssh/id_ed25519.pub
```

**إضافة المفتاح إلى GitHub:**
1. اذهب إلى GitHub → Settings → SSH and GPG keys
2. اضغط "New SSH key"
3. الصق المفتاح العام
4. احفظ

#### 2. رفع المشروع

```bash
# تهيئة git إذا لم يكن مُهيأً
git init
git branch -M main

# إضافة الملفات
git add .
git commit -m "Initial commit: Bilingual Book Formatter v2.4 Enhanced"

# إضافة المستودع البعيد
git remote add origin git@github.com:DrAbdulmalek/Bilingual-Book-Formatter.git

# رفع الملفات
git push -u origin main

# إنشاء tag للإصدار
git tag v2.4.0
git push origin v2.4.0
```

### الطريقة الثالثة: استخدام GitHub CLI

```bash
# تثبيت GitHub CLI
# Ubuntu/Debian: sudo apt install gh
# Arch: sudo pacman -S github-cli
# macOS: brew install gh

# تسجيل الدخول
gh auth login

# إنشاء المستودع ورفع الملفات
gh repo create DrAbdulmalek/Bilingual-Book-Formatter --public --source=. --remote=origin --push
```

## 📁 هيكل المشروع المُحسن

```
Bilingual-Book-Formatter/
├── 📄 README_Enhanced.md              # ملف README محسن
├── 📄 CHANGELOG.md                    # سجل التغييرات
├── 📄 GITHUB_UPLOAD_GUIDE.md          # هذا الدليل
├── 📄 todo.md                         # قائمة المهام
├── 📄 config.json                     # إعدادات التطبيق
├── 📄 requirements.txt                # متطلبات Python
├── 🐍 bilingual_book_formatter.py     # الملف الرئيسي
├── 🐍 app.py                          # خادم FastAPI
├── 🐍 enhanced_windows_installer.py   # مثبت ويندوز محسن
├── 🐍 windows_installer.py            # مثبت ويندوز أصلي
├── 🐍 build_windows_executable.py     # بناء ملف تنفيذي
├── 📁 scripts/                        # سكريپتات مساعدة
│   ├── 🔧 install_arch.sh            # مثبت Arch Linux
│   ├── 🔍 diagnose_qt.py             # أداة تشخيص Qt
│   └── 📤 publish_to_github.sh       # سكريپت نشر آمن
├── 📁 bilingual-formatter-web/        # الواجهة الويب
│   ├── 📁 src/                       # كود المصدر
│   ├── 📁 dist/                      # ملفات البناء
│   ├── 📄 package.json               # متطلبات Node.js
│   └── ⚙️ vite.config.js             # إعدادات Vite
├── 📁 .github/workflows/              # GitHub Actions
│   └── 🚀 build-and-release.yml      # بناء تلقائي
├── 📁 tests/                          # الاختبارات
│   └── 🧪 test_basic_functionality.py # اختبارات أساسية
└── 📁 docs/                           # التوثيق (اختياري)
```

## 🎯 الميزات الجديدة في v2.4

### ✨ تحسينات الواجهة الرسومية
- إصلاح مشكلة عدم ظهور GUI على Arch Linux
- أداة تشخيص Qt متقدمة
- دعم أفضل لـ Wayland و X11

### 🌐 الواجهة الويب المحسنة
- تصميم عصري مع React
- دعم RTL للعربية
- واجهة متجاوبة للجوال

### 📦 مثبت ويندوز متقدم
- تحميل تلقائي للمتطلبات
- تقرير تقدم مرئي
- إنشاء اختصارات تلقائياً

### 🐧 دعم Linux محسن
- سكريپت تثبيت خاص بـ Arch
- إعداد تلقائي للبيئة الافتراضية
- حل مشاكل Qt الشائعة

### 🚀 CI/CD تلقائي
- بناء تلقائي للإصدارات
- رفع الملفات التنفيذية
- إنشاء releases تلقائياً

## 🔧 بعد الرفع: إعداد GitHub Actions

بعد رفع المشروع، GitHub Actions سيعمل تلقائياً عند:
- إنشاء tag جديد (`git tag v2.4.1 && git push origin v2.4.1`)
- Push إلى الفرع الرئيسي

سيقوم بـ:
- بناء ملف تنفيذي لويندوز
- إنشاء حزمة Linux
- رفع الملفات كـ GitHub Release

## 📊 اختبار المشروع

```bash
# تشغيل الاختبارات
python tests/test_basic_functionality.py

# تشخيص Qt
python scripts/diagnose_qt.py

# اختبار الواجهة الويب
cd bilingual-formatter-web
npm run build
```

## 🎨 تخصيص المشروع

### إضافة لغات جديدة
عدّل `config.json`:
```json
{
    "fonts": {
        "spanish": "Times New Roman",
        "german": "Arial"
    },
    "rtl_languages": ["arabic", "persian", "hebrew", "urdu"]
}
```

### تخصيص الواجهة الويب
```bash
cd bilingual-formatter-web
npm install
npm run dev
# عدّل الملفات في src/
```

## 🐛 حل المشاكل الشائعة

### مشكلة: GUI لا تظهر على Linux
```bash
python scripts/diagnose_qt.py
export QT_QPA_PLATFORM=xcb
./run_gui.sh
```

### مشكلة: فشل في رفع المشروع
```bash
# تحقق من الاتصال
ssh -T git@github.com

# إعادة تعيين remote
git remote set-url origin git@github.com:DrAbdulmalek/Bilingual-Book-Formatter.git
```

### مشكلة: الواجهة الويب لا تعمل
```bash
cd bilingual-formatter-web
rm -rf node_modules package-lock.json
npm install
npm run dev
```

## 📞 الدعم والمساعدة

- **GitHub Issues**: لتقرير المشاكل
- **GitHub Discussions**: للأسئلة العامة
- **Wiki**: للتوثيق المفصل

## 🎉 تهانينا!

بعد اتباع هذا الدليل، ستكون قد رفعت مشروعاً محسناً وشاملاً يتضمن:

- ✅ واجهة رسومية تعمل على Linux و Windows
- ✅ واجهة ويب عصرية
- ✅ مثبت تلقائي لويندوز
- ✅ أدوات تشخيص وإصلاح
- ✅ بناء تلقائي للإصدارات
- ✅ توثيق شامل
- ✅ اختبارات أساسية

**لا تنس إعطاء المشروع ⭐ على GitHub!**

---

*تم إنشاء هذا الدليل بواسطة Manus AI - أغسطس 2025*

