#!/bin/bash
# سكريپت نشر آمن لـ GitHub باستخدام SSH
# يتجنب استخدام التوكينات لضمان الأمان

set -euo pipefail

echo "=== نشر مشروع Bilingual Book Formatter على GitHub ==="

# التحقق من الأدوات المطلوبة
for cmd in git ssh; do
    if ! command -v "$cmd" >/dev/null 2>&1; then
        echo "خطأ: $cmd غير مثبت"
        echo "يرجى تثبيت git و openssh"
        exit 1
    fi
done

# طلب المعلومات من المستخدم
read -p "اسم المستخدم على GitHub (مثل DrAbdulmalek): " USER
read -p "اسم المستودع (مثل Bilingual-Book-Formatter): " REPO
read -p "رسالة الـ commit (مثل 'تحديث v2.4 مع تحسينات GUI'): " COMMIT_MSG

# التحقق من إعداد SSH
echo "التحقق من إعداد SSH..."
if [ ! -f ~/.ssh/id_rsa ] && [ ! -f ~/.ssh/id_ed25519 ]; then
    echo "لا يوجد مفتاح SSH. إنشاء مفتاح جديد..."
    read -p "أدخل بريدك الإلكتروني: " EMAIL
    ssh-keygen -t ed25519 -C "$EMAIL" -f ~/.ssh/id_ed25519 -N ""
    
    echo ""
    echo "تم إنشاء مفتاح SSH. يرجى إضافة المفتاح العام التالي إلى GitHub:"
    echo "GitHub → Settings → SSH and GPG keys → New SSH key"
    echo ""
    cat ~/.ssh/id_ed25519.pub
    echo ""
    read -p "اضغط Enter بعد إضافة المفتاح إلى GitHub..."
fi

# تشغيل ssh-agent وإضافة المفتاح
eval "$(ssh-agent -s)"
if [ -f ~/.ssh/id_ed25519 ]; then
    ssh-add ~/.ssh/id_ed25519
elif [ -f ~/.ssh/id_rsa ]; then
    ssh-add ~/.ssh/id_rsa
fi

# اختبار الاتصال بـ GitHub
echo "اختبار الاتصال بـ GitHub..."
if ! ssh -T git@github.com 2>&1 | grep -q "successfully authenticated"; then
    echo "فشل الاتصال بـ GitHub. يرجى التحقق من:"
    echo "1. إضافة المفتاح العام إلى GitHub"
    echo "2. صحة اسم المستخدم"
    echo "3. الاتصال بالإنترنت"
    exit 1
fi

echo "✓ تم التحقق من الاتصال بـ GitHub"

# إعداد git إذا لم يكن مُعداً
if [ ! -d ".git" ]; then
    echo "إنشاء مستودع git جديد..."
    git init
    git branch -M main
fi

# إعداد معلومات المستخدم إذا لم تكن مُعدة
if [ -z "$(git config --global user.name 2>/dev/null || true)" ]; then
    read -p "أدخل اسمك للـ git config: " GIT_NAME
    git config --global user.name "$GIT_NAME"
fi

if [ -z "$(git config --global user.email 2>/dev/null || true)" ]; then
    read -p "أدخل بريدك الإلكتروني للـ git config: " GIT_EMAIL
    git config --global user.email "$GIT_EMAIL"
fi

# إضافة الملفات وعمل commit
echo "إضافة الملفات..."
git add .

# التحقق من وجود تغييرات
if git diff --staged --quiet; then
    echo "لا توجد تغييرات جديدة للـ commit"
else
    echo "عمل commit للتغييرات..."
    git commit -m "$COMMIT_MSG"
fi

# إعداد remote origin
REMOTE_URL="git@github.com:${USER}/${REPO}.git"
if git remote get-url origin >/dev/null 2>&1; then
    echo "تحديث remote origin..."
    git remote set-url origin "$REMOTE_URL"
else
    echo "إضافة remote origin..."
    git remote add origin "$REMOTE_URL"
fi

# التحقق من وجود المستودع على GitHub
echo "التحقق من وجود المستودع..."
if ! git ls-remote --exit-code origin >/dev/null 2>&1; then
    echo "تحذير: المستودع غير موجود أو لا توجد صلاحيات للوصول إليه"
    echo "يرجى التأكد من:"
    echo "1. إنشاء المستودع على GitHub: https://github.com/new"
    echo "2. صحة اسم المستخدم واسم المستودع"
    echo "3. صلاحيات SSH"
    read -p "هل تريد المتابعة؟ (y/N): " CONTINUE
    if [[ ! "$CONTINUE" =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# رفع الملفات
echo "رفع الملفات إلى GitHub..."
if git push -u origin main; then
    echo ""
    echo "✅ تم النشر بنجاح!"
    echo "رابط المستودع: https://github.com/${USER}/${REPO}"
    echo ""
    
    # اقتراح إنشاء release
    read -p "هل تريد إنشاء tag للإصدار؟ (y/N): " CREATE_TAG
    if [[ "$CREATE_TAG" =~ ^[Yy]$ ]]; then
        read -p "أدخل رقم الإصدار (مثل v2.4.0): " VERSION
        git tag "$VERSION"
        git push origin "$VERSION"
        echo "✅ تم إنشاء tag: $VERSION"
        echo "سيتم بناء الملف التنفيذي تلقائياً عبر GitHub Actions"
    fi
    
else
    echo "فشل في رفع الملفات. يرجى التحقق من:"
    echo "1. الاتصال بالإنترنت"
    echo "2. صلاحيات المستودع"
    echo "3. حالة المستودع المحلي"
    
    # اقتراح حلول
    echo ""
    echo "حلول مقترحة:"
    echo "git pull --rebase origin main  # لدمج التغييرات البعيدة"
    echo "git push --force-with-lease origin main  # للرفع القسري (احذر!)"
    exit 1
fi

echo ""
echo "نصائح:"
echo "- لإنشاء إصدار جديد: git tag v2.4.1 && git push origin v2.4.1"
echo "- لعرض الحالة: git status"
echo "- لعرض السجل: git log --oneline"

