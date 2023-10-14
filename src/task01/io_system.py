from data_manager import write_address, write_department, write_position, write_email, write_phone_number, write_staff
from query_manager import read_address, read_department, read_position, read_email, read_phone_number, read_staff
from view import view_input1, view_input2, view_write, view_read


def button_click():
    lister1 = view_input1()
    if lister1 == '0':
        lister2 = view_input2()
        if lister2 == '0':
            view_write(write_address())
        elif lister2 == '1':
            view_write(write_department())
        elif lister2 == '2':
            view_write(write_position())
        elif lister2 == '3':
            view_write(write_email())
        elif lister2 == '4':
            view_write(write_phone_number())
        elif lister2 == '5':
            view_write(write_staff())

    elif lister1 == '1':
        lister2 = view_input2()
        if lister2 == '0':
            view_read(read_address())
        elif lister2 == '1':
            view_read(read_department())
        elif lister2 == '2':
            view_read(read_position())
        elif lister2 == '3':
            view_read(read_email())
        elif lister2 == '4':
            view_read(read_phone_number())
        elif lister2 == '5':
            view_read(read_staff())
