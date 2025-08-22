#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enhanced Windows Installer Script for Bilingual Book Formatter
سكريپت التثبيت المحسن لويندوز - معالج الكتب ثنائية اللغة
"""

import os
import sys
import subprocess
import urllib.request
import zipfile
import tempfile
import shutil
import json
from pathlib import Path
from urllib.parse import urlparse

class EnhancedWindowsInstaller:
    """مثبت محسن لويندوز مع تقرير التقدم ومعالجة أخطاء محسنة"""
    
    def __init__(self):
        self.install_dir = Path.home() / "BilingualBookFormatter"
        self.temp_dir = Path(tempfile.gettempdir()) / "bbf_installer"
        self.progress_callback = None
        
    def set_progress_callback(self, callback):
        """تعيين دالة لتقرير التقدم"""
        self.progress_callback = callback
        
    def report_progress(self, message, percentage=None):
        """تقرير التقدم"""
        if self.progress_callback:
            self.progress_callback(message, percentage)
        else:
            if percentage is not None:
                print(f"[{percentage:3.0f}%] {message}")
            else:
                print(f"[INFO] {message}")
    
    def create_directories(self):
        """إنشاء المجلدات المطلوبة"""
        self.report_progress("إنشاء المجلدات...", 5)
        try:
            self.install_dir.mkdir(parents=True, exist_ok=True)
            self.temp_dir.mkdir(parents=True, exist_ok=True)
            return True
        except Exception as e:
            self.report_progress(f"فشل في إنشاء المجلدات: {e}")
            return False
    
    def check_python(self):
        """فحص وجود Python"""
        self.report_progress("فحص Python...", 10)
        try:
            result = subprocess.run([sys.executable, "--version"], 
                                  check=True, capture_output=True, text=True)
            version = result.stdout.strip()
            self.report_progress(f"Python موجود: {version}")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
    
    def download_python(self):
        """تحميل وتثبيت Python"""
        if self.check_python():
            return True
            
        self.report_progress("تحميل Python...", 15)
        python_url = "https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe"
        python_installer = self.temp_dir / "python_installer.exe"
        
        try:
            def progress_hook(block_num, block_size, total_size):
                if total_size > 0:
                    percentage = min(100, (block_num * block_size * 100) // total_size)
                    self.report_progress(f"تحميل Python... {percentage}%", 15 + percentage * 0.1)
            
            urllib.request.urlretrieve(python_url, python_installer, reporthook=progress_hook)
            
            self.report_progress("تثبيت Python...", 30)
            subprocess.run([
                str(python_installer), 
                "/quiet", 
                "InstallAllUsers=1", 
                "PrependPath=1",
                "Include_test=0"
            ], check=True)
            
            self.report_progress("تم تثبيت Python بنجاح", 35)
            return True
            
        except Exception as e:
            self.report_progress(f"فشل في تحميل/تثبيت Python: {e}")
            return False
    
    def download_project(self):
        """تحميل المشروع من GitHub"""
        self.report_progress("تحميل المشروع من GitHub...", 40)
        
        # استخدام رابط عام بدون توكين
        project_url = "https://github.com/DrAbdulmalek/Bilingual-Book-Formatter/archive/refs/heads/main.zip"
        project_zip = self.temp_dir / "project.zip"
        
        try:
            def progress_hook(block_num, block_size, total_size):
                if total_size > 0:
                    percentage = min(100, (block_num * block_size * 100) // total_size)
                    self.report_progress(f"تحميل المشروع... {percentage}%", 40 + percentage * 0.2)
            
            urllib.request.urlretrieve(project_url, project_zip, reporthook=progress_hook)
            
            self.report_progress("استخراج الملفات...", 65)
            with zipfile.ZipFile(project_zip, 'r') as zip_ref:
                zip_ref.extractall(self.temp_dir)
            
            # نسخ الملفات إلى مجلد التثبيت
            extracted_dir = self.temp_dir / "Bilingual-Book-Formatter-main"
            if extracted_dir.exists():
                if self.install_dir.exists():
                    shutil.rmtree(self.install_dir)
                shutil.copytree(extracted_dir, self.install_dir)
            
            self.report_progress("تم تحميل المشروع بنجاح", 70)
            return True
            
        except Exception as e:
            self.report_progress(f"فشل في تحميل المشروع: {e}")
            return False
    
    def install_dependencies(self):
        """تثبيت المتطلبات"""
        self.report_progress("تثبيت متطلبات Python...", 75)
        
        requirements_file = self.install_dir / "requirements.txt"
        if not requirements_file.exists():
            self.report_progress("ملف requirements.txt غير موجود، تثبيت المتطلبات الأساسية...")
            basic_requirements = [
                "PyQt6", "python-docx", "pdfplumber", "ebooklib", 
                "Pillow", "beautifulsoup4", "deepl", "fastapi", "uvicorn"
            ]
            
            for i, package in enumerate(basic_requirements):
                try:
                    self.report_progress(f"تثبيت {package}...", 75 + (i * 2))
                    subprocess.run([
                        sys.executable, "-m", "pip", "install", package
                    ], check=True, capture_output=True)
                except subprocess.CalledProcessError as e:
                    self.report_progress(f"تحذير: فشل في تثبيت {package}")
            
            return True
        
        try:
            subprocess.run([
                sys.executable, "-m", "pip", "install", "-r", str(requirements_file)
            ], check=True, capture_output=True)
            
            self.report_progress("تم تثبيت المتطلبات بنجاح", 85)
            return True
            
        except subprocess.CalledProcessError as e:
            self.report_progress(f"فشل في تثبيت المتطلبات: {e}")
            return False
    
    def check_nodejs(self):
        """فحص وجود Node.js"""
        try:
            result = subprocess.run(["node", "--version"], 
                                  check=True, capture_output=True, text=True)
            version = result.stdout.strip()
            self.report_progress(f"Node.js موجود: {version}")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
    
    def install_nodejs(self):
        """تثبيت Node.js للواجهة الويب"""
        if self.check_nodejs():
            return True
            
        self.report_progress("تحميل Node.js...", 87)
        nodejs_url = "https://nodejs.org/dist/v20.18.0/node-v20.18.0-x64.msi"
        nodejs_installer = self.temp_dir / "nodejs_installer.msi"
        
        try:
            urllib.request.urlretrieve(nodejs_url, nodejs_installer)
            
            self.report_progress("تثبيت Node.js...", 90)
            subprocess.run([
                "msiexec", "/i", str(nodejs_installer), "/quiet"
            ], check=True)
            
            self.report_progress("تم تثبيت Node.js بنجاح", 92)
            return True
            
        except Exception as e:
            self.report_progress(f"فشل في تثبيت Node.js: {e}")
            return False
    
    def setup_web_interface(self):
        """إعداد الواجهة الويب"""
        self.report_progress("إعداد الواجهة الويب...", 94)
        
        web_dir = self.install_dir / "bilingual-formatter-web"
        if not web_dir.exists():
            self.report_progress("مجلد الواجهة الويب غير موجود، تخطي...")
            return True
        
        try:
            # تثبيت متطلبات npm
            subprocess.run(["npm", "install"], cwd=web_dir, check=True, capture_output=True)
            self.report_progress("تم إعداد الواجهة الويب بنجاح", 96)
            return True
            
        except subprocess.CalledProcessError as e:
            self.report_progress(f"تحذير: فشل في إعداد الواجهة الويب: {e}")
            return True  # لا نفشل التثبيت بسبب الواجهة الويب
    
    def create_shortcuts(self):
        """إنشاء اختصارات سطح المكتب"""
        self.report_progress("إنشاء الاختصارات...", 97)
        
        try:
            # اختصار للواجهة الرسومية
            gui_script = self.install_dir / "run_gui.bat"
            gui_script.write_text(f"""@echo off
