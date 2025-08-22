#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Qt Diagnostic Tool for Bilingual Book Formatter
أداة تشخيص Qt لمعالج الكتب ثنائية اللغة
"""

import sys
import os
import platform
from pathlib import Path

def print_system_info():
    """طباعة معلومات النظام"""
    print("=== معلومات النظام ===")
    print(f"نظام التشغيل: {platform.system()} {platform.release()}")
    print(f"إصدار Python: {sys.version}")
    print(f"مسار Python: {sys.executable}")
    print(f"المجلد الحالي: {os.getcwd()}")
    print(f"DISPLAY: {os.environ.get('DISPLAY', 'غير محدد')}")
    print(f"XDG_SESSION_TYPE: {os.environ.get('XDG_SESSION_TYPE', 'غير محدد')}")
    print(f"QT_QPA_PLATFORM: {os.environ.get('QT_QPA_PLATFORM', 'غير محدد')}")
    print()

def test_qt_import():
    """اختبار استيراد مكتبات Qt"""
    print("=== اختبار استيراد Qt ===")
    
    # اختبار PyQt6
    try:
        from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
        from PyQt6.QtCore import QTimer
        print("✓ PyQt6 متاح")
        return "PyQt6"
    except ImportError as e:
        print(f"✗ PyQt6 غير متاح: {e}")
    
    # اختبار PySide6 كبديل
    try:
        from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
        from PySide6.QtCore import QTimer
        print("✓ PySide6 متاح (بديل)")
        return "PySide6"
    except ImportError as e:
        print(f"✗ PySide6 غير متاح: {e}")
    
    # اختبار PyQt5 كبديل أخير
    try:
        from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
        from PyQt5.QtCore import QTimer
        print("✓ PyQt5 متاح (بديل قديم)")
        return "PyQt5"
    except ImportError as e:
        print(f"✗ PyQt5 غير متاح: {e}")
    
    print("✗ لا توجد مكتبة Qt متاحة!")
    return None

def test_qt_window(qt_lib):
    """اختبار إنشاء نافذة Qt"""
    print(f"=== اختبار نافذة {qt_lib} ===")
    
    try:
        if qt_lib == "PyQt6":
            from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
            from PyQt6.QtCore import QTimer
        elif qt_lib == "PySide6":
            from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
            from PySide6.QtCore import QTimer
        elif qt_lib == "PyQt5":
            from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
            from PyQt5.QtCore import QTimer
        else:
            print("مكتبة Qt غير مدعومة")
            return False
        
        # إنشاء التطبيق
        app = QApplication(sys.argv)
        
        # إنشاء النافذة
        window = QWidget()
        window.setWindowTitle("Qt Diagnostic Test")
        window.setGeometry(100, 100, 400, 200)
        
        # إضافة محتوى
        layout = QVBoxLayout()
        label = QLabel(f"اختبار {qt_lib} نجح!\nهذه النافذة ستُغلق تلقائياً خلال 5 ثوانٍ")
        label.setStyleSheet("font-size: 14px; padding: 20px;")
        layout.addWidget(label)
        window.setLayout(layout)
        
        # عرض النافذة
        window.show()
        
        # إغلاق تلقائي بعد 5 ثوانٍ
        timer = QTimer()
        timer.timeout.connect(app.quit)
        timer.start(5000)
        
        print("✓ تم إنشاء النافذة بنجاح")
        print("إذا ظهرت النافذة، فإن Qt يعمل بشكل صحيح")
        
        # تشغيل حلقة الأحداث
        app.exec()
        return True
        
    except Exception as e:
        print(f"✗ فشل في إنشاء النافذة: {e}")
        return False

def check_dependencies():
    """فحص التبعيات الأخرى"""
    print("=== فحص التبعيات ===")
    
    dependencies = [
        ("docx", "python-docx"),
        ("pdfplumber", "pdfplumber"),
        ("ebooklib", "ebooklib"),
        ("PIL", "Pillow"),
        ("bs4", "beautifulsoup4"),
        ("deepl", "deepl"),
        ("fastapi", "fastapi"),
        ("uvicorn", "uvicorn")
    ]
    
    for module, package in dependencies:
        try:
            __import__(module)
            print(f"✓ {package}")
        except ImportError:
            print(f"✗ {package} (غير مثبت)")

def suggest_fixes():
    """اقتراح حلول للمشاكل الشائعة"""
    print("=== اقتراحات الإصلاح ===")
    
    system = platform.system()
    
    if system == "Linux":
        print("لـ Arch Linux/Manjaro:")
        print("  sudo pacman -S python-pyqt6 python-pyqt6-sip qt6-wayland")
        print()
        print("لـ Ubuntu/Debian:")
        print("  sudo apt install python3-pyqt6 python3-pyqt6.qtwidgets")
        print()
        print("إعداد متغيرات البيئة:")
        print("  export QT_QPA_PLATFORM=xcb")
        print("  # أو للـ Wayland:")
        print("  export QT_QPA_PLATFORM=wayland")
        print()
        
    elif system == "Darwin":  # macOS
        print("لـ macOS:")
        print("  brew install pyqt6")
        print("  pip install PyQt6")
        print()
        
    elif system == "Windows":
        print("لـ Windows:")
        print("  pip install PyQt6")
        print()
    
    print("إذا استمرت المشاكل:")
    print("1. تأكد من تشغيل X11 أو Wayland")
    print("2. جرب تشغيل التطبيق من terminal")
    print("3. تحقق من صلاحيات الملفات")
    print("4. أعد تثبيت PyQt6: pip uninstall PyQt6 && pip install PyQt6")

def main():
    """الدالة الرئيسية"""
    print("أداة تشخيص Qt لمعالج الكتب ثنائية اللغة")
    print("=" * 50)
    print()
    
    # طباعة معلومات النظام
    print_system_info()
    
    # اختبار استيراد Qt
    qt_lib = test_qt_import()
    print()
    
    # اختبار النافذة إذا كان Qt متاحاً
    if qt_lib:
        test_qt_window(qt_lib)
        print()
    
    # فحص التبعيات الأخرى
    check_dependencies()
    print()
    
    # اقتراح حلول
    suggest_fixes()
    
    print()
    print("انتهى التشخيص.")
    
    if not qt_lib:
        print("تحذير: لا توجد مكتبة Qt متاحة. الواجهة الرسومية لن تعمل.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

