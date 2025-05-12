Aquí tienes un resumen de los comandos más útiles de **Git**:

---

### **Configuración Inicial**
| Comando | Descripción |
|---------|-------------|
| `git config --global user.name "Nombre"` | Establece el nombre del usuario |
| `git config --global user.email "email@ejemplo.com"` | Establece el correo del usuario |
| `git config --list` | Muestra la configuración actual |

---

### **Iniciar un Repositorio**
| Comando | Descripción |
|---------|-------------|
| `git init` | Inicia un repositorio Git en la carpeta actual |
| `git clone <url_repositorio>` | Clona un repositorio remoto |

---

### **Trabajar con Cambios**
| Comando | Descripción |
|---------|-------------|
| `git status` | Muestra el estado de los archivos (modificados, staged, etc.) |
| `git add <archivo>` | Añade un archivo al **área de staging** |
| `git add .` | Añade **todos** los cambios al staging |
| `git commit -m "mensaje"` | Guarda los cambios en el repositorio con un mensaje |
| `git commit --amend` | Modifica el último commit (mensaje o archivos) |

---

### **Historial y Diferencias**
| Comando | Descripción |
|---------|-------------|
| `git log` | Muestra el historial de commits |
| `git log --oneline` | Muestra commits en una línea |
| `git diff` | Muestra cambios no staged |
| `git diff --staged` | Muestra cambios staged pero no commitados |

---

### **Ramas (Branches)**
| Comando | Descripción |
|---------|-------------|
| `git branch` | Lista todas las ramas |
| `git branch <nombre_rama>` | Crea una nueva rama |
| `git checkout <nombre_rama>` | Cambia a otra rama |
| `git switch <nombre_rama>` | Alternativa moderna a `checkout` |
| `git merge <nombre_rama>` | Fusiona una rama con la actual |
| `git branch -d <nombre_rama>` | Elimina una rama (seguro) |
| `git branch -D <nombre_rama>` | Elimina una rama (forzado) |

---

### **Trabajar con Remotos**
| Comando | Descripción |
|---------|-------------|
| `git remote add origin <url>` | Añade un repositorio remoto |
| `git push -u origin <rama>` | Sube cambios al remoto (primera vez) |
| `git push` | Sube cambios al remoto |
| `git pull` | Descarga cambios del remoto y los fusiona |
| `git fetch` | Descarga cambios del remoto sin fusionar |

---

### **Deshacer Cambios**
| Comando | Descripción |
|---------|-------------|
| `git restore <archivo>` | Descarta cambios en un archivo no staged |
| `git reset <archivo>` | Saca un archivo del staging (pero mantiene cambios) |
| `git reset --hard` | **Elimina todos los cambios** (¡cuidado!) |
| `git revert <commit>` | Crea un commit que deshace otro commit |

---

### **Etiquetas (Tags)**
| Comando | Descripción |
|---------|-------------|
| `git tag <nombre_tag>` | Crea un tag en el commit actual |
| `git tag -a <nombre_tag> -m "mensaje"` | Crea un tag anotado |
| `git push --tags` | Sube tags al remoto |

---

### **Otros Útiles**
| Comando | Descripción |
|---------|-------------|
| `git stash` | Guarda cambios temporales sin commitear |
| `git stash pop` | Recupera cambios guardados con `stash` |
| `git cherry-pick <commit>` | Aplica un commit específico a la rama actual |

---

¿Necesitas más detalles sobre algún comando en particular? 😊