chcp 65001 > nul
title Bilingual Book Formatter - GUI
cd /d "{self.install_dir}"
python bilingual_book_formatter.py --gui
if errorlevel 1 (
    echo حدث خطأ في تشغيل التطبيق
    pause
)
""", encoding='utf-8')
            
            # اختصار للواجهة الويب
            web_script = self.install_dir / "run_web.bat"
            web_script.write_text(f"""@echo off
chcp 65001 > nul
title Bilingual Book Formatter - Web Interface
cd /d "{self.install_dir}/bilingual-formatter-web"
if exist node_modules (
    echo تشغيل الواجهة الويب...
    npm run dev
) else (
    echo تثبيت المتطلبات...
    npm install
    if errorlevel 0 (
        npm run dev
    ) else (
        echo فشل في تثبيت المتطلبات
        pause
    )
)
""", encoding='utf-8')
            
            # اختصار لسطر الأوامر
            cli_script = self.install_dir / "run_cli.bat"
            cli_script.write_text(f"""@echo off
chcp 65001 > nul
title Bilingual Book Formatter - Command Line
cd /d "{self.install_dir}"
echo استخدام سطر الأوامر:
echo python bilingual_book_formatter.py --lang1 file1.docx --lang2 file2.docx --output result
echo.
python bilingual_book_formatter.py %*
pause
""", encoding='utf-8')
            
            self.report_progress("تم إنشاء الاختصارات بنجاح", 98)
            return True
            
        except Exception as e:
            self.report_progress(f"فشل في إنشاء الاختصارات: {e}")
            return False
    
    def create_uninstaller(self):
        """إنشاء أداة إلغاء التثبيت"""
        self.report_progress("إنشاء أداة إلغاء التثبيت...", 99)
        
        try:
            uninstaller_script = self.install_dir / "uninstall.bat"
            uninstaller_script.write_text(f"""@echo off
