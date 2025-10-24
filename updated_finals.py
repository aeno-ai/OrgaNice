import os
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")
import tkinter as tk
import shutil
from tkinter import filedialog, messagebox
import pygame
import sys

# vfx and music
# vfx and music

# Get the correct path for bundled files or use the normal path for development
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores the path there
        base_path = sys._MEIPASS
    except Exception:
        # If running as a normal script, use the current directory
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

pygame.mixer.init()

# Use resource_path to get correct paths for sound files
undo_confirmation = pygame.mixer.Sound(resource_path("undo_confirmation.mp3"))  # undo confirmation
success_sound = pygame.mixer.Sound(resource_path("success.mp3"))  # successfull sound
organize_all_sound = pygame.mixer.Sound(resource_path("organizingfiles_sound.mp3"))  # confirmation of organize all
click_sound = pygame.mixer.Sound(resource_path("clicksound.mp3"))  # click sound
welcome_message = pygame.mixer.Sound(resource_path("welcome.mp3"))  # welcome message
continue_sound = pygame.mixer.Sound(resource_path("continue.mp3"))  # continue sound
guide_sound = pygame.mixer.Sound(resource_path("guide.mp3"))  # guide sound
valid_format = pygame.mixer.Sound(resource_path("valid_format.mp3"))  # enter valid format sound
pygame.mixer.music.load(resource_path("music.mp3"))  # bg music
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# initialize music, sound, and dark mode

sounds_on = True
music_on = True

# themes ng color
is_dark = False

BG_LIGHT = "#358597"  # light mode bg
FG_LIGHT = "#FFFFFF"  # light mode text
BUTTON_BG_LIGHT = "#4CAF50"

BG_DARK = "#2E2E2E"  # dark mode bg
FG_DARK = "#D3D3D3"  # dark mode bg
BUTTON_BG_DARK = "#555555"

# fonts


TITLE_FONT = ("Helvetica", 20, "bold")
BUTTON_FONT = ("Helvetica", 14)
LABEL_FONT = ("Helvetica", 16)

formats = {
    # text and docs
    "txt": "Text Files",
    "pdf": "PDFs",
    "doc": "Word Files",
    "docx": "Word Files",
    "odt": "OpenDocument Text",
    "rtf": "Rich Text Format",
    "xls": "Excel Files",
    "xlsx": "Excel Files",
    "ppt": "PowerPoint Presentations",
    "pptx": "PowerPoint Presentations",
    "csv": "Comma-Separated Values",
    "xml": "XML Files",
    "md": "Markdown Files",  # pictures
    "jpg": "Pictures JPGs",
    "jpeg": "Pictures JPEGs",
    "png": "Pictures PNGs",
    "gif": "GIF Images",
    "bmp": "Bitmap Images",
    "tif": "TIFF Images",
    "tiff": "TIFF Images",
    "svg": "Vector Images",
    "ico": "Icons",
    "webp": "Web Picture",
    "jfif": "JFIF Files",

    # vids
    "mov": "Videos",
    "mp4": "Videos",
    "avi": "Videos",
    "mkv": "Videos",
    "flv": "Flash Videos",
    "wmv": "Windows Media Videos",
    "webm": "Web Videos",

    # audio
    "mp3": "Music",
    "wav": "WAV Audio",
    "flac": "Lossless Audio",
    "aac": "AAC Audio",
    "ogg": "OGG Audio",
    "m4a": "M4A Audio",

    # compressed
    "zip": "Compressed Files",
    "rar": "Compressed Files",
    "7z": "Compressed Files",
    "tar": "Tar Archives",
    "gz": "Gzip Files",

    # coding files
    "py": "Python Scripts",
    "java": "Java Source Code",
    "cpp": "C++ Source Code",
    "c": "C Source Code",
    "html": "HTML Files",
    "css": "CSS Files",
    "js": "JavaScript Files",
    "php": "PHP Files",
    "json": "JSON Files",
    "yml": "YAML Files",
    "yaml": "YAML Files",
    "rb": "Ruby Files",
    "go": "Go Source Code",
    "sql": "SQL Files",

    # executables
    "exe": "Executable Files",
    "msi": "Windows Installers",
    "sh": "Shell Scripts",
    "bat": "Batch Files",
    "apk": "Android Packages",
    "dmg": "MacOS Disk Images",
}

