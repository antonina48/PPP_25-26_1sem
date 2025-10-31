##6. Кинотеатр и места
##Смоделировать зал (массив NxM, где 0 — свободно, 1 — занято).
##Реализовать функцию бронирования ряда мест подряд (например, 3 места подряд).
##Если места заняты — программа ищет следующий подходящий ряд.

def cinema_hall(row, rows_in_place):      #ряды(N) и места в рядах(M)
    hall=[]
    for a in range(row):
        row_list=[]
        for b in range(rows_in_place):
            row_list.append(0)   #своб место
        hall.append(row_list)
    return hall

def count_place_in_hall(hall):
    print("Сейчас в зале: (0-свободно, 1-занято) ")
    for row in hall:
        row_str=""
        for seat in row:
            row_str+=str(seat)+" "
    print(row_str)

def seatreservation(hall, need_seat):    #ф-ция на бронь подряд идущих мест
    total_rows=len(hall)
    for number_row in range(total_rows):
        all_rows=hall[number_row]   #все настоящие
        count_free_place=0
        start=0   #начальная точка

        for number_seat in range(len(all_rows)):
            if all_rows[number_seat]==0:   #если место свободно
                if count_free_place==0:    #сли первое во множ
                    start=number_seat
                count_free_place+=1
                    
            else:   #занятоо
                count_free_place=0  #обнуление счёт
            if count_free_place==need_seat:  #подряд идущ
                for a in range(start, start+need_seat):  #бронь подряж идущ
                    hall[number_row][a]=1
                return (number_row+1, start+1)  #счёт с единцы
    return None  #если ничо нет
if __name__=="__main__":
    cinema_hall_5=cinema_hall(5,10)
    count_place_in_hall(cinema_hall_5)
    result=seatreservation(cinema_hall_5, 3)
    if result:
        print(f" забронированные места: {result[0]} , начиная с места {result[1]}")
    else:
        print("не удалось забронировать")
    count_place_in_hall(cinema_hall_5)

    
#if __name__ == "__main__":
    pass # Ваш код здесь
