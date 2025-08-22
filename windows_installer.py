#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Windows Installer Script for Bilingual Book Formatter
سكريبت التثبيت التلقائي لويندوز - معالج الكتب ثنائية اللغة
"""

import os
import sys
import subprocess
import urllib.request
import zipfile
import tempfile
import shutil
from pathlib import Path
import json

class WindowsInstaller:
    """مثبت تلقائي لويندوز"""
    
    def __init__(self):
        self.install_dir = Path.home() / "BilingualBookFormatter"
        self.temp_dir = Path(tempfile.gettempdir()) / "bbf_installer"
        self.github_token = "REMOVED_TOKEN"
        
    def create_directories(self):
        """إنشاء المجلدات المطلوبة"""
        print("إنشاء المجلدات...")
        self.install_dir.mkdir(parents=True, exist_ok=True)
        self.temp_dir.mkdir(parents=True, exist_ok=True)
        
    def download_python(self):
        """تحميل Python إذا لم يكن مثبتاً"""
        try:
            subprocess.run([sys.executable, "--version"], check=True, capture_output=True)
            print("Python مثبت بالفعل")
            return True
        except:
            print("تحميل Python...")
            python_url = "https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe"
            python_installer = self.temp_dir / "python_installer.exe"
            
            try:
                urllib.request.urlretrieve(python_url, python_installer)
                subprocess.run([str(python_installer), "/quiet", "InstallAllUsers=1", "PrependPath=1"], check=True)
                print("تم تثبيت Python بنجاح")
                return True
            except Exception as e:
                print(f"فشل في تحميل Python: {e}")
                return False
    
    def download_project(self):
        """تحميل المشروع من GitHub"""
        print("تحميل المشروع من GitHub...")
        
        project_url = "https://github.com/DrAbdulmalek/Bilingual-Book-Formatter/archive/refs/heads/main.zip"
        project_zip = self.temp_dir / "project.zip"
        
        try:
            # إضافة رأس التوكين للمصادقة
            req = urllib.request.Request(project_url)
            if self.github_token:
                req.add_header('Authorization', f'token {self.github_token}')
            
            with urllib.request.urlopen(req) as response:
                with open(project_zip, 'wb') as f:
                    f.write(response.read())
            
            # استخراج الملفات
            with zipfile.ZipFile(project_zip, 'r') as zip_ref:
                zip_ref.extractall(self.temp_dir)
            
            # نسخ الملفات إلى مجلد التثبيت
            extracted_dir = self.temp_dir / "Bilingual-Book-Formatter-main"
            if extracted_dir.exists():
                shutil.copytree(extracted_dir, self.install_dir, dirs_exist_ok=True)
            
            print("تم تحميل المشروع بنجاح")
            return True
            
        except Exception as e:
            print(f"فشل في تحميل المشروع: {e}")
            return False
    
    def install_dependencies(self):
        """تثبيت المتطلبات"""
        print("تثبيت المتطلبات...")
        
        requirements_file = self.install_dir / "requirements.txt"
        if not requirements_file.exists():
            print("ملف requirements.txt غير موجود")
            return False
        
        try:
            subprocess.run([
                sys.executable, "-m", "pip", "install", "-r", str(requirements_file)
            ], check=True)
            print("تم تثبيت المتطلبات بنجاح")
            return True
        except Exception as e:
            print(f"فشل في تثبيت المتطلبات: {e}")
            return False
    
    def create_shortcuts(self):
        """إنشاء اختصارات سطح المكتب"""
        print("إنشاء الاختصارات...")
        
        try:
            # اختصار للواجهة الرسومية
            gui_script = self.install_dir / "run_gui.bat"
            gui_script.write_text(f"""@echo off
cd /d "{self.install_dir}"
python bilingual_book_formatter.py --gui
pause
""", encoding='utf-8')
            
            # اختصار للواجهة الويب
            web_script = self.install_dir / "run_web.bat"
            web_script.write_text(f"""@echo off
