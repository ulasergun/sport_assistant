import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton,
    QLabel, QMessageBox, QTabWidget, QTextEdit, QListWidget, QListWidgetItem, QComboBox
)
from PyQt6.QtGui import QFont, QCursor, QColor, QPalette
from PyQt6.QtCore import Qt

DAYS = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]

#diyet programı 
def get_weekly_diet(goal, gender, weight):
    goal = goal.lower()
    gender = gender.lower()
    if goal == "pilates":
        if gender == "kadın":
            return {
                "Pazartesi": "Kahvaltı: Yulaf, badem, süt\nÖğle: Izgara tavuklu salata\nAkşam: Izgara somon, yeşillik\nAra: 10 badem\nGece: Kefir",
                "Salı": "Kahvaltı: 2 haşlanmış yumurta, avokado\nÖğle: Sebzeli kinoa\nAkşam: Fırında tavuk, yoğurt\nAra: 1 elma\nGece: Süt",
                "Çarşamba": "Kahvaltı: Tam buğday ekmek, lor peyniri\nÖğle: Izgara hindi, salata\nAkşam: Izgara balık, sebze\nAra: 1 muz\nGece: Kefir",
                "Perşembe": "OFF GÜNÜ - Hafif beslenme\nKahvaltı: Meyveli yoğurt\nÖğle: Sebze çorbası\nAkşam: Salata, peynir\nAra: 5 badem",
                "Cuma": "Kahvaltı: Yulaf, ceviz, süt\nÖğle: Izgara tavuk, bulgur pilavı\nAkşam: Izgara somon, yeşillik\nAra: 1 portakal\nGece: Süt",
                "Cumartesi": "Kahvaltı: 2 yumurta, domates, salatalık\nÖğle: Kinoa salatası\nAkşam: Fırında sebzeli tavuk\nAra: 1 avuç fındık",
                "Pazar": "OFF GÜNÜ - Serbest gün\nKahvaltı: Serbest (abartmadan)\nÖğle: Hafif salata\nAkşam: Yoğurt, meyve"
            }
        else:
            return {
                "Pazartesi": "Kahvaltı: 3 yumurta, tam buğday ekmek\nÖğle: Izgara tavuk, bulgur pilavı\nAkşam: Izgara balık, salata\nAra: 10 badem\nGece: Kefir",
                "Salı": "Kahvaltı: Lor peyniri, domates\nÖğle: Hindi göğüs, kinoa\nAkşam: Fırında tavuk, yoğurt\nAra: 1 muz\nGece: Süt",
                "Çarşamba": "Kahvaltı: Yulaf, süt, ceviz\nÖğle: Izgara et, salata\nAkşam: Izgara somon, sebze\nAra: 1 elma\nGece: Kefir",
                "Perşembe": "OFF GÜNÜ - Hafif beslenme\nKahvaltı: Meyveli yoğurt\nÖğle: Sebze çorbası\nAkşam: Salata, peynir\nAra: 5 badem",
                "Cuma": "Kahvaltı: 2 yumurta, tam buğday ekmek\nÖğle: Tavuklu salata\nAkşam: Izgara balık, yeşillik\nAra: 1 portakal\nGece: Süt",
                "Cumartesi": "Kahvaltı: Lor peyniri, domates\nÖğle: Kinoa salatası\nAkşam: Fırında sebzeli tavuk\nAra: 1 avuç fındık",
                "Pazar": "OFF GÜNÜ - Serbest gün\nKahvaltı: Serbest (abartmadan)\nÖğle: Hafif salata\nAkşam: Yoğurt, meyve"
            }
    elif goal == "crossfit":
        if gender == "kadın":
            return {
                "Pazartesi": "Kahvaltı: Yulaf, süt, ceviz\nÖğle: Izgara tavuk, esmer pirinç\nAkşam: Izgara somon, kinoa\nAra: 1 protein bar",
                "Salı": "Kahvaltı: 2 yumurta, tam buğday ekmek\nÖğle: Hindi göğüs, bulgur pilavı\nAkşam: Izgara balık, salata\nAra: 1 muz",
                "Çarşamba": "Kahvaltı: Yulaf, badem, süt\nÖğle: Izgara tavuk, sebze\nAkşam: Fırında tavuk, yoğurt\nAra: 1 elma",
                "Perşembe": "OFF GÜNÜ - Hafif karbonhidrat\nKahvaltı: Meyveli yoğurt\nÖğle: Sebze çorbası\nAkşam: Salata, peynir",
                "Cuma": "Kahvaltı: 2 yumurta, lor peyniri\nÖğle: Kinoa salatası\nAkşam: Izgara somon, yeşillik\nAra: 1 portakal",
                "Cumartesi": "Kahvaltı: Yulaf, süt, ceviz\nÖğle: Izgara tavuk, bulgur pilavı\nAkşam: Izgara balık, salata",
                "Pazar": "OFF GÜNÜ - Serbest gün\nKahvaltı: Serbest\nÖğle: Hafif salata\nAkşam: Yoğurt, meyve"
            }
        else:
            return {
                "Pazartesi": "Kahvaltı: 4 yumurta, tam buğday ekmek\nÖğle: Izgara tavuk, esmer pirinç\nAkşam: Izgara somon, kinoa\nAra: 1 protein shake",
                "Salı": "Kahvaltı: Lor peyniri, domates\nÖğle: Hindi göğüs, bulgur pilavı\nAkşam: Izgara balık, salata\nAra: 1 muz",
                "Çarşamba": "Kahvaltı: Yulaf, süt, ceviz\nÖğle: Izgara et, salata\nAkşam: Izgara somon, sebze\nAra: 1 elma\nGece: Kefir",
                "Perşembe": "OFF GÜNÜ - Hafif karbonhidrat\nKahvaltı: Meyveli yoğurt\nÖğle: Sebze çorbası\nAkşam: Salata, peynir",
                "Cuma": "Kahvaltı: 3 yumurta, lor peyniri\nÖğle: Kinoa salatası\nAkşam: Izgara balık, yeşillik\nAra: 1 portakal",
                "Cumartesi": "Kahvaltı: Yulaf, süt, ceviz\nÖğle: Izgara tavuk, bulgur pilavı\nAkşam: Izgara balık, salata",
                "Pazar": "OFF GÜNÜ - Serbest gün\nKahvaltı: Serbest\nÖğle: Hafif salata\nAkşam: Yoğurt, meyve"
            }
    elif goal == "bodybuilding":
        if gender == "kadın":
            return {
                "Pazartesi": "Kahvaltı: 4 yumurta beyazı, yulaf\nÖğle: Izgara tavuk, esmer pirinç\nAkşam: Izgara somon, kinoa\nAra: 1 protein shake",
                "Salı": "Kahvaltı: 2 yumurta, lor peyniri\nÖğle: Hindi göğüs, bulgur pilavı\nAkşam: Izgara balık, salata\nAra: 1 muz",
                "Çarşamba": "Kahvaltı: Yulaf, badem, süt\nÖğle: Izgara tavuk, sebze\nAkşam: Fırında tavuk, yoğurt\nAra: 1 elma",
                "Perşembe": "OFF GÜNÜ - Hafif protein\nKahvaltı: Meyveli yoğurt\nÖğle: Sebze çorbası\nAkşam: Salata, peynir",
                "Cuma": "Kahvaltı: 2 yumurta, lor peyniri\nÖğle: Kinoa salatası\nAkşam: Izgara somon, yeşillik\nAra: 1 portakal",
                "Cumartesi": "Kahvaltı: Yulaf, süt, ceviz\nÖğle: Izgara tavuk, bulgur pilavı\nAkşam: Izgara balık, salata",
                "Pazar": "OFF GÜNÜ - Serbest gün\nKahvaltı: Serbest\nÖğle: Hafif salata\nAkşam: Yoğurt, meyve"
            }
        else:
            return {
                "Pazartesi": "Kahvaltı: 6 yumurta beyazı, yulaf\nÖğle: Izgara tavuk, esmer pirinç\nAkşam: Izgara somon, kinoa\nAra: 1 protein shake",
                "Salı": "Kahvaltı: 3 yumurta, lor peyniri\nÖğle: Hindi göğüs, bulgur pilavı\nAkşam: Izgara balık, salata\nAra: 1 muz",
                "Çarşamba": "Kahvaltı: Yulaf, badem, süt\nÖğle: Izgara tavuk, sebze\nAkşam: Fırında tavuk, yoğurt\nAra: 1 elma",
                "Perşembe": "OFF GÜNÜ - Hafif protein\nKahvaltı: Meyveli yoğurt\nÖğle: Sebze çorbası\nAkşam: Salata, peynir",
                "Cuma": "Kahvaltı: 4 yumurta, lor peyniri\nÖğle: Kinoa salatası\nAkşam: Izgara somon, yeşillik\nAra: 1 portakal",
                "Cumartesi": "Kahvaltı: Yulaf, süt, ceviz\nÖğle: Izgara tavuk, bulgur pilavı\nAkşam: Izgara balık, salata",
                "Pazar": "OFF GÜNÜ - Serbest gün\nKahvaltı: Serbest\nÖğle: Hafif salata\nAkşam: Yoğurt, meyve"
            }
    else:
        return {day: "Veri yok" for day in DAYS}

