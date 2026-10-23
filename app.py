import streamlit as st
import pandas as pd
import sympy as sp
import itertools

# ---------------------------------------------------------
# Page Configuration & Styling
# ---------------------------------------------------------
st.set_page_config(
    page_title="Mathematical Logic Interactive App",
    page_icon="🧮",
    layout="wide"
)

st.markdown("""
<style>
    .main-title { font-size: 32px; font-weight: bold; color: #1E3A8A; }
    .sub-title { font-size: 16px; color: #4B5563; }
    .card { background-color: #F8FAFC; padding: 15px; border-radius: 8px; border: 1px solid #E2E8F0; margin-bottom: 10px; }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Sidebar Main Navigation
# ---------------------------------------------------------
st.sidebar.title("📚 บทเรียนตรรกศาสตร์")
main_menu = st.sidebar.radio(
    "เลือกบทเรียนหลัก:",
    [
        "หน้าแรก & ข้อมูลรายงาน",
        "Chapter 1: Introduction to Logic",
        "Chapter 2: Connectives & Truth Tables",
        "Chapter 3: Tautologies",
        "Chapter 4: Arguments",
        "Chapter 5: Quantifiers",
        "Chapter 6: Inductive & Deductive",
        "References (เอกสารอ้างอิง)"
    ]
)

# ---------------------------------------------------------
# 1. หน้าแรก & ข้อมูลรายงาน (Cover & Overview)
# ---------------------------------------------------------
if main_menu == "หน้าแรก & ข้อมูลรายงาน":
    st.markdown('<p class="main-title">Mathematical Logic Interactive Learning App</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">สื่อการเรียนรู้ออนไลน์วิชาตรรกศาสตร์เชิงคณิตศาสตร์ (English for Teaching Mathematics)</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("""
        **ผู้จัดทำรายงาน:**
        * Ms. Asma Cheloh (ID 6711070055)[cite: 1]
        * Ms. Nur-aima Mahae (ID 671107068)[cite: 1]
        
        **เสนอต่อ:**
        * Assistant Professor Dr. litiwat Tocharoennirattisa[cite: 1]
        
        **สังกัด:**
        * คณะครุศาสตร์ สาขาคณิตศาสตร์ มหาวิทยาลัยราชภัฏธนบุรี[cite: 1]
        """)
    with col2:
        st.success("""
        ### 🎯 วัตถุประสงค์ของแอปพลิเคชัน
        แอปพลิเคชันนี้พัฒนาขึ้นเพื่อรวบรวมเนื้อหา สูตร ตัวอย่างการพิสูจน์ และแบบฝึกหัดโต้ตอบ (Interactive Exercises) ทั้ง 6 บท ตามเอกสารการเรียนรู้ตรรกศาสตร์เชิงคณิตศาสตร์ เพื่อให้นักเรียนและผู้สนใจสามารถศึกษาและทดลองทำโจทย์ได้ทันที[cite: 2, 3]
        """)

# ---------------------------------------------------------
# 2. Chapter 1
# ---------------------------------------------------------
elif main_menu == "Chapter 1: Introduction to Logic":
    st.markdown("## 📘 Chapter 1: Introduction to Mathematical Logic")
    
    sub_menu = st.selectbox("เลือกหัวข้อย่อย (Chapter 1):", ["1.1 เนื้อหาและทฤษฎี", "1.2 สูตรและสัญลักษณ์", "1.3 ตัวอย่างการพิสูจน์", "1.4 แบบฝึกหัดทดสอบความเข้าใจ"])
    
    if sub_menu == "1.1 เนื้อหาและทฤษฎี":
        st.write("ศึกษาโครงสร้างรูปแบบของการให้เหตุผลที่สมเหตุสมผล ประพจน์ (Proposition) จะมีค่าความจริงเป็นจริง (T) หรือเท็จ (F) อย่างใดอย่างหนึ่ง ประพจน์เชิงซ้อนสร้างขึ้นโดยใช้ตัวเชื่อมทางตรรกศาสตร์[cite: 5]")
    elif sub_menu == "1.2 สูตรและสัญลักษณ์":
        st.markdown("- **Atomic Propositions:** $p, q, r, s$[cite: 5]\n- **Modus Ponens Rule:** จาก $p$ และ $p \\rightarrow q$ สามารถสรุป $q$ ได้[cite: 5]")
    elif sub_menu == "1.3 ตัวอย่างการพิสูจน์":
        st.markdown("**Proof 1.1 Chained Inference:** จากเหตุ $p \\rightarrow q, q \\rightarrow r, r \\rightarrow s, p$ พิสูจน์ว่าได้ $s$[cite: 5]")
    elif sub_menu == "1.4 แบบฝึกหัดทดสอบความเข้าใจ":
        st.write("📝 **โจทย์ฝึกหัด:** กำหนดให้เหตุคือ $p \\rightarrow q, q \\rightarrow r$ และ $p$ จงตรวจสอบว่าสามารถสรุปผลเป็น $r$ ได้หรือไม่ตามกฎ Modus Ponens")
        ans = st.radio("เลือกคำตอบ:", ["ได้ (Valid)", "ไม่ได้ (Invalid)"])
        if st.button("ส่งคำตอบ Chained"):
            if ans == "ได้ (Valid)":
                st.success("ถูกต้อง! เป็นการอ้างเหตุผลที่สมเหตุสมผล")
            else:
                st.error("ลองใหม่อีกครั้ง การอ้างเหตุผลนี้สมเหตุสมผล")

# ---------------------------------------------------------
# 3. Chapter 2
# ---------------------------------------------------------
elif main_menu == "Chapter 2: Connectives & Truth Tables":
    st.markdown("## 📘 Chapter 2: Logical Connectives and Truth Tables")
    
    sub_menu = st.selectbox("เลือกหัวข้อย่อย (Chapter 2):", ["2.1 เนื้อหาและทฤษฎี", "2.2 สูตรและสมมูลสำคัญ", "2.3 ตัวอย่างการสร้างตาราง", "2.4 โจทย์และเครื่องมือคำนวณ"])
    
    if sub_menu == "2.1 เนื้อหาและทฤษฎี":
        st.write("ศึกษาตัวเชื่อมทางตรรกศาสตร์ เช่น นิเสธ ($\neg$), และ ($\wedge$), หรือ ($\vee$), การ implie ($\rightarrow$) และสมมูล ($\leftrightarrow$)[cite: 7]")
    elif sub_menu == "2.2 สูตรและสมมูลสำคัญ":
        st.markdown("- $A \\rightarrow B \\equiv \\neg A \\vee B$[cite: 7]\n- De Morgan's Laws: $\\neg(A \\wedge B) \\equiv \\neg A \\vee \\neg B$[cite: 7]")
    elif sub_menu == "2.3 ตัวอย่างการสร้างตาราง":
        st.write("ตารางค่าความจริงของประพจน์ย่อย $n$ ตัว จะมีทั้งหมด $2^n$ แถว[cite: 7]")
    elif sub_menu == "2.4 โจทย์และเครื่องมือคำนวณ":
        st.subheader("⚡ โปรแกรมสร้างตารางค่าความจริงอัตโนมัติ")
        expr_input = st.text_input("ป้อนประพจน์ (เช่น (p & q) >> r):", value="(p & q) >> r")
        if st.button("สร้างตาราง"):
            try:
                expr = sp.sympify(expr_input)
                v_list = sorted([str(s) for s in expr.free_symbols])
                combos = list(itertools.product([True, False], repeat=len(v_list)))
                res_rows = []
                for cb in combos:
                    v_map = dict(zip([sp.Symbol(v) for v in v_list], cb))
                    val = bool(expr.subs(v_map))
                    res_rows.append(list(cb) + [val])
                st.dataframe(pd.DataFrame(res_rows, columns=v_list + ["Result"]), use_container_width=True)
            except Exception as e:
                st.error(f"รูปแบบประพจน์ไม่ถูกต้อง: {e}")

# ---------------------------------------------------------
# 4. Chapter 3
# ---------------------------------------------------------
elif main_menu == "Chapter 3: Tautologies":
    st.markdown("## 📘 Chapter 3: Tautologies")
    
    sub_menu = st.selectbox("เลือกหัวข้อย่อย (Chapter 3):", ["3.1 เนื้อหาและทฤษฎี", "3.2 วิธีการตรวจสอบ", "3.3 ตัวอย่างโจทย์สัจนิรันดร์", "3.4 แบบฝึกหัดให้นักเรียนทำ"])
    
    if sub_menu == "3.1 เนื้อหาและทฤษฎี":
        st.write("สัจนิรันดร์ (Tautology) คือประพจน์ที่เป็นจริงทุกกรณีค่าความจริง ส่วนข้อขัดแย้ง (Contradiction) เป็นเท็จทุกกรณี[cite: 11]")
    elif sub_menu == "3.2 วิธีการตรวจสอบ":
        st.write("สามารถใช้ตารางค่าความจริง หรือสมมติให้ประพจน์เป็นเท็จเพื่อหาข้อขัดแย้ง (Countervaluation)[cite: 11]")
    elif sub_menu == "3.3 ตัวอย่างโจทย์สัจนิรันดร์":
        st.write("ตัวอย่าง: $[(p \wedge q) \rightarrow r] \leftrightarrow [p \rightarrow (q \rightarrow r)]$ เป็นสัจนิรันดร์[cite: 16]")
    elif sub_menu == "3.4 แบบฝึกหัดให้นักเรียนทำ":
        st.write("📝 **โจทย์ฝึกหัด:** ตรวจสอบว่าประพจน์ $p \vee \neg p$ เป็นสัจนิรันดร์หรือไม่?")
        ans3 = st.radio("เลือกคำตอบ:", ["เป็นสัจนิรันดร์", "ไม่เป็นสัจนิรันดร์"])
        if st.button("ตรวจคำตอบ Chapter 3"):
            if ans3 == "เป็นสัจนิรันดร์":
                st.success("ถูกต้อง! $p \vee \neg p$ เป็นจริงเสมอ (Law of Excluded Middle)")
            else:
                st.error("ยังไม่ถูกต้อง ลองใหม่อีกครั้ง")

# ---------------------------------------------------------
# 5. Chapter 4
# ---------------------------------------------------------
elif main_menu == "Chapter 4: Arguments":
    st.markdown("## 📘 Chapter 4: Arguments")
    
    sub_menu = st.selectbox("เลือกหัวข้อย่อย (Chapter 4):", ["4.1 เนื้อหาและทฤษฎี", "4.2 รูปแบบการอ้างเหตุผล", "4.3 ตัวอย่างการพิสูจน์", "4.4 โจทย์ฝึกหัดความสมเหตุสมผล"])
    
    if sub_menu == "4.1 เนื้อหาและทฤษฎี":
        st.write("การอ้างเหตุผลประกอบด้วยเหตุ (Premises) และผลสรุป (Conclusion) จะสมเหตุสมผล (Valid) เมื่อเหตุทุกข้อเป็นจริงแล้วผลสรุปต้องเป็นจริง[cite: 17]")
    elif sub_menu == "4.2 รูปแบบการอ้างเหตุผล":
        st.markdown("- **Modus Ponens:** $A \\rightarrow B, A \\vdash B$[cite: 17]\n- **Modus Tollens:** $A \\rightarrow B, \\neg B \\vdash \\neg A$[cite: 17]")
    elif sub_menu == "4.3 ตัวอย่างการพิสูจน์":
        st.write("ตัวอย่าง Proof 4.1: ใช้ Modus Tollens และ Disjunctive Syllogism ในการหาข้อสรุป[cite: 17]")
    elif sub_menu == "4.4 โจทย์ฝึกหัดความสมเหตุสมผล":
        st.write("📝 **โจทย์ฝึกหัด:** หากกำหนดเหตุคือ $p \\rightarrow q$ และ $\\neg q$ ถามว่าข้อสรุป $\\neg p$ สมเหตุสมผลตามกฎใด?")
        ans4 = st.selectbox("เลือกกฎ:", ["Modus Ponens", "Modus Tollens", "Hypothetical Syllogism"])
        if st.button("ส่งคำตอบ Ch 4"):
            if ans4 == "Modus Tollens":
                st.success("ถูกต้องเยี่ยมมาก! นี่ือกฎ Modus Tollens")
            else:
                st.error("ผิดพลาดเล็กน้อย ลองทบทวนกฎการอ้างเหตุผลดูอีกทีนะ")

# ---------------------------------------------------------
# 6. Chapter 5
# ---------------------------------------------------------
elif main_menu == "Chapter 5: Quantifiers":
    st.markdown("## 📘 Chapter 5: Open Sentences and Quantifiers")
    
    sub_menu = st.selectbox("เลือกหัวข้อย่อย (Chapter 5):", ["5.1 เนื้อหาและทฤษฎี", "5.2 นิเสธตัวบ่งปริมาณ", "5.3 ตัวอย่างลำดับตัวบ่งปริมาณ", "5.4 โจทย์คำถามสำหรับนักเรียน"])
    
    if sub_menu == "5.1 เนื้อหาและทฤษฎี":
        st.write("ประโยคเปิด $P(x)$ จะมีตัวบ่งปริมาณสำหรับทุกตัว ($\forall x$) และมีบางตัว ($\exists x$)[cite: 21]")
    elif sub_menu == "5.2 นิเสธตัวบ่งปริมาณ":
        st.markdown("- $\\neg \forall x P(x) \equiv \exists x \neg P(x)$[cite: 21]\n- $\\neg \exists x P(x) \equiv \forall x \neg P(x)$[cite: 21]")
    elif sub_menu == "5.3 ตัวอย่างลำดับตัวบ่งปริมาณ":
        st.write("ลำดับตัวบ่งปริมาณมีความสำคัญ เช่น บนจำนวนเต็ม $\forall x \exists y (x < y)$ เป็นจริง แต่สลับกันจะเป็นเท็จ[cite: 21]")
    elif sub_menu == "5.4 โจทย์คำถามสำหรับนักเรียน":
        st.write("📝 **โจทย์ฝึกหัด:** นิเสธของข้อความ $\forall x P(x)$ คือข้อใด?")
        ans5 = st.radio("เลือกข้อ:", ["$\exists x \neg P(x)$", "$\forall x \neg P(x)$", "$\neg \exists x P(x)$"])
        if st.button("ตรวจคำตอบ Ch 5"):
            if ans5 == "$\exists x \neg P(x)$":
                st.success("ถูกต้องที่สุด!")
            else:
                st.error("ลองทบทวนกฎนิเสธของ Quantifier ดูอีกครั้ง")

# ---------------------------------------------------------
# 7. Chapter 6
# ---------------------------------------------------------
elif main_menu == "Chapter 6: Inductive & Deductive":
    st.markdown("## 📘 Chapter 6: Inductive and Deductive Reasoning")
    
    sub_menu = st.selectbox("เลือกหัวข้อย่อย (Chapter 6):", ["6.1 เนื้อหาและทฤษฎี", "6.2 หลักการอุปนัยเชิงคณิตศาสตร์", "6.3 ตัวอย่างการพิสูจน์", "6.4 เครื่องมือคำนวณและทดลอง"])
    
    if sub_menu == "6.1 เนื้อหาและทฤษฎี":
        st.write("อุปนัย (Inductive) สรุปจากกรณีตัวอย่าง ส่วนนิรนัย (Deductive) สรุปตามหลักตรรกะ[cite: 24]")
    elif sub_menu == "6.2 หลักการอุปนัยเชิงคณิตศาสตร์":
        st.write("ประกอบด้วย Base case ($n=1$) และ Inductive step สมมติให้เป็นจริงที่ $k$ แล้วพิสูจน์ที่ $k+1$[cite: 24]")
    elif sub_menu == "6.3 ตัวอย่างการพิสูจน์":
        st.write("พิสูจน์ว่า $1^3 + 2^3 + \dots + n^3 = [\frac{n(n+1)}{2}]^2$[cite: 29]")
    elif sub_menu == "6.4 เครื่องมือคำนวณและทดลอง":
        st.subheader("🔢 ตัวจำลองการคำนวณสูตรผลบวกกำลังสาม")
        n_val = st.slider("เลือกค่า n:", 1, 15, 4)
        lhs = sum([i**3 for i in range(1, n_val+1)])
        rhs = int((n_val * (n_val + 1) / 2) ** 2)
        st.write(f"ผลลัพธ์ฝั่งซ้าย (LHS): {lhs}")
        st.write(f"ผลลัพธ์ฝั่งขวา (RHS): {rhs}")
        if lhs == rhs:
            st.success("✅ สมการเป็นจริงสอดคล้องกับการพิสูจน์ทางอุปนัยเชิงคณิตศาสตร์!")

# ---------------------------------------------------------
# 8. References
# ---------------------------------------------------------
elif main_menu == "References (เอกสารอ้างอิง)":
    st.markdown("## 📖 References / เอกสารอ้างอิง")
    st.markdown("""
    * **Epp, S. S. (2011).** *Discrete Mathematics with Applications* (4th ed.). Brooks/Cole.[cite: 32]
    * **Rosen, K. H. (2019).** *Discrete Mathematics and Its Applications* (8th ed.). McGraw-Hill Education.[cite: 32]
    * **Enderton, H. B. (2001).** *A Mathematical Introduction to Logic* (2nd ed.). Academic Press.[cite: 32]
    * **Velleman, D. J. (2019).** *How to Prove It: A Structured Approach* (3rd ed.). Cambridge University Press.[cite: 32]
    """)
