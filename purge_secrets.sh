#!/bin/bash
echo "=== إزالة جميع التوكنات من تاريخ Git ==="

FILES_TO_CLEAN=(
    "GITHUB_UPLOAD_GUIDE.md"
    "QUICK_START_COMMANDS.md"
    "windows_installer.py"
)

# تشغيل filter-branch لمسح الملفات من كل الكوميتات
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch ${FILES_TO_CLEAN[*]}" \
  --prune-empty --tag-name-filter cat -- --all

echo "✅ تم تنظيف التاريخ من الملفات الحساسة"

# إعادة رفع بالقوة
git push origin --force --all
git push origin --force --tags

echo "🚀 المشروع مرفوع بدون أي توكنات في التاريخ"
