import tkinter as tk  # рисование окна через ткинтер
from PIL import Image, ImageDraw, ImageTk

# Создаем новое окно Tkinter
root = tk.Tk()

# Устанавливаем размер окна
root.geometry('3840x1080+0+0')  # Для двух мониторов 1920x1080, расположенных горизонтально

# Устанавливаем прозрачность окна в 50%
root.attributes('-alpha', 0.05)

# Устанавливаем заголовок окна
root.title("Draw on Window")

# Создаем новое белое изображение с размерами окна
image = Image.new('RGB', (3840, 1080), 'white')
draw = ImageDraw.Draw(image)

# Хранить последнюю позицию мыши
last_position = None

# Функция для рисования на изображении при движении мыши
def draw_on_image(event):
    global last_position
    x, y = event.x, event.y
    if last_position is not None:
        # Рисуем линию от последней позиции до текущей
        draw.line([last_position, (x, y)], fill='red', width=5)
    last_position = (x, y)  # Обновляем последнюю позицию
    update_canvas()

def stop_drawing(event):
    global last_position
    last_position = None  # Обнуляем последнюю позицию, когда кнопка мыши отпущена

# Функция для обновления холста
def update_canvas():
    # Преобразуем изображение PIL в PhotoImage Tkinter
    photo = ImageTk.PhotoImage(image)

    # Если холст еще не создан, создаем его
    if not hasattr(update_canvas, 'canvas_image'):
        update_canvas.canvas_image = canvas.create_image(0, 0, image=photo, anchor='nw')
    else:
        # Если холст уже существует, обновляем его изображение
        canvas.itemconfig(update_canvas.canvas_image, image=photo)
    # Сохраняем ссылку на изображение, чтобы оно не было удалено сборщиком мусора
    update_canvas.photo = photo

# Создаем холст Tkinter и связываем его с функцией рисования
canvas = tk.Canvas(root, width=3840, height=1080)
canvas.pack()
canvas.bind('<B1-Motion>', draw_on_image)
canvas.bind('<ButtonRelease-1>', stop_drawing)

root.mainloop()