moved_files = []
# ayoko naaaaaaaaaaaaaaaaaaaaaaaaa


def toggle_sound():
    global sounds_on
    sounds_on = not sounds_on
    if sounds_on:
        click_sound.play()
    sound_vfx.config(text="🔊" if sounds_on else "🔇")


def toggle_music():
    if sounds_on:
        click_sound.play()
    global music_on
    music_on = not music_on
    if music_on:
        pygame.mixer.music.set_volume(0.5)
    else:
        pygame.mixer.music.set_volume(0)
    sound_music.config(text="🎵" if music_on else "🚫🎵")


def toggle_dark_mode():
    if sounds_on:
        click_sound.play()
    global is_dark
    is_dark = not is_dark
    if is_dark:
        window.config(bg=BG_DARK)
        title_label.config(bg=BG_DARK, fg=FG_DARK)
        organize_button.config(bg=BUTTON_BG_DARK, fg=FG_DARK)
        undo_button.config(bg=BUTTON_BG_DARK, fg=FG_DARK)
        dark_mode_button.config(bg=BUTTON_BG_DARK, fg=FG_DARK)
        sound_vfx.config(bg=BUTTON_BG_DARK, fg=FG_DARK)
        sound_music.config(bg=BUTTON_BG_DARK, fg=FG_DARK)
    else:
        window.config(bg=BG_LIGHT)
        title_label.config(bg=BG_LIGHT, fg=FG_LIGHT)
        organize_button.config(bg=BUTTON_BG_LIGHT, fg=FG_LIGHT)
        undo_button.config(bg=BUTTON_BG_LIGHT, fg=FG_LIGHT)
        dark_mode_button.config(bg=BUTTON_BG_LIGHT, fg=FG_LIGHT)
        sound_vfx.config(bg=BUTTON_BG_LIGHT, fg=FG_LIGHT)
        sound_music.config(bg=BUTTON_BG_LIGHT, fg=FG_LIGHT)


def preview_files(directory):
    if sounds_on:
        click_sound.play()
    preview_list = []
    for files in os.listdir(directory):
        preview_list.append(files)
    preview_list_text = "\n".join(preview_list)
    messagebox.showinfo("Preview Files", f"The following files/folders are in the selected folder\n\n{preview_list_text}")


def organize_all(directory):
    if sounds_on:
        click_sound.play()

    if not directory:
        messagebox.showinfo("No directory", "Invalid Directory.")
        return

    # list for previewing
    files_to_preview = []
    for file in os.listdir(directory):
        for ext in formats.keys():
            if file.lower().endswith(f".{ext}"):
                files_to_preview.append(file)
                break

    # preview
    if files_to_preview:
        if sounds_on:
            organize_all_sound.play()
        preview_text = "\n".join(files_to_preview)
        preview_message = f"The following files will be moved:\n\n{preview_text}"
        if not messagebox.askyesno("Preview Files", f"{preview_message}\n\nDo you want to continue?"):
            return
    else:
        messagebox.showinfo("No Files", "No files to organize.")
        return

    # moving ng files
    files_count = 0
    files_found = False

    for file in os.listdir(directory):
        for ext in formats.keys():
            if file.lower().endswith(f".{ext}"):
                files_found = True
                file_name = formats[ext]
                folder_path = os.path.join(directory, file_name)

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                file_path = os.path.join(directory, file)
                # error handler lang kung sakali
                try:
                    shutil.move(str(file_path), str(folder_path))
                    moved_files.append((file_path, folder_path))
                    files_count += 1
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to move file {file}: {e}")
                    continue
                break

    if not files_found:
        messagebox.showinfo("No files", "No files to organize.")
    else:
        if sounds_on:
            success_sound.play()
        messagebox.showinfo("Success", f"Selected files have been organized.\nFiles moved: {files_count}")


