#!/bin/bash
echo "=== تنظيف المشروع من التوكنات وإعادة رفعه على GitHub ==="

# ملفات حساسة اكتشفها GitHub
FILES_TO_CLEAN=(
    "GITHUB_UPLOAD_GUIDE.md"
    "QUICK_START_COMMANDS.md"
    "windows_installer.py"
)

# استبدال أي توكن ghp_XXXXXX بنص وهمي
for FILE in "${FILES_TO_CLEAN[@]}"; do
    if [ -f "$FILE" ]; then
        echo "🔍 تنظيف $FILE ..."
        sed -i 's/ghp_[A-Za-z0-9]*/YOUR_GITHUB_TOKEN_HERE/g' "$FILE"
    fi
done

# إضافة الملفات بعد التنظيف
git add "${FILES_TO_CLEAN[@]}"

# تعديل آخر كوميت
git commit --amend --no-edit

# تحديد الفرع (main أو master)
if git show-ref --verify --quiet refs/heads/main; then
    BRANCH="main"
elif git show-ref --verify --quiet refs/heads/master; then
    BRANCH="master"
else
    BRANCH="main"
    git branch -M main
fi

echo "🚀 إعادة رفع المشروع على الفرع: $BRANCH"

# رفع مع إجبار (force) لتجاوز الكوميتات القديمة
git push -u origin "$BRANCH" --force

echo "✅ تم تنظيف ورفع المشروع بنجاح بدون توكنات!"