cd /d "{self.install_dir}/bilingual-formatter-web"
npm run dev
pause
""", encoding='utf-8')
            
            # اختصار لسطر الأوامر
            cli_script = self.install_dir / "run_cli.bat"
            cli_script.write_text(f"""@echo off
cd /d "{self.install_dir}"
python bilingual_book_formatter.py %*
pause
""", encoding='utf-8')
            
            print("تم إنشاء الاختصارات بنجاح")
            return True
            
        except Exception as e:
            print(f"فشل في إنشاء الاختصارات: {e}")
            return False
    
    def install_nodejs(self):
        """تثبيت Node.js للواجهة الويب"""
        print("فحص Node.js...")
        
        try:
            subprocess.run(["node", "--version"], check=True, capture_output=True)
            print("Node.js مثبت بالفعل")
            return True
        except:
            print("تحميل Node.js...")
            nodejs_url = "https://nodejs.org/dist/v20.18.0/node-v20.18.0-x64.msi"
            nodejs_installer = self.temp_dir / "nodejs_installer.msi"
            
            try:
                urllib.request.urlretrieve(nodejs_url, nodejs_installer)
                subprocess.run(["msiexec", "/i", str(nodejs_installer), "/quiet"], check=True)
                print("تم تثبيت Node.js بنجاح")
                return True
            except Exception as e:
                print(f"فشل في تحميل Node.js: {e}")
                return False
    
    def setup_web_interface(self):
        """إعداد الواجهة الويب"""
        print("إعداد الواجهة الويب...")
        
        web_dir = self.install_dir / "bilingual-formatter-web"
        if not web_dir.exists():
            print("مجلد الواجهة الويب غير موجود")
            return False
        
        try:
            # تثبيت متطلبات npm
            subprocess.run(["npm", "install"], cwd=web_dir, check=True)
            print("تم إعداد الواجهة الويب بنجاح")
            return True
        except Exception as e:
            print(f"فشل في إعداد الواجهة الويب: {e}")
            return False
    
    def create_uninstaller(self):
        """إنشاء أداة إلغاء التثبيت"""
        print("إنشاء أداة إلغاء التثبيت...")
        
        uninstaller_script = self.install_dir / "uninstall.bat"
        uninstaller_script.write_text(f"""@echo off
echo إلغاء تثبيت Bilingual Book Formatter...
cd /d "{self.install_dir.parent}"
rmdir /s /q "{self.install_dir.name}"
echo تم إلغاء التثبيت بنجاح
pause
""", encoding='utf-8')
        
        print("تم إنشاء أداة إلغاء التثبيت")
    
    def cleanup(self):
        """تنظيف الملفات المؤقتة"""
        print("تنظيف الملفات المؤقتة...")
        try:
            shutil.rmtree(self.temp_dir, ignore_errors=True)
            print("تم التنظيف بنجاح")
        except Exception as e:
            print(f"تحذير: فشل في التنظيف: {e}")
    
    def install(self):
        """تشغيل عملية التثبيت الكاملة"""
        print("=== بدء تثبيت Bilingual Book Formatter ===")
        
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
            print(f"\n--- {step_name} ---")
            try:
                if not step_func():
                    print(f"فشل في: {step_name}")
                    return False
            except Exception as e:
                print(f"خطأ في {step_name}: {e}")
                return False
        
        print(f"\n=== تم التثبيت بنجاح! ===")
        print(f"مجلد التثبيت: {self.install_dir}")
        print("\nطرق التشغيل:")
        print("1. الواجهة الرسومية: تشغيل run_gui.bat")
        print("2. الواجهة الويب: تشغيل run_web.bat")
        print("3. سطر الأوامر: تشغيل run_cli.bat")
        
        return True

def main():
    """الدالة الرئيسية"""
    installer = WindowsInstaller()
    
    try:
        success = installer.install()
        if success:
            input("\nاضغط Enter للخروج...")
        else:
            input("\nفشل في التثبيت. اضغط Enter للخروج...")
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