def undo_move():
    if sounds_on:
        click_sound.play()
        undo_confirmation.play()
    if not messagebox.askyesno("Confirmation", "Are you sure you want to undo previous changes?"):
        return

    if not moved_files:
        messagebox.showinfo("Undo", "No actions to undo.")
        return

    # removal ng empty folders
    folders_to_remove = []
    for original_path, target_folder in reversed(moved_files):
        file_name = os.path.basename(original_path)
        target_path = os.path.join(target_folder, file_name)

        if os.path.exists(target_path):
            shutil.move(str(target_path), str(original_path))

        # check if clear yung folder, alisin niya
        if os.path.isdir(target_folder) and not os.listdir(target_folder):
            folders_to_remove.append(target_folder)

    # remove empty folders
    for folder in folders_to_remove:
        os.rmdir(folder)  # Remove the empty folder
    if sounds_on:
        success_sound.play()
    messagebox.showinfo("Undo", f"Files have been moved back to their original locations and empty folders removed.\n"
                                f"Files moved: {len(moved_files)}\n"
                                f"Folders removed: {len(folders_to_remove)}")
    moved_files.clear()


# specific files code ito
def prepare_folder(input_format, directory):
    if sounds_on:
        click_sound.play()

    user_input = input_format.get().lower()

    # Check if the user input is a valid format
    if user_input not in formats:
        valid_format.play() if sounds_on else None
        messagebox.showerror("Error!", "Please enter a valid format")
        return

    folder_name = formats[user_input]
    folder = os.path.join(directory, folder_name)

    files_to_preview = []
    for filename in os.listdir(directory):
        if filename.endswith(user_input):
            files_to_preview.append(filename)

    # preview
    if files_to_preview:
        preview_text = "\n".join(files_to_preview)
        preview_message = f"The following files will be moved:\n\n{preview_text}"
        if sounds_on:
            continue_sound.play()
        preview_confirmation = messagebox.askyesno("Preview Files", f"{preview_message}\n\nDo you want to continue?")
        if not preview_confirmation:
            return
    else:
        messagebox.showinfo("No Files", "No files of the specified type found.")
        return

    if not os.path.exists(folder):
        os.makedirs(folder)

    files_moved = 0
    for filename in files_to_preview:
        path = os.path.join(directory, filename)
        shutil.move(str(path), str(folder))
        moved_files.append((path, folder))
        files_moved += 1

    # Show success message
    if files_moved == 0:
        messagebox.showinfo("No moved files", "No files of the specified type were moved.")
    else:
        if sounds_on:
            success_sound.play()
        messagebox.showinfo("Success", f"Files organized into: {folder}\nFiles moved: {files_moved}")


