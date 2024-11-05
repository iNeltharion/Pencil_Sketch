import os
import cv2


def pencil_sketch(image_path, output_folder='my_sketch', output_filename='sketch.jpg', blur_ksize=21, show=False):
    # Загрузка изображения
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Не удалось загрузить изображение по пути: {image_path}")

    # Конвертация изображения в оттенки серого
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Инвертирование серого изображения и размытие
    inverted_gray_image = cv2.bitwise_not(gray_image)
    blurred_image = cv2.GaussianBlur(inverted_gray_image, (blur_ksize, blur_ksize), 0)

    # Создание эффекта наброска
    pencil_sketch_image = cv2.divide(gray_image, 255 - blurred_image, scale=256.0)

    # Создание выходной папки, если она не существует
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Полный путь к выходному файлу
    output_path = os.path.join(output_folder, output_filename)

    # Сохранение результата
    cv2.imwrite(output_path, pencil_sketch_image)

    # Показ изображения на экране, если show=True
    if show:
        cv2.imshow('Pencil Sketch', pencil_sketch_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return output_path


# Использование функции
input_image_path = 'w2.jpg'
output_path = pencil_sketch(input_image_path, output_folder='my_sketch', output_filename='w2.jpg',
                            blur_ksize=21, show=True)
print(f"Скетч сохранен по пути: {output_path}")
