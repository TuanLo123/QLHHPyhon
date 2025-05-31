import tkinter as tk
import tkinter.messagebox as mb
from tkinter import ttk
import datetime
root = tk.Tk()

def NhapHangHoa():
    root.title("Hàng hóa")
    root.geometry("1024x768")
    root.resizable(width=True, height=True)
    root.configure(bg='white')

    #FORM NHẬP khi thêm hàng hóa
    def open_add_form():
    # Tạo form nhập hàng hóa
        window_Con = tk.Toplevel(root)#tạo cửa số con
        window_Con.title("Nhập thông tin hàng hóa")
        window_Con.geometry("400x350")
        window_Con.configure(bg='white')
    
        TT_HangHoa = ["Tên sản phẩm:", "Mã hàng hóa:", "Số tiền:", "Ngày gửi:", "Loại hàng hóa:"]#Thuộc tính hàng hóa
        #Tạo khung để chưa các thuộc tính hàng hóa
        vatpham = {}
        for i, text in enumerate(TT_HangHoa):
            khung_form = tk.Frame(window_Con, bg='white')
            khung_form.pack(fill='x', pady=5)
            label_TT = tk.Label(khung_form, text=text, font=('Times New Roman', 14), bg='white', width=15, anchor='w')
            label_TT.pack(side='left')
            entry_TT = tk.Entry(khung_form, font=('Times New Roman', 14))
            entry_TT.pack(side='left', fill='x', expand=True)
            vatpham[text] = entry_TT
        #Hiển thị thông báo
        label_message = tk.Label(window_Con, text="", fg='red', bg='white', font=('Times New Roman', 12))
        label_message.pack(pady=10)

        def add_package():
            ten_sp = vatpham["Tên sản phẩm:"].get().strip()#lấy thông tin và xử lý khoảng trắng
            ma_hh = vatpham["Mã hàng hóa:"].get().strip()
            tien = vatpham["Số tiền:"].get().strip()
            ngay_gui = vatpham["Ngày gửi:"].get().strip()
            loai_hh = vatpham["Loại hàng hóa:"].get().strip()

            if not ten_sp or not ma_hh:
                label_message.config(text="Tên sản phẩm và mã hàng hóa không được để trống")
                return
            try:
                tien1 = float(tien)
                if tien1 < 0:
                    label_message.config(text="Số tiền phải là số không âm!")
                    return
            except:
                label_message.config(text="Số tiền phải là số hợp lệ!")
                return
            try:
        # Định dạng ngày: dd/mm/yyyy
        #Xử lý các vấn đề: năm gửi không quá năm hiện và ngày gửi không quá ngày gửi hiện tại
                Nam_Gui=datetime.datetime.strptime(ngay_gui, "%d/%m/%Y")
                Nam_HienTai=datetime.datetime.now().year
                if Nam_Gui.year > Nam_HienTai:
                    label_message.config(text="Năm gừi không được vượt qua năm hiện tại!",fg="red")
                    return
                elif Nam_Gui > datetime.datetime.now():
                    label_message.config(text="Ngày gửi không được vượt qua ngày hiện tại!",fg="red")
                    return
            except ValueError:
                label_message.config(text="Ngày gửi không đúng định dạng (dd/mm/yyyy)!", fg='red')
                return

            Hien_thi = f"Tên sản phẩm: {ten_sp}              | Mã: {ma_hh}      | Giá: {tien1:.2f}      | Ngày gửi: {ngay_gui}     | Loại: {loai_hh}"
            listbox_HangHoa.insert(tk.END, Hien_thi)
            label_message.config(text="Thêm thành công!", fg='green')
            window_Con.destroy()  # đóng from

        Button_ok = tk.Button(window_Con, text="Thêm", command=add_package, width=15, bg='blue', fg='white', font=('Times New Roman', 12))
        Button_ok.pack(pady=10)
        '''Xóa hàng hóa'''
    def delete_package():
        HH_delete = listbox_HangHoa.curselection()
        if HH_delete:
            listbox_HangHoa.delete(HH_delete)
            Label_Nofi.config(text="Đã tắt hàng hóa",fg='red')
        else:
            Label_Nofi.config(text="Chọn hàng hóa để xóa!")
    '''Cập nhập hàng hóa'''
    '''Cập nhập bằng cách chon hàng hóa trên bảng list box '''
    def update_package():
        HH_upd=listbox_HangHoa.curselection()
        if HH_upd:
            #Lấy dòng chọn
            dong_chon=listbox_HangHoa.get(HH_upd[0])
            DS_TTDongchon=dong_chon.split('|')
            #Thông tin cũ 
            data_dongchon={
                "Tên sản phẩm:": DS_TTDongchon[0].strip(),
                "Mã hàng hóa:": DS_TTDongchon[1].strip().split(': ')[1],
                "Số tiền:": DS_TTDongchon[2].strip().split(': ')[1],
                "Ngày gửi:": DS_TTDongchon[3].strip().split(': ')[1],
                "Loại hàng hóa:": DS_TTDongchon[4].strip().split(': ')[1],
            }
            #Lưu thông tin của hàng hóa cũ
            TT_HHold=dong_chon
            #Tạo cửa số cho form cập nhập
            window_upd=tk.Toplevel(root)
            window_upd.title("Cập nhập thông tin hàng hóa")
            window_upd.geometry("400x350")
            window_upd.configure(bg="white")
            #Thông tin ô cần update
            TT_HangHoa = ["Tên sản phẩm:", "Mã hàng hóa:", "Số tiền:", "Ngày gửi:", "Loại hàng hóa:"]
            vatpham_upd = {}
            for vp in TT_HangHoa:
                khung_upd = tk.Frame(window_upd, bg='white')
                khung_upd.pack(fill='x', pady=5)
                label_TT = tk.Label(khung_upd, text=vp, font=('Times New Roman', 14), bg='white', width=15, anchor='w')
                label_TT.pack(side='left')
                entry_TT = tk.Entry(khung_upd, font=('Times New Roman', 14)) 
                entry_TT.insert(0, data_dongchon[vp])
                entry_TT.pack(side='left', fill='x', expand=True)
                vatpham_upd[vp] = entry_TT
            label_message = tk.Label(window_upd, text="", fg='red', bg='white', font=('Times New Roman', 12))
            label_message.pack(pady=10)

            def save_update():
                ten_sp = vatpham_upd["Tên sản phẩm:"].get().strip()#lấy thông tin và xử lý khoảng trắng
                ma_hh = vatpham_upd["Mã hàng hóa:"].get().strip()
                tien = vatpham_upd["Số tiền:"].get().strip()
                ngay_gui = vatpham_upd["Ngày gửi:"].get().strip()
                loai_hh = vatpham_upd["Loại hàng hóa:"].get().strip()

                if not ten_sp or not ma_hh:
                    label_message.config(text="Tên sản phẩm và mã hàng hóa không được để trống")
                    return
                try:
                    tien1 = float(tien)
                    if tien1 < 0:
                        label_message.config(text="Số tiền phải là số không âm!")
                        return
                except:
                    label_message.config(text="Số tiền phải là số hợp lệ!")
                    return
                try:
            # Định dạng ngày: dd/mm/yyyy
            #Xử lý các vấn đề: năm gửi không quá năm hiện và ngày gửi không quá ngày gửi hiện tại
                    Nam_Gui=datetime.datetime.strptime(ngay_gui, "%d/%m/%Y")
                    Nam_HienTai=datetime.datetime.now().year
                    if Nam_Gui.year > Nam_HienTai:
                        label_message.config(text="Năm gừi không được vượt qua năm hiện tại!",fg="red")
                        return
                    elif Nam_Gui > datetime.datetime.now():
                        label_message.config(text="Ngày gửi không được vượt qua ngày hiện tại!",fg="red")
                        return
                except ValueError:
                    label_message.config(text="Ngày gửi không đúng định dạng (dd/mm/yyyy)!", fg='red')
                mo_ta = f"tên sản phẩm: \t{ten_sp} | Mã: {ma_hh} | Giá: {tien1:.2f} | Ngày gửi: {ngay_gui} | Loại: {loai_hh}"

                # Xóa dòng cũ và thêm dòng mới
                listbox_HangHoa.delete(HH_upd[0])
                listbox_HangHoa.insert(HH_upd[0], mo_ta)

                # Bạn có thể lưu previous_value vào file/log hoặc in ra nếu muốn
                print(f"Giá trị trước khi cập nhật: {TT_HHold}")
                print(f"Giá trị sau khi cập nhật: {mo_ta}")

                label_message.config(text="Cập nhật thành công!", fg='green')
                window_upd.destroy()
        else:
            Label_Nofi.config(text="Chọn hàng hóa để cập nhập!", fg='red')
            return

        btn_save = tk.Button(window_upd, text="Lưu cập nhật", command=save_update, width=15, bg='orange', fg='white', font=('Times New Roman', 12))
        btn_save.pack(pady=10)

    CSchinh = tk.Frame(root, bg='white')
    CSchinh.pack(expand=True, fill='both', padx=20, pady=20)

    label = tk.Label(CSchinh, text="Hàng hóa", font=("Times New Roman", 24,'bold'), fg='red',bg='white')
    label.pack(pady=(0, 20))

    listbox_HangHoa = tk.Listbox(CSchinh, font=('Times New Roman', 14), width=60, height=20)
    listbox_HangHoa.pack(pady=(0, 15), fill='x')

    khung = tk.Frame(CSchinh, bg='white')
    khung.pack(pady=10)
    #các button
    #Nút thêm
    khung = tk.Frame(CSchinh, bg='white')
    khung.pack(pady=10)

    # Nút thêm
    Button_add = tk.Button(khung, text="Thêm hàng hóa", command=open_add_form, width=20,height=5, bg='blue', fg='black', font=('Times New Roman', 16,'bold'))
    Button_add.pack(side='left', padx=10)

    # Nút xóa
    Button_delete = tk.Button(khung, text="Xóa hàng hóa", command=delete_package, width=20,height=5, bg='red', fg='black', font=('Times New Roman', 16,'bold'))
    Button_delete.pack(side='left', padx=10)

    # Nút cập nhật
    Button_update = tk.Button(khung, text="Cập nhật hàng hóa", command=update_package, width=20,height=5, bg='yellow', fg='black', font=('Times New Roman', 16,'bold'))
    Button_update.pack(side='left', padx=10)
    #Nút Thoát
    Button_leave=tk.Button(root, text="Thoát",command=root.quit,width=10,height=4,fg='black',font=("Times New Roman",14))
    Button_leave.pack(side="right",padx=5)
    '''Thông báo tin nhắn'''
    Label_Nofi = tk.Label(CSchinh, text="", bg='white', fg='red', font=('Times New Roman', 25))
    Label_Nofi.pack()
    
    '''---------------------------------------------------------------------------------------------------------------------------------------'''
NhapHangHoa()
root.mainloop()