#antrenman programı
def get_weekly_workout(goal, gender, age):
    goal = goal.lower()
    gender = gender.lower()
    if goal == "pilates":
        if gender == "kadın":
            return {
                "Pazartesi": "Mat Pilates (30 dk), Esneme (10 dk)",
                "Salı": "Core güçlendirme (20 dk), Hafif kardiyo (20 dk)",
                "Çarşamba": "OFF GÜNÜ - Yürüyüş (30 dk)",
                "Perşembe": "Pilates topu ile denge (20 dk), Esneme (10 dk)",
                "Cuma": "Mat Pilates (30 dk), Karın egzersizleri (15 dk)",
                "Cumartesi": "OFF GÜNÜ - Hafif yoga (20 dk)",
                "Pazar": "Serbest gün"
            }
        else:
            return {
                "Pazartesi": "Dinamik pilates (30 dk), Core (15 dk)",
                "Salı": "Hafif koşu (20 dk), Esneme (10 dk)",
                "Çarşamba": "OFF GÜNÜ - Yürüyüş (30 dk)",
                "Perşembe": "Pilates topu ile denge (20 dk), Core (10 dk)",
                "Cuma": "Mat Pilates (30 dk), Karın egzersizleri (15 dk)",
                "Cumartesi": "OFF GÜNÜ - Hafif yoga (20 dk)",
                "Pazar": "Serbest gün"
            }
    elif goal == "crossfit":
        if gender == "kadın":
            return {
                "Pazartesi": "WOD: 3 tur (15 squat, 10 burpee, 10 push-up), Plank (3x1 dk)",
                "Salı": "Kettlebell swing (3x12), Deadlift (3x10)",
                "Çarşamba": "OFF GÜNÜ - Yürüyüş (30 dk)",
                "Perşembe": "WOD: 2 tur (10 squat, 8 burpee, 8 push-up), Plank (2x45 sn)",
                "Cuma": "Kettlebell swing (3x12), Hafif koşu (20 dk)",
                "Cumartesi": "OFF GÜNÜ - Hafif yoga (20 dk)",
                "Pazar": "Serbest gün"
            }
        else:
            return {
                "Pazartesi": "WOD: 4 tur (20 squat, 15 burpee, 15 push-up), Plank (4x1 dk)",
                "Salı": "Deadlift (4x8), Kettlebell swing (4x12)",
                "Çarşamba": "OFF GÜNÜ - Yürüyüş (30 dk)",
                "Perşembe": "WOD: 2 tur (12 squat, 10 burpee, 10 push-up), Plank (2x45 sn)",
                "Cuma": "Deadlift (3x10), Hafif koşu (20 dk)",
                "Cumartesi": "OFF GÜNÜ - Hafif yoga (20 dk)",
                "Pazar": "Serbest gün"
            }
    elif goal == "bodybuilding":
        if gender == "kadın":
            return {
                "Pazartesi": "Squat (4x12), Bench press (3x10), Karın (3x15)",
                "Salı": "Lat pulldown (3x12), Dumbbell shoulder press (3x10)",
                "Çarşamba": "OFF GÜNÜ - Yürüyüş (30 dk)",
                "Perşembe": "Squat (3x10), Bench press (2x8), Karın (2x12)",
                "Cuma": "Lat pulldown (2x10), Dumbbell shoulder press (2x8)",
                "Cumartesi": "OFF GÜNÜ - Hafif yoga (20 dk)",
                "Pazar": "Serbest gün"
            }
        else:
            return {
                "Pazartesi": "Squat (5x12), Bench press (4x10), Karın (4x15)",
                "Salı": "Deadlift (4x8), Barbell row (4x10)",
                "Çarşamba": "OFF GÜNÜ - Yürüyüş (30 dk)",
                "Perşembe": "Squat (3x10), Bench press (3x8), Karın (2x12)",
                "Cuma": "Deadlift (2x8), Barbell row (2x10)",
                "Cumartesi": "OFF GÜNÜ - Hafif yoga (20 dk)",
                "Pazar": "Serbest gün"
            }
    else:
        return {day: "Veri yok" for day in DAYS}

