import os

def create_slide_file(filename, day_num, title, subtitle, axis_text, slides_content):
    template = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>اليوم {day_num}: {title} | عرض تقديمي</title>
<script src="https://cdn.tailwindcss.com"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/fontsource/fonts/tajawal@latest/arabic-400-normal.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/fontsource/fonts/tajawal@latest/arabic-700-normal.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />
<style>
  body {{
    font-family: 'Tajawal', sans-serif;
    background: #0f172a;
    color: #fff;
    margin: 0;
    padding: 0;
    height: 100vh;
  }}
  .swiper {{
    width: 100%;
    height: 100vh;
  }}
  .swiper-slide {{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 40px;
    box-sizing: border-box;
    text-align: center;
  }}
  .slide-bg-1 {{ background: linear-gradient(135deg, #0f172a 0%, #064e3b 100%); }}
  .slide-bg-2 {{ background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); }}
  .content-box {{
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 16px;
    padding: 40px;
    max-width: 900px;
    width: 100%;
    text-align: right;
    box-shadow: 0 20px 40px rgba(0,0,0,0.3);
  }}
  .title-text {{
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 20px;
    color: #34d399;
  }}
  .theory-box {{
    background: rgba(255, 255, 255, 0.1);
    border-right: 4px solid #059669;
    padding: 20px;
    border-radius: 8px;
    margin-bottom: 16px;
    color: #e2e8f0;
  }}
  .step-card {{
    background: rgba(255,255,255,0.05);
    border-right: 4px solid #059669;
    padding: 16px 20px;
    border-radius: 8px;
    margin-bottom: 12px;
  }}
  .step-num {{
    background: #059669;
    color: #fff;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    margin-left: 10px;
  }}
  .shortcut-key {{
    background: #1e293b;
    color: #34d399;
    padding: 3px 8px;
    border-radius: 4px;
    font-family: Consolas, monospace;
    font-size: 14px;
    margin: 0 2px;
    direction: ltr;
    display: inline-block;
  }}
  .formula-chip {{
    background: rgba(16, 184, 129, 0.15);
    border: 1px solid #10b981;
    color: #a7f3d0;
    padding: 6px 12px;
    border-radius: 6px;
    font-family: Consolas, monospace;
    direction: ltr;
    display: inline-block;
    margin: 4px 0;
  }}
  
  /* Swiper Pagination and Nav */
  .swiper-pagination-bullet {{ background: #fff; opacity: 0.5; }}
  .swiper-pagination-bullet-active {{ background: #34d399; opacity: 1; }}
  .swiper-button-next, .swiper-button-prev {{ color: #34d399; }}
  
  .back-btn {{
    position: absolute;
    top: 20px;
    right: 20px;
    z-index: 100;
    background: rgba(255,255,255,0.1);
    padding: 10px 20px;
    border-radius: 8px;
    color: #fff;
    text-decoration: none;
    font-weight: bold;
    display: flex;
    align-items: center;
    gap: 8px;
    transition: 0.3s;
  }}
  .back-btn:hover {{ background: rgba(255,255,255,0.2); }}
</style>
</head>
<body>

<a href="index.html" class="back-btn"><i class="fas fa-arrow-right"></i> العودة للرئيسية</a>

<div class="swiper mySwiper">
  <div class="swiper-wrapper">
    
    <!-- Slide 1: Welcome -->
    <div class="swiper-slide slide-bg-1">
      <i class="fas fa-file-excel text-7xl text-emerald-400 mb-6"></i>
      <h1 class="text-5xl font-bold text-white mb-4">اليوم {day_num}: {title}</h1>
      <p class="text-xl text-emerald-200">{subtitle}</p>
      <div class="mt-8 bg-emerald-900/50 px-6 py-3 rounded-full text-emerald-100">
        {axis_text}
      </div>
      <p class="mt-12 text-sm text-slate-400">اسحب لليسار للبدء <i class="fas fa-arrow-left ml-2 animate-bounce"></i></p>
    </div>

{slides_content}

    <!-- Slide End -->
    <div class="swiper-slide slide-bg-2">
      <i class="fas fa-check-circle text-7xl text-emerald-500 mb-6"></i>
      <h1 class="text-4xl font-bold text-white mb-4">اكتمل اليوم {day_num}!</h1>
      <p class="text-lg text-emerald-200 mb-8">لقد أنهيت محتوى هذا اليوم بنجاح.</p>
      <a href="index.html" class="bg-emerald-600 hover:bg-emerald-500 text-white font-bold py-3 px-8 rounded-full transition shadow-lg shadow-emerald-900/50">
        العودة للجدول الزمني
      </a>
    </div>

  </div>
  
  <!-- Add Pagination -->
  <div class="swiper-pagination"></div>
  <!-- Add Navigation -->
  <div class="swiper-button-next"></div>
  <div class="swiper-button-prev"></div>
</div>

<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
<script>
  var swiper = new Swiper(".mySwiper", {{
    keyboard: {{
      enabled: true,
    }},
    pagination: {{
      el: ".swiper-pagination",
      clickable: true,
      dynamicBullets: true,
    }},
    navigation: {{
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    }},
  }});
</script>
</body>
</html>"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(template)


# Day 2
day2_slides = """
    <div class="swiper-slide slide-bg-2">
      <div class="content-box">
        <h2 class="title-text">الأساس النظري: عائلات الدوال</h2>
        <div class="theory-box">
          <ul class="list-disc pr-6 space-y-4 text-lg">
            <li><strong>دوال التجميع:</strong> SUM, SUMIF, SUMIFS</li>
            <li><strong>دوال البحث والربط:</strong> VLOOKUP, XLOOKUP</li>
            <li><strong>الدوال المنطقية:</strong> IF, IFERROR</li>
            <li><strong>التنسيق الشرطي:</strong> لتلوين الخلايا تلقائياً</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="swiper-slide slide-bg-1">
      <div class="content-box">
        <h2 class="title-text">أهم المعادلات المحاسبية</h2>
        <div class="step-card"><span class="step-num">1</span><strong>الجمع بشرط:</strong> <code class="formula-chip">=SUMIF(B2:B100,"مبيعات",C2:C100)</code></div>
        <div class="step-card"><span class="step-num">2</span><strong>البحث عن حساب:</strong> <code class="formula-chip">=XLOOKUP(A2,COA!A:A,COA!B:B,"غير موجود")</code></div>
        <div class="step-card"><span class="step-num">3</span><strong>معالجة الأخطاء:</strong> <code class="formula-chip">=IFERROR(A2/B2, 0)</code></div>
        <div class="step-card"><span class="step-num">4</span><strong>التحقق من التوازن:</strong> <code class="formula-chip">=IF(SUM(D)=SUM(C),"متزن","فارق")</code></div>
      </div>
    </div>
"""

# Day 3
day3_slides = """
    <div class="swiper-slide slide-bg-2">
      <div class="content-box">
        <h2 class="title-text">نظرية القيد المزدوج</h2>
        <div class="theory-box">
          <p class="text-xl leading-relaxed">
            كل عملية مالية تؤثر على حسابين على الأقل،
            بحيث يكون مجموع المدين مساوياً لمجموع الدائن دائماً.
          </p>
          <ul class="list-disc pr-6 mt-4 space-y-2">
            <li><strong>الأصول والمصروفات:</strong> تزيد بالمدين وتقل بالدائن</li>
            <li><strong>الالتزامات والملكية والإيرادات:</strong> تزيد بالدائن وتقل بالمدين</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="swiper-slide slide-bg-1">
      <div class="content-box">
        <h2 class="title-text">ترحيل الحركات (الأستاذ)</h2>
        <div class="step-card"><span class="step-num">1</span><strong>جلب المجاميع:</strong> <code class="formula-chip">=SUMIFS(Journal!F:F,Journal!C:C,A2)</code></div>
        <div class="step-card"><span class="step-num">2</span><strong>حساب الرصيد المتحرك:</strong> <br><br>الرصيد = الرصيد السابق + مدين - دائن (للحسابات المدينة)</div>
      </div>
    </div>
"""

# Day 4
day4_slides = """
    <div class="swiper-slide slide-bg-2">
      <div class="content-box">
        <h2 class="title-text">ميزان المراجعة (Trial Balance)</h2>
        <div class="theory-box">
          <p class="text-xl">
            قائمة بجميع حسابات الأستاذ تُظهر أرصدة كل حساب للتحقق من التوازن وصحة الترحيل.
          </p>
        </div>
      </div>
    </div>
    <div class="swiper-slide slide-bg-1">
      <div class="content-box">
        <h2 class="title-text">بناء ميزان المراجعة</h2>
        <div class="step-card"><span class="step-num">1</span><strong>الرصيد النهائي:</strong> <code class="formula-chip">=IF((C2+E2-G2)>0, C2+E2-G2, 0)</code></div>
        <div class="step-card"><span class="step-num">2</span><strong>فحص التوازن:</strong> <code class="formula-chip">=IF(SUM(G:G)=SUM(H:H),"متزن ✔","فارق")</code></div>
      </div>
    </div>
"""

# Day 5
day5_slides = """
    <div class="swiper-slide slide-bg-2">
      <div class="content-box">
        <h2 class="title-text">القوائم المالية (Financial Statements)</h2>
        <div class="theory-box">
          <ul class="list-disc pr-6 space-y-4 text-lg">
            <li><strong>قائمة الدخل:</strong> الإيرادات - تكلفة المبيعات - المصروفات = صافي الربح</li>
            <li><strong>الميزانية العمومية:</strong> الأصول = الالتزامات + حقوق الملكية</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="swiper-slide slide-bg-1">
      <div class="content-box">
        <h2 class="title-text">الأتمتة والربط</h2>
        <div class="step-card"><span class="step-num">1</span><strong>استدعاء الأرصدة:</strong> باستخدام <code>XLOOKUP</code> من ميزان المراجعة</div>
        <div class="step-card"><span class="step-num">2</span><strong>ترحيل صافي الربح:</strong> يضاف إلى الأرباح المبقاة في حقوق الملكية</div>
        <div class="step-card"><span class="step-num">3</span><strong>حماية الخلايا:</strong> Protect Sheet لمنع التعديل الخاطئ</div>
      </div>
    </div>
"""

# Day 6
day6_slides = """
    <div class="swiper-slide slide-bg-2">
      <div class="content-box">
        <h2 class="title-text">التقارير المحورية والمؤشرات</h2>
        <div class="theory-box">
          <ul class="list-disc pr-6 space-y-4 text-lg">
            <li><strong>الجداول المحورية:</strong> (Pivot Tables) لتلخيص آلاف الصفوف</li>
            <li><strong>لوحة التحكم:</strong> (Dashboard) تجمع أهم KPIs بصرياً</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="swiper-slide slide-bg-1">
      <div class="content-box">
        <h2 class="title-text">مؤشرات الأداء المالي (KPIs)</h2>
        <div class="step-card"><span class="step-num">1</span><strong>صافي هامش الربح:</strong> صافي الربح / الإيرادات</div>
        <div class="step-card"><span class="step-num">2</span><strong>نسبة التداول:</strong> الأصول المتداولة / الالتزامات المتداولة</div>
        <div class="step-card"><span class="step-num">3</span><strong>العائد على الأصول (ROA):</strong> صافي الربح / إجمالي الأصول</div>
      </div>
    </div>
"""

# Day 7
day7_slides = """
    <div class="swiper-slide slide-bg-2">
      <div class="content-box">
        <h2 class="title-text">مشروع التخرج: التطبيق الشامل</h2>
        <div class="theory-box">
          <p class="text-xl">
            محاكاة دورة محاسبية كاملة لـ "شركة النجاح التجارية" عبر 10 عمليات مالية واقعية.
          </p>
        </div>
      </div>
    </div>
    <div class="swiper-slide slide-bg-1">
      <div class="content-box">
        <h2 class="title-text">خطوات المشروع</h2>
        <div class="step-card"><span class="step-num">1</span>أرصدة أول المدة وتسجيل العمليات الـ 10</div>
        <div class="step-card"><span class="step-num">2</span>تسجيل التسويات الجردية اللازمة</div>
        <div class="step-card"><span class="step-num">3</span>إعداد ميزان المراجعة بعد التسويات</div>
        <div class="step-card"><span class="step-num">4</span>إقفال الحسابات وإصدار القوائم المالية</div>
      </div>
    </div>
"""

base_path = "c:/Users/pc/Desktop/موقع الاكسل/"

create_slide_file(base_path+"day2-slides.html", "الثاني", "الدوال والمعادلات المحاسبية", "Accounting Formulas Mastery", "المحور 3 | تركيز عالٍ", day2_slides)
create_slide_file(base_path+"day3-slides.html", "الثالث", "دفتر اليومية ودفتر الأستاذ", "Journal & General Ledger", "المحور 4 | القيد المزدوج", day3_slides)
create_slide_file(base_path+"day4-slides.html", "الرابع", "ميزان المراجعة الآلي", "Automated Trial Balance", "المحور 5 | الأتمتة المحاسبية", day4_slides)
create_slide_file(base_path+"day5-slides.html", "الخامس", "إعداد القوائم المالية", "Financial Statements Design", "المحور 6 | قائمة الدخل + الميزانية", day5_slides)
create_slide_file(base_path+"day6-slides.html", "السادس", "التقارير المحورية ولوحة التحكم", "Pivot Tables & Dashboards", "المحوران 7 + 8 | الرؤى المالية", day6_slides)
create_slide_file(base_path+"day7-slides.html", "السابع", "مشروع التخرج", "Capstone Project", "المحور 9 | التطبيق الشامل", day7_slides)

print("Files generated successfully!")
