"""FileTidy: preview-first folder organizer with safe undo."""
from __future__ import annotations
import json
import shutil
from pathlib import Path
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

VERSION = "1.0.0"
GROUPS = {
 "Images":{".jpg",".jpeg",".png",".webp",".gif",".bmp"},
 "Video":{".mp4",".mkv",".mov",".avi",".webm"},
 "Audio":{".mp3",".flac",".wav",".m4a",".aac",".ogg"},
 "Documents":{".pdf",".txt",".docx",".xlsx",".pptx",".csv"},
 "Archives":{".zip",".7z",".rar",".gz"},
 "Apps":{".exe",".msi",".apk"}
}
UNDO_NAME=".filetidy_undo.json"

def category(name):
    return next((k for k,v in GROUPS.items() if Path(name).suffix.lower() in v),"Other")

def make_plan(folder):
    folder=Path(folder).resolve(strict=True)
    if not folder.is_dir():raise NotADirectoryError(folder)
    plan=[]
    reserved=set()
    for item in sorted(folder.iterdir()):
        if not item.is_file() or item.is_symlink() or item.name==UNDO_NAME:continue
        dest=folder/category(item.name)/item.name
        n=1
        while dest.exists() or dest in reserved:
            dest=folder/category(item.name)/f"{item.stem} ({n}){item.suffix}"
            n+=1
        plan.append((item,dest))
        reserved.add(dest)
    return plan

def organize(folder,plan):
    folder=Path(folder).resolve()
    log=folder/UNDO_NAME
    if log.exists():raise RuntimeError("Please undo the previous organization first.")
    moves=[]
    try:
        for src,dst in plan:
            if src.parent!=folder or dst.parent.parent!=folder or src.is_symlink() or not src.is_file() or dst.exists():
                raise RuntimeError(f"Unsafe or changed file: {src}")
            dst.parent.mkdir(exist_ok=True)
            shutil.move(str(src),str(dst))
            moves.append({"src":src.name,"dst":str(dst.relative_to(folder))})
        if moves:log.write_text(json.dumps(moves,ensure_ascii=False),encoding="utf-8")
    except Exception:
        for entry in reversed(moves):
            moved=folder/entry["dst"]
            original=folder/entry["src"]
            if moved.is_file() and not original.exists():shutil.move(str(moved),str(original))
        raise
    return len(moves)

def undo(folder):
    folder=Path(folder).resolve(strict=True)
    log=folder/UNDO_NAME
    moves=json.loads(log.read_text(encoding="utf-8"))
    count=0
    for entry in reversed(moves):
        moved=(folder/entry["dst"]).resolve()
        original=folder/entry["src"]
        if not moved.is_relative_to(folder) or not moved.is_file() or original.exists():
            raise RuntimeError(f"Cannot undo safely: {entry['src']}")
        shutil.move(str(moved),str(original))
        count+=1
    log.unlink()
    for name in set(GROUPS)|{"Other"}:
        p=folder/name
        if p.is_dir() and not any(p.iterdir()):p.rmdir()
    return count

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("FileTidy "+VERSION)
        self.geometry("740x500")
        self.folder=tk.StringVar(value=str(Path.home()/"Downloads"))
        self.status=tk.StringVar(value="Choose folder, then Preview before organizing.")
        self.plan=[]
        line=ttk.Frame(self,padding=12);line.pack(fill="x")
        ttk.Entry(line,textvariable=self.folder).pack(side="left",fill="x",expand=True)
        ttk.Button(line,text="Browse",command=self.browse).pack(side="left",padx=5)
        controls=ttk.Frame(self,padding=12);controls.pack(fill="x")
        for label,method in [("Preview",self.preview),("Organize",self.apply),("Undo",self.restore)]:
            ttk.Button(controls,text=label,command=method).pack(side="left",padx=5)
        self.tree=ttk.Treeview(self,columns=("from","to"),show="headings")
        self.tree.heading("from",text="Filename");self.tree.heading("to",text="Target folder")
        self.tree.column("from",width=250);self.tree.column("to",width=430)
        self.tree.pack(fill="both",expand=True,padx=12)
        ttk.Label(self,textvariable=self.status,padding=12).pack(anchor="w")
    def browse(self):
        path=filedialog.askdirectory()
        if path:self.folder.set(path);self.plan=[]
    def preview(self):
        try:
            self.plan=make_plan(self.folder.get())
            self.tree.delete(*self.tree.get_children())
            for src,dst in self.plan:self.tree.insert("","end",values=(src.name,str(dst)))
            self.status.set(f"Preview: {len(self.plan)} file(s). No changes yet.")
        except Exception as exc:messagebox.showerror("FileTidy",str(exc))
    def apply(self):
        self.preview()
        if self.plan and messagebox.askyesno("FileTidy",f"Move {len(self.plan)} files?"):
            try:self.status.set(f"Moved {organize(self.folder.get(),self.plan)} files. Undo available.");self.plan=[]
            except Exception as exc:messagebox.showerror("FileTidy",str(exc))
    def restore(self):
        try:self.status.set(f"Restored {undo(self.folder.get())} files.");self.tree.delete(*self.tree.get_children())
        except Exception as exc:messagebox.showerror("FileTidy",str(exc))
if __name__=="__main__":App().mainloop()
