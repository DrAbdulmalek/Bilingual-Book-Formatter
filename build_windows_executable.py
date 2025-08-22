#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build Windows Executable Script
سكريبت بناء ملف تنفيذي لويندوز
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def create_main_executable():
    """إنشاء ملف تنفيذي رئيسي للتطبيق"""
    
    # إنشاء ملف main.py مبسط
    main_content = '''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bilingual Book Formatter - Main Executable
الملف التنفيذي الرئيسي لمعالج الكتب ثنائية اللغة
"""

import sys
import os
from pathlib import Path

# إضافة المجلد الحالي إلى مسار Python
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

try:
    from bilingual_book_formatter import main
    if __name__ == "__main__":
        main()
except ImportError as e:
    print(f"خطأ في استيراد المكتبات: {e}")
    print("يرجى التأكد من تثبيت جميع المتطلبات")
    input("اضغط Enter للخروج...")
    sys.exit(1)
except Exception as e:
    print(f"خطأ غير متوقع: {e}")
    input("اضغط Enter للخروج...")
    sys.exit(1)
'''
    
    with open('main.py', 'w', encoding='utf-8') as f:
        f.write(main_content)
    
    print("تم إنشاء main.py")

def create_spec_file():
    """إنشاء ملف .spec مخصص لـ PyInstaller"""
    
    spec_content = '''# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('config.json', '.'),
        ('requirements.txt', '.'),
        ('README.md', '.'),
        ('bilingual-formatter-web', 'bilingual-formatter-web'),
    ],
    hiddenimports=[
        'docx',
        'pdfplumber',
        'ebooklib',
        'PIL',
        'deepl',
        'googleapiclient',
        'PyQt6',
        'beautifulsoup4',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='BilingualBookFormatter',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='favicon.ico' if os.path.exists('favicon.ico') else None,
)
'''
    
    with open('BilingualBookFormatter.spec', 'w', encoding='utf-8') as f:
        f.write(spec_content)
    
    print("تم إنشاء ملف .spec")

def create_batch_files():
    """إنشاء ملفات batch لتشغيل التطبيق"""
    
    # ملف تشغيل الواجهة الرسومية
    gui_batch = '''@echo off
chcp 65001 > nul
title Bilingual Book Formatter - GUI
echo تشغيل الواجهة الرسومية...
BilingualBookFormatter.exe --gui
if errorlevel 1 (
    echo حدث خطأ في تشغيل التطبيق
    pause
)
'''
    
    # ملف تشغيل الواجهة الويب
    web_batch = '''@echo off
chcp 65001 > nul
title Bilingual Book Formatter - Web Interface
echo تشغيل الواجهة الويب...
cd bilingual-formatter-web
if exist node_modules (
    npm run dev
) else (
    echo تثبيت المتطلبات...
    npm install
    npm run dev
)
pause
'''
    
    # ملف تشغيل سطر الأوامر
    cli_batch = '''@echo off
chcp 65001 > nul
title Bilingual Book Formatter - Command Line
echo استخدام سطر الأوامر:
echo BilingualBookFormatter.exe --lang1 file1.docx --lang2 file2.docx --output result
echo.
BilingualBookFormatter.exe %*
pause
'''
    
    with open('run_gui.bat', 'w', encoding='utf-8') as f:
        f.write(gui_batch)
    
    with open('run_web.bat', 'w', encoding='utf-8') as f:
        f.write(web_batch)
    
    with open('run_cli.bat', 'w', encoding='utf-8') as f:
        f.write(cli_batch)
    
    print("تم إنشاء ملفات batch")

def build_executable():
    """بناء الملف التنفيذي"""
    
    print("بناء الملف التنفيذي...")
    
    try:
        # تنظيف المجلدات السابقة
        if os.path.exists('build'):
            shutil.rmtree('build')
        if os.path.exists('dist'):
            shutil.rmtree('dist')
        
        # بناء الملف التنفيذي
        subprocess.run([
            'pyinstaller',
            '--clean',
            'BilingualBookFormatter.spec'
        ], check=True)
        
        print("تم بناء الملف التنفيذي بنجاح!")
        
        # نسخ ملفات batch إلى مجلد dist
        for batch_file in ['run_gui.bat', 'run_web.bat', 'run_cli.bat']:
            if os.path.exists(batch_file):
                shutil.copy2(batch_file, 'dist/')
        
        print("تم نسخ ملفات التشغيل")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"فشل في بناء الملف التنفيذي: {e}")
        return False
    except Exception as e:
        print(f"خطأ غير متوقع: {e}")
        return False

def create_installer_package():
    """إنشاء حزمة التثبيت"""
    
    print("إنشاء حزمة التثبيت...")
    
    # إنشاء مجلد الحزمة
    package_dir = Path('BilingualBookFormatter_Package')
    if package_dir.exists():
        shutil.rmtree(package_dir)
    
    package_dir.mkdir()
    
    # نسخ الملفات المطلوبة
    files_to_copy = [
        'dist/BilingualBookFormatter.exe',
        'dist/run_gui.bat',
        'dist/run_web.bat', 
        'dist/run_cli.bat',
        'README.md',
        'config.json',
        'requirements.txt'
    ]
    
    for file_path in files_to_copy:
        if os.path.exists(file_path):
            shutil.copy2(file_path, package_dir)
    
    # نسخ مجلد الواجهة الويب
    if os.path.exists('bilingual-formatter-web'):
        shutil.copytree('bilingual-formatter-web', package_dir / 'bilingual-formatter-web')
    
    # إنشاء ملف README للحزمة
    readme_content = '''# Bilingual Book Formatter v2.3

## طريقة الاستخدام:

### 1. الواجهة الرسومية:
- تشغيل ملف `run_gui.bat`
- أو تشغيل `BilingualBookFormatter.exe --gui`

### 2. الواجهة الويب:
- تشغيل ملف `run_web.bat`
- فتح المتصفح على http://localhost:5173

### 3. سطر الأوامر:
- تشغيل ملف `run_cli.bat`
- أو استخدام: `BilingualBookFormatter.exe --lang1 file1.docx --lang2 file2.docx --output result`

## المتطلبات:
- Windows 10 أو أحدث
- Node.js (للواجهة الويب)

## الدعم:
- GitHub: https://github.com/DrAbdulmalek/Bilingual-Book-Formatter
- البريد الإلكتروني: [البريد الإلكتروني]

تم التطوير بواسطة د. عبدالمالك تامر الحسيني
'''
    
    with open(package_dir / 'README_Package.txt', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"تم إنشاء حزمة التثبيت في: {package_dir}")
    
    return package_dir

def main():
    """الدالة الرئيسية"""
    
    print("=== بناء ملف تنفيذي لويندوز ===")
    
    steps = [
        ("إنشاء الملف الرئيسي", create_main_executable),
        ("إنشاء ملف .spec", create_spec_file),
        ("إنشاء ملفات batch", create_batch_files),
        ("بناء الملف التنفيذي", build_executable),
        ("إنشاء حزمة التثبيت", create_installer_package),
    ]
    
    for step_name, step_func in steps:
        print(f"\n--- {step_name} ---")
        try:
            result = step_func()
            if result is False:
                print(f"فشل في: {step_name}")
                return False
        except Exception as e:
            print(f"خطأ في {step_name}: {e}")
            return False
    
    print("\n=== تم بناء الملف التنفيذي بنجاح! ===")
    print("الملفات متاحة في:")
    print("- dist/BilingualBookFormatter.exe")
    print("- BilingualBookFormatter_Package/")
    
    return True

if __name__ == "__main__":
    main()

