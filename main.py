import tkinter as tk
from PIL import Image, ImageTk
import json
import re
import datetime
import tkinter.messagebox as mb
from GiaoDienNgDung import NhapTTNguoiGui,NhapHangHoa,NhapTTNguoiNhan,xem_don_hang,hoan_tat_don_hang
import os

def DangNhap():
    global root
    global bg_image
    root.title("Đăng nhập")
    root.geometry("470x250")
    # Tạo ảnh nền trước tiên để nằm dưới cùng
    image = Image.open("FormDangNhap.png")  # ảnh nền
    image = image.resize((470, 250))
    bg_image = ImageTk.PhotoImage(image)
    bg_label = tk.Label(root, image=bg_image)
    bg_label.image = bg_image
    bg_label.grid(row=0, column=0, columnspan=3, rowspan=10, sticky='nsew')
    # Tiêu đề
    Label_TD = tk.Label(root, text="Đăng nhập", font=("Times New Roman", 20, 'bold'), fg='red', bg='white')
    Label_TD.grid(row=0, column=1, padx=10, pady=5)
    # Ô nhập thông tin (tạo 1 lần rồi grid)
    label_User = tk.Label(root, text='Tài khoản: ', font=('Times New Roman', 16), bg='white')
    label_Password = tk.Label(root, text='Mật khẩu: ', font=('Times New Roman', 16), bg='white')
    entry_User = tk.Entry(root, width=20, font=('Times New Roman', 16), bg='white')
    entry_Password = tk.Entry(root, width=20, font=('Times New Roman', 16), bg='white', show='*')
    label_User.grid(row=2, column=0, sticky='nsew', padx=10, pady=5)
    entry_User.grid(row=2, column=1, sticky='nsew', padx=10, pady=5)
    label_Password.grid(row=4, column=0, sticky='nsew', padx=10, pady=5)
    entry_Password.grid(row=4, column=1, sticky='nsew', padx=10, pady=5)
    #Note cho phần tài khoản
    Label_Note=tk.Label(root,text="(*Tài khoản là email của bạn)",bg='white',fg='red',font=("Times New Roman",10))
    Label_Note.grid(row=3,column=1,columnspan=1)
    #Xử lý các nút bấm
   
    '''Nút Đăng ký'''
    def Form_Resignter():
        root.withdraw()
        #Tên người dùng, email người dùng, mật khẩu người dùng, ngày tháng năm sinh
        window_DangKy=tk.Toplevel(root)
        window_DangKy.title("Form Đăng ký")
        window_DangKy.geometry("600x350")
        window_DangKy.configure(bg='white')
        #Đăng ký
        Label_DK=tk.Label(window_DangKy,text="Đăng Ký",bg='white',fg='red',font=("Times New Roman",20,'bold'))
        Label_DK.grid(row=0,column=1)
        TT_Dangky=["Tên người dùng:","Email:","Mật khẩu:","Năm sinh:"]
        FormDK={}
        #Xử lý định dạng email
        def is_valid_email(email):
            pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
            if re.match(pattern, email):
                return True
            else:
                return False
        for i, text in enumerate(TT_Dangky):
            label_TT = tk.Label(window_DangKy, text=text, font=('Times New Roman', 14), bg='white', width=15, anchor='w')
            label_TT.grid(row=i+1,column=0,padx=10,pady=5,sticky='w')
            entry_TT = tk.Entry(window_DangKy, font=('Times New Roman', 14),width=30)
            entry_TT.grid(row=i+1,column=1,padx=10,pady=5,sticky='e')
            FormDK[text] = entry_TT
        #Hiển thị thông báo
        label_message = tk.Label(window_DangKy, text="", fg='red', bg='white', font=('Times New Roman', 17,'bold'))
        label_message.grid(row=5,column=0,pady=10,columnspan=2,sticky='w')

        #THêm người dùng vào file jsson
        def Add_UserJsonFile():
            #Thông tin đưa vào json
            data_json={
                "Tên người dùng":FormDK["Tên người dùng:"].get().strip() ,
                "Email":FormDK["Email:"].get().strip(),
                "Mật khẩu":FormDK["Mật khẩu:"].get().strip(),
                "Năm sinh":FormDK["Năm sinh:"].get().strip()
                }
            #Xử lý các ngoại lệ
            if not data_json['Tên người dùng'] or not data_json['Email'] or not data_json['Mật khẩu'] or not data_json['Năm sinh']:
                label_message.config(text="Vui lòng nhập đầy đủ thông tin",fg='red')
                return
            #Email
            if is_valid_email(data_json['Email'])==False:
                label_message.config(text="Email không đúng định dạng!",fg='red')
                return
            #Ngoại lệ ngày
            try:
                Nam_sinh=datetime.datetime.strptime(data_json["Năm sinh"], "%d/%m/%Y")
                Nam_HienTai=datetime.datetime.now().year
                if Nam_sinh.year > Nam_HienTai:
                    label_message.config(text="Năm sinh không được vượt qua năm hiện tại!",fg="red")
                    return
                elif Nam_sinh > datetime.datetime.now():
                    label_message.config(text="Ngày sinh không được vượt qua ngày hiện tại!",fg="red")
                    return
            except ValueError:
                label_message.config(text="Năm sinh phải định dạng (dd/mm/yyyy)!", fg='red')
                return
            file="users.json"
            #Kiểm tra xem file có tồn tại không
            try:
                with open(file,'r',encoding='utf-8') as file1:
                    data=json.load(file1)
            except(FileNotFoundError):
                data=[]
            except(json.JSONDecodeError):
                data=[]
            #Kiểm tra email có trong file chx
            for NgDung in data:
                if NgDung.get("Email","").lower() == data_json["Email"].lower():
                    label_message.config(text="Email đã tồn tại!",fg='red')
                    return
            #Thêm thông tin người dùng
            data.append(data_json)
            #Ghi file json
            with open(file,'w',encoding='utf-8') as file1:
                json.dump(data,file1,indent=4,ensure_ascii=False)
            label_message.config(text="Đăng ký thành công",fg='green')
            window_DangKy.destroy() 
            root.deiconify()# Hiện lại form đăng nhập

        # Nút Đăng ký
        Button_Register = tk.Button(window_DangKy, text="Đăng ký",command=Add_UserJsonFile, fg='black', font=("Times New Roman", 16))
        Button_Register.grid(row=6, column=2, padx=10, pady=10, sticky='e')
    '''Nút Đăng nhập'''
    def Button_Login():
        DN=entry_User.get().strip()
        PS=entry_Password.get().strip()
        #Thông báo
        if not DN or not PS:
            mb.showerror("Lỗi","Vui lòng nhập đầy đủ thông tin!")
            return
        #Kiểm tra có trong file jsson
        try:
            with open('users.json','r',encoding='utf-8') as file:
                NgDung=json.load(file)
        except(FileNotFoundError):
            mb.showerror("Lỗi","Dữ liệu người dùng không có")
            return
        except(json.JSONDecodeError):
            mb.showerror("Lỗi","Dữ liệu người dùng không có")
            return
        for ng in NgDung:
            if ng.get("Email","").lower() == DN.lower() and ng.get("Mật khẩu","")==PS:
                mb.showinfo("Thông báo","Đăng nhập tài khoản thành công")
                root.withdraw()
                CSC=tk.Tk()
                CSC.title("Quy trình Gửi hàng")
                CSC.geometry("1024x768")
                CSC.resizable(width=True, height=True)
                label_chinh=tk.Label(CSC, text="Quy trình thêm đơn hàng", font=("Times New Roman", 30, 'bold'))
                label_chinh.pack(padx=20,pady=20)
                Button_NgGui=tk.Button(CSC, text="Nhập thông tin người gửi", font=("Times New Roman", 20), command=lambda:NhapTTNguoiGui(CSC))
                Button_NgGui.pack(pady=20)

                Button_NgNhan=tk.Button(CSC, text="Nhập thông tin người nhận", font=("Times New Roman", 20), command=lambda:NhapTTNguoiNhan(CSC))
                Button_NgNhan.pack(pady=20)

                Button_HH=tk.Button(CSC, text="Thêm hàng hóa", font=("Times New Roman", 20), command=lambda:NhapHangHoa(CSC))
                Button_HH.pack(pady=20)

                Button_HoanThanh=tk.Button(CSC, text="Hoàn tất đơn hàng", font=("Times New Roman", 20), command=lambda:hoan_tat_don_hang(CSC))
                Button_HoanThanh.pack(pady=20)
                # Thêm nút xem thông tin đơn hàng bằng Treeview vào giao diện chính:
                Button_XemThongTin=tk.Button(CSC, text="Xem thông tin đơn hàng", font=("Times New Roman", 20), command=lambda:xem_don_hang(CSC))
                Button_XemThongTin.pack(pady=20,padx=20)

                #Note 
                label_NOTE=tk.Label(CSC, text="*Lưu ý: Thực hiện đủ các bước để đặt đơn hàng, Nếu làm sai thì ...............", fg='red', font=("Times New Roman", 20, 'bold'))
                label_NOTE.pack(padx=10)

                #Nút đăng xuât
                def Button_LogOut():
                    CSC.destroy()
                    root.deiconify()#mở lại cửa sổ đăng nhập là root
                def XacNhan():
                    respon=mb.askquestion("Thông báo","Bạn muốn đăng xuất ?")
                    if respon=='yes':
                        Button_LogOut()
                    else:
                        pass
                Button_DangXuat=tk.Button(CSC, text="Đăng xuất", font=("Times New Roman", 16), command=XacNhan)
                Button_DangXuat.pack(pady=10, padx=10, anchor='ne') 
                return
        mb.showerror("Lỗi","Tài khoản hoặc mật khẩu sai!")
    
    # Nút đăng nhập
    Button_Login = tk.Button(root, text="Đăng nhập", command=Button_Login,fg='black', font=("Times New Roman", 16))
    Button_Login.grid(row=5, column=1, pady=10, padx=2)

    # Nút Đăng ký
    Button_Register = tk.Button(root, text="Đăng ký",command=Form_Resignter, fg='black', font=("Times New Roman", 16))
    Button_Register.grid(row=7, column=2, padx=10, pady=10, sticky='nsew')
root = tk.Tk()
DangNhap()
root.mainloop()