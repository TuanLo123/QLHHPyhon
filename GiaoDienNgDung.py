import tkinter as tk
import tkinter.messagebox as mb
import datetime
from tkinter import ttk
import json
import re

root = tk.Tk()
root.title("Quy trình Gửi hàng")
root.geometry("1024x768")
root.resizable(width=True, height=True)
root.configure(bg='Lightblue')
label_chinh=tk.Label(root, text="Quy trình thêm đơn hàng", bg='Lightblue', fg='black', font=("Times New Roman", 30, 'bold'))
label_chinh.pack(padx=20,pady=20)

HangHoa = {
    "Ng_Gui": None,
    "Ng_Nhan": None,
    "Hang_Hoa": None
}
DS_HH = []

def NhapTTNguoiGui():
    def KhuVucDiaLy_JsonLoad(filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            cities = [item['City'] for item in data['Area']]
            return cities
        except Exception as e:
            mb.showerror("Lỗi", f"Không thể đọc file JSON: {e}")
            return []

    def Form_TTNguoiGui():
        window_NgGui = tk.Toplevel(root)
        window_NgGui.title("Điền thông tin người gửi")
        window_NgGui.geometry("420x370")
        window_NgGui.configure(bg='white')

        label_title = tk.Label(window_NgGui, text="Thông tin người gửi", bg='white', fg='red', font=("Times New Roman", 20, 'bold'))
        label_title.pack(padx=10)

        TTNg_Gui = ["Tên người Gửi:", "Địa chỉ người Gửi:", "Thành phố:", "Điện thoại người Gửi:"]
        Ng_Gui = {}
        ThanhPho = KhuVucDiaLy_JsonLoad("khuvucdialy.json")

        for text in TTNg_Gui:
            khung_form = tk.Frame(window_NgGui, bg='white')
            khung_form.pack(fill='x', pady=5, padx=10)
            label_TT = tk.Label(khung_form, text=text, font=('Times New Roman', 14), bg='white', width=17, anchor='w')
            label_TT.pack(side='left')

            if text == "Thành phố:":
                combo = ttk.Combobox(khung_form, values=ThanhPho, font=('Times New Roman', 14), state='readonly')
                if ThanhPho:
                    combo.set(ThanhPho[0])
                combo.pack(side='left', fill='x', expand=True)
                Ng_Gui[text] = combo
            else:
                entry_TT = tk.Entry(khung_form, font=('Times New Roman', 14))
                entry_TT.pack(side='left', fill='x', expand=True)
                Ng_Gui[text] = entry_TT

        label_message = tk.Label(window_NgGui, text="", fg='red', bg='white', font=('Times New Roman', 12))
        label_message.pack(pady=10)

        def add_NgGui():
            tenNgGui = Ng_Gui["Tên người Gửi:"].get().strip()
            diachiNgGui = Ng_Gui["Địa chỉ người Gửi:"].get().strip()
            thanhpho = Ng_Gui["Thành phố:"].get().strip()
            dienthoaiNgGui = Ng_Gui["Điện thoại người Gửi:"].get().strip()

            if not tenNgGui or not diachiNgGui or not dienthoaiNgGui:
                label_message.config(text="Không được thiếu thông tin!")
                return
            pattern = r'^0\d{9}$'
            if not re.match(pattern, dienthoaiNgGui):
                label_message.config(text="Số điện thoại phải có 10 chữ số và bắt đầu bằng 0")
                return

            HangHoa["Ng_Gui"] = {
                "Tên": tenNgGui,
                "Địa chỉ": diachiNgGui,
                "Thành phố": thanhpho,
                "Điện thoại": dienthoaiNgGui
            }
            mb.showinfo("Thông báo", "Đã hoàn tất thêm người gửi")
            window_NgGui.destroy()

        Button_HT = tk.Button(window_NgGui, text="Thêm", command=add_NgGui, width=15, bg='blue', fg='white', font=('Times New Roman', 12))
        Button_HT.pack(pady=10)

    Form_TTNguoiGui()

def NhapTTNguoiNhan():
    def KhuVucDiaLy_JsonLoad(filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            cities = [item['City'] for item in data['Area']]
            return cities
        except Exception as e:
            mb.showerror("Lỗi", f"Không thể đọc file JSON: {e}")
            return []

    def Form_TTNguoiNhan():
        window_NgNhan = tk.Toplevel(root)
        window_NgNhan.title("Điền thông tin người nhận")
        window_NgNhan.geometry("420x370")
        window_NgNhan.configure(bg='white')

        label_title = tk.Label(window_NgNhan, text="Thông tin người nhận", bg='white', fg='red', font=("Times New Roman", 20, 'bold'))
        label_title.pack(padx=10)

        TTNg_Nhan = ["Tên người nhận:", "Địa chỉ người nhận:", "Thành phố:", "Điện thoại người nhận:"]
        Ng_Nhan = {}
        ThanhPho = KhuVucDiaLy_JsonLoad("khuvucdialy.json")

        for text in TTNg_Nhan:
            khung_form = tk.Frame(window_NgNhan, bg='white')
            khung_form.pack(fill='x', pady=5, padx=10)
            label_TT = tk.Label(khung_form, text=text, font=('Times New Roman', 14), bg='white', width=17, anchor='w')
            label_TT.pack(side='left')

            if text == "Thành phố:":
                combo = ttk.Combobox(khung_form, values=ThanhPho, font=('Times New Roman', 14), state='readonly')
                if ThanhPho:
                    combo.set(ThanhPho[0])
                combo.pack(side='left', fill='x', expand=True)
                Ng_Nhan[text] = combo
            else:
                entry_TT = tk.Entry(khung_form, font=('Times New Roman', 14))
                entry_TT.pack(side='left', fill='x', expand=True)
                Ng_Nhan[text] = entry_TT

        label_message = tk.Label(window_NgNhan, text="", fg='red', bg='white', font=('Times New Roman', 12))
        label_message.pack(pady=10)

        def add_NgNhan():
            tenNgNhan = Ng_Nhan["Tên người nhận:"].get().strip()
            diachiNgNhan = Ng_Nhan["Địa chỉ người nhận:"].get().strip()
            thanhpho = Ng_Nhan["Thành phố:"].get().strip()
            dienthoaiNgNhan = Ng_Nhan["Điện thoại người nhận:"].get().strip()

            if not tenNgNhan or not diachiNgNhan or not dienthoaiNgNhan:
                label_message.config(text="Không được thiếu thông tin!")
                return
            pattern = r'^0\d{9}$'
            if not re.match(pattern, dienthoaiNgNhan):
                label_message.config(text="Số điện thoại phải có 10 chữ số và bắt đầu bằng 0")
                return

            HangHoa['Ng_Nhan'] = {
                "Tên": tenNgNhan,
                "Địa chỉ": diachiNgNhan,
                "Thành phố": thanhpho,
                "Điện thoại": dienthoaiNgNhan
            }
            mb.showinfo("Thông báo", "Đã thêm người nhận thành công")
            window_NgNhan.destroy()

        Button_HT = tk.Button(window_NgNhan, text="Thêm", command=add_NgNhan, width=15, bg='blue', fg='white', font=('Times New Roman', 12))
        Button_HT.pack(pady=10)

    Form_TTNguoiNhan()

def NhapHangHoa():
    window_Con = tk.Toplevel(root)
    window_Con.title("Nhập thông tin hàng hóa")
    window_Con.geometry("400x350")
    window_Con.configure(bg='white')

    window_Con_label=tk.Label(window_Con,text="Nhập thông tin hàng hóa",bg='white',fg='red',font=('Times New Roman',20,'bold'))
    window_Con_label.pack(padx=10)
    TT_HangHoa = ["Tên sản phẩm:", "Mã hàng hóa:", "Số tiền:", "Ngày gửi:", "Loại hàng hóa:"]
    vatpham = {}

    for text in TT_HangHoa:
        khung_form = tk.Frame(window_Con, bg='white')
        khung_form.pack(fill='x', pady=5, padx=10)
        label_TT = tk.Label(khung_form, text=text, font=('Times New Roman', 14), bg='white', width=15, anchor='w')
        label_TT.pack(side='left')
        entry_TT = tk.Entry(khung_form, font=('Times New Roman', 14))
        entry_TT.pack(side='left', fill='x', expand=True)
        vatpham[text] = entry_TT

    label_message = tk.Label(window_Con, text="", fg='red', bg='white', font=('Times New Roman', 12))
    label_message.pack(pady=10)

    def add_package():
        ten_sp = vatpham["Tên sản phẩm:"].get().strip()
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
            Nam_Gui = datetime.datetime.strptime(ngay_gui, "%d/%m/%Y")
            Nam_HienTai = datetime.datetime.now().year
            if Nam_Gui.year > Nam_HienTai:
                label_message.config(text="Năm gửi không được vượt qua năm hiện tại!", fg="red")
                return
            elif Nam_Gui > datetime.datetime.now():
                label_message.config(text="Ngày gửi không được vượt quá ngày hiện tại!", fg="red")
                return
        except ValueError:
            label_message.config(text="Ngày gửi không đúng định dạng (dd/mm/yyyy)!", fg='red')
            return

        HangHoa["Hang_Hoa"] = {
            "Tên sản phẩm": ten_sp,
            "Mã hàng hóa": ma_hh,
            "Số tiền": tien1,
            "Ngày gửi": ngay_gui,
            "Loại hàng hóa": loai_hh
        }
        DS_HH.append(HangHoa["Hang_Hoa"])
        mb.showinfo("Thông báo", "Đã thêm hàng hóa thành công!")
        window_Con.destroy()

    Button_add = tk.Button(window_Con, text="Thêm", bg='blue', fg='white', command=add_package, width=15, font=('Times New Roman', 12))
    Button_add.pack(pady=10)

def hoan_tat_don_hang():
    window = tk.Toplevel()
    window.title("Thông tin đơn hàng")
    window.geometry("650x500")
    window.configure(bg='white')
    label_window=tk.Label(window,text="thông tin hàng hóa",bg='white',fg='red',font=('Times New Roman',20,'bold'))
    label_window.pack(padx=10)
    frame_DH = tk.Frame(window, bg='white')
    frame_DH.pack(fill='both', expand=True, padx=10, pady=10)#Khung show đơn hàng

    # Thông tin người gửi
    if HangHoa.get('Ng_Gui'):
        NgGui = HangHoa['Ng_Gui']
        TT_NgGui = (f"Người gửi:\n"f"Tên: {NgGui.get('Tên', '')}\n"f"Địa chỉ: {NgGui.get('Địa chỉ', '')}\n"f"Thành phố: {NgGui.get('Thành phố', '')}\n"f"Điện thoại: {NgGui.get('Điện thoại', '')}")
    else:
        TT_NgGui = "Chưa có thông tin người gửi."

    label_NgGui = tk.Label(frame_DH, text=TT_NgGui, bg='white', fg='black', font=("Times New Roman", 14), justify='left')
    label_NgGui.pack(pady=5, anchor='w', padx=10)

    # Thông tin người nhận
    if HangHoa.get('Ng_Nhan'):
        NgNhan = HangHoa['Ng_Nhan']
        TT_NgNhan = (f"Người nhận:\n"f"Tên: {NgNhan.get('Tên', '')}\n"f"Địa chỉ: {NgNhan.get('Địa chỉ', '')}\n"f"Thành phố: {NgNhan.get('Thành phố', '')}\n"f"Điện thoại: {NgNhan.get('Điện thoại', '')}")
    else:
        TT_NgNhan = "Chưa có thông tin người nhận."

    label_NgNhan = tk.Label(frame_DH, text=TT_NgNhan, bg='white', fg='black',font=("Times New Roman", 14), justify='left')
    label_NgNhan.pack(pady=5, anchor='w', padx=10)

    # Danh sách hàng hóa
    if DS_HH:
        HH_Ten = "Danh sách hàng hóa:\n"
        for  hh in enumerate(DS_HH, start=1):
            HH_Ten += (f" {hh.get('Tên sản phẩm', '')} (Mã: {hh.get('Mã hàng hóa', '')}), "f"Số tiền: {hh.get('Số tiền', '')}, Ngày gửi: {hh.get('Ngày gửi', '')}, "f"Loại: {hh.get('Loại hàng hóa', '')}\n")
    else:
        hh_text = "Chưa có hàng hóa nào được thêm."

    label_hh = tk.Label(frame_DH, text=hh_text, bg='white', fg='black',font=("Times New Roman", 14), justify='left')
    label_hh.pack(pady=5, anchor='w', padx=10)

    # Nếu muốn lưu file ở đây

    donhang_data = {
        "Ng_Gui": HangHoa.get("Ng_Gui", {}),
        "Ng_Nhan": HangHoa.get("Ng_Nhan", {}),
        "Hang_Hoa": DS_HH
    }
    try:
        with open("DonHang.json", "r", encoding="utf-8") as file:
            data_cu = json.load(file)
    except(FileNotFoundError):
        data=[]
    except(json.JSONDecodeError):
        data=[]
    
    # Thêm đơn hàng mới
    data_cu.append(donhang_data)
    try:
        with open("DonHang.json", "w", encoding="utf-8") as f:
            json.dump(data_cu, f, ensure_ascii=False, indent=4)
    except Exception as e:
        mb.showerror("Lỗi", f"Lưu đơn hàng thất bại: {e}")
    # Nút thoát
    def XacMinh():
        if mb.askquestion("Xác nhận thông tin", "Bạn có chắc chắn thông tin đơn hàng đã đúng?"):
            window.destroy()  # hoặc window.destroy() nếu bạn đang ở cửa sổ con
        else:
            # Người dùng chọn No, không làm gì, vẫn ở lại cửa sổ
            pass
    Button_XacMinh=tk.Button(frame_DH,text="Xác nhận",fg='red',command=XacMinh,width=15, font=('Times New Roman', 14))
    Button_XacMinh.pack(pady=10)
#Show thông tin đơn hàng
def xem_don_hang():
    window = tk.Toplevel(root)
    window.title("Danh sách hàng hóa")
    window.geometry("1240x600")
    window.configure(bg='white')
    #Tree view xem hàng hóa
    tree = ttk.Treeview(window)
    tree.pack(fill='both', expand=True)
    #tạo khung để tìm kiếm hàng hóa theo mã
    khung_search=tk.Frame(window, bg='white')
    khung_search.pack(anchor='w', padx=10, pady=5)
    label_search=tk.Label(khung_search, text="Nhập mã đơn: ", bg='white').pack(side='left')
    entry_search = tk.Entry(khung_search)
    entry_search.pack(side='left', padx=5)
    #Các teen cột
    tree['columns'] = ('Người gửi', 'Địa chỉ gửi', 'Thành phố gửi', 'Điện thoại gửi','Người nhận', 'Địa chỉ nhận', 'Thành phố nhận', 'Điện thoại nhận','Tên sản phẩm', 'Mã hàng hóa', 'Số tiền', 'Ngày gửi', 'Loại hàng hóa')

    tree.column('#0', width=0, stretch=tk.NO)  #ngắn người dùng kéo dài cột đầu'
    for col in tree['columns']:
        tree.column(col, anchor=tk.W, width=120)
        tree.heading(col, text=col, anchor=tk.W)

    # Đọc dữ liệu từ file JSON
    try:
        with open("DonHang.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        mb.showwarning("Thông báo", "Chưa có đơn hàng nào được lưu.")
        window.destroy()
        return
    except json.JSONDecodeError:
        mb.showerror("Lỗi", "File đơn hàng bị lỗi hoặc trống.")
        window.destroy()
        return

    # Duyệt dữ liệu và thêm vào Treeview
    for donhang in data:
        Ng_Gui = donhang.get("Ng_Gui", {})
        Ng_Nhan = donhang.get("Ng_Nhan", {})
        List_HH = donhang.get("Hang_Hoa", [])
        # Xuất đơn hàng ở dạng nhiều người
        for hh in List_HH:
            tree.insert(parent='', index='end', iid=None, values=(Ng_Gui.get("Tên", ""),Ng_Gui.get("Địa chỉ", ""),Ng_Gui.get("Thành phố", ""),Ng_Gui.get("Điện thoại", ""),Ng_Nhan.get("Tên", ""),Ng_Nhan.get("Địa chỉ", ""),Ng_Nhan.get("Thành phố", ""),Ng_Nhan.get("Điện thoại", ""),hh.get("Tên sản phẩm", ""),hh.get("Mã hàng hóa", ""),hh.get("Số tiền", ""),hh.get("Ngày gửi", ""),hh.get("Loại hàng hóa", "")))
#Hộp tìm kiếm thông tin theo mã
    def TimKiem_HHMa():
        Ma=entry_search.get().strip()
        if not Ma:
            mb.showwarning("Cảnh báo","Vui lòng nhập mã hàng hóa để tìm kiếm")
            return
        KQ=[]
        for dh in data:
            for hang in donhang.get("Hang_Hoa", []):
                if hang.get("Mã hàng hóa", "").lower() == Ma.lower():
                    KQ.append({
                    "Ng_Gui": donhang.get("Ng_Gui", {}),
                    "Ng_Nhan": donhang.get("Ng_Nhan", {}),
                    "Hang_Hoa": [hang]
                })
        if KQ:
            xem_don_hang(KQ[0])
        else:
            mb.showinfo("Không tìm thấy", f"Không tìm thấy mã hàng hóa: {Ma}")
    #Nút bấm tìm kiếm
    Button_timkiem=tk.Button(khung_search, text="Tìm kiếm", command=TimKiem_HHMa)
    Button_timkiem.pack(side="left")
        
# Giao diện chính nút bấm
Button_NgGui=tk.Button(root, text="Nhập thông tin người gửi", font=("Times New Roman", 20), fg='white', bg='blue', command=NhapTTNguoiGui)
Button_NgGui.pack(pady=20)

Button_NgNhan=tk.Button(root, text="Nhập thông tin người nhận", font=("Times New Roman", 20), fg='white', bg='blue', command=NhapTTNguoiNhan)
Button_NgNhan.pack(pady=20)

Button_HH=tk.Button(root, text="Thêm hàng hóa", font=("Times New Roman", 20), fg='white', bg='blue', command=NhapHangHoa)
Button_HH.pack(pady=20)

Button_HoanThanh=tk.Button(root, text="Hoàn tất đơn hàng", font=("Times New Roman", 20), fg='white', bg='green', command=hoan_tat_don_hang)
Button_HoanThanh.pack(pady=20)
# Thêm nút xem thông tin đơn hàng bằng Treeview vào giao diện chính:
Button_XemThongTin=tk.Button(root, text="Xem thông tin đơn hàng", font=("Times New Roman", 20), fg='white', bg='blue', command=xem_don_hang)
Button_XemThongTin.pack(pady=20,padx=20)

#Note 
label_NOTE=tk.Label(root, text="*Lưu ý: Thực hiện đủ các bước để đặt đơn hàng", fg='red',bg='Lightblue', font=("Times New Roman", 20, 'bold'))
label_NOTE.pack(padx=10)

root.mainloop()