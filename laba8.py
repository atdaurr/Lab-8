#Дружинина 6 вариант
import cv2

#Задание№1
img = cv2.imread('images/variant-6.png')#Загружаем изображение
height, width = img.shape[:2]#Получаем текущие размеры изображения
new_img = cv2.resize(img, (2*width, 2*height), interpolation=cv2.INTER_LINEAR)#Растягиваем изображение в 2 раза
#Отображаем новое изображение
cv2.imshow('var6', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Задание№2
cap = cv2.VideoCapture("sample.mp4")
down_points = (640, 480)
old_position = 2
counter_right = 0
counter_left = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        centreX = frame.shape[1] // 2
        if x > (centreX):
            new_position = 2
        if x + w < (centreX):
            new_position = 1
        if new_position != old_position:
            if old_position == 2:
                 counter_left += 1
            if old_position == 1:
                counter_right += 1
            old_position = new_position
        cv2.putText(frame, f'{counter_left}', (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0),1)
        cv2.putText(frame, f'{counter_right}', (down_points[0] - 90, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

    cv2.imshow('sample', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f'The left counter: {counter_left}')
print(f'The right counter: {counter_right}')