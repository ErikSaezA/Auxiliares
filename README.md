<img src="https://github.com/ErikSaezA/Auxiliares/blob/a734ed37e3f254b44b9a7b0d7f999a8cec547ac4/Logo%20DIE%20FCFM.png" width="500">


# Recursos de Docencia — Ingeniería Eléctrica · Universidad de Chile

Por si buscas contactarme,

- [![LinkedIn](https://img.shields.io/badge/LinkedIn-Erik%20Sáez-lightgray?logo=linkedin&logoColor=white&color=lightgray)](https://www.linkedin.com/in/erik-s%C3%A1ez-aravena-447352210/)
- [![](https://img.shields.io/badge/Correo-erik.saez%40ug.uchile.cl-lightgray?logo=gmail&logoColor=white&color=lightgray)](mailto:erik.saez@ug.uchile.cl)
- [![](https://img.shields.io/badge/Correo-esaez.das%40uchile.cl-lightgray?logo=gmail&logoColor=white&color=lightgray)](mailto:esaez.das@uchile.cl)

Erik Sáez
Estudiante de Magíster en Ingeniería Civil Eléctrica en la Universidad de Chile

Desde mis años escolares, la docencia ha sido una de mis mayores motivaciones. La búsqueda y comprensión profunda del porqué de las cosas ha sido el motor que me ha impulsado a mantenerme resiliente y comprometido con mi desarrollo, aun cuando el camino ha sido desafiante.

A lo largo de mi trayectoria universitaria, he tenido el privilegio de contribuir activamente en el ámbito de la docencia universitaria como profesor auxiliar. Además, he participado en la gestión estudiantil, desempeñándome inicialmente en el equipo de Docencia del Centro de Estudiantes y posteriormente como Vicepresidente del CEIE (Centro de Estudiantes de Ingeniería Eléctrica).

Con el objetivo de apoyar a quienes continúan fortaleciendo la docencia en nuestro departamento, pongo a disposición diversos materiales y recursos en los que participé junto a los equipos docentes, tales como auxiliares, presentaciones, aplicaciones y métodos de estudio que me han sido de gran utilidad a lo largo de mi carrera. Espero que estos recursos también sean de beneficio para otros.
## Cursos donde participé en el equipo docente

### Profesor Auxiliar
- **FI1100 — Introducción a la Física Moderna** *(Primavera 2025)*
- **EL3202-1 — Circuitos Eléctricos Analógicos** *(Primavera 2025)*
- **EL3204 — Análisis de Sistemas Dinámicos y Estimación** *(Primavera 2025)*
- **EL3204 — Análisis de Señales** *(Primavera 2025)*
- **EL3101 — Análisis y Diseño de Circuitos Eléctricos** *(Otoño 2025)*
- **EL3103 — Electromagnetismo Aplicado** *(Otoño 2025)*
- **EL3204 — Análisis de Sistemas Dinámicos y Estimación** *(Primavera 2024)*
- **EL4113 — Fundamentos de Control de Sistemas** *(Primavera 2024)*
- **EL4111 — Conversión de la Energía y Sistemas Eléctricos** *(Primavera 2024)*
- **EL3103 — Electromagnetismo Aplicado** *(Otoño 2024)*
- **EL3101 — Análisis y Diseño de Circuitos Eléctricos** *(Otoño 2024)*
- **FI1000 — Introducción a la Física Clásica** *(Otoño 2024)*
- **EL3103 — Electromagnetismo Aplicado** *(Primavera 2023)*
- **EL3103 — Electromagnetismo Aplicado** *(Otoño 2023)*
- **FI1000 — Introducción a la Física Clásica** *(Otoño 2022)*

### Ayudante
- **EL4112 — Principios de Comunicaciones** *(Primavera 2025)*
- **EL3101 — Análisis y Diseño de Circuitos Eléctricos** *(Primavera 2025)*
- **EL3105 — Seminario de Ingeniería Eléctrica e Innovación Tecnológica** *(Primavera 2025)*
- **EL3105 — Seminario de Ingeniería Eléctrica e Innovación Tecnológica** *(Otoño 2025)*
- **FI2002 — Electromagnetismo** *(Verano 2023)*


# VS Code + LaTeX + Copilot + GitHub — Guía rápida
A continuación doy una guía detallada de cómo trabajo al editar mis documentos.

[![Overleaf](https://img.shields.io/badge/Overleaf-Editor%20online-44B78B?logo=overleaf&logoColor=white)](https://www.overleaf.com/)

**Overleaf** es una gran herramienta, pero por sus **límites de plan gratuito** (p. ej., *compile timeouts* y restricciones de colaboración) y la necesidad de estar **siempre en línea**, opté por trabajar **en local** con **VS Code + LaTeX + Copilot + GitHub**. Así obtienes sugerencias con IA, compilación local (sin límites de tiempo) e integración directa con control de versiones.

## Videos de referencia
Dejo unos videos de referencia para realizar las instalaciones. Más abajo incluyo una guía paso a paso.
- [![YouTube](https://img.shields.io/badge/Ver%20en-YouTube-red?logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=9w7eb56bF7Y) **Instalación de LaTeX en VS Code**
- [![YouTube](https://img.shields.io/badge/Ver%20en-YouTube-red?logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=TuOQBfhp-r0) **GitHub Desktop (GUI oficial) paso a paso**

## Instalación (Windows / macOS / Linux)

#### 1) Instala VS Code
[![Descargar VS Code](https://img.shields.io/badge/Download-VS%20Code-007ACC?logo=visualstudiocode&logoColor=white)](https://code.visualstudio.com/download)  
Primero descarga el instalador para tu sistema (Windows/macOS/Linux), ejecútalo y abre VS Code. Es el editor donde escribirás `.tex`, con Git integrado y extensiones.

#### 2) Instala una distribución de LaTeX (elige una según tu sistema)
- **Windows (recomendado por simplicidad): MiKTeX**  
  [![MiKTeX](https://img.shields.io/badge/Download-MiKTeX-2D2D2D?logo=windows&logoColor=white)](https://miktex.org/download)  
  Instala el **Basic MiKTeX** y deja activada la instalación de paquetes “on-the-fly” (MiKTeX los descarga cuando hacen falta). **Tip:** actualiza apenas lo instales.
- **macOS: MacTeX**  
  [![MacTeX](https://img.shields.io/badge/Download-MacTeX-000000?logo=apple&logoColor=white)](https://www.tug.org/mactex/mactex-download.html)  
  Descarga **MacTeX-2025** (≈6 GB) o, si buscas algo liviano, **BasicTeX**. Instala con el `.pkg`.
- **Linux: TeX Live**  
  [![TeX Live](https://img.shields.io/badge/Download-TeX%20Live-555555?logo=linux&logoColor=white)](https://www.tug.org/texlive/)  
  Instala TeX Live desde tu gestor de paquetes o el instalador oficial.

#### 3) (Solo Windows + MiKTeX) Instala Perl
[![Strawberry Perl](https://img.shields.io/badge/Install-Strawberry%20Perl-DA1F26?logo=perl&logoColor=white)](https://strawberryperl.com/)  
En Windows instala **Strawberry Perl** y verifica con `perl -v`. Esto habilita **`latexmk`** en Windows.

#### 4) Instala la extensión de LaTeX en VS Code
[![LaTeX Workshop](https://img.shields.io/badge/VS%20Code-LaTeX%20Workshop-1f425f?logo=visualstudiocode&logoColor=white)](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop)  
En VS Code abre la **Paleta de comandos** (`Ctrl/Cmd+P`) → escribe `ext install latex-workshop`.  
**Cómo compilar:** abre tu `main.tex` → “**LaTeX Workshop: Build LaTeX project**” (o `Ctrl+Alt+B`) → se abre el visor PDF integrado. Por defecto se usa **`latexmk`** (requiere Perl).

#### 5) Activa GitHub Copilot en VS Code (opcional pero recomendado)
[![Copilot Overview](https://img.shields.io/badge/Docs-Copilot%20Overview-181717?logo=github&logoColor=white)](https://code.visualstudio.com/docs/copilot/overview)
[![Copilot Get Started](https://img.shields.io/badge/Docs-Get%20Started-181717?logo=github&logoColor=white)](https://code.visualstudio.com/docs/copilot/getting-started)  
Inicia sesión con tu cuenta, habilita Copilot y prueba las sugerencias en el editor. *(Si tienes correo institucional, suele incluir plan completo gratuito.)*

#### 6) (Opcional) Vincular tu proyecto con GitHub Desktop — **resumen con acciones**
[![GitHub Desktop](https://img.shields.io/badge/Download-GitHub%20Desktop-181717?logo=github&logoColor=white)](https://desktop.github.com/download/)  
**¿Para qué?** Para gestionar Git/GitHub con interfaz gráfica: *clone/commit/push/pull/branches* sin usar terminal.

**Pasos rápidos**
1. **Nuevo repo**: *File → New repository* → carpeta de tu proyecto → **Create** → **Publish repository** (elige Público/Privado).  
   **o** **Repo existente**: *File → Add local repository* → selecciona tu carpeta → **Add** → **Publish repository**.
2. **Flujo básico**: edita archivos → **Commit** (escribe un mensaje) → **Push origin**; para traer cambios remotos: **Fetch/Pull**.  
3. **Ramas**: *Branch → New branch* (ej. `feature/figuras`) → **Commit/Push** → crea el **Pull Request** (se abre en GitHub.com).  
4. **.gitignore (LaTeX)**: añade un `.gitignore` con temporales (`*.aux`, `*.log`, `*.fdb_latexmk`, etc.) para mantener el repo limpio.  
5. **(Opcional) Archivos grandes**: si vas a subir PDFs/medios pesados, configura **Git LFS** (`git lfs install`, `git lfs track "*.pdf"`); GitHub **bloquea >100 MiB** por archivo (25 MiB vía navegador).


## Métodos de estudio 
> 📋 A lo largo de mi carrera probé varios métodos de estudio y aplicaciones. Estas fueron las que más me sirvieron y **cómo** las uso en la práctica.

- [![Pomofocus](https://img.shields.io/badge/Pomofocus-Pomodoro%20Timer-ff4d4d)](https://pomofocus.io/)  
  **Pomofocus** — Temporizador Pomodoro simple y configurable.  
  **Mi configuración:** **55 min estudio + 5 min descanso**.  
  Permite añadir **notas**; ahí anoto las actividades del bloque y marco el avance.

- [![Forest](https://img.shields.io/badge/Forest-Stay%20Focused-228B22)](https://www.forestapp.cc/)  
  **Forest** — Muy útil para **dejar el celular** mientras estudias: “planta” un árbol y te enfocas en la tarea.  
  Si sales de la app, tu árbol se marchita. Ideal para acompañar Pomodoro.

- [![Notion](https://img.shields.io/badge/Notion-Workspace-000000?logo=notion&logoColor=white)](https://www.notion.so/)  
  **Notion** — De las herramientas más potentes hoy: bases de datos, vistas Kanban/calendario, checklists y páginas anidadas para **organizar cursos, proyectos y lecturas**.  
  Probé muchas plantillas sin convencerme… hasta que encontré esta:  
  [![YouTube](https://img.shields.io/badge/Ver%20plantilla-YouTube-red?logo=youtube&logoColor=white)](https://www.youtube.com/watch?v=eHOv8D1fsAg&t=1520s)  

- [![Zotero](https://img.shields.io/badge/Zotero-Reference%20Manager-B32024?logo=zotero&logoColor=white)](https://www.zotero.org/)  
  **Zotero** — Gestor de referencias que me sirvió **mucho para la tesis**.  
  Guarda bibliografía con un clic, etiqueta y organiza; exporta a `.bib` para LaTeX y genera citas/bibliografías en segundos.
