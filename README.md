ملف README.md للمشروع

```markdown
# Bilingual Book Formatter v2.3 🌐📖

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub release](https://img.shields.io/badge/release-v2.3-green)](https://github.com/DrAbdulmalek/Bilingual-Book-Formatter/releases)

أداة متطورة لمعالجة الكتب والمستندات ثنائية اللغة تدعم العديد من الصيغ والميزات المتقدمة.

## ✨ الميزات الرئيسية

- **دعم صيغ متعددة**: DOCX, DOC, EPUB, HTML, وغيرها
- **واجهة رسومية متقدمة**: واجهة PyQt6 مع معاينة المحتوى
- **واجهة برمجة تطبيقات (API)**: للدمج مع أنظمة أخرى
- **معالجة الصور**: دعم تضمين الصور وتحويلها إلى صيغ مختلفة
- **دمج الترجمة**: دعم مترجم DeepL وخدمات الترجمة الأخرى
- **تخزين سحابي**: تكامل مع Google Drive
- **معالجة متقدمة**: استخدام multiprocessing للمستندات الكبيرة

## ⚙️ متطلبات النظام

- **Python 3.8+**
- **RAM**: 4GB كحد أدنى (8GB موصى به للمستندات الكبيرة)
- **مساحة تخزين**: 500MB
- **نظام التشغيل**: Windows, macOS, Linux, أو Android (Termux)

## 🚀 التثبيت السريع

### على جهاز الكمبيوتر:
```bash
# استنساخ المشروع
git clone https://github.com/DrAbdulmalek/Bilingual-Book-Formatter.git
cd Bilingual-Book-Formatter

# تثبيت المتطلبات
pip install -r requirements.txt
```

📖 طريقة الاستخدام

عبر سطر الأوامر:

```bash
# معالجة مستندين بلغتين مختلفتين
python bilingual_book_formatter.py --lang1 english.docx --lang2 arabic.docx --output result

# استخدام الواجهة الرسومية
python bilingual_book_formatter.py --gui

# إنشاء مستند EPUB
python bilingual_book_formatter.py --lang1 file1.docx --lang2 file2.docx --format epub
```

عبر الواجهة الرسومية:

1. تشغيل البرنامج بالخيار --gui
2. اختيار الملفات من خلال واجهة التصفح
3. ضبط الإعدادات المطلوبة
4. معاينة النتيجة قبل الحفظ
5. حفظ المخرجات بالصيغة المطلوبة

عبر API:

```bash
curl -X POST "http://localhost:8000/process/" \
     -F "lang1_file=@english.docx" \
     -F "lang2_file=@arabic.docx" \
     -F "output_format=docx" \
     -F "api_key=your_secret_key"
```

🛠️ الإعدادات المتقدمة

تكوين موضع الصور:

```json
{
  "image_alignment": "center",
  "image_format": "webp",
  "max_image_width": "600px"
}
```

إعدادات الخطوط:

```json
{
  "font_english": "Arial",
  "font_arabic": "Traditional Arabic",
  "font_size": "12pt"
}
```

🤝 المساهمة في المشروع

نرحب بمساهماتكم لتطوير هذا المشروع:

1. عمل Fork للمشروع
2. إنشاء فرع للميزة الجديدة (git checkout -b feature/AmazingFeature)
3. حفظ التغييرات (git commit -m 'Add AmazingFeature')
4. رفع التغييرات (git push origin feature/AmazingFeature)
5. فتح طلب دمج (Pull Request)

📊 هيكل المشروع

```
Bilingual-Book-Formatter/
├── app.py                 # التطبيق الرئيسي
├── bilingual_book_formatter.py # المحرك الأساسي
├── requirements.txt       # متطلبات Python
├── docs/                 # الوثائق
├── templates/            # قوالب HTML
└── tests/                # الاختبارات
```

📞 الدعم والمساعدة

· الإبلاغ عن مشاكل: إنشاء Issue جديد
· الأسئلة الشائعة: راجع قسم Wiki
· الاتصال المباشر: عبر البريد الإلكتروني أو من خلال مناقشات GitHub

📄 الترخيص

هذا المشروع مرخص تحت رخصة MIT. انظر ملف LICENSE للتفاصيل.

🙏 الشكر والعرفان

· فريق تطوير Python ومجتمع المصادر المفتوحة
· المساهمون والمختبرون الذين ساعدوا في تطوير الأداة
· جميع المستخدمين الذين قدموا ملاحظات قيمة

---

<div align="center">
تم التطوير بواسطة د عبدالمالك الحسيني / حمص - سوريا <a href="https://github.com/DrAbdulmalek">DrAbdulmalek</a>
</div>
├── app.py                 # التطبيق الرئيسي
├── bilingual_book_formatter.py # المحرك الأساسي
├── requirements.txt       # متطلبات Python
├── docs/                 # الوثائق
├── templates/            # قوالب HTML
└── tests/                # الاختبارات
```

📞 الدعم والمساعدة

· الإبلاغ عن مشاكل: إنشاء Issue جديد
· الأسئلة الشائعة: راجع قسم Wiki
· الاتصال المباشر: عبر البريد الإلكتروني أو من خلال مناقشات GitHub

📄 الترخيص

هذا المشروع مرخص تحت رخصة MIT. انظر ملف LICENSE للتفاصيل.

🙏 الشكر والعرفان

· فريق تطوير Python ومجتمع المصادر المفتوحة
· المساهمون والمختبرون الذين ساعدوا في تطوير الأداة
· جميع المستخدمين الذين قدموا ملاحظات قيمة

---

<div align="center">
تم التطوير بواسطة <a href="https://github.com/DrAbdulmalek">DrAbdulmalek</a>
</div>
