import tkinter as tk
import pytube as pyt

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.geometry("500x400")
        self.labels = {
            "top_lable" : tk.Label(self, text = "Enter video link", font = "bold 12"),
            "msg_label" : tk.Label(self, text = "", fg = "red"),
            "vid_title" : tk.Label(self, text = "")
        }
        self.link_input = tk.Entry(self, width = 30)
        self.process_btn = tk.Button(self, text = "Process", font = "bold 12", command=self.process_link)
        self.vid_url = ""
        self.download_btn_list  = [tk.Button(self, text = "", width=10) for i in range(32)]
        self.place_widgets()

    def place_widgets(self):
        self.labels["top_lable"].grid(row = 0, pady=(8, 8))
        self.link_input.grid(row = 1)
        self.process_btn.grid(row = 2, pady=(8, 8))

    def process_link(self):
        if self.vid_url != self.link_input.get():
            self.vid_url = self.link_input.get()
            for btn in self.download_btn_list:
                btn.grid_remove()
            self.labels["msg_label"].grid_remove()
            self.labels["vid_title"].grid_remove()
            try:
                vid = pyt.YouTube(self.vid_url)
                try:
                    title = vid.title
                    self.labels["vid_title"]["text"] = title
                    self.labels["vid_title"].grid(row = 3)
                    self.process_stream(vid)
                except:
                    self.labels["msg_label"]["text"] = "Incurrect link or network error."
                    self.labels["msg_label"].grid(row = 4)
            except:
                self.labels["msg_label"]["text"] = "Not a valid YouTube link."
                self.labels["msg_label"].grid(row = 4)
        
    def process_stream(self, vid: pyt.YouTube):
        streams = vid.streams
        tmp_rsln = ["144p", "240p", "360p", "480p", "720p", "1080p"]
        i = 0
        for stream in streams:
            if stream.resolution and stream.resolution in tmp_rsln and stream.mime_type == "video/mp4":
                self.download_btn_list[i]["text"] = stream.resolution
                self.download_btn_list[i]["command"] = stream.download
                i += 1
        for j in range(i):
            self.download_btn_list[j].grid(row = 5 + j)


if __name__ == "__main__":
    app = App()
    app.mainloop()