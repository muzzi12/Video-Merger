from moviepy import editor
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
import sys
import random
import threading
import webbrowser as wb


video1 = ''
video2 = ''
video3 = ''
video4 = ''
video5 = ''
video6 = ''
video7 = ''
video8 = ''
video9 = ''
video10 = ''
videos = []

class VIDEO_EDITOR:
    def __init__(self, master):
        self.master = master
        self.title = master.title('Video Merger')
        self.resizable = master.resizable(0,0)
        self.geometry = master.geometry('600x200')
        self.background = master.config(background='grey16')
        frame = Frame(master,background='red')
        self.label1 = Label(frame,text='Welcome To The Video Merger!',font='cursive 20 bold italic',fg='aqua',bd=0,bg='black')
        self.label1.pack(pady=5,padx=5)
        frame.pack(side=TOP)
        self.choose = Button(master,text='Choose Files',bg='orange',fg='white',font='cursive 10 bold',cursor='hand2'
                             ,activeforeground='grey',activebackground='black',command=self.choose1)
        self.choose.pack(pady=20)
        self.choose.bind('<Enter>',self.enter1)
        self.choose.bind('<Leave>',self.leave1)
        self.merge = Button(master, text='Merge!', bg='orange', fg='white', font='cursive 10 bold', cursor='hand2'
                            , activeforeground='grey', activebackground='black',command=self.create1)
        self.merge.pack(side=BOTTOM)
        self.merge.bind('<Enter>',self.enter2)
        self.merge.bind('<Leave>',self.leave2)

        self.v1 = Label(master,text=''
                         ,font='cursive 9',bg='grey16',fg='white',activeforeground='white',activebackground='grey16')
        self.v1.pack(anchor='w',padx=15,pady=10)

        self.v2 = Label(master,text='',font='cursive 9',bg='grey16',fg='white'
                        ,activeforeground='white',activebackground='grey16')
        self.v2.pack(anchor='w',padx=15,pady=10)

        self.v3 = Label(master,text='',font='cursive 9',bg='grey16',fg='white'
                        ,activeforeground='white',activebackground='grey16')
        self.v3.pack(anchor='w',padx=15,pady=10)

        self.v4 = Label(master,text='',font='cursive 9',bg='grey16',fg='white'
                     ,activeforeground='white',activebackground='grey16')
        self.v4.pack(anchor='w',padx=15,pady=10)

        self.v5 = Label(master,text='',font='cursive 9',bg='grey16',fg='white'
                        ,activeforeground='white',activebackground='grey16')
        self.v5.pack(anchor='w',padx=15,pady=10)

        self.v6 = Label(master,text='',font='cursive 9',bg='grey16',fg='white'
                        ,activeforeground='white',activebackground='grey16')
        self.v6.pack(anchor='w',padx=15,pady=10)

        self.v7 = Label(master,text='',font='cursive 9',bg='grey16',fg='white'
                        ,activeforeground='white',activebackground='grey16')
        self.v7.pack(anchor='w',padx=15,pady=10)
        self.v8 = Label(master,text='',font='cursive 9',bg='grey16',fg='white'
                        ,activeforeground='white',activebackground='grey16')
        self.v8.pack(anchor='w',padx=15,pady=10)

        self.v9 = Label(master,text='',font='cursive 9',bg='grey16',fg='white'
                        ,activeforeground='white',activebackground='grey16')
        self.v9.pack(anchor='w',padx=15,pady=10)

        self.v10 = Label(master,text='',font='cursive 9',bg='grey16',fg='white'
                        ,activeforeground='white',activebackground='grey16')
        self.v10.pack(anchor='w',padx=15,pady=10)
        self.master.protocol('WM_DELETE_WINDOW',self.close)

        self.menubar = Menu(master)
        self.menu1 = Menu(self.menubar,tearoff=0)
        self.menu1.add_command(label='Credits',command=self.credits)
        self.menu1.add_command(label='Source Code',command=self.source)
        self.menu1.add_command(label='About Author',command=self.about)
        self.menubar.add_cascade(label='Help',menu=self.menu1)
        master.config(menu=self.menubar)

        def change_frame_color():
            colors = ['blue','green','yellow','red','orange','aqua','violet','purple','grey','black','indigo','pink']
            color = random.choice(colors)
            frame.config(background=color)
            frame.after(500,change_frame_color)


        change_frame_color()
    def source(self):
        wb.open_new_tab('https://github.com/kalinbhaiya/File-Downloader/blob/main/main.py')

    def about(self):
        messagebox.showinfo('File Downloader', "Author : \nMuhammad Muzammil Alam\
                                                    Author's E-mail Address : \nmuzammil.alam231@gmail.com\
                                                    Author's Github Profile : \nhttps://github.com/kalinbhaiya\
                                                    Author's Facebook Profile : \nhttps://www.facebook.com/profile.php?id=100052280166322 Author's Instagram Profile : \nhttps://www.instagram.com/m.muzammil1231/")

        wb.open_new_tab('https://github.com/kalinbhaiya')
        wb.open_new_tab('https://www.facebook.com/profile.php?id=100052280166322')
        wb.open_new_tab('https://www.instagram.com/m.muzammil1231/')

    def close(self):
        question = messagebox.askquestion('Video Merger','Do you want to exit?')
        if question=='yes':
            sys.exit()
        else:
            pass

    def create(self):
        global videos,lenght1,length2,length3,length4,length5,length6,length7,length8,length9,length10
        if len(videos)<=1:
            messagebox.showerror('Video Merger','Please select some videos')

        elif len(videos) == 2:
            file = filedialog.asksaveasfilename(defaultextension='.mp4')
            m1 = editor.VideoFileClip(videos[0])
            m2 = editor.VideoFileClip(videos[1])
            final = editor.concatenate_videoclips([m1, m2], method='compose')

            try:
                final.write_videofile(file)
                os.startfile(file)
            except ValueError:
                pass

        elif len(videos) == 3:
            file = filedialog.asksaveasfilename(defaultextension='.mp4')
            m1 = editor.VideoFileClip(videos[0])
            m2 = editor.VideoFileClip(videos[1])
            m3 = editor.VideoFileClip(videos[2])


            final = editor.concatenate_videoclips([m1,m2,m3],method='compose')
            try:
                final.write_videofile(file)
                os.startfile(file)
            except ValueError:
                pass

        elif len(videos) == 4:
            file = filedialog.asksaveasfilename(defaultextension='.mp4')
            m1 = editor.VideoFileClip(videos[0])
            m2 = editor.VideoFileClip(videos[1])
            m3 = editor.VideoFileClip(videos[2])
            m4 = editor.VideoFileClip(videos[3])


            final = editor.concatenate_videoclips([m1,m2,m3,m4],method='compose')
            try:
                os.startfile(file)
            except ValueError:
                pass

        elif len(videos) == 5:
            file = filedialog.asksaveasfilename(defaultextension='.mp4')
            m1 = editor.VideoFileClip(videos[0])
            m2 = editor.VideoFileClip(videos[1])
            m3 = editor.VideoFileClip(videos[2])
            m4 = editor.VideoFileClip(videos[3])
            m5 = editor.VideoFileClip(videos[4])


            final = editor.concatenate_videoclips([m1,m2,m3,m4,m5],method='compose')
            try:
                final.write_videofile(file)
                os.startfile(file)
            except ValueError:
                pass

        elif len(videos) == 6:
            file = filedialog.asksaveasfilename(defaultextension='.mp4')
            m1 = editor.VideoFileClip(videos[0])
            m2 = editor.VideoFileClip(videos[1])
            m3 = editor.VideoFileClip(videos[2])
            m4 = editor.VideoFileClip(videos[3])
            m5 = editor.VideoFileClip(videos[4])
            m6 = editor.VideoFileClip(videos[5])


            final = editor.concatenate_videoclips([m1,m2,m3,m4,m4,m5,m6],method='compose')
            try:
                final.write_videofile(file)
                os.startfile(file)
            except ValueError:
                pass

        elif len(videos) == 7:
            file = filedialog.asksaveasfilename(defaultextension='.mp4')
            m1 = editor.VideoFileClip(videos[0])
            m2 = editor.VideoFileClip(videos[1])
            m3 = editor.VideoFileClip(videos[2])
            m4 = editor.VideoFileClip(videos[3])
            m5 = editor.VideoFileClip(videos[4])
            m6 = editor.VideoFileClip(videos[5])
            m7 = editor.VideoFileClip(videos[6])


            final = editor.concatenate_videoclips([m1,m2,m3,m4,m5,m6,m7],method='compose')
            try:
                final.write_videofile(file)
                os.startfile(file)
            except ValueError:
                pass

        elif len(videos) == 8:
            file = filedialog.asksaveasfilename(defaultextension='.mp4')
            m1 = editor.VideoFileClip(videos[0])
            m2 = editor.VideoFileClip(videos[1])
            m3 = editor.VideoFileClip(videos[2])
            m4 = editor.VideoFileClip(videos[3])
            m5 = editor.VideoFileClip(videos[4])
            m6 = editor.VideoFileClip(videos[5])
            m7 = editor.VideoFileClip(videos[6])
            m8 = editor.VideoFileClip(videos[7])


            final = editor.concatenate_videoclips([m1,m2,m3,m4,m5,m6,m7,m8],method='compose')
            try:
                final.write_videofile(file)
                os.startfile(file)
            except ValueError:
                pass

        elif len(videos) == 9:
            file = filedialog.asksaveasfilename(defaultextension='.mp4')
            m1 = editor.VideoFileClip(videos[0])
            m2 = editor.VideoFileClip(videos[1])
            m3 = editor.VideoFileClip(videos[2])
            m4 = editor.VideoFileClip(videos[3])
            m5 = editor.VideoFileClip(videos[4])
            m6 = editor.VideoFileClip(videos[5])
            m7 = editor.VideoFileClip(videos[6])
            m8 = editor.VideoFileClip(videos[7])
            m9 = editor.VideoFileClip(videos[8])


            final = editor.concatenate_videoclips([m1,m2,m3,m4,m5,m6,m7,m8,m9],method='compose')
            try:
                final.write_videofile(file)
                os.startfile(file)
            except ValueError:
                pass

        elif len(videos) == 10:
            file = filedialog.asksaveasfilename(defaultextension='.mp4')
            m1 = editor.VideoFileClip(videos[0])
            m2 = editor.VideoFileClip(videos[1])
            m3 = editor.VideoFileClip(videos[2])
            m4 = editor.VideoFileClip(videos[3])
            m5 = editor.VideoFileClip(videos[4])
            m6 = editor.VideoFileClip(videos[5])
            m7 = editor.VideoFileClip(videos[6])
            m8 = editor.VideoFileClip(videos[7])
            m9 = editor.VideoFileClip(videos[8])
            m10 = editor.VideoFileClip(videos[9])


            final = editor.concatenate_videoclips([m1,m2,m3,m4,m5,m6,m7,m8,m9,m10],method='compose')
            try:
                final.write_videofile(file)
                os.startfile(file)
            except ValueError:
                pass

    def create1(self):
        a = threading.Thread(target=self.create)
        a.start()


    def choose1(self):

        global video1,video2,video3,video4,video5,video6,video7,video8,video9,video10,videos
        self.master.geometry('600x200')
        self.v1.config(text='')
        self.v2.config(text='')
        self.v3.config(text='')
        self.v4.config(text='')
        self.v5.config(text='')
        self.v6.config(text='')
        self.v7.config(text='')
        self.v8.config(text='')
        self.v9.config(text='')
        self.v10.config(text='')
        files = filedialog.askopenfilenames(filetypes=[('Mp4 files', '*.mp4'), ('webm files', '*.webm')],
                                              defaultextension='.mp4')
        if len(files)>10:

            self.v1.config(text='')
            self.v2.config(text='')
            self.v3.config(text='')
            self.v4.config(text='')
            self.v5.config(text='')
            self.v6.config(text='')
            self.v7.config(text='')
            self.v8.config(text='')
            self.v9.config(text='')
            self.v10.config(text='')
            messagebox.showerror('Video Merger','Sorry we cant merge more than 10 clips!')
            self.master.geometry('600x600')
            self.merge.pack(side=BOTTOM)
            video1 = files[0]
            video2 = files[1]
            video3 = files[2]
            video4 = files[3]
            video5 = files[4]
            video6 = files[5]
            video7 = files[6]
            video8 = files[7]
            video9 = files[8]
            video10 = files[9]
            videos = [video1,video2,video3,video4,video5,video6,video7,video8,video9,video10]
            self.v1.config(text=f'File 1 :     {video1}')
            self.v2.config(text=f'File 2 :     {video2}')
            self.v3.config(text=f'File 3 :     {video3}')
            self.v4.config(text=f'File 4 :     {video4}')
            self.v5.config(text=f'File 5 :     {video5}')
            self.v6.config(text=f'File 6 :     {video6}')
            self.v7.config(text=f'File 7 :     {video7}')
            self.v8.config(text=f'File 8 :     {video8}')
            self.v9.config(text=f'File 9 :     {video9}')
            self.v10.config(text=f'File 10 :     {video10}')

        elif len(files) == 1:
            messagebox.showerror('Video Merger','Please select atleast 2 videos!')
            videos = []
        elif len(files) == 2:
            self.master.geometry('600x250')
            video1 = files[0]
            video2 = files[1]
            videos = [video1, video2]
            self.v1.config(text=f'File 1 :     {video1}')
            self.v2.config(text=f'File 2 :     {video2}')

        elif len(files) == 3:
            self.master.geometry('600x300')
            video1 = files[0]
            video2 = files[1]
            video3 = files[2]
            videos = [video1, video2, video3]
            self.v1.config(text=f'File 1 :     {video1}')
            self.v2.config(text=f'File 2 :     {video2}')
            self.v3.config(text=f'File 3 :     {video3}')

        elif len(files) == 4:
            self.master.geometry('600x350')
            video1 = files[0]
            video2 = files[1]
            video3 = files[2]
            video4 = files[3]
            videos = [video1, video2, video3, video4]
            self.v1.config(text=f'File 1 :     {video1}')
            self.v2.config(text=f'File 2 :     {video2}')
            self.v3.config(text=f'File 3 :     {video3}')
            self.v4.config(text=f'File 4 :     {video4}')

        elif len(files) == 5:
            self.master.geometry('600x400')
            video1 = files[0]
            video2 = files[1]
            video3 = files[2]
            video4 = files[3]
            video5 = files[4]
            videos = [video1, video2, video3, video4, video5]
            self.v1.config(text=f'File 1 :     {video1}')
            self.v2.config(text=f'File 2 :     {video2}')
            self.v3.config(text=f'File 3 :     {video3}')
            self.v4.config(text=f'File 4 :     {video4}')
            self.v5.config(text=f'File 5 :     {video5}')

        elif len(files) == 6:
            self.master.geometry('600x450')
            video1 = files[0]
            video2 = files[1]
            video3 = files[2]
            video4 = files[3]
            video5 = files[4]
            video6 = files[5]
            videos = [video1, video2, video3, video4, video5, video6]
            self.v1.config(text=f'File 1 :     {video1}')
            self.v2.config(text=f'File 2 :     {video2}')
            self.v3.config(text=f'File 3 :     {video3}')
            self.v4.config(text=f'File 4 :     {video4}')
            self.v5.config(text=f'File 5 :     {video5}')
            self.v6.config(text=f'File 6 :     {video6}')

        elif len(files) == 7:
            self.master.geometry('600x500')
            video1 = files[0]
            video2 = files[1]
            video3 = files[2]
            video4 = files[3]
            video5 = files[4]
            video6 = files[5]
            video7 = files[6]
            videos = [video1, video2, video3, video4, video5, video6, video7]
            self.v1.config(text=f'File 1 :     {video1}')
            self.v2.config(text=f'File 2 :     {video2}')
            self.v3.config(text=f'File 3 :     {video3}')
            self.v4.config(text=f'File 4 :     {video4}')
            self.v5.config(text=f'File 5 :     {video5}')
            self.v6.config(text=f'File 6 :     {video6}')
            self.v7.config(text=f'File 7 :     {video7}')

        elif len(files) == 8:
            self.master.geometry('600x550')
            video1 = files[0]
            video2 = files[1]
            video3 = files[2]
            video4 = files[3]
            video5 = files[4]
            video6 = files[5]
            video7 = files[6]
            video8 = files[7]
            videos = [video1, video2, video3, video4, video5, video6, video7, video8]
            self.v1.config(text=f'File 1 :     {video1}')
            self.v2.config(text=f'File 2 :     {video2}')
            self.v3.config(text=f'File 3 :     {video3}')
            self.v4.config(text=f'File 4 :     {video4}')
            self.v5.config(text=f'File 5 :     {video5}')
            self.v6.config(text=f'File 6 :     {video6}')
            self.v7.config(text=f'File 7 :     {video7}')
            self.v8.config(text=f'File 8 :     {video8}')

        elif len(files) == 9:
            self.master.geometry('600x600')
            video1 = files[0]
            video2 = files[1]
            video3 = files[2]
            video4 = files[3]
            video5 = files[4]
            video6 = files[5]
            video7 = files[6]
            video8 = files[7]
            video9 = files[8]
            videos = [video1, video2, video3, video4, video5, video6, video7, video8, video9]
            self.v1.config(text=f'File 1 :     {video1}')
            self.v2.config(text=f'File 2 :     {video2}')
            self.v3.config(text=f'File 3 :     {video3}')
            self.v4.config(text=f'File 4 :     {video4}')
            self.v5.config(text=f'File 5 :     {video5}')
            self.v6.config(text=f'File 6 :     {video6}')
            self.v7.config(text=f'File 7 :     {video7}')
            self.v8.config(text=f'File 8 :     {video8}')
            self.v9.config(text=f'File 9 :     {video9}')

        elif len(files) == 10:
            self.merge.pack(side=BOTTOM)
            self.master.geometry('600x600')
            video1 = files[0]
            video2 = files[1]
            video3 = files[2]
            video4 = files[3]
            video5 = files[4]
            video6 = files[5]
            video7 = files[6]
            video8 = files[7]
            video9 = files[8]
            video10 = files[9]
            videos = [video1, video2, video3, video4, video5, video6, video7, video8, video9, video10]
            self.v1.config(text=f'File 1 :     {video1}')
            self.v2.config(text=f'File 2 :     {video2}')
            self.v3.config(text=f'File 3 :     {video3}')
            self.v4.config(text=f'File 4 :     {video4}')
            self.v5.config(text=f'File 5 :     {video5}')
            self.v6.config(text=f'File 6 :     {video6}')
            self.v7.config(text=f'File 7 :     {video7}')
            self.v8.config(text=f'File 8 :     {video8}')
            self.v9.config(text=f'File 9 :     {video9}')
            self.v10.config(text=f'File 10 :     {video10}')

    def credits(self):
        messagebox.showinfo('Video Merger','Video Merger app created by Muhammad Muzammil Alam, if you have any problem regarding this app, you can email to muzammil.alam231@gmail.com. Thanks!')

    def enter1(self,event):
        self.choose.config(bg='aqua',fg='orange',relief=GROOVE)

    def leave1(self,event):
        self.choose.config(bg='orange',fg='white',relief=RAISED)

    def enter2(self,event):
        self.merge.config(bg='aqua',fg='orange',relief=GROOVE)

    def leave2(self,event):
        self.merge.config(bg='orange',fg='white',relief=RAISED)

app = Tk()
VIDEO_EDITOR(app)
app.mainloop()