def organize():
    if sounds_on:
        click_sound.play()
    directory = filedialog.askdirectory(title="Select folder to Organize")
    if not directory:
        return
    window.withdraw()
    # WINDOW 2
    if sounds_on:
        guide_sound.play()
    window2 = tk.Toplevel(window)
    window2.title("Orga-Nice")
    window2.geometry("500x500")
    window2.config(bg=BG_LIGHT if not is_dark else BG_DARK)

    # enter format to organize label
    ask_format = tk.Label(window2,
                          font=LABEL_FONT,
                          text="Enter format to organize: ",
                          bg=BG_LIGHT if not is_dark else BG_DARK,
                          fg=FG_LIGHT if not is_dark else FG_DARK)
    ask_format.pack(pady=(20, 10))

    guide = tk.Label(window2,
                     font=("Helvetica", 12),
                     text="Organize specific file types\n\nExamples: 'txt' 'pdf' 'docx'",
                     bg=BG_LIGHT if not is_dark else BG_DARK,
                     fg=FG_LIGHT if not is_dark else FG_DARK)
    guide.pack(pady=(0, 20))

    # typing area
    input_format = tk.Entry(window2, width=24)
    input_format.pack(pady=(0, 20))

    submit = tk.Button(window2,
                       font=BUTTON_FONT,
                       text="Submit",
                       bg=BUTTON_BG_LIGHT if not is_dark else BUTTON_BG_DARK,
                       fg=FG_LIGHT if not is_dark else FG_DARK,
                       command=lambda: prepare_folder(input_format, directory))
    submit.pack(pady=(0, 30))

    ask_format_all = tk.Label(window2,
                              font=LABEL_FONT,
                              text="Organize All",
                              bg=BG_LIGHT if not is_dark else BG_DARK,
                              fg=FG_LIGHT if not is_dark else FG_DARK)
    ask_format_all.pack(pady=(10, 5))

    # guide label
    guide_all = tk.Label(window2,
                         font=("Helvetica", 12),
                         text="This will organize all the files in the selected folder",
                         bg=BG_LIGHT if not is_dark else BG_DARK,
                         fg=FG_LIGHT if not is_dark else FG_DARK)
    guide_all.pack(pady=(0, 20))

    # organize all button
    organize_all_files = tk.Button(window2,
                                   font=BUTTON_FONT,
                                   text="Organize all files",
                                   bg=BUTTON_BG_LIGHT if not is_dark else BUTTON_BG_DARK,
                                   fg=FG_LIGHT if not is_dark else FG_DARK,
                                   command=lambda: [organize_all(directory), click_sound.play() if sounds_on else None])
    organize_all_files.pack(pady=(0, 20))

    # preview files button
    preview_button = tk.Button(window2,
                               text="View Files/Folders",
                               bg=BUTTON_BG_LIGHT if not is_dark else BUTTON_BG_DARK,
                               fg=FG_LIGHT if not is_dark else FG_DARK,
                               command=lambda: preview_files(directory))
    preview_button.pack(pady=(0, 20))

    # back button
    back_button = tk.Button(window2, font=BUTTON_FONT, text="Back",
                            bg=BUTTON_BG_LIGHT if not is_dark else BUTTON_BG_DARK,
                            fg=FG_LIGHT if not is_dark else FG_DARK, width=8,
                            command=lambda: [window.deiconify(),
                                             window2.withdraw(),
                                             click_sound.play() if sounds_on else None])
    back_button.pack(pady=10, anchor="w", padx=20)


# main window
if sounds_on:
    click_sound.play()
welcome_message.play()
window = tk.Tk()
window.title("Orga-Nice")
window.geometry("500x400")
window.config(bg=BG_LIGHT)

# Welcome to Orga-Nice
title_label = tk.Label(window,
                       font=TITLE_FONT,
                       text="Welcome to Orga-Nice!",
                       bg=BG_LIGHT,
                       fg=FG_LIGHT)
title_label.pack(pady=20)

# Buttons
organize_button = tk.Button(window,
                            text="Choose a Folder",
                            bg=BUTTON_BG_LIGHT,
                            fg=FG_LIGHT,
                            font=BUTTON_FONT,
                            command=organize)
organize_button.pack(pady=20)

dark_mode_button = tk.Button(window,
                             text="Toggle Dark Mode",
                             bg=BUTTON_BG_LIGHT,
                             fg=FG_LIGHT,
                             font=BUTTON_FONT,
                             command=toggle_dark_mode)
dark_mode_button.pack(pady=10)

undo_button = tk.Button(window, text="Undo Last Move",
                        bg=BUTTON_BG_LIGHT,
                        fg=FG_LIGHT,
                        font=BUTTON_FONT,
                        command=undo_move)
undo_button.pack(pady=10)
# vfx
sound_vfx = tk.Button(window,
                      text="🔊",
                      bg=BUTTON_BG_LIGHT,
                      fg=FG_LIGHT,
                      width=7,
                      font=BUTTON_FONT,
                      command=toggle_sound)
sound_vfx.pack(anchor="w", padx=20, pady=10)
# music
sound_music = tk.Button(text="🎵",
                        bg=BUTTON_BG_LIGHT,
                        fg=FG_LIGHT,
                        width=7,
                        font=BUTTON_FONT,
                        command=toggle_music)
sound_music.pack(anchor="w", padx=20, pady=10)


window.mainloop()