#uygulamanın ara yüzü
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spor Takip Uygulaması")
        self.resize(800, 520)
        self.user_data = {}

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#f5f7fa"))
        palette.setColor(QPalette.ColorRole.Base, QColor("#e3eafc"))
        palette.setColor(QPalette.ColorRole.Button, QColor("#1976d2"))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor("#fff"))
        palette.setColor(QPalette.ColorRole.Text, QColor("#000"))
        palette.setColor(QPalette.ColorRole.WindowText, QColor("#000"))
        self.setPalette(palette)

        self.tabs = QTabWidget()
        self.tabs.setStyleSheet("""
            QTabBar::tab:selected {background: #1976d2; color: #000; font-weight: bold;}
            QTabBar::tab {background: #e3eafc; color: #000; font-size: 15px; padding: 10px;}
            QTabWidget::pane {border: 2px solid #1976d2; border-radius: 8px;}
        """)
        self.setCentralWidget(self.tabs)

        self.create_user_tab()
        self.create_diet_tab()
        self.create_exercise_tab()
        self.create_goal_tab()
        self.create_exercise_video_tab()

#user tab oluşturma
    def create_user_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        title = QLabel("Kullanıcı Bilgileri")
        title.setFont(QFont("Arial", 22, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: #000;")
        layout.addWidget(title)

        form_layout = QHBoxLayout()
        left = QVBoxLayout()
        right = QVBoxLayout()

        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("İsim")
        left.addWidget(self.name_edit)

        self.age_edit = QLineEdit()
        self.age_edit.setPlaceholderText("Yaş")
        left.addWidget(self.age_edit)

        
        gender_label = QLabel("Cinsiyet")
        gender_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        gender_label.setStyleSheet("color: #fff; background: #1976d2; padding: 4px 8px; border-radius: 4px;")
        left.addWidget(gender_label)

        self.gender_combo = QComboBox()
        self.gender_combo.addItems(["Kadın", "Erkek"])
        self.gender_combo.setStyleSheet("background: #1976d2; color: #fff; font-weight: bold;")
        left.addWidget(self.gender_combo)

        self.height_edit = QLineEdit()
        self.height_edit.setPlaceholderText("Boy (cm)")
        right.addWidget(self.height_edit)

        self.weight_edit = QLineEdit()
        self.weight_edit.setPlaceholderText("Kilo (kg)")
        right.addWidget(self.weight_edit)

        #hedef seçimi
        goal_label = QLabel("Hedef")
        goal_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        goal_label.setStyleSheet("color: #fff; background: #388e3c; padding: 4px 8px; border-radius: 4px;")
        right.addWidget(goal_label)

        self.goal_combo = QComboBox()
        self.goal_combo.addItems(["Pilates", "Crossfit", "Bodybuilding"])
        self.goal_combo.setStyleSheet("background: #388e3c; color: #fff; font-weight: bold;")
        right.addWidget(self.goal_combo)

        form_layout.addLayout(left)
        form_layout.addSpacing(30)
        form_layout.addLayout(right)
        layout.addLayout(form_layout)

        save_btn = QPushButton("Bilgileri Kaydet")
        save_btn.setStyleSheet("padding: 10px; font-weight: bold; background: #1976d2; color: #fff; border-radius: 8px;")
        save_btn.clicked.connect(self.save_user_data)
        layout.addWidget(save_btn)

        layout.addStretch()
        tab.setLayout(layout)
        self.tabs.addTab(tab, "Kullanıcı")

    def save_user_data(self):
        name = self.name_edit.text()
        age = self.age_edit.text()
        gender = self.gender_combo.currentText()
        height = self.height_edit.text()
        weight = self.weight_edit.text()
        goal = self.goal_combo.currentText()
        if not name or not age or not gender or not height or not weight or not goal:
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm alanları doldurun.")
            return
        try:
            age_int = int(age)
            weight_float = float(weight)
        except ValueError:
            QMessageBox.warning(self, "Uyarı", "Yaş ve kilo sayısal olmalıdır.")
            return
        self.user_data = {
            "name": name,
            "age": age_int,
            "gender": gender,
            "height": height,
            "weight": weight_float,
            "goal": goal
        }
        QMessageBox.information(self, "Kayıt", "Kullanıcı bilgileri kaydedildi.")
#diyet penceresi oluşturma 
    def create_diet_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        title = QLabel("Haftalık Diyet Programı")
        title.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: #000;")
        layout.addWidget(title)

        btn = QPushButton("Haftalık Diyet Listesini Göster")
        btn.setStyleSheet("padding: 10px; font-weight: bold; background: #388e3c; color: #fff; border-radius: 8px;")
        result_area = QTextEdit()
        result_area.setReadOnly(True)
        result_area.setMinimumHeight(320)
        result_area.setStyleSheet("background: #e3eafc; font-size: 15px; color: #000;")

        def show_diets():
            if not self.user_data:
                QMessageBox.warning(self, "Uyarı", "Önce kullanıcı bilgilerini girin.")
                return
            gender = self.user_data.get("gender", "").lower()
            weight = self.user_data.get("weight", 0)
            goal = self.user_data.get("goal", "").lower()
            haftalik = get_weekly_diet(goal, gender, weight)
            metin = f"{self.user_data['name']} için haftalık diyet programı ({self.user_data['goal']}):\n\n"
            for day in DAYS:
                metin += f"<b>{day}:</b>\n{haftalik[day]}\n\n"
            result_area.setHtml(metin)

        btn.clicked.connect(show_diets)
        layout.addWidget(btn)
        layout.addWidget(result_area)
        layout.addStretch()
        self.tabs.addTab(tab, "Diyet")
#antrenman programı penceresi oluturma
    def create_exercise_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        title = QLabel("Haftalık Antrenman Programı")
        title.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: #000;")
        layout.addWidget(title)

        btn = QPushButton("Haftalık Antrenman Programını Göster")
        btn.setStyleSheet("padding: 10px; font-weight: bold; background: #d32f2f; color: #fff; border-radius: 8px;")
        result_area = QTextEdit()
        result_area.setReadOnly(True)
        result_area.setMinimumHeight(320)
        result_area.setStyleSheet("background: #e3eafc; font-size: 15px; color: #000;")

        def show_exercises():
            if not self.user_data:
                QMessageBox.warning(self, "Uyarı", "Önce kullanıcı bilgilerini girin.")
                return
            gender = self.user_data.get("gender", "").lower()
            age = self.user_data.get("age", 0)
            goal = self.user_data.get("goal", "").lower()
            haftalik = get_weekly_workout(goal, gender, age)
            metin = f"{self.user_data['name']} için haftalık antrenman programı ({self.user_data['goal']}):\n\n"
            for day in DAYS:
                metin += f"<b>{day}:</b>\n{haftalik[day]}\n\n"
            result_area.setHtml(metin)

        btn.clicked.connect(show_exercises)
        layout.addWidget(btn)
        layout.addWidget(result_area)
        layout.addStretch()
        self.tabs.addTab(tab, "Antrenman")
#hedefe göre tahmin penceresi oluşturma
    def create_goal_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        title = QLabel("Hedef ve Tahmin")
        title.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: #000;")
        layout.addWidget(title)

        hedef_combo = QComboBox()
        hedef_combo.addItems(["Kilo Verme", "Kilo Alma"])
        hedef_combo.setCurrentIndex(0)
        hedef_combo.setStyleSheet("font-size: 15px; padding: 6px; color: #000;")
        layout.addWidget(hedef_combo)

        sure_combo = QComboBox()
        sure_combo.addItems(["3 Ay", "6 Ay", "1 Yıl"])
        sure_combo.setCurrentIndex(0)
        sure_combo.setStyleSheet("font-size: 15px; padding: 6px; color: #000;")
        layout.addWidget(sure_combo)

        btn = QPushButton("Hedef Sonucunu Göster")
        btn.setStyleSheet("padding: 10px; font-weight: bold; background: #1976d2; color: #fff; border-radius: 8px;")
        result_area = QTextEdit()
        result_area.setReadOnly(True)
        result_area.setMinimumHeight(120)
        result_area.setStyleSheet("background: #e3eafc; font-size: 15px; color: #000;")

        layout.addWidget(btn)
        layout.addWidget(result_area)
        layout.addStretch()

        def show_goal():
            if not self.user_data:
                QMessageBox.warning(self, "Uyarı", "Önce kullanıcı bilgilerini girin.")
                return

            hedef = hedef_combo.currentText()
            sure = sure_combo.currentText()
            weight = self.user_data.get("weight", 0)
            try:
                weight = float(weight)
            except Exception:
                QMessageBox.warning(self, "Uyarı", "Kilo bilgisi hatalı.")
                return
            if hedef == "Kilo Verme":
                if sure == "3 Ay":
                    yag_kaybi = round(weight * 0.06, 1)
                    kas_kazanci = round(weight * 0.01, 1)
                elif sure == "6 Ay":
                    yag_kaybi = round(weight * 0.11, 1)
                    kas_kazanci = round(weight * 0.02, 1)
                else:  # 1 Yıl
                    yag_kaybi = round(weight * 0.18, 1)
                    kas_kazanci = round(weight * 0.04, 1)
                sonuc = (
                    f"{sure} sonunda tahmini yağ kaybı: <b>{yag_kaybi} kg</b><br>"
                    f"{sure} sonunda tahmini kas kazanımı: <b>{kas_kazanci} kg</b><br>"
                    f"<br><i>Not: Tahminler ortalama değerlerdir ve kişisel farklılıklar gösterebilir.</i>"
                )
            else:  # Kilo Alma
                if sure == "3 Ay":
                    kas_kazanci = round(weight * 0.03, 1)
                    yag_kazanci = round(weight * 0.01, 1)
                elif sure == "6 Ay":
                    kas_kazanci = round(weight * 0.06, 1)
                    yag_kazanci = round(weight * 0.02, 1)
                else:  # 1 Yıl
                    kas_kazanci = round(weight * 0.12, 1)
                    yag_kazanci = round(weight * 0.04, 1)
                sonuc = (
                    f"{sure} sonunda tahmini kas kazanımı: <b>{kas_kazanci} kg</b><br>"
                    f"{sure} sonunda tahmini yağ kazanımı: <b>{yag_kazanci} kg</b><br>"
                    f"<br><i>Not: Tahminler ortalama değerlerdir ve kişisel farklılıklar gösterebilir.</i>"
                )

            result_area.setHtml(sonuc)

        btn.clicked.connect(show_goal)
        self.tabs.addTab(tab, "Hedef")

    def create_exercise_video_tab(self):
        tab = QWidget()
        layout = QVBoxLayout(tab)
        title = QLabel("Egzersiz Video Rehberi")
        title.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: #000;")
        layout.addWidget(title)

        exercise_list = QListWidget()
        exercises = {
            "Şınav": "https://www.youtube.com/watch?v=RyzxRrBHn7k",
            "Mekik": "https://www.youtube.com/watch?v=PL0qkUkWTZk",
            "Squat": "https://www.youtube.com/shorts/OgBJMup5Ycw",
            "Plank": "https://www.youtube.com/watch?v=zN4ztr3IFCI",
            "Bench Press": "https://www.youtube.com/watch?v=HQMumy_G4oo",
            "Deadlift": "https://www.youtube.com/shorts/htP2vgcq0fk",
            "Barbell Row": "https://www.youtube.com/watch?v=NYtMT7aRNmg",
            "Kettlebell Swing": "https://www.youtube.com/watch?v=jxkUPgHwtoU",
            "Dumbbell Shoulder Press": "https://www.youtube.com/shorts/osEKVtXBLlU",
            "Lunge": "https://www.youtube.com/watch?v=tQNktxPkSeE",
            "Burpee": "https://www.youtube.com/watch?v=auBLPXO8Fww",
            "Mountain Climber": "https://www.youtube.com/watch?v=ruQ4ZwncXBg",
            "Jumping Jack": "https://www.youtube.com/watch?v=uLVt6u15L98",
            "Core Güçlendirme": "https://www.youtube.com/shorts/QQYviTCnKWU",
            "Pilates Topu ile Denge": "https://www.youtube.com/watch?v=m_8PWpvl6vs",

        }
        for name in exercises:
            item = QListWidgetItem(name)
            exercise_list.addItem(item)
        exercise_list.setStyleSheet("font-size: 15px; background: #fffde7; color: #000;")
        layout.addWidget(exercise_list)

        url_label = QLabel("Bir egzersiz seçin.")
        url_label.setFont(QFont("Arial", 13))
        url_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
        url_label.setOpenExternalLinks(True)
        url_label.setStyleSheet("color: #000; margin-top: 20px;")
        layout.addWidget(url_label)

        def show_url():
            selected = exercise_list.currentItem()
            if selected:
                url = exercises[selected.text()]
                url_label.setText(f'<a href="{url}" style="color:#000;">{url}</a>')
                url_label.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            else:
                url_label.setText("Bir egzersiz seçin.")

        exercise_list.currentItemChanged.connect(show_url)
        layout.addStretch()
        self.tabs.addTab(tab, "Egzersiz Videoları")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