chcp 65001 > nul
title إلغاء تثبيت Bilingual Book Formatter
echo.
echo هذا سيحذف جميع ملفات Bilingual Book Formatter
echo المجلد: {self.install_dir}
echo.
set /p confirm=هل أنت متأكد؟ (y/N): 
if /i "%confirm%" neq "y" (
    echo تم إلغاء العملية
    pause
    exit /b
)

echo إلغاء تثبيت Bilingual Book Formatter...
cd /d "{self.install_dir.parent}"
rmdir /s /q "{self.install_dir.name}"
if errorlevel 1 (
    echo فشل في حذف بعض الملفات. يرجى حذفها يدوياً.
) else (
    echo تم إلغاء التثبيت بنجاح
)
pause
""", encoding='utf-8')
            
            return True
            
        except Exception as e:
            self.report_progress(f"فشل في إنشاء أداة إلغاء التثبيت: {e}")
            return False
    
    def cleanup(self):
        """تنظيف الملفات المؤقتة"""
        self.report_progress("تنظيف الملفات المؤقتة...", 100)
        try:
            shutil.rmtree(self.temp_dir, ignore_errors=True)
            return True
        except Exception as e:
            self.report_progress(f"تحذير: فشل في التنظيف: {e}")
            return True  # لا نفشل التثبيت بسبب التنظيف
    
    def install(self):
        """تشغيل عملية التثبيت الكاملة"""
        self.report_progress("بدء تثبيت Bilingual Book Formatter", 0)
        
        steps = [
            ("إنشاء المجلدات", self.create_directories),
            ("تحميل Python", self.download_python),
            ("تحميل المشروع", self.download_project),
            ("تثبيت المتطلبات", self.install_dependencies),
            ("تثبيت Node.js", self.install_nodejs),
            ("إعداد الواجهة الويب", self.setup_web_interface),
            ("إنشاء الاختصارات", self.create_shortcuts),
            ("إنشاء أداة إلغاء التثبيت", self.create_uninstaller),
            ("تنظيف الملفات المؤقتة", self.cleanup)
        ]
        
        for step_name, step_func in steps:
            try:
                if not step_func():
                    self.report_progress(f"فشل في: {step_name}")
                    return False
            except Exception as e:
                self.report_progress(f"خطأ في {step_name}: {e}")
                return False
        
        self.report_progress("تم التثبيت بنجاح!", 100)
        return True
    
    def show_completion_message(self):
        """عرض رسالة الإكمال"""
        print(f"\n{'='*60}")
        print("تم تثبيت Bilingual Book Formatter بنجاح!")
        print(f"{'='*60}")
        print(f"مجلد التثبيت: {self.install_dir}")
        print("\nطرق التشغيل:")
        print("1. الواجهة الرسومية: تشغيل run_gui.bat")
        print("2. الواجهة الويب: تشغيل run_web.bat")
        print("3. سطر الأوامر: تشغيل run_cli.bat")
        print("\nلإلغاء التثبيت: تشغيل uninstall.bat")
        print(f"{'='*60}")

def main():
    """الدالة الرئيسية"""
    installer = EnhancedWindowsInstaller()
    
    try:
        success = installer.install()
        if success:
            installer.show_completion_message()
            input("\nاضغط Enter للخروج...")
        else:
            print("\nفشل في التثبيت.")
            input("اضغط Enter للخروج...")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\nتم إلغاء التثبيت بواسطة المستخدم")
        sys.exit(1)
    except Exception as e:
        print(f"\nخطأ غير متوقع: {e}")
        input("اضغط Enter للخروج...")
        sys.exit(1)

if __name__ == "__main__":
    main()

