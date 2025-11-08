import tkinter as tk
from tkinter import messagebox, ttk
from User_controller import ver_usuarios, agregar_usuarios, actualizar_usuarios, eliminar_usuarios

class UserApp:
    def __init__(self, username):
        self.username = username
        self.root = tk.Tk()
        self.root.title(f"Bienvenido {username}")
        self.root.geometry("600x400")
        self.root.resizable(True, True)        
        
        self.crear_elementos()
        self.ver_usuarios()
        self.root.mainloop()

    def crear_elementos(self):
        tk.Label(self.root, text=f"Hola, {self.username}", font=("Arial", 22, "bold")).pack(pady=10)
        tk.Button(self.root, text="Cerrar sesión", width=15, command=self.cerrar_sesion).pack(pady=20, padx=10)

        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Agregar usuarios", width=20, command=self.agregar_usuarios).pack(pady=5)
        tk.Button(frame_botones, text="Actualizar usuarios", width=20, command=self.actualizar_usuarios).pack(pady=5)
        tk.Button(frame_botones, text="Eliminar usuarios", width=20, command=self.eliminar_usuarios).pack(pady=5)

        tk.Label(self.root, text="Lista de usuarios", font=("Arial", 16, "bold")).pack(pady=10)

        # CORRECCIÓN: Usar "id" en minúsculas
        self.tree = ttk.Treeview(self.root, columns=("id", "Usuario"), show="headings", height=10)
        self.tree.heading("id", text="ID")
        self.tree.heading("Usuario", text="Usuario")
        self.tree.column("id", width=100, anchor="center")
        self.tree.column("Usuario", width=250, anchor="center")
        self.tree.pack(padx=10, pady=10, fill="both", expand=True)

    def ver_usuarios(self):
        # Limpiar tabla
        for row in self.tree.get_children():
            self.tree.delete(row)
        
        # Obtener usuarios
        usuarios = ver_usuarios()
        print(f"DEBUG: Usuarios obtenidos: {usuarios}")  # Para ver qué datos llegan
        
        # Insertar en la tabla
        for usuario in usuarios:
            self.tree.insert("", tk.END, values=usuario)

    def agregar_usuarios(self):
        def guardar():
            u = entry_user.get().strip()
            p = entry_pass.get().strip()
            if not u or not p:
                messagebox.showwarning("Campos vacíos", "Ingrese usuario y contraseña.")
                return
            if agregar_usuarios(u, p):
                messagebox.showinfo("Éxito", f"Usuario {u} creado correctamente.")
                self.ver_usuarios()
                ventana.destroy()
            else:
                messagebox.showerror("Error", "No se pudo crear el usuario.")
        
        ventana = tk.Toplevel(self.root)
        ventana.title("Agregar Usuario")
        ventana.geometry("300x200")
        ventana.transient(self.root)
        ventana.grab_set()
        
        tk.Label(ventana, text="Usuario").pack(pady=5)
        entry_user = tk.Entry(ventana)
        entry_user.pack(pady=5)
        tk.Label(ventana, text="Contraseña").pack(pady=5)
        entry_pass = tk.Entry(ventana, show="*")
        entry_pass.pack(pady=5)
        tk.Button(ventana, text="Crear usuario", command=guardar).pack(pady=10)

    def actualizar_usuarios(self):
        seleccionado = self.tree.focus()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un usuario de la lista.")
            return

        
        valores = self.tree.item(seleccionado, "values")
        id_usuario = valores[0]  
        nombre_actual = valores[1]  

        def guardar():
            nuevo_nombre = entry_user.get().strip()
            nueva_contra = entry_pass.get().strip()
            if not nuevo_nombre or not nueva_contra:
                messagebox.showwarning("Campos vacíos", "Ingrese usuario y contraseña.")
                return
            if actualizar_usuarios(id_usuario, nuevo_nombre, nueva_contra):
                messagebox.showinfo("Éxito", f"Usuario '{nuevo_nombre}' actualizado correctamente.")
                self.ver_usuarios()
                ventana.destroy()
            else:
                messagebox.showerror("Error", "No se pudo actualizar el usuario.")

        ventana = tk.Toplevel(self.root)
        ventana.title("Actualizar Usuario")
        ventana.geometry("300x200")
        ventana.transient(self.root)
        ventana.grab_set()
        
        tk.Label(ventana, text="Nuevo usuario").pack(pady=5)
        entry_user = tk.Entry(ventana)
        entry_user.insert(0, nombre_actual)
        entry_user.pack(pady=5)
        tk.Label(ventana, text="Nueva contraseña").pack(pady=5)
        entry_pass = tk.Entry(ventana, show="*")
        entry_pass.pack(pady=5)
        tk.Button(ventana, text="Guardar cambios", command=guardar).pack(pady=10)

    def eliminar_usuarios(self):
        seleccionado = self.tree.focus()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un usuario para eliminar.")
            return

        # CORRECCIÓN: Obtener los valores usando los nombres correctos de columnas
        valores = self.tree.item(seleccionado, "values")
        id_usuario = valores[0]  # Primera columna es "id"
        nombre_usuario = valores[1]  # Segunda columna es "Usuario"

        confirmar = messagebox.askyesno("Confirmar", f"¿Desea eliminar el usuario '{nombre_usuario}'?")
        if confirmar:
            if eliminar_usuarios(id_usuario):
                messagebox.showinfo("Eliminado", f"Usuario '{nombre_usuario}' eliminado correctamente.")
                self.ver_usuarios()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el usuario.")

    def cerrar_sesion(self):
        self.root.destroy()

if __name__ == "__main__":
    App = UserApp("admin")
