# 🏨 Hotel Management Website  

یک وبسایت مدیریت هتل با استفاده از **Django** توسعه داده شده است.  
این پروژه شامل مدیریت اتاق‌ها، رویدادها، پیشنهادهای ویژه (offers)، گالری تصاویر و نظرات کاربران (testimonials) می‌باشد.  

---

## ✨ ویژگی‌ها
- مدیریت و رزرو اتاق‌ها (Rooms)  
- نمایش و مدیریت رویدادهای هتل (Events)  
- پیشنهادهای ویژه با تاریخ شروع و پایان (Offers)  
- گالری تصاویر (Gallery)  
- نمایش و مدیریت نظرات و امتیاز کاربران (Testimonials)  
- پنل ادمین حرفه‌ای برای مدیریت محتوا  

---

## 🛠 تکنولوژی‌ها
- [Python 3.11](https://www.python.org/)  
- [Django 5.2](https://www.djangoproject.com/)  
- [SQLite / PostgreSQL] (قابل انتخاب)  
- HTML5, CSS3, Bootstrap / Tailwind  
- Pillow برای مدیریت تصاویر  

---

## ⚙️ نصب و راه‌اندازی
```bash
# 1️⃣ کلون کردن پروژه
git clone https://github.com/Rasool0786/Grandoria-Hotel.git
cd Grandoria-Hotel

# 2️⃣ ساخت محیط مجازی
python -m venv venv
source venv/bin/activate   # برای لینوکس / مک
venv\Scripts\activate      # برای ویندوز

# 3️⃣ نصب وابستگی‌ها
pip install -r requirements.txt

# 4️⃣ اعمال مایگریشن‌ها
python manage.py migrate

# 5️⃣ ساخت سوپر یوزر
python manage.py createsuperuser

# 6️⃣ اجرای سرور توسعه
python manage.py runserver
