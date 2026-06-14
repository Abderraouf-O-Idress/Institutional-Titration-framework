import pandas as pd
import matplotlib.pyplot as plt
import os

def run_system():
    # المسار المباشر للملف (تأكد من كتابة الاسم بدقة)
    file_name = 'ITF_Institutional Titration System - Sheet1.csv'
    input_path = os.path.join('..', 'data', 'raw', file_name)
    output_path = os.path.join('..', 'data', 'processed', 'analysis_result.png')

    if not os.path.exists(input_path):
        print(f"خطأ: الملف غير موجود في المسار: {input_path}")
        return

    # معالجة البيانات
    df = pd.read_csv(input_path)
    print("تم تحميل البيانات بنجاح، جاري التحليل...")

    # التحليل (يمكنك تعديل الأعمدة حسب ملفك)
    # بافتراض أن لديك أعمدة باسم 'Criteria' و 'Score'
    df.plot(kind='bar', x='Criteria', y='Score', color='skyblue')
    plt.title('Institutional Titration Analysis')
    plt.savefig(output_path)
    print(f"تمت المعايرة! النتائج محفوظة في: {output_path}")

if __name__ == "__main__":
    run_system()