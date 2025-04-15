import os

def create_project_structure():
    """Создает структуру папок и пустые файлы для веб-проекта."""

    project_root = os.getcwd()  # Получаем текущую рабочую директорию

    # Создаем корневые файлы
    open(os.path.join(project_root, ".babelrc"), 'a').close()
    open(os.path.join(project_root, ".eslintrc.js"), 'a').close()
    open(os.path.join(project_root, "gulpfile.js"), 'a').close()
    open(os.path.join(project_root, "package.json"), 'a').close()

    # Создаем папку src
    src_dir = os.path.join(project_root, "src")
    os.makedirs(src_dir, exist_ok=True)

    # Создаем подпапки в src/html
    html_dir = os.path.join(src_dir, "html")
    os.makedirs(os.path.join(html_dir, "blocks"), exist_ok=True)
    os.makedirs(os.path.join(html_dir, "pages"), exist_ok=True)

    # Создаем подпапки и файлы в src/scss
    scss_dir = os.path.join(src_dir, "scss")
    os.makedirs(scss_dir, exist_ok=True)
    open(os.path.join(scss_dir, "style.scss"), 'a').close()
    os.makedirs(os.path.join(scss_dir, "components"), exist_ok=True)
    os.makedirs(os.path.join(scss_dir, "layout"), exist_ok=True)
    os.makedirs(os.path.join(scss_dir, "utils"), exist_ok=True)
    os.makedirs(os.path.join(scss_dir, "vendors"), exist_ok=True)

    # Создаем подпапки и файлы в src/js
    js_dir = os.path.join(src_dir, "js")
    os.makedirs(js_dir, exist_ok=True)
    open(os.path.join(js_dir, "main.js"), 'a').close()
    os.makedirs(os.path.join(js_dir, "components"), exist_ok=True)
    os.makedirs(os.path.join(js_dir, "utils"), exist_ok=True)
    os.makedirs(os.path.join(js_dir, "vendors"), exist_ok=True)

    # Создаем подпапки в src/img
    img_dir = os.path.join(src_dir, "img")
    os.makedirs(os.path.join(img_dir, "general"), exist_ok=True)
    os.makedirs(os.path.join(img_dir, "pages"), exist_ok=True)
    os.makedirs(os.path.join(img_dir, "raster"), exist_ok=True)
    os.makedirs(os.path.join(img_dir, "svg"), exist_ok=True)

    # Создаем папку src/svg
    os.makedirs(os.path.join(src_dir, "svg"), exist_ok=True)

    # Создаем подпапки в src/fonts
    fonts_dir = os.path.join(src_dir, "fonts")
    os.makedirs(os.path.join(fonts_dir, "custom"), exist_ok=True)
    os.makedirs(os.path.join(fonts_dir, "vendors"), exist_ok=True)

    # Создаем файлы в src
    open(os.path.join(src_dir, "favicon.ico"), 'a').close()
    open(os.path.join(src_dir, "robots.txt"), 'a').close()

    # Создаем папку dist
    os.makedirs(os.path.join(project_root, "dist"), exist_ok=True)

    print("Структура проекта успешно создана.")

if __name__ == "__main__":
    create_project_structure()
