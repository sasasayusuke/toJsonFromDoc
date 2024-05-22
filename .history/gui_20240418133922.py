import tkinter as tk
import config
import util

# 以下の設定値は実際の設定ファイルまたはここに直接定義されています
UI_WIDTH = 600
UI_HEIGHT = 400
UI_API_KEY_WIDTH = 50
UI_SERVER_WIDTH = 50
UI_SITE_ID_WIDTH = 50
UI_LOG_WIDTH = 80

class Gui(tk.Tk):
    def __init__(self, title, execute_callback=None):
        super().__init__()
        self.title(title)
        self.geometry(f"{UI_WIDTH}x{UI_HEIGHT}")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.radio_value = tk.StringVar(value="API")
        self.execute_callback = execute_callback  # コールバック関数を保存

        self.create_widgets()
        self.initialize_default_values()

    def create_widgets(self):
        row_index = 0
        # self.label_input_dir = tk.Label(self, text="APIキー")
        # self.label_input_dir.grid(row=row_index, column=0)
        # self.entry_input_dir = tk.Entry(self, width=UI_input_dir_WIDTH)
        # self.entry_input_dir.grid(row=row_index, column=1)
        # row_index += 1

        # self.label_output_dir = tk.Label(self, text="APIキー")
        # self.label_output_dir.grid(row=row_index, column=0)
        # self.entry_output_dir = tk.Entry(self, width=UI_input_dir_WIDTH)
        # self.entry_output_dir.grid(row=row_index, column=1)
        row_index += 1

        self.radioApi = tk.Radiobutton(self, text="POSTリクエスト", variable=self.radio_value, value="API", command=self.toggle_entries)
        self.radioApi.grid(row=row_index, column=0)
        row_index += 1

        self.radioJson = tk.Radiobutton(self, text="JSON出力", variable=self.radio_value, value="JSON", command=self.toggle_entries)
        self.radioJson.grid(row=row_index, column=1)
        row_index += 1

        self.label_api_key = tk.Label(self, text="APIキー")
        self.label_api_key.grid(row=row_index, column=0)
        self.entry_api_key = tk.Entry(self, width=UI_API_KEY_WIDTH)
        self.entry_api_key.grid(row=row_index, column=1)
        row_index += 1

        self.label_server = tk.Label(self, text="サーバー")
        self.label_server.grid(row=row_index, column=0)
        self.entry_server = tk.Entry(self, width=UI_SERVER_WIDTH)
        self.entry_server.grid(row=row_index, column=1)
        row_index += 1

        self.label_site = tk.Label(self, text="サイトID")
        self.label_site.grid(row=row_index, column=0)
        self.entry_site = tk.Entry(self, width=UI_SITE_ID_WIDTH)
        self.entry_site.grid(row=row_index, column=1)
        row_index += 1

        self.button = tk.Button(self, text="実行", command=self.execute)
        self.button.grid(row=row_index, column=0, columnspan=2)
        row_index += 1

        self.log_box = tk.Text(self, width=UI_LOG_WIDTH)
        self.log_box.grid(row=row_index, column=0, columnspan=2)

        self.configure_text_tags()

    def toggle_entries(self):
        if self.radio_value.get() == "API":
            self.entry_api_key.config(state=tk.NORMAL)
            self.entry_server.config(state=tk.NORMAL)
            self.entry_site.config(state=tk.NORMAL)
        else:
            self.entry_api_key.config(state=tk.DISABLED)
            self.entry_server.config(state=tk.DISABLED)
            self.entry_site.config(state=tk.DISABLED)

    def execute(self):
        # コールバック関数を呼び出す
        if self.execute_callback:
            self.execute_callback(self)

    def initialize_default_values(self):
        self.toggle_entries()
        # デフォルト値はconfigモジュールに定義
        self.entry_api_key.insert(0, config.DEFAULT_API_KEY)
        self.entry_server.insert(0, config.DEFAULT_SERVER)
        self.entry_site.insert(0, config.DEFAULT_SITE_ID)

    def configure_text_tags(self):
        self.log_box.tag_configure("error", foreground="red")
        self.log_box.tag_configure("warning", foreground="orange")

    def log_output(self, message, msg_type="info"):
        if msg_type == "error":
            self.log_box.insert(tk.END, message + "\n", "error")
            util.print_color(message, "red")
        elif msg_type == "warning":
            self.log_box.insert(tk.END, message + "\n", "warning")
            util.print_color(message, "yellow")
        else:
            self.log_box.insert(tk.END, message + "\n")
            print(message)

if __name__ == "__main__":
    app = Gui("test",execute_callback="")
    app.mainloop()
