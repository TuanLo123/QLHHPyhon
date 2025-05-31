import tkinter as tk
import tkinter.messagebox as mb
import datetime
from tkinter import ttk
import json
import re
root = tk.Tk()

def NhapTTNguoiNhan():
    #Gồm thông tin như tên địa chỉ điện thoại và email
    #Tạo cửa số chính
    root.title("Thông tin người nhận")
    root.geometry("1024x770")
    root.resizable(width=True, height=True)
    root.configure(bg='Lightblue')
    #hàm load file json thành phố
    # Hàm load danh sách thành phố từ file JSON
    def KhuVucDiaLy_JsonLoad(filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            cities = [item['City'] for item in data['Area']]
            return cities
        except Exception as e:
            mb.showerror("Lỗi", f"Không thể đọc file JSON: {e}")
            return []
    #Form nhập thông tin người Nhan
    def Form_TTNguoiNhan():
        window_NgNhan=tk.Toplevel(root)
        window_NgNhan.title("Điền thông tin")
        window_NgNhan.geometry("420x370")
        window_NgNhan.configure(bg='white')
        window_NgGui_Label=tk.Label(window_NgNhan,text="Thông tin người nhận",bg='white',fg='red',font=("Times New Roman",20,'bold'))
        window_NgGui_Label.pack(padx=10) 
       
        TTNg_Nhan=["Tên người nhận:","Địa chỉ người nhận:","Thành phố:","Điện thoại người nhận:"]
        Ng_Nhan={}
        ThanhPho=KhuVucDiaLy_JsonLoad("khuvucdialy.json")
        for text in TTNg_Nhan:
            khung_form = tk.Frame(window_NgNhan, bg='white')
            khung_form.pack(fill='x', pady=5)
            label_TT = tk.Label(khung_form, text=text, font=('Times New Roman', 14), bg='white', width=17, anchor='w')
            label_TT.pack(side='left')
            
            if text=="Thành phố:":
                combo = ttk.Combobox(khung_form, values=ThanhPho, font=('Times New Roman', 14), state='readonly')
                if ThanhPho:
                    combo.set(ThanhPho[0])  # Mặc định chọn thành phố đầu
                combo.pack(side='left', fill='x', expand=True)
                Ng_Nhan[text] = combo
            else:
                entry_TT = tk.Entry(khung_form, font=('Times New Roman', 14))
                entry_TT.pack(side='left', fill='x', expand=True)
                Ng_Nhan[text] = entry_TT
        label_message = tk.Label(window_NgNhan, text="", fg='red', bg='white', font=('Times New Roman', 12))
        label_message.pack(pady=10)

        def add_NgNhan():
            tenNgNhan=Ng_Nhan["Tên người nhận:"].get().strip()
            diachiNgNhan=Ng_Nhan["Địa chỉ người nhận:"].get().strip()
            thanhpho = Ng_Nhan["Thành phố:"].get().strip()
            dienthoaiNgNhan=Ng_Nhan["Điện thoại người nhận:"].get().strip()

            #xử lý ngoại lệ
            if not tenNgNhan or not diachiNgNhan or not dienthoaiNgNhan:
                label_message.config(text="Không được thiếu thông tin! ")
                return
            pattern=r'^0\d{9}$'
            if not re.match(pattern,dienthoaiNgNhan):
                label_message.config(text="Số điện thoại phải có 10 chữ số và bắt đầu bằng 0")
                return
            Hien_thi=f"Tên người nhận: {tenNgNhan} | Địa chỉ: {diachiNgNhan}| Thành Phố: {thanhpho} | Điện thoại: {dienthoaiNgNhan}"
            tree_viewNgNhan.insert('', 'end', values=(tenNgNhan, diachiNgNhan, thanhpho,dienthoaiNgNhan))
            label_message.config(text="Thêm thành công!", fg='green')
            window_NgNhan.destroy()
        Button_HT=tk.Button(window_NgNhan, text="Thêm", command=add_NgNhan, width=15, bg='blue', fg='white', font=('Times New Roman', 12))
        Button_HT.pack(pady=10)
    #xóa ng nhận
    def delete_NgNhan():
        NgNhan_delete = tree_viewNgNhan.selection()
        if NgNhan_delete:
            response = mb.askyesno("Xác nhận", "Bạn có chắc muốn xóa những người nhận đã chọn?")
            if response:
                for item in NgNhan_delete:
                    tree_viewNgNhan.delete(item)
                label_message.config(text="Đã xóa người nhận", fg="green")
            else:
                label_message.config(text="Đã tắt xóa", fg="red")
        else:
            label_message.config(text="Chọn người nhận để xóa!")
    #Cập nhập người nhận
    def upadte_NgNhan():
        upd_NgNhan=tree_viewNgNhan.selection()
        if upd_NgNhan:
            dongchon=upd_NgNhan[0]
            dataold=tree_viewNgNhan.item(dongchon,'values')
            window_upd = tk.Toplevel(root)
            window_upd.title("Cập nhật thông tin người nhận")
            window_upd.geometry("400x300")
            window_upd.configure(bg="white")
            window_upd_Label=tk.Label(window_upd,text="Thông tin người nhận",bg='white',fg='red',font=("Times New Roman",20,'bold'))
            window_upd_Label.pack(padx=10) 

            TTNg_Nhan = ["Tên người nhận:", "Địa chỉ người nhận:", "Thành phố:", "Điện thoại người nhận:"]
            NgNhan_upd = {}
            ThanhPho=KhuVucDiaLy_JsonLoad("khuvucdialy.json")
            for i, text in enumerate(TTNg_Nhan):
                khung_upd = tk.Frame(window_upd, bg='white')
                khung_upd.pack(fill='x', pady=5)
                label_TT = tk.Label(khung_upd, text=text, font=('Times New Roman', 14), bg='white', width=18, anchor='w')
                label_TT.pack(side='left')
                combo = ttk.Combobox(khung_upd, values=ThanhPho, font=('Times New Roman', 14), state='readonly')
                if text=="Thành phố:":
                    combo = ttk.Combobox(khung_upd, values=ThanhPho, font=('Times New Roman', 14),state="readonly")
                    if ThanhPho:
                        combo.set(ThanhPho[0])  # Mặc định chọn thành phố đầu
                    combo.pack(side='left', fill='x', expand=True)
                    NgNhan_upd[text] = combo
                else:
                    entry_TT = tk.Entry(khung_upd, font=('Times New Roman', 14))
                    entry_TT.insert(0, dataold[i])
                    entry_TT.pack(side='left', fill='x', expand=True)
                    NgNhan_upd[text] = entry_TT

            def save_update():
                ten = NgNhan_upd["Tên người nhận:"].get().strip()
                diachi = NgNhan_upd["Địa chỉ người nhận:"].get().strip()
                thanhpho = NgNhan_upd["Thành phố:"].get().strip()
                dienthoai = NgNhan_upd["Điện thoại người nhận:"].get().strip()

                if not ten or not diachi or not dienthoai:
                    label_message.config(text="Tên, địa chỉ và điện thoại không được để trống")
                    return

                # Kiểm tra số điện thoại bắt đầu 0 và 10 chữ số
                pattern = r'^0\d{9}$'
                if not re.match(pattern, dienthoai):
                    label_message.config(text="Số điện thoại phải có 10 chữ số và bắt đầu bằng 0")
                    return

                # Cập nhật lại Treeview
                tree_viewNgNhan.item(dongchon, values=(ten, diachi, thanhpho, dienthoai))

                label_message.config(text="Cập nhật thành công!", fg='green')
                window_upd.destroy()

            btn_save = tk.Button(window_upd, text="Lưu", command=save_update, width=15, bg='blue', fg='white', font=('Times New Roman', 14))
            btn_save.pack(pady=10)
        else:
            label_message.config(text="Chọn người nhận để cập nhật!", fg='red')

    CSchinh = tk.Frame(root, bg='Lightblue')
    CSchinh.pack(expand=True, fill='both', padx=20, pady=20)

    label = tk.Label(CSchinh, text="Người Nhận", font=("Times New Roman", 30,'bold'),fg='red',bg='Light blue')
    label.pack(pady=(0, 20))
    #Khung cây
    tree_viewNgNhan = ttk.Treeview(CSchinh, columns=('ten', 'diachi','thanhpho' ,'dienthoai'), show='headings', selectmode='extended', height=20)
    tree_viewNgNhan.heading('ten', text='Tên người nhận')
    tree_viewNgNhan.heading('diachi', text='Địa chỉ')
    tree_viewNgNhan.heading('thanhpho',text='Thành phố')
    tree_viewNgNhan.heading('dienthoai', text='Điện thoại')
    tree_viewNgNhan.column('ten', width=200)
    tree_viewNgNhan.column('diachi', width=300)
    tree_viewNgNhan.column('thanhpho',width=180)
    tree_viewNgNhan.column('dienthoai', width=150)
    tree_viewNgNhan.pack(pady=(20, 15), fill='x')
    #Kích thước chữ
    style = ttk.Style()
    style.configure("Treeview", font=('Times New Roman', 16))
    #Khung chứa nút bấm
    khung = tk.Frame(CSchinh)
    khung.pack(pady=10)
    #các button
    # Nút thêm
    Button_add = tk.Button(khung, text="Thêm người nhận", command=Form_TTNguoiNhan, width=20,height=5, font=('Times New Roman', 16,'bold'))
    Button_add.pack(side='left', padx=10)
    #Nút xóa
    Button_delete=tk.Button(khung,text="Xóa người nhận",command=delete_NgNhan,width=20,height=5, font=('Times New Roman', 16,'bold'))
    Button_delete.pack(side="left",padx=10)
    #Nút cập nhập
    Button_update=tk.Button(khung,text="Cập nhập người nhận",command=upadte_NgNhan,width=20,height=5, font=('Times New Roman', 16,'bold'))
    Button_update.pack(side="left",padx=10)
    #Nút Thoát
    Button_leave=tk.Button(root, text="Thoát",command=root.quit,width=10,height=4,fg='black',font=("Times New Roman",14))
    Button_leave.pack(side="right",padx=5)
    #Hiệu ứng thông báo
    label_message = tk.Label(root, text="", fg='red',bg='Light blue' ,font=('Times New Roman', 20))
    label_message.pack(pady=10) 
NhapTTNguoiNhan()
root.mainloop()
            
