import configparser
import os
from shutil import copyfile
import tkinter as tk
from tkinter import filedialog

class Main(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.init_window(title="Fortnite Stretch Config",geo="640x240")

        self.config_path = os.path.expandvars("%LOCALAPPDATA%\FortniteGame\Saved\Config\WindowsClient\GameUserSettings.ini")
        self.game_path = "Fortnite.url"
        self.resolution = "1440x1440"

        self.cfg = configparser.ConfigParser()
        self.cfg.optionxform = str

        if not os.path.exists("Config.ini"):
            settingsfile = open("Config.ini", "w+")
            self.cfg.add_section("Filepaths")
            self.cfg.add_section("Settings")
            self.cfg.set("Filepaths","GameFile", self.game_path)
            self.cfg.set("Filepaths","ConfigFile",self.config_path)
            self.cfg.set("Settings","Resolution", self.resolution)
            self.cfg.write(settingsfile, space_around_delimiters=False)
            settingsfile.close()
        else:
            self.cfg.read("Config.ini")
            self.game_path = self.cfg["Filepaths"]["GameFile"]
            self.resolution = self.cfg["Settings"]["Resolution"]
            self.config_path = self.cfg["Filepaths"]["ConfigFile"]

        self.config_path_entry.insert(0, self.config_path)
        self.game_path_entry.insert(0, self.game_path)
        self.resolution_entry.insert(0, self.resolution)
        self.cfg.clear()

    # Initialize Window
    def init_window(self, title, geo):
        root.title(title)
        root.geometry(geo)
        root.protocol("WM_DELETE_WINDOW", self.quit)
        root.resizable(0,0)

        self.create_widgets(title)

    def create_widgets(self, title):
        # Create Title
        self.title = tk.Label(self,text=title, font=("Helvetica", 24))
        self.title.grid(column=1, row=1)

        tk.Label(root, text="Path to Fortnite Executable", font=("Helvetica", 16)).grid(row=1, column=0, sticky=tk.W, padx=10)

        self.game_path_entry = tk.Entry(root, width=35, font=("Helvetica", 16))
        self.game_path_entry.grid(row=2, column=0, sticky=tk.NW, padx=10)
        self.game_path_entry.bind("<Return>", self.set_game_path)

        self.browse_game = tk.Button(root, font=("Helvetica", 8), text="Browse",
                                     command=lambda:self.select_game_dir())

        self.browse_game.grid(row=2, column=1, sticky=tk.NW, padx=5)

        tk.Label(root, text="Path to Config File",font=("Helvetica",16)).grid(row=3,column=0,sticky=tk.W,padx=10)

        # Create Config Entry
        self.config_path_entry = tk.Entry(root,width=35,font=("Helvetica",16))
        self.config_path_entry.grid(row=4,column=0,sticky=tk.NW,padx=10)
        self.config_path_entry.bind("<Return>",self.set_config_path)

        # Create Browse Button
        self.browse_config = tk.Button(root, font=("Helvetica", 8), text="Browse",
                                       command=lambda:self.select_config_dir())
        self.browse_config.grid(row=4, column=1, sticky=tk.NW, padx=5)

        # Resolution Input
        tk.Label(root, text="Resolution", font=("Helvetica",16)).grid(row=5, column=0, padx=10, sticky=tk.NW)
        self.resolution_entry = tk.Entry(root, width=15, font=("Helvetica", 16))
        self.resolution_entry.grid(row=5,column=0,padx=125,sticky=tk.W)

        # Create launch and reset buttons
        self.launch_game_btn = tk.Button(root,font=("Helvetica",16),text="Apply & Launch",
                                         command=lambda: self.launch_game())
        self.launch_game_btn.grid(row=6, column=0,padx=25, pady=5, sticky=tk.NW)

        self.reset_settings_btn = tk.Button(root, font=("Helvetica", 16), text="Reset Game Settings",
                                            command=lambda:self.reset_settings())
        self.reset_settings_btn.grid(row=6, column=0,pady=5, sticky=tk.NE)

    def reset_settings(self):
        os.remove(self.config_path)
        os.rename(self.config_path + ".bak", self.config_path)

    def launch_game(self):
        if not os.path.exists(self.game_path) or not os.path.exists(self.config_path):
            return

        self.cfg.read("Config.ini")
        self.cfg["Settings"]["Resolution"] = self.resolution_entry.get()

        with open("Config.ini", "w") as configfile:
            self.cfg.write(configfile)
            configfile.close()
            self.cfg.clear()

        try:
            self.set_config_path(None)
            self.set_game_path(None)
            config = self.config_path
            if not os.path.exists(config + ".bak"):
                copyfile(config, config + ".bak")

            self.cfg.read(config)
            print(self.cfg.sections())

        except Exception as e:
            print(e)
            return

        try:
            resolution_x = self.resolution_entry.get().split("x")[0]
            resolution_y = self.resolution_entry.get().split("x")[1]

            self.cfg["/Script/FortniteGame.FortGameUserSettings"]["ResolutionSizeX"] = resolution_x
            self.cfg["/Script/FortniteGame.FortGameUserSettings"]["ResolutionSizeY"] = resolution_y
            self.cfg["/Script/FortniteGame.FortGameUserSettings"]["LastUserConfirmedResolutionSizeX"] = resolution_x
            self.cfg["/Script/FortniteGame.FortGameUserSettings"]["LastUserConfirmedResolutionSizeY"] = resolution_y
            self.cfg["/Script/FortniteGame.FortGameUserSettings"]["FullscreenMode"] = "0"
            self.cfg["/Script/FortniteGame.FortGameUserSettings"]["LastConfirmedFullscreenMode"] = "0"
            self.cfg["/Script/FortniteGame.FortGameUserSettings"]["PrefferedFullscreenMode"] = "0"

            with open(config, "w") as configfile:
                self.cfg.write(configfile, space_around_delimiters=False)
                configfile.close()
            os.system(self.game_path)
            self.cfg.clear()
        except Exception as e:
            print(e)

    def select_game_dir(self):
        file = tk.filedialog.askopenfilename(filetypes=[("Fortnite Executable","FortniteClient-Win64-Shipping.exe")])
        self.game_path_entry.delete(0, tk.END)
        self.game_path_entry.insert(0, file)
        self.set_game_path(None)

    def select_config_dir(self):
        directory = tk.filedialog.askopenfilename(filetypes=[("Fortnite Config","GameUserSettings.ini")])
        self.config_path_entry.delete(0,tk.END)
        self.config_path_entry.insert(0,directory)
        self.set_config_path(None)

    def set_config_path(self,event):
        self.cfg.clear()
        self.config_path = self.config_path_entry.get()
        self.cfg.read("Config.ini")
        self.cfg["Filepaths"]["ConfigFile"] = self.config_path
        with open("Config.ini", "w") as configfile:
            self.cfg.write(configfile,space_around_delimiters=False)
            configfile.close()
        self.cfg.clear()

    def set_game_path(self,event):
        self.cfg.clear()
        self.game_path = self.game_path_entry.get()
        self.cfg.read("Config.ini")
        self.cfg["Filepaths"]["GameFile"] = self.game_path
        with open("Config.ini", "w") as configfile:
            self.cfg.write(configfile,space_around_delimiters=False)
            configfile.close()
        self.cfg.clear()

root = tk.Tk()
app = Main(master=root)
app.mainloop()
root.destroy